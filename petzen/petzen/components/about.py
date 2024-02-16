import reflex as rx

import petzen.styles.styles as style


class about:
    def __init__(self, icon, title, description):
        self.icon = icon
        self.title = title
        self.description = description

    def advice(self) -> rx.Component:
        return rx.box(
            rx.center(
                rx.image(src=self.icon),
            ),
            rx.box(rx.text(self.title, style=style.TITLE_CARD), margin_y="8px"),
            rx.box(rx.text(self.description), style=style.TEXT_CARD),
            style=style.ABOUT_BOX,
        )
