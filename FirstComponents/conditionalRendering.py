from reactpy import component, html, run

@component
def Item(name, done):
    return html.li(name, "✔" if done else "❌")

@component
def TodoList():
    return html.section(
        html.h1("My Todo List"),
        Item("Learn React", done=True),
        Item("Learn ReactPy", done=True),
        Item("Build something awesome", done=False)
    )

run(TodoList)
