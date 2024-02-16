import reflex as rx
from petzen.pages.index import index
import petzen.styles.styles as style

# Create app instance and add index page.
app = rx.App(
    stylesheets=style.STYLESHEETS,
    style=style.BASE_STYLE,
)
# app.add_page(index)
