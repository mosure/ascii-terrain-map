import copy
from typing import List

from generators import terrain_height_generator, terrain_height_to_density_character, terrain_height_to_color
from output import print_state
from shared import GeneratorStep, State, Vector2


generator_steps: List[GeneratorStep] = [
    terrain_height_generator,
    terrain_height_to_density_character,
    terrain_height_to_color
]


def main() -> None:
    previous_state = State()

    for step in generator_steps:
        current_state = copy.deepcopy(previous_state)

        for x in range(previous_state.width):
            for y in range(previous_state.height):
                st = Vector2(x / previous_state.width, y / previous_state.height)
                coord = Vector2(x, y)

                out = current_state.elements[coord.x][coord.y]

                step(
                    st,
                    coord,
                    previous_state,
                    out,
                )

        previous_state = current_state

    print_state(previous_state)


if __name__ == '__main__':
    main()
