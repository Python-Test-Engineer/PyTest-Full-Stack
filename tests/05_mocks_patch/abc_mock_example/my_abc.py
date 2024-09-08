"""Doc"""

from abc import ABC, abstractmethod


class AbstractAdder(ABC):
    """doc"""

    @abstractmethod
    def add(self, value1: str, value2: str):
        """Doc"""


class ConcreteAdder(AbstractAdder):
    """doc"""

    def add(self, value1: str, value2: str) -> str:
        """doc"""
        return value1 + value2


def add_executer(abstract_adder: AbstractAdder):
    """doc"""
    return abstract_adder.add(1, 2)
