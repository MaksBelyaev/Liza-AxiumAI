import asyncio
import logging
import webbrowser
from Interfece.Liza.event import Event, EventTypes

logger = logging.getLogger(__name__)


def open_url(url):
    async def wrapper(event):
        webbrowser.open(url)
        print("maker url_opener отработал")
    return wrapper
