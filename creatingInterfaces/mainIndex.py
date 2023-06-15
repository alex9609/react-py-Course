#HTML with ReactPy
from reactpy import component, html, run

@component
def prove():
    return html.div(
    html.h1("My todo list"),
    html.ul(
        html.li("Design a cool new app"),
        html.li("Build it"),
        html.li("Share it with the world!")
    )
)

run(prove)