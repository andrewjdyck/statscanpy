import statscanpy as scp
import pprint as pp

# Search for farm debt
search = scp.datasearch('labour force')
search.print_results()

# initialize product class for productId 14100287.
# This will download metadata for the product cube.
print('Retrieving product metadata...')
product = scp.product('14100287')

# read the product metadata
print('Output the metadata...')
meta = product.metadata
pp.pprint(meta)

# dimensions of the product cube
print('Getting dimensions...')
dims = product.dimensions
pp.pprint(dims)

# get details on the sub-dimensions
subdims = product.dimension_members_to_df()
pp.pprint(subdims)

# get coordinate
coord = '1.1.1.1.1.1.0.0.0.0'
product.get_series_info(coord)
cdata = product.get_coordinate_data()


