
import statscanpy as scp


# initialize product class for productId 14100287.
# This will download metadata for the product cube.
product = scp.product('32100051')

# read the product metadata
meta = product.metadata
dim = meta['dimension']

dd = list()
for d in dim:
  dd.append({ key: d[key] for key in ['dimensionPositionId', 'dimensionNameEn']})

def dimension_members_to_df(dimensions, metadata):
  dimension_members = list()
  for dim_pos_id in dimensions.dimensionPositionId:
    dim = metadata['dimension'][dim_pos_id-1]
    dimension_members.append( { key: dim[key] for key in ['parentMemberId', 'memberId', 'memberNameEn'] } )
  return(pd.DataFrame(dimension_members))

