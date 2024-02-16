import reflex as rx

from petzen.components.navbar import navbar
from petzen.components.logo import petzen

social_icon = ["img/tw-icon.png", "img/fb-icon.png", "img/lk-icon.png"]


def icon_bar(icon: str):
    return rx.image(src=icon)


def menu_footer() -> rx.Component:
    return rx.flex(
        rx.square(petzen, font_size="2.8rem"),
        rx.spacer(),
        rx.square(
            navbar(),
        ),
        rx.spacer(),
        rx.square(
            *[icon_bar(icon) for icon in social_icon],
            gap=4,
        ),
    )
