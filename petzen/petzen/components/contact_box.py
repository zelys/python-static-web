import reflex as rx

contact = dict(
    title="Entre en contacto:",
    email="Email: email@gmail.com",
    phone="Teléfono: 73 9 9999-9999",
    address="Dirección:",
)


def contact_box() -> rx.Component:
    return rx.box(
        rx.text(
            rx.span(
                contact["title"],
                bg="#FBBC05",
                border_radius="4px",
                padding="4px",
            ),
        ),
        rx.box(
            rx.text(contact["email"]),
            rx.text(contact["phone"]),
            rx.text(contact["address"]),
            margin_y="1rem",
            line_height="2.8rem",
        ),
        w="40%",
    )
