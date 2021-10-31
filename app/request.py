from app import app
import urllib.request,json
from .models import source
Source=source.Source

# Getting api key
api_key = app.config['NEWS_API_KEY']


# Getting the movie base url
base_url = app.config['NEWS_API_BASE_URL']

# # Getting api key
# api_key = None
# # Getting the movie base url
# base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_sources():
    '''
    Function that gets the json response to url request
    '''
    get_source_url= base_url.format(api_key)
    # print(get_source_url)
    with urllib.request.urlopen(get_source_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    '''
    function to process results and transform them to a list of objects
    Args:
        source_list:dictionary cotaining source details
    Returns:
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category=source_item.get('category')
        if id:
            source_object = Source(id,name,description,url,category)
            source_results.append(source_object)

    return source_results