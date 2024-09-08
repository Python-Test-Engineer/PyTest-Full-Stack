"""Utilities"""
import json

import requests


# get API call and return response data
def get_api_data(url: str):
    """GET URL"""
    headers = {"Content-Type": "application/json"}
    print("RequestURL: ", url)
    response = requests.get(url, verify=False, headers=headers, timeout=5)
    data = response.json()
    assert len(data) > 0, "empty response!!"
    time_taken = response.elapsed.total_seconds()
    return data, response.status_code, time_taken


# put api call
def put_data(url: str, body: str):
    """PUT URL"""
    headers = {"Content-Type": "application/json"}
    print("RequestURL: ", url)
    print("ReqBody: ", json.dumps(body))
    response = requests.put(url, verify=False, json=body, headers=headers, timeout=5)
    data = response.json()
    time_taken = response.elapsed.total_seconds()
    return data, response.status_code, time_taken


# delete api call
def delete_data(url: str, op_headers: str = ""):
    """DELETE URL"""
    headers = {"Content-Type": "application/json"}
    print("RequestURL: ", url)
    # (headers | op_headers) means merge op_headers into headers
    # if op_headerss is a dict, i.e. not None then do this merge else use headers
    headers = (headers | op_headers) if isinstance(op_headers, dict) else headers
    response = requests.delete(url, verify=False, headers=headers, timeout=5)
    print(response.request.headers)
    data = response.json()
    time_taken = response.elapsed.total_seconds()
    return data, response.status_code, time_taken
