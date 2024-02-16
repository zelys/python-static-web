import reflex as rx

import petzen.styles.styles as style
from petzen.styles.fonts import Font


def Create_logo(normal_text: str, higlight_text: str) -> rx.Component:
    return rx.text(
        normal_text,
        rx.span(
            higlight_text,
            style=style.HIGHLIGHT_MAIN,
        ),
        font_family=Font.LOGO.value,
    )


petzen = Create_logo("Pet ", "Zen")
