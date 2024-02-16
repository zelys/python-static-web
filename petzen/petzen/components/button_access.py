import reflex as rx
import petzen.styles.styles as style


def button_access(text: str, width: str) -> rx.Component:
    return rx.button(text, width=width, style=style.BUTTON_ACCESS)
