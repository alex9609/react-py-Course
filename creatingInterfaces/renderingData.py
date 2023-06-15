from reactpy import component, html, run

@component
def Datalist(items, filter_by_priority=None, sort_by_priority=False):
    if filter_by_priority is not None:
        items = [i for i in items if i["priority"] <= filter_by_priority]
    if sort_by_priority:
        items = sorted(items, key=lambda i: i["priority"])
    #Creando una lista de componentes que parten de un diccionario
    list_item_elements = [html.li({"key": i["id"]}, i["text"]) for i in items]
    # Retornando una lista desordenada, que contienen la lista de elementos creados anteriormente
    return html.ul(list_item_elements)

@component
def TodoList():
    tasks = [
        {"id": 1, "text": "Learn React", "priority": 5},
        {"id": 2, "text": "Learn ReactPy", "priority": 1},
        {"id": 3, "text": "Build something fun!", "priority": 2},
        {"id": 4, "text": "Go to the beach","priority": 1},
        {"id": 5, "text": "Buy a house","priority": 2},
        {"id": 6, "text": "Buy a car","priority": 1},
        {"id": 7, "text": "Buy a boat","priority": 5}
        ]
    return html.section(
        html.h1("My todo list"),
        Datalist(tasks, filter_by_priority=5,sort_by_priority=True)
    )

run(TodoList)