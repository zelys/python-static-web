import reflex as rx

# icon unicode
copy_ico = "\u00A9"


def copy() -> rx.Component:
    return rx.box(
        rx.text(
            copy_ico, " 2023 Desarrollado por Zelys. Todos los derechos reservados."
        ),
        margin="40px 0 0 0",
    )
