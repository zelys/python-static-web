import reflex as rx


def button_sub(text: str) -> rx.Component:
    return rx.button(
        text,
        w="100%",
        h="68px",
        font_weight="400",
        border_radius="14px",
    )
