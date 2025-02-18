
from .item_repository_interface import IItemRepository
import hashlib

class ItemRepositoryMock(IItemRepository):
    nome: str
    deslocamento: int
    def __init__(self):
        self.nome = ""
        self.deslocamento = 0
    
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