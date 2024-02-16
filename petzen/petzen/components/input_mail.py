import reflex as rx
import petzen.styles.styles as style
from petzen.styles.colors import Color


def input_mail(text: str) -> rx.Component:
    return rx.input(
        type_="email",
        placeholder=text,
        h="68px",
        border_radius="14px",
        focus_border_color=Color.FOCUS.value,
    )
