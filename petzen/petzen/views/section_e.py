import reflex as rx
from petzen.components.comment_card import comment_card
from petzen.styles.fonts import Font
import petzen.styles.styles as style

title_section = rx.text(
    "¡Descubra lo que piensan los usuarios de ",
    rx.span("Pet ", font_family=Font.LOGO.value),
    rx.span("Zen", style=style.HIGHLIGHT_MAIN),
    " sobre la aplicación!",
)


comment_content = [
    (
        "img/picture01.png",
        "Carlos Santana",
        "Tutor de gato",
        "La aplicación simplificó el entrenamiento y me mantuvo actualizado sobre la salud de mi amigo peludo. Nunca ha sido tan fácil brindarle lo mejor. ¡Se lo recomiendo a todos los amantes de los animales!",
    ),
    (
        "img/picture02.png",
        "Giovanna Lima",
        "Tutora de cachorro",
        "Desde que comencé a usar la aplicación, noté un cambio positivo en el comportamiento de mi mascota. ¡Los consejos de entrenamiento son valiosos!",
    ),
    (
        "img/picture03.png",
        "Regina Santos",
        "Tutora de gato",
        "La aplicación no sólo me recuerda las vacunas y las citas, sino que también me conecta con una increíble comunidad de amantes de los animales.",
    ),
]


def section_e() -> rx.Component:
    return rx.box(
        rx.box(title_section, style=style.TITLE_SECTION),
        rx.center(
            # generate cards
            *[
                comment_card(image, name, role, comment)
                for image, name, role, comment in comment_content
            ],
            gap="8",
            margin_y="40px",
        ),
    )
