import reflex as rx
import petzen.styles.styles as style
from petzen.components.button_access import button_access

# Text section

title_section = "¡Tú y tu mascota están aún más conectados!"

txt_content = """Nuestra aplicación simplifica la vida del propietario, 
registra el historial de salud de su mascota, administra los gastos
mensuales y loconecta con una animada comunidad de dueños de mascotas."""

button_section = button_access("¡Ingresa ahora!", "230px")

image_cat = "img/cat_ilustration.png"


def section_c() -> rx.Component:
    return rx.flex(
        rx.hstack(
            rx.box(
                rx.box(title_section, style=style.TITLE_CARD),
                rx.box(txt_content, style=style.TEXT_CARD, margin_y="30px"),
                rx.hstack(button_section),
                w="70%",
                padding_x="60px",
            ),
            rx.box(rx.image(src=image_cat)),
            h="308px",
            bg="#EDE8E8",
        ),
        padding_y="80px",
    )
