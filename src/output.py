from shared import Color, State


def cprint(text: str, color: Color, end: str = '\n') -> None:
    print(f'\x1b[38;2;{int(color[0])};{int(color[1])};{int(color[2])}m{text}\x1b[0m', end=end)


def print_state(state: State) -> None:
    print('-' * (state.width + 2))

    for y in range(state.height):
        print('|', end='')
        for x in range(state.width):
            element = state.elements[x][y]
            cprint(element.character, element.color, end='')
        print('|')

    print('-' * (state.width + 2))
