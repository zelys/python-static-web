import reflex as rx
from petzen.components.about import about
import petzen.styles.styles as style

title_tips = (
    "¡Aprende consejos esenciales para darle a tu mascota el confort que se merece!"
)

images = [
    "img/icon001.png",
    "img/icon002.png",
    "img/icon003.png",
    "img/icon004.png",
    "img/icon005.png",
    "img/icon006.png",
]

titles = [
    "Adiestramiento",
    "Alimentación",
    "Adopción",
    "Salud",
    "Cuidado",
    "Curiosidades",
]

descriptions = [
    "Corrija conductas, eduque, diviértase y fortalezca la relación con su mascota.",
    "Descubre dietas equilibradas, aprende sobre dietas caseras, elige la mejor comida y mucho más.",
    "Descubre nombres encantadores, consejos, qué hacer y todo lo que necesitas saber para adoptar una mascota.",
    "Aprende todo lo que necesitas saber sobre la salud de tu mascota y protégela de enfermedades.",
    "Comprenda el calor, el embarazo, la higiene dental, el cuidado de los oídos y mucho más.",
    "Aprende consejos, descubre especies en peligro de extinción, aprende sobre diferentes razas y mucho más.",
]

advice_a = about(images[0], titles[0], descriptions[0])
advice_b = about(images[1], titles[1], descriptions[1])
advice_c = about(images[2], titles[2], descriptions[2])
advice_d = about(images[3], titles[3], descriptions[3])
advice_e = about(images[4], titles[4], descriptions[4])
advice_f = about(images[5], titles[5], descriptions[5])


def section_b() -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(title_tips, style=style.TITLE_SECTION),
            margin="40px 40px 0 40px",
        ),
        rx.center(
            rx.responsive_grid(
                advice_a.advice(),
                advice_b.advice(),
                advice_c.advice(),
                advice_d.advice(),
                advice_e.advice(),
                advice_f.advice(),
                columns=[3],
                spacing="20",
            ),
            padding_y="40px",
        ),
    )
