import reflex as rx
import petzen.styles.styles as style


def button_app(text: str, icon: str) -> rx.Component:
    return rx.button(
        rx.square(rx.text(text), rx.image(src=icon), gap=4), style=style.BUTTON_APP
    )
