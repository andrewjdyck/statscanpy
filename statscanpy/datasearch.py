import requests
# from urllib.parse import urlencode, quote_plus, quote
import urllib.parse
import pprint


class DataSearch(object):
    def __init__(self, search_term):
        self.search_term = search_term
        self.full_results = self.search(search_term)
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
        self.simple_results = list()
        for result in self.full_results:
            table_id = result['data_series_issue_identification']['en']
            try:
                pid = table_id.split('; ')[0].split(' ')[1]
            except:
                pid = result['data_series_issue_identification']['en']
            self.full_results[counter]['pid'] = pid
            self.simple_results.append({'ProductId': pid, 'Title': result['title']})
            counter += 1
            

    def print_results(self):
        pprint.pprint(self.simple_results)




