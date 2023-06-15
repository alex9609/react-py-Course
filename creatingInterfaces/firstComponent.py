from reactpy import component, html, run

@component
def photo():
    return html.img(
        {
            "src": "https://picsum.photos/id/237/500/300",
            "style": {"width":"50%"},
            "alt": "React logo"
        }
    )

run(photo)