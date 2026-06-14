import os


def somar(a, b):
    return a + b


def conectar_api():
    token = os.environ.get("MINHA_API_SECRET")
    if not token:
