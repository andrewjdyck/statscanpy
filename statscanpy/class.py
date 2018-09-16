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
#'

import requests

class Product(object):

    def __init__(self, productId):
        self.productId = productId

    def get_product_metadata(self, productId):
      url = 'https://www150.statcan.gc.ca/t1/wds/rest/getCubeMetadata'

      payload = [{'productId': int(productId)}]

      req = requests.post(
        url,
        json=payload
      )

      response = req.json()[0]

      if (response['status'] == "SUCCESS"):
          return(response['object'])
      else:
          print('ERROR')
