import reflex as rx


def navbar() -> rx.Component:
    return rx.square(
        rx.menu(
            rx.menu_button("Inicio"),
            rx.menu_button("Acerca de"),
            rx.menu_button("Servicios"),
            rx.menu_button("Nuestra App"),
            rx.menu_button("Blog"),
        ),
        gap=8,
    )
