import statscanpy as sc

# Initiate the class
census = sc.Census()

# Get data with default parameters
result = census.get_cpr_geo()
print(result)

# Prairies, 2016
# dguid = '2016A00014'
# result = census.get_cpr_geo(dguid=dguid)

