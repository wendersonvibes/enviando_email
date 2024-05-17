import requests

def buscar_cep(cep):
    cep_request = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    return cep_request.content