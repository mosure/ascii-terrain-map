import colorsys
import math
import random

from noise import pnoise2

from shared import Element, State, Vector2



noise_x_seed = random.random() * 1000
noise_y_seed = random.random() * 1000


def terrain_height_generator(
    st: Vector2,
    coord: Vector2,
    previous: State,
    current: State,
    out: Element,
) -> None:
    noise_scale = 1.8
    height_scale = 2.1

    noise_st = st * noise_scale

    out.height = pnoise2(
        noise_st.x + noise_x_seed,
        noise_st.y + noise_y_seed,
        octaves=4,
    ) * height_scale


def terrain_height_to_density_character(
    st: Vector2,
    coord: Vector2,
    previous: State,
    current: State,
    out: Element,
) -> None:
    ascii_character_density: str = '.:-=+*#%@'

    clamped_height = max(0, min(1, abs(out.height)))
    out.character = ascii_character_density[
        math.floor(clamped_height * (len(ascii_character_density) - 1))
    ]


def terrain_height_to_color(
    st: Vector2,
    coord: Vector2,
    previous: State,
    current: State,
    out: Element,
) -> None:
    sea_level = 0.0
    beach_level = 0.05
    grass_level = 0.7
    snow_level = 0.95

    if out.height < sea_level:
        out.color = 'cyan'
    elif out.height < beach_level:
        out.color = 'yellow'
    elif out.height < grass_level:
        out.color = 'green'
    elif out.height < snow_level:
        out.color = 'grey'
    else:
        out.color = 'white'
