from reactpy import component, html, run

@component
def fragment():
    return html.ul(
        html._(
        html.h1("My Todo List"),
        html.img(
            {
                "src": "https://picsum.photos/id/0/500/300",
                "style": {"width":"30%"},
                "alt": "Random image"
            }
        ),
        html.ul(html.li("The first thing I need to do is ...")),
    ),
    html._(
        html.h1("My Todo List"),
        html.img(
            {
                "src": "https://picsum.photos/id/0/500/300",
                "style": {"width":"30%"},
                "alt": "Random image"
            }
        ),
        html.ul(html.li("The first thing I need to do is ...")),
    )
    )

run(fragment)