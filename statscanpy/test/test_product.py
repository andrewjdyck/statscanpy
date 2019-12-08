import statscanpy as sc

product = sc.Product('14100287')

# read the product metadata
meta = product.metadata

# dimensions of the product cube
dims = product.dimensions

# get details on the sub-dimensions
subdims = product.dimension_members_to_df()

coord = '1.7.1.1.1.1.0.0.0.0'

product.get_series_info(coord)

data = product.get_coordinate_data()
