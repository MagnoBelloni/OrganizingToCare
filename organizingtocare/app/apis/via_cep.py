import requests


def busca_cep(cep):
    resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    dic = resposta.json()
    return dic['logradouro']
