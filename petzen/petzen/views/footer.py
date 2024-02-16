import reflex as rx
from petzen.components.menu_footer import menu_footer
from petzen.components.contact_box import contact_box
from petzen.components.copyright import copy
from petzen.components.subscribe_footer import subscribe_footer
import petzen.styles.styles as style


def footer() -> rx.Component:
    return rx.box(
        menu_footer(),
        rx.flex(
            contact_box(),
            subscribe_footer(),
            margin="40px 0 25px 0",
        ),
        rx.divider(
            border_color="black",
        ),
        copy(),
        style=style.FOOTER,
    )
