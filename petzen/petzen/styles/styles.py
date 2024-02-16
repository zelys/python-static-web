import reflex as rx
from enum import Enum
from .fonts import Font, FontWeight
from .colors import Color, TextColor

# Constants

MAX_WIDTH = "1200px"

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Paytone+One&display=swap",
    "https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&family=Paytone+One&display=swap",
    "https://fonts.googleapis.com/css2?family=Alata&family=Open+Sans:ital,wght@0,300..800;1,300..800&family=Paytone+One&display=swap",
]

# Sizes


class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.3em"
    BIG = "2em"
    VERY_BIG = "4em"


BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.MEDIUM.value,
    "font_size": Size.DEFAULT.value,
}

MAIN = dict(
    max_width="1200px",
    position="absolute",
    top=210,
    margin_y="20px",
    font_family="open_sans",
)

BUTTON_ACCESS = dict(
    bg=Color.BTN.value,
    font_family=Font.DEFAULT.value,
    color=TextColor.BTN_TXT.value,
    font_size=Size.LARGE.value,
    font_weight=FontWeight.BOLD.value,
    border_radius="3.6rem",
    height="68px",
)

BUTTON_APP = dict(
    font_family=Font.DEFAULT.value,
    font_weight=FontWeight.BOLD.value,
    bg=Color.BACKGROUND.value,
    w="230px",
    h="60px",
    box_shadow="1px 1px 4px 0px rgba(0,0,0,0.75)",
)

TEXT_MAIN = dict(
    font_family=Font.TITLE_MAIN.value,
    color=Color.PRIMARY.value,
    font_size=Size.VERY_BIG.value,
    line_height=Size.LARGE.value,
)

HIGHLIGHT_MAIN = {"font_family": Font.LOGO.value, "color": Color.BTN.value}


TITLE_SECTION = dict(
    font_family=Font.DEFAULT.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.BIG.value,
    line_height=Size.LARGE.value,
    text_align="center",
)

ABOUT_BOX = dict(
    width="300px",
    height="230px",
    text_align="center",
    padding_y="24px",
    padding_x="36px",
    border="none",
    border_radius="8px",
    box_shadow="0px 4px 4px 2px rgba(0,0,0,0.25)",
)

TITLE_CARD = dict(
    font_family=Font.DEFAULT.value,
    font_weight=FontWeight.BOLD.value,
    font_size=Size.LARGE.value,
)

TEXT_CARD = dict(
    font_family=Font.DEFAULT.value,
    font_size=Size.MEDIUM.value,
)

CARD_COMMENT = dict(
    padding_y="35px",
    padding_x="35px",
    width="340px",
    height="340px",
    color="#323232",
    border="1px solid",
    border_radius="45px",
    box_shadow="0px 4px 4px 2px rgba(0,0,0,0.25)",
)

FOOTER = dict(
    font_family=Font.DEFAULT.value,
    font_size=Size.DEFAULT.value,
    bg=Color.CONTENT.value,
    border_radius="30px 30px 0 0",
    padding="55px 60px 50px 60px",
)
