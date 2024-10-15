import asyncio
import logging
import webbrowser
import keyboard
import requests
from bs4 import BeautifulSoup

from Interfece.Liza.event import Event, EventTypes

logger = logging.getLogger(__name__)


def open_url(url):
    async def wrapper(event):
        webbrowser.open(url)
        print("maker url_opener отработал")
    return wrapper

def keyboard_shortcut(key):
    async def key_short(event):
        keyboard.send(key)
        print("maker keyboard_shortcut отработал")
    return key_short
