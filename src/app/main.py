from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments

from .repo.item_repository_mock import ItemRepositoryMock

from .errors.entity_errors import ParamNotValidated

from .enums.item_type_enum import ItemTypeEnum

from .entities.item import Item

from  basemodel import BaseModel

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

def nome_binario(nome:str):
    return '' .join(format(ord(i), '08b') for i in nome)

def hash_nome(nome:str):
    return hashlib.md5(nome.encode()).hexdigest()
 
@app.post("/transformando_nomes")
async def transformando_nomes(request: NomeRequest):
    return {"nome_cifrado": cifra_cezar(request.nome, request.deslocamento), "nome_invertido": inverter_nome(request.nome), "nome_binario":nome_binario(request.nome), "hash_nome":hash_nome(request.nome)}

 