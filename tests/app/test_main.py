from fastapi.exceptions import HTTPException
import pytest
from src.app.entities.item import Item
from src.app.enums.item_type_enum import ItemTypeEnum
from src.app.main import get_all_items, get_item, create_item, delete_item, update_item
from src.app.repo.item_repository_mock import ItemRepositoryMock


class teste_main:
    def __init__(self):
        self.items: Dict[int, Item] = {
            1: Item(name="joão", deslocamento=3),
            2: Item(name="ana", deslocamento=2),
            3: Item(name="miguel", deslocamento=5),
            4: Item(name="claudio", deslocamento=5),
            5: Item(name="nicoli", deslocamento=5),
        }