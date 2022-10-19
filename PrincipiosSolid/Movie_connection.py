import requests

def url_connection(url: str):

    response = requests.get(url)
    return response

# Principio de solid SRP: Solo se encarga de obtener el url