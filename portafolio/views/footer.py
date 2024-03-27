import reflex as rx
from portafolio.components.media import media
from portafolio.data import Media
from portafolio.styles.styles import Size


def footer(data: Media) -> rx.Component:
    return rx.vstack(
        rx.text("© 2024 - Portafolio por Juan Manuel Guerrero"),
        media(data),
        spacing=Size.SMALL.value
    )
