# Usando componentes
from reactpy import component, html, run

@component
def photo():
    return html.img(
        {
            "src": "https://picsum.photos/id/237/500/300",
            "style": {"width":"30%"},
            "alt": "Random image"
        }
    )

@component
def Gallery():
    return html.section(
        html.h1("Gallery"),
        photo(),
        photo(),
        photo()
    )

run(Gallery)