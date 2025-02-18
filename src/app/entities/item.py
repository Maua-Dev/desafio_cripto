from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.item_type_enum import ItemTypeEnum


class Item:
    name: str
    deslocamento: int
    
    def __init__(self, name: str=None, deslocamento: int=None):
        validation_name = self.validate_name(name)
        if validation_name[0] is False:
            raise ParamNotValidated("name", validation_name[1])
        self.name = name
        
        validation_deslocamento = self.validate_deslocamento(deslocamento)
        if validation_deslocamento[0] is False:
            raise ParamNotValidated("deslocamento", validation_deslocamento[1])
        self.deslocamento = deslocamento

        
    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
        if name is None:
            return (False, "Nome é obrigatório!")
        if type(name) != str:
            return (False, "Nome deve ser uma string")
        if len(name) < 3:
            return (False, "Nome deve ter no mínimo 3 caracteres")
        return (True, "")
        
    @staticmethod
    def validate_deslocamento(deslocamento:int) -> Tuple[bool, int]:
        if deslocamento is None:
            return (False, "definir o deslocamento é obrigatório!")
        if type(deslocamento) != int:
            return (False, "deslocamento deve ser um número inteiro")
        if deslocamento < 0:
            return (False, "deslocamento deve ser maior que 0")
        return (True, "")
    
