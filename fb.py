import requests

def api(url):
    resp = requests.get(url)
    return resp.content
