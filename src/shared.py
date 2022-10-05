from typing import List, Protocol, Sequence

from vec import Vector2



class Element():
    def __init__(
        self,
        biome: float = 0.0,
        height: float = 0.0,
        character: str ='.',
        color: str = 'white',
    ) -> None:
        self.biome = biome
        self.height = height
        self.character = character
        self.color = color


class State():
    def __init__(
        self,
        width: int = 96,
        height: int = 30,
        elements: List[List[Element]] = [],
    ) -> None:
        self.width = width
        self.height = height
        self.elements = elements or [[Element() for _ in range(height)] for _ in range(width)]


class GeneratorStep(Protocol):
    def __call__(
        self,
        st: Vector2,
        xy: Vector2,
        previous: State,
        current: State,
    ) -> None: ...
