import reflex as rx
import petzen.styles.styles as style
from petzen.components.button_app import button_app

img_iphone = "img/iphone.png"

apple_ico = "img/apple_icon.png"

title_section = "¡DESCARGA NUESTRA APLICACIÓN!"

info_content = [
    (
        "img/fi-rr-alarm-clock.png",
        "Alertas y recordatorios inteligentes",
        "Reciba notificaciones personalizadas sobre vacunas, citas veterinarias y otras necesidades, asegurándose de que nunca se pierda la atención esencial para su mascota.",
    ),
    (
        "img/fi-rr-apps.png",
        "Interfaz fácil de usar para todos",
        "Nuestra aplicación está diseñada para ser intuitiva, permitiendo que todos, independientemente de su experiencia digital, aprovechen al máximo las funciones de la aplicación.",
    ),
    (
        "img/fi-rr-confetti.png",
        "Diseño intuitivo y atractivo.",
        "Desfrute de uma interface visualmente agradável e fácil de navegar, projetada para proporcionar uma experiência fluida e atraente a cada usuário.",
    ),
]


def content(icon: str, title_txt: str, content_txt: str) -> rx.Component:
    return rx.box(
        rx.flex(
            rx.square(rx.image(src=icon, w="20px")),
            rx.box(rx.text(title_txt, style=style.TITLE_CARD)),
            gap=2,
        ),
        rx.box(rx.text(content_txt, style=style.TEXT_CARD, margin_y="10px")),
    )


def section_d() -> rx.Component:
    return rx.responsive_grid(
        rx.box(
            rx.image(
                src=img_iphone,
                w="430px",
            ),
            w="90%",
        ),
        rx.box(
            rx.box(title_section, text_align="left", style=style.TITLE_SECTION),
            rx.box(
                # generate content
                *[
                    content(icon, title_txt, content_txt)
                    for icon, title_txt, content_txt in info_content
                ],
                margin_y="40px",
            ),
            rx.box(button_app("Descargar App", apple_ico)),
        ),
        columns=[1, 2],
    )
