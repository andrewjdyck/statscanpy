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
product = scp.product('14100287')

# read the product metadata
product.metadata
```


## Links

Statistics Canada Web Data Services: https://www.statcan.gc.ca/eng/developers/wds

User guide: https://www.statcan.gc.ca/eng/developers/wds/user-guide

