from abc import ABC, abstractmethod
import math

# Абстрактный класс геометрической фигуры
class Shape(ABC):
    
    @abstractmethod
    def area(self) -> float:
        pass