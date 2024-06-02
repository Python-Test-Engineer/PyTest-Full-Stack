"""Test"""
import requests
from tut9.myapp.dice import roll_dice


def guess_number(num: int) -> str:
    """docstring"""
    result = roll_dice()
    if result == num:
        return "You won!"
    else:
        return "You lost!"


def get_ip():
    """docstring"""
    response = requests.get("https://httpbin.org/ip", timeout=5)
    if response.status_code == 200:
        return response.json()["origin"]
