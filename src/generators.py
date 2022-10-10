import colorsys
import math
import random

from noise import pnoise2

from shared import Element, State, Vector2


noise_x_seed = 0
noise_y_seed = 0

def set_seed(seed) -> None:
    global noise_x_seed, noise_y_seed

    noise_x_seed = seed * 1000
    noise_y_seed = seed * 1000


def terrain_height_generator(
    st: Vector2,
    coord: Vector2,
    previous: State,
    out: Element,
) -> None:
    noise_scale = 1.8
    height_scale = 2.3

    noise_st = st * noise_scale + Vector2(noise_x_seed, noise_y_seed)

    def noise(st: Vector2) -> float:
        return pnoise2(
            st.x,
            st.y,
            octaves=4,
        ) * height_scale

    st_delta_x = Vector2(0.01, 0.0)
    st_delta_y = Vector2(0.0, 0.01)

    out.height = noise(noise_st)
    out.gradient_x = noise(noise_st + st_delta_x) - out.height
    out.gradient_y = noise(noise_st + st_delta_y) - out.height


def terrain_height_to_density_character(
    st: Vector2,
    coord: Vector2,
    previous: State,
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
    out: Element,
) -> None:
    def map(value, start1, stop1, start2, stop2):
        return start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1))

    hue = 240
    sat = 0.5
    lit = 0.5

    sea_level = 0.0
    beach_level = 0.05
    grass_level = 0.7
    snow_level = 0.95

    if out.height < sea_level:
        sat = 1
        hue = map(out.height, -1, sea_level, 230, 175)
        lit = map(out.height, -1, sea_level, 0.2, 0.6)
    elif out.height < beach_level:
        hue = 57
        sat = 0.7
        lit = 0.7
    elif out.height < grass_level:
        hue = map(out.height, beach_level, grass_level, 120, 90)
        lit = map(out.height, beach_level, grass_level, 0.6, 0.2)
    elif out.height < snow_level:
        hue = 120
        lit = 0.3
        sat = map(out.height, grass_level, snow_level, 0.1, 0)
    else:
        lit = 1.0

    rgb = colorsys.hls_to_rgb(hue / 360, lit, sat)
    out.color = (rgb[0] * 255, rgb[1] * 255, rgb[2] * 255)


def shoreline_gradient_edge(
    st: Vector2,
    coord: Vector2,
    previous: State,
    out: Element,
) -> None:
    shoreline_height = 0.07

    if out.height < 0 or out.height > shoreline_height:
        return

    gradient_chars = [
        ['/', '-', '\\'],
        ['|', out.character, '|'],
        ['\\', '-', '/'],
    ]

    def gradient_to_index(x):
        epsilon = 0.01
        if x < -epsilon:
            return 0
        elif x > epsilon:
            return 2

        return 1

    gradient_row = gradient_to_index(out.gradient_y)
    gradient_col = gradient_to_index(out.gradient_x)

    out.character = gradient_chars[gradient_row][gradient_col]
