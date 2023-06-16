from reactpy import component, html, run

#We can use html._ fragment to group elements together

@component
def MyTodoList():
    return html._(
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

run(MyTodoList)