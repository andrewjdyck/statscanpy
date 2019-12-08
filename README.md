# statscanpy

A package for using data from Statistics Canada Web Services with python.

## Installation

```{python}
pip install git+https://github.com/andrewjdyck/statscanpy#egg=statscanpy
```

## Usage

```{python}
import statscanpy as scp

# Search for farm debt
search = scp.datasearch('labour force')
search.print_results()

# initialize product class for productId 14100287.
# This will download metadata for the product cube.
product = scp.Product('14100287')

# read the product metadata
meta = product.metadata

# dimensions of the product cube
dims = product.dimensions

# get details on the sub-dimensions
subdims = product.dimension_members_to_df()

# Canada's seasonally adjusted unemployment rate for ages 15+
coord = '1.7.1.1.1.1.0.0.0.0'

# Get the information about the data series
product.get_series_info(coord)
print(product.series_info)

# Retrieve the most recent 10 observations for the data series
data = product.get_coordinate_data()
```


## Links

Statistics Canada Web Data Services: https://www.statcan.gc.ca/eng/developers/wds

User guide: https://www.statcan.gc.ca/eng/developers/wds/user-guide

Census web data services: https://www12.statcan.gc.ca/wds-sdw/index-eng.cfm

- https://www12.statcan.gc.ca/wds-sdw/cpr2016-eng.cfm
- https://www12.statcan.gc.ca/wds-sdw/cr2016geo-eng.cfm
- https://www12.statcan.gc.ca/wds-sdw/2016ind1-eng.cfm
- https://www12.statcan.gc.ca/wds-sdw/2016ind2-eng.cfm

Dissemination Geography Unique Identifier (DGUID): https://www150.statcan.gc.ca/n1/pub/92f0138m/92f0138m2019001-eng.htm
