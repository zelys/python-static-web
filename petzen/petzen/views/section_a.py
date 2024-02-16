import reflex as rx
from petzen.components.button_access import button_access
import petzen.styles.styles as style

button_main = button_access("Ingresar", "290px")

text_main = rx.text(
    "El mejor soporte de atención para tu ",
    rx.span("mejor amigo", style=style.HIGHLIGHT_MAIN),
    style=style.TEXT_MAIN,
)

text_content = "Aquí encontrarás respuesta a todas tus dudas, desde elegir la mejor comida hasta consejos imprescindibles para garantizar el bienestar de tu peludo compañero."

image = rx.image(src="img/pets.png")


def section_a() -> rx.Component:
    return rx.flex(
        rx.box(
            rx.box(text_main),
            rx.box(
                text_content,
                style=style.TITLE_CARD,
                font_weight="300",
                margin_y="20px",
                w="80%",
            ),
            rx.box(button_main),
            w="60%",
        ),
        rx.square(image, w="40%"),
        gap=8,
        margin_bottom="100px",
    )
