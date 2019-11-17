
import statscanpy as scp


# initialize product class for productId 14100287.
# This will download metadata for the product cube.
product = scp.product('14100287')

# read the product metadata
meta = product.metadata
