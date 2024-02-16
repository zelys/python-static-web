import reflex as rx
import petzen.styles.styles as style

img_social = "img/social_icon.png"


def comment_card(image: str, name: str, role: str, comment: str) -> rx.Component:
    return rx.box(
        rx.flex(
            rx.box(
                rx.image(
                    src=image,
                ),
                w="80px",
            ),
            rx.box(
                rx.text(name),
                rx.text(role, font_weight="400"),
                style=style.TITLE_CARD,
                font_size="1em",
                margin_left="0.5rem",
                align_self="end",
            ),
            rx.spacer(),
            rx.box(
                rx.image(
                    src=img_social,
                ),
            ),
        ),
        rx.divider(
            border_color="black",
            margin_y="20px",
        ),
        rx.box(rx.text(comment, style=style.TEXT_CARD)),
        style=style.CARD_COMMENT,
    )
