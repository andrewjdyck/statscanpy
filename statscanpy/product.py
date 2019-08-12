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
        self.get_metadata()

    ## Documentation for a method.
    #  @param self The object pointer.
    def get_metadata(self):
        """metadata

        Retrieve metadata for a given productId.
        """
        url = 'https://www150.statcan.gc.ca/t1/wds/rest/getCubeMetadata'
        payload = [{'productId': int(productId)}]
        req = requests.post(
            url,
            json=payload
        )
        response = req.json()
        if (response[0]['status'] == "SUCCESS"):
            self.metadata = response[0]['object']
            return(self.metadata)
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

