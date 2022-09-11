from abc import ABC
from typing import TypeVar


class Entity(ABC):
    entity_name = "Entity"


E = TypeVar("E", bound=Entity)
