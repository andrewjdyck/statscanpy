# statscanpy

A package for using data from Statistics Canada Web Services with python.

## Installation

```{python}
pip install git+git@github.com:andrewjdyck/statscanpy.git
```

## Usage

```{python}
from statscanpy import product as scp

# initialize product class for productId 14100287.
# This will download metadata for the product cube.
P = scp.Product('14100287')

# read the product metadata
P.metadata
```


## Links

Statistics Canada Web Data Services: https://www.statcan.gc.ca/eng/developers/wds

User guide: https://www.statcan.gc.ca/eng/developers/wds/user-guide

