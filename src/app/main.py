
from .entities.item import Item
from fastapi import FastAPI
from .repo.item_repository_mock import ItemRepositoryMock
from src.app.entities.item import Item
app = FastAPI()

@app.post("/transformando_nomes")
async def transformando_nome(item: Item):
    item_mock = Item(name= item.name, deslocamento= item.deslocamento)
    repo_mock = ItemRepositoryMock()
    nome_cifrado = repo_mock.cifra_cezar(name= item_mock.name, deslocamento = item_mock.deslocamento)
    nome_invertido = repo_mock.inverter_nome(name=item_mock.name)
    nome_binario = repo_mock.nome_binario(name=item_mock.name)
    hash_nome = repo_mock.hash_nome(name=item_mock.name)
    return {
        "name": item_mock.name,
        "nome_cifrado": nome_cifrado,
        "nome_invertido": nome_invertido,
        "nome_binario": nome_binario,
        "hash_nome": hash_nome,
    } 
   
     