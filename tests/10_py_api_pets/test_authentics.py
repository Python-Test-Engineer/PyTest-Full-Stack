""" Testing auth"""

import requests
from requests.auth import HTTPDigestAuth

URL = "https://httpbin.org/digest-auth/auth/123/123/MD5"
auth = HTTPDigestAuth("123", "123")


def test_0160_basic_auth() -> None:
    """Testing basic auth"""
    # use the 'auth' parameter to send requests with HTTP Basic Auth:
    # headers = {"Accept": "application/json"}
    r = requests.get(URL, auth=auth, verify=True, timeout=5)
    print(f"STATUS_CODE: {r.status_code}")
    assert r.status_code == 200
