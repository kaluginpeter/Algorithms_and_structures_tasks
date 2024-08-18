# Your task in this Kata is to emulate text justification in monospace font. You will be given a single-lined text and the expected justification width. The longest word will never be greater than this width.
#
# Here are the rules:
#
# Use spaces to fill in the gaps between words.
# Each line should contain as many words as possible.
# Use '\n' to separate lines.
# Last line should not terminate in '\n'
# '\n' is not included in the length of a line.
# Gaps between words can't differ by more than one space.
# Lines should end with a word not a space.
# Large gaps go first, then smaller ones ('Lorem--ipsum--dolor--sit-amet,' (2, 2, 2, 1 spaces)).
# Last line should not be justified, use only one space between words.
# Lines with one word do not need gaps ('somelongword\n').
# Example with width=30:
#
# Lorem  ipsum  dolor  sit amet,
# consectetur  adipiscing  elit.
# Vestibulum    sagittis   dolor
# mauris,  at  elementum  ligula
# tempor  eget.  In quis rhoncus
# nunc,  at  aliquet orci. Fusce
# at   dolor   sit   amet  felis
# suscipit   tristique.   Nam  a
# imperdiet   tellus.  Nulla  eu
# vestibulum    urna.    Vivamus
# tincidunt  suscipit  enim, nec
# ultrices   nisi  volutpat  ac.
# Maecenas   sit   amet  lacinia
# arcu,  non dictum justo. Donec
# sed  quam  vel  risus faucibus
# euismod.  Suspendisse  rhoncus
# rhoncus  felis  at  fermentum.
# Donec lorem magna, ultricies a
# nunc    sit    amet,   blandit
# fringilla  nunc. In vestibulum
# velit    ac    felis   rhoncus
# pellentesque. Mauris at tellus
# enim.  Aliquam eleifend tempus
# dapibus. Pellentesque commodo,
# nisi    sit   amet   hendrerit
# fringilla,   ante  odio  porta
# lacus,   ut   elementum  justo
# nulla et dolor.
# Also you can always take a look at how justification works in your text editor or directly in HTML (css: text-align: justify).
#
# Have fun :)
#
# STRINGSALGORITHMS
# Solution
def calc_whitespaces(count_spaces: int, needed_spaces: int) -> list[int]:
    if needed_spaces == 0: return count_spaces
    if count_spaces % needed_spaces == 0:
        return [count_spaces // needed_spaces for _ in range(needed_spaces)]
    space_size: int = 1
    while needed_spaces * space_size < count_spaces:
        space_size += 1
    output: list[int] = [space_size for _ in range(needed_spaces)]
    for idx in range(-1, -(space_size * needed_spaces - count_spaces) - 1, -1):
        output[idx] -= 1
    return output


def create_sentence(whitespaces: list[int], words: list[str]) -> str:
    if len(words) == 1: return words[0]
    output: list[str] = list()
    for _ in range(len(whitespaces)):
        if not output:
            output.append(words.pop(0))
        output.append(' ' * whitespaces.pop(0))
        output.append(words.pop(0))
    return ''.join(output)


def justify(text, width):
    if not text: return ''
    output: list[str] = list()
    top: list[str] = list()
    top_len: int = 0
    space_len: int = 0
    for word in text.split(' '):
        if top_len + len(word) + (space_len if (top and len(top) < 1) else space_len + 1) <= width:
            top_len += len(word)
            top.append(word)
            space_len = len(top) - 1
        else:
            space_len += width - (top_len + space_len)
            whitespaces: list[int] = calc_whitespaces(space_len, len(top) - 1)
            sentence: str = create_sentence(whitespaces, top)
            output.append(sentence)

            space_len = 0
            top_len = len(word)
            top = [word]

    whitespaces: list[int] = calc_whitespaces(space_len, len(top) - 1)
    sentence: str = create_sentence(whitespaces, top)
    output.append(sentence)
    return '\n'.join(output)