
import statscanpy as scp


# initialize product class for productId 14100287.
# This will download metadata for the product cube.
product = scp.product('32100051')

# read the product metadata
meta = product.metadata
dim = meta['dimension']
