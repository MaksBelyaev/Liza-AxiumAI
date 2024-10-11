from .utils import open_url


#
intents = [
    {
        "name": "open_youtube",
        "function": open_url("https://www.youtube.com/"),
    },
    {
        "name": "google",
        "function": open_url("https://google.ru/")
    }
]