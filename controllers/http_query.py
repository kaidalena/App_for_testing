from __init__ import logger
import uuid
import json
import requests

""" 
Examples:
  url: 
    '/user'
    '/views/users_group'
  
  headers: 
    {
      'Content-Type': mimetype,
      'Accept': mimetype,
      'Token': '7aae3af2-db0f-11ea-bbec-1d927588410c'
    }
              
  query_params (Query parameters):
    for url GET:/users: {
                          'login': 'login',
                          'pass': 'password'
                        }
  
  json_data (Request body):
    for url PUT:/views/carwash_settings:  [
                                            {
                                              "name": "valid_hours_pin",
                                              "value": 5.5
                                            }
                                          ]
"""


base_url = 'https://dev-pc.eos-studio.com'

def decorator_http_query(func):
  def wrapper(*args, **kwargs):
    global base_url
    kwargs['url'] = f"{base_url}{kwargs['url']}"
    logger.info('{type_query}: {url}\t\tparams: {params}\t\tjson={json}\t\theaders: {headers}'.format(
      type_query=func.__name__.upper(),
      url=f"{kwargs['url']}",
      params=kwargs['query_params'] if 'query_params' in kwargs else None,
      json=kwargs['json_data'] if 'json_data' in kwargs else None,
      headers=kwargs['headers'] if 'headers' in kwargs else None)
    )
    response = func(*args, **kwargs)
    logger.info('Response: {resp}'.format(resp=response.json()))
    return response
  wrapper.__name__ = func.__name__
  return wrapper


@decorator_http_query
def get(url, headers=None, query_params=None, json_data=None):
  return requests.get(
    url=url,
    params=query_params,
    headers=headers)
  # return test_client.get(url, query_string=query_params, headers=headers, json=json_data)


@decorator_http_query
def post(url, headers, json_data=None, query_params=None):
  headers['transaction'] = str(uuid.uuid1())
  return requests.post(
    url=url,
    headers=headers,
    params=query_params,
    json=json_data
  )
  # return test_client.post(url, query_string=query_params, json=json_data, headers=headers)


@decorator_http_query
def put(url, headers, json_data=None, query_params=None):
  headers['transaction'] = str(uuid.uuid1())
  return requests.put(
    url=url,
    headers=headers,
    params=query_params,
    json=json_data
  )
  # return test_client.put(url, query_string=query_params, json=json_data, headers=headers)


http_query_by_type = {
  'get': get,
  'put': put,
  'post': post
}