import reflex as rx
from petzen.components.button_access import button_access
from petzen.components.navbar import navbar
from petzen.components.logo import petzen

button_header = button_access("Ingresar", "204px")


def header() -> rx.Component:
    return rx.square(
        rx.flex(
            rx.square(petzen, font_size="3.7rem"),
            rx.spacer(),
            rx.square(
                navbar(),
            ),
            rx.spacer(),
            rx.square(button_header),
            style=style_flex,
        ),
        w="100%",
        position="fixed",
        bg="#ffffff",
        z_index="999",
    )


# CSS

style_flex = dict(
    width="1200px",
    h="130px",
)
