"""API"""

from typing import Any
import requests


def get_url(url: str, timeout: int) -> Any:
    """Get API"""

    return requests.get(url, timeout=timeout)
