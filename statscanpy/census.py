import requests
import csv
import zipfile
import io
import pandas as pd
from datetime import datetime
"""@package docstring
Download StatsCan data from Census web data services

This class enables download product census data
from Statistics Canada.
"""

"""Documentation for a class.
 
More details.
"""
class CensusWDS(object):
    
    def __init__(self, dtype='json', lang='E', notes=0, stat=0):
        self.params = {
            "dtype": dtype,
            "lang": lang,
            "notes": notes,
            "stat": stat,
        }

    def params_to_dict(self):
        return(self.params)

    def get_cpr_geo(self, dguid="2016A000011124", topic=0):
        # Returns all 2016 Census Profile data for a geography of interest.
        # https://www12.statcan.gc.ca/wds-sdw/cpr2016-eng.cfm
        params = self.params
        params['dguid'] = dguid
        params['topic'] = topic
        resource_url = 'https://www12.statcan.gc.ca/rest/census-recensement/CPR2016.{dtype}?lang={lang}&dguid={dguid}&topic={topic}&notes={notes}&stat={stat}'
        url = resource_url.format(**params)
        req = requests.get(url)
        return(url)

    def get_census_geo(self, geos="PR", cpt="00"):
        # Returns a list of 2016 Census geographies and geographic attributes for a geographic level.
        # https://www12.statcan.gc.ca/wds-sdw/cr2016geo-eng.cfm
        params = self.params
        params['geos'] = geos
        params['cpt'] = cpt
        resource_url = 'https://www12.statcan.gc.ca/rest/census-recensement/CR2016geo.{dtype}?lang={lang}&geos={geos}&cpt={cpt}'
        url = resource_url.format(**params)
        return(url)

    def get_census_geo_indicators(self, dguid="2016A000011124", theme=0):
        # https://www12.statcan.gc.ca/wds-sdw/2016ind1-eng.cfm
        # Returns 2016 Census indicator data for Canada or a selected province or territory.
        params = self.params
        params['dguid'] = dguid
        params['theme'] = theme
        resource_url = 'https://www12.statcan.gc.ca/rest/census-recensement/2016ind1.{dtype}?lang={lang}&dguid={dguid}&theme={theme}'
        url = resource_url.format(**params)
        return('Returns 2016 Census indicator data for Canada or a selected province or territory.')

    def get_census_indicator(self, indid=1):
        # https://www12.statcan.gc.ca/wds-sdw/2016ind2-eng.cfm
        # Returns one selected 2016 Census indicator for Canada, provinces and territories.
        params = self.params
        params['indid'] = indid
        resource_url = 'https://www12.statcan.gc.ca/rest/census-recensement/2016ind2.{dtype}?lang={lang}&indid={indid}'
        url = resource_url.format(**params)
        return('Returns one selected 2016 Census indicator for Canada, provinces and territories.')
