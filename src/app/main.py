
from .entities.item import Item
from fastapi import FastAPI
from pydantic import BaseModel
import hashlib

app = FastAPI()

class NomeRequest(BaseModel):
    nome: str
    deslocamento: int

def cifra_cezar(nome: str, deslocamento: int):
    cezar = ""
    for letra in nome:
        if letra.isalpha():
            base = ord('A') if letra.isupper() else ord('a')
            cezar += chr((ord(letra) - base + deslocamento) % 26 + base)
        else:
            cezar += letra
    return cezar

def inverter_nome(nome: str):
    return nome[::-1]

def nome_binario(nome: str):
    return ''.join(format(ord(i), '08b') for i in nome)

def hash_nome(nome: str):
    return hashlib.md5(nome.encode()).hexdigest()

@app.post("/transformando_nomes")
async def transformando_nomes(dados: NomeRequest):
    return {
        "nome_cifrado": cifra_cezar(dados.nome, dados.deslocamento),
        "nome_invertido": inverter_nome(dados.nome),
        "nome_binario": nome_binario(dados.nome),
        "hash_nome": hash_nome(dados.nome),
    }

 