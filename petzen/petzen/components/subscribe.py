import reflex as rx
import petzen.styles.styles as style
from petzen.styles.colors import Color

# Components

input_email = rx.input(
    type_="email",
    placeholder="Email",
    h="68px",
    border_radius="14px",
    focus_border_color=Color.FOCUS.value,
    style=style.INPUT,
)

button_sub = rx.button(
    "Suscríbete al boletín",
    w="100%",
    h="68px",
    font_weight="400",
    border_radius="14px",
)

# CSS

style_square = dict(
    gap="4",
    h="100%",
    padding_x="40px",
)

style_box = dict(
    bg="#ffffff",
    w="700px",
    h="160px",
    border_radius="14px",
)


def subscribe() -> rx.Component:
    return rx.box(
        rx.square(input_email, button_sub, style=style_square), style=style_box
    )
