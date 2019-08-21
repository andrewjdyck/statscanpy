import requests
# from urllib.parse import urlencode, quote_plus, quote
import urllib.parse

class DataSearch(object):
    def __init__(self, search_term):
        self.search_term = search_term
        self.search_results = self.search(search_term)
        self.parse_metadata()      
    
    def search(self, search_term):
        # example query from open canada CKAN page
        # https://open.canada.ca/data/en/api/3/action/package_search?q=spending
        base_url = 'https://open.canada.ca/data/en/api/3/action/package_search?q={}&fq=organization:statcan'
        req = requests.get(
            url = base_url.format(urllib.parse.quote(search_term))
        )
        return_json = req.json()
        return(return_json['result']['results'])
    
    def parse_metadata(self):
        counter = 0
        for result in self.search_results:
            # title = self.search_result['result']['results'][0]['title']
            table_id = result['data_series_issue_identification']['en']
            pid = table_id.split('; ')[0].split(' ')[1]
            self.search_results[counter]['pid'] = pid
            counter += 1




ds = DataSearch('farm%20debt')