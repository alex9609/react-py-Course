from reactpy import component, html, run

@component
def HelloWorld():
    return html.h1("Hello, world!")

run(HelloWorld)