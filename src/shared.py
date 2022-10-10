from typing import List, Protocol, Tuple

from vec import Vector2


Color = Tuple[float, float, float]

class Element():
    def __init__(
        self,
        biome: float = 0.0,
        height: float = 0.0,
        character: str ='.',
        color: Color = (255, 255, 255),
        gradient_x: float = 0.0,
        gradient_y: float = 0.0
    ) -> None:
        self.biome = biome
        self.height = height
        self.character = character
        self.color = color
        self.gradient_x = gradient_x
        self.gradient_y = gradient_y


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
        out: Element,
    ) -> None: ...
