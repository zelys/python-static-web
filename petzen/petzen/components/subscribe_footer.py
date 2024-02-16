import reflex as rx
from petzen.components.button_sub import button_sub
from petzen.components.input_mail import input_mail


def subscribe_footer() -> rx.Component:
    return rx.box(
        rx.square(
            input_mail("Email"),
            button_sub("Suscríbete al boletín"),
            gap="4",
            h="100%",
            padding_x="40px",
        ),
        bg="#ffffff",
        w="700px",
        h="160px",
        border_radius="14px",
    )
