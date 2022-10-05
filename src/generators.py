import colorsys
import math
import random

from noise import pnoise2

from shared import State, Vector2



noise_x_seed = random.random() * 1000
noise_y_seed = random.random() * 1000


def terrain_height_generator(
    st: Vector2,
    coord: Vector2,
    previous: State,
    current: State,
) -> None:
    element = current.elements[coord.x][coord.y]

    noise_scale = 1.8
    height_scale = 2.1

    noise_st = st * noise_scale

    element.height = pnoise2(
        noise_st.x + noise_x_seed,
        noise_st.y + noise_y_seed,
        octaves=4,
    ) * height_scale


def terrain_height_to_density_character(
    st: Vector2,
    coord: Vector2,
    previous: State,
    current: State,
) -> None:
    ascii_character_density: str = '.:-=+*#%@'

    element = current.elements[coord.x][coord.y]

    clamped_height = max(0, min(1, abs(element.height)))
    element.character = ascii_character_density[
        math.floor(clamped_height * (len(ascii_character_density) - 1))
    ]


def terrain_height_to_color(
    st: Vector2,
    coord: Vector2,
    previous: State,
    current: State,
) -> None:
    element = current.elements[coord.x][coord.y]

    sea_level = 0.0
    beach_level = 0.05
    grass_level = 0.7

    if element.height < sea_level:
        element.color = 'cyan'
    elif element.height < beach_level:
        element.color = 'yellow'
    elif element.height < grass_level:
        element.color = 'green'
    else:
        element.color = 'grey'
