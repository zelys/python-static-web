import reflex as rx
import petzen.styles.styles as style
from petzen.styles.colors import Color

section_title = "¡No te pierdas nuestras actualizaciones!"

section_text = "Regístrate para recibir noticias, nuevas herramientas, descuentos, actualizaciones..."

list_txt = [
    ("01", "Reciba actualizaciones de primera mano"),
    ("02", "Obtener cupones de descuento"),
    ("03", "Leer artículos sobre temas relevantes."),
]

text_form = "Introduce tu correo electrónico..."

dog_img = "img/dog.png"

input_reg = rx.input(
    placeholder=text_form,
    type_="email",
    h="60px",
    border_radius="30px",
    focus_border_color=Color.FOCUS.value,
    style=style.BASE_STYLE,
)

button_reg = rx.button(
    rx.icon(tag="chevron_right"),
    w="60px",
    h="60px",
    style=style.BUTTON_ACCESS,
)


def list_info(num: str, txt: str):
    return rx.list(
        rx.list_item(
            rx.flex(
                rx.center(
                    num,
                    w="35px",
                    h="35px",
                    bg="#FDF0C9",
                    border_radius="10px",
                ),
                rx.square(txt),
                style=style.TEXT_CARD,
                margin_y="1rem",
                gap=2,
            ),
        ),
    )


def section_f() -> rx.Component:
    return rx.flex(
        rx.box(
            rx.box(section_title, style=style.TITLE_SECTION, text_align="left"),
            rx.box(
                section_text, style=style.TITLE_CARD, font_weight="300", margin_y="10px"
            ),
            # generate list
            rx.box(*[list_info(num, txt) for num, txt in list_txt]),
            # input email
            rx.flex(
                rx.box(input_reg, w="80%"),
                rx.square(button_reg),
                margin_top="20px",
                gap=1,
            ),
            padding="10px 40px 36px 100px",
        ),
        rx.box(rx.image(src=dog_img)),
        gap="8",
        color="#323232",
        padding="40px",
    )
