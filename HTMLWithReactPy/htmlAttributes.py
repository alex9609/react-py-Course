# Exist a differences between the way of we represent the css attributes and the class_name of the attributes
from reactpy import component, html, run

@component
def HTMLAtributtes():
    tags =  html.div(
        {"class_name":"container"},
        html.h1({"class_name":"title"}, "My todo list"),
        html.ul(
            {"class_name": "list"},
            html.li({"class_name":"item"},"Design a cool new app"),
            html.li({"class_name":"item"},"Build it"),
            html.li({"class_name":"item"},"Share it with the world!"),
        )
    )

    return tags

run(HTMLAtributtes)