import pytest
from src.app.entities.item import Item
from src.app.enums.item_type_enum import ItemTypeEnum
from src.app.errors.entity_errors import ParamNotValidated


class Test_Item:
    def test_item(self):
        item = Item("joão", deslocamento=3, )
        assert item.name == "joão"
        assert item.deslocamento == 3
        
