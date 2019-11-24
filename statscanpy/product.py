#' Download StatsCan Metadata from Product Cube
#'
#' This function allows you to download product metadata from
#' Statistics Canada.
#' @param productId The Statistics Canada Product ID.
#' @keywords productId, product, metadata
#' @importFrom httr POST content content_type
#' @export
#' @examples
#' get_product_metadata('14100287')
#' cansimId = '2820087'
#' productId = '14100287'
#'
import requests
import csv
import zipfile
import io
import pandas as pd
from datetime import datetime
"""@package docstring
Download StatsCan Metadata from Product Cube

This function allows you to download product metadata from
Statistics Canada.
"""

"""Documentation for a class.
 
More details.
"""
class Product(object):
    
    def __init__(self, productId, lang='en'):
        self.productId = productId
        self.lang = lang
        self.camelLang = lang.capitalize()
        self.metadata = self.get_metadata()
        self.dimensions = self.get_dimensions()

    ## Documentation for a method.
    #  @param self The object pointer.
    def get_metadata(self):
        """metadata

        Retrieve metadata for a given productId.
        """
        url = 'https://www150.statcan.gc.ca/t1/wds/rest/getCubeMetadata'
        payload = [{'productId': int(self.productId)}]
        print('Retreiving metadata for Product ID: ' + self.productId)
        req = requests.post(
            url,
            json=payload
        )
        response = req.json()
        if (response[0]['status'] == "SUCCESS"):
            return(response[0]['object'])
        else:
            print('ERROR')

    def read_cansim_product_mapping(self, Id='all'):
        if (Id == 'all'):
            print("ERROR: Only one of cansimId or productId can be entered")
        else:
            response = requests.get(
                'https://www.statcan.gc.ca/eng/developers-developpeurs/cansim_id-product_id-concordance.csv')
            reader = csv.DictReader(io.StringIO(response.text))
            cansim_concordance = [row for row in reader]
            for row in cansim_concordance:
                if row['PRODUCT_ID'] == Id:
                    returnFrame = row['CANSIM_ID']
        return (returnFrame)

    def downloadProductCube(self):
        url = 'https://www150.statcan.gc.ca/t1/wds/rest/getFullTableDownloadCSV/' + self.productId + '/' + self.lang
        response = requests.get(url).json()
        if response['status'] == 'SUCCESS':
            print('Downloading zip file of product cube....')
            remote_zip = requests.get(response['object'])
            root = zipfile.ZipFile(io.BytesIO(remote_zip.content))
            name = self.productId + '.csv'
            df = pd.read_csv(root.open(name))
            return(df)
        else:
            print('ERROR - cannot find download url for productId: ' + self.productId)

    def read_metadata(self):
        d = self.dimensions
        dim_names = [dim['dimensionName' + self.camelLang] for dim in self.metadata['dimension']]
        # There are 6 dimensions. Some may have more or less?
        print('The product has ' + str(len(d)) + ' dimensions.')
        print('The dimensions are: ' + ', '.join(dim_names))
        # This is the first dimension. for 14100287, this is geography
        # Member is a list of all the values the dimension can take
        # dimension 2 is labour force characterisitics
        d[0]['member'][0].keys()
        d[0]['member'][0].values()
        # One can use the dims to generate a coordinate, which is a better way to download data.
        # coordinate ID must have 10 digits. The last few are zeros if not defined.
        # Example: Coordinate ID 1.1.1.1.1.2.0.0.0.0 is for the following:
        # Canada, Population, Both sexes, 15 years and over, Estimate, Unadjusted
        coordinateId = '1.1.1.1.1.2.0.0.0.0'

    def get_series_info(self, coordinateId):
        # coordinateId = '1.1.1.1.1.2.0.0.0.0'
        self.coordinateId = coordinateId
        payload = [{'productId': int(self.productId), "coordinate": self.coordinateId}]
        req = requests.post(
            url = 'https://www150.statcan.gc.ca/t1/wds/rest/getSeriesInfoFromCubePidCoord',
            json=payload
        )
        if req.json()[0]['status'] == 'SUCCESS':
            self.series_info = req.json()[0]['object']
            self.vectorId = self.series_info['vectorId']
            print('Series info stored in object.series_info')
        else:
            print('ERROR: Something went wrong with the API request')

    def get_coordinate_data(self, n=10):
        payload = [{'productId': int(self.productId), "coordinate": self.coordinateId, "latestN": n}]
        req = requests.post(
            url = 'https://www150.statcan.gc.ca/t1/wds/rest/getDataFromCubePidCoordAndLatestNPeriods',
            json=payload
        )
        coord_data = req.json()
        status = coord_data[0]['status']
        if status == 'SUCCESS':
            object_data = pd.DataFrame(coord_data[0]['object'])
            self.vectorIds = object_data.vectorId.unique().tolist()
            vector_data = pd.DataFrame(coord_data[0]['object']['vectorDataPoint'])
        else:
            print('ERROR: the status returned was: ' + status)
        return(vector_data)

    def get_vector_data(self, startDate=None, endDate=None):
        if (startDate is not None and endDate is not None):
            #startDate = "2015-12-01T08:30"
            #tt = datetime.strptime(startDate, '%Y-%m-%dT%H:%M')
            #stringtime = tt.strfptime('%Y-%m-%dT%H:%M')
            #endDate = "2018-03-31T19:00"
            payload = {
                "vectorId": [self.series_info['vectorId']], 
                "startDataPointReleaseDate": startDate,
                "endDataPointReleaseDate": endDate
            }
            req = requests.post(
                url = 'https://www150.statcan.gc.ca/t1/wds/rest/getBulkVectorDataByRange',
                json=payload
            )
            vector_data = req.json()[0]['object']
        else:
            print('Start or end date not properly specified. Returning 10 latest data points instead.')
            payload = [{'vectorId': self.series_info['vectorId'], "latestN": 10}]
            req = requests.post(
                url = 'https://www150.statcan.gc.ca/t1/wds/rest/getDataFromVectorsAndLatestNPeriods',
                json=payload
            )
            vector_data = req.json()[0]['object']
        return(vector_data)
    
    def get_dimensions(self):
        dimensions = list()
        for dim in self.metadata['dimension']:
            dimensions.append( { key: dim[key] for key in ['dimensionPositionId', 'dimensionNameEn'] } )
        return( pd.DataFrame(dimensions) )

    def dimension_members_to_df(self):
        dimension_members = list()
        for dim_pos_id in self.dimensions['dimensionPositionId']:
            dim = self.metadata['dimension'][dim_pos_id-1]['member']
            df = pd.DataFrame(dim)
            dimension_members.append(df)
            # dimension_members.append( { key: dim[key] for key in ['parentMemberId', 'memberId', 'memberNameEn'] } )
        return(dimension_members)


