import copy
from typing import List

import colorama
colorama.init()
from termcolor import cprint

from generators import terrain_height_generator, terrain_height_to_density_character, terrain_height_to_color
from shared import GeneratorStep, State, Vector2



generator_steps: List[GeneratorStep] = [
    terrain_height_generator,
    terrain_height_to_density_character,
    terrain_height_to_color
]


def print_state(state: State) -> None:
    print('-' * (state.width + 2))

    for y in range(state.height):
        print('|', end='')
        for x in range(state.width):
            element = state.elements[x][y]
            cprint(element.character, element.color, end='')
        print('|')

    print('-' * (state.width + 2))


def main() -> None:
    previous_state = State()

    for step in generator_steps:
        current_state = copy.deepcopy(previous_state)

        for x in range(previous_state.width):
            for y in range(previous_state.height):
                st = Vector2(x / previous_state.width, y / previous_state.height)
                xy = Vector2(x, y)

                step(
                    st,
                    xy,
                    previous_state,
                    current_state
                )

        previous_state = current_state

    print_state(previous_state)


if __name__ == '__main__':
    main()
