import reflex as rx
import petzen.styles.styles as style
from petzen.views.header import header
from petzen.views.section_a import section_a
from petzen.views.section_b import section_b
from petzen.views.section_c import section_c
from petzen.views.section_d import section_d
from petzen.views.section_e import section_e
from petzen.views.section_f import section_f
from petzen.views.footer import footer


@rx.page(
    title="Pet Zen",
    description="A beautiful landing page",
)
def index() -> rx.Component:
    return rx.box(
        header(),
        rx.center(
            rx.box(
                section_a(),
                section_b(),
                section_c(),
                section_d(),
                section_e(),
                section_f(),
                footer(),
                style=style.MAIN,
            ),
        ),
    )
