import string
from random import choice


def gerar_senha_aleatoria():
    tamanho = 8
    valores = string.ascii_lowercase + string.digits
    senha = ''
    for i in range(tamanho):
        senha += choice(valores)

    return senha
