#for on hmtl is an attribute to specitfy the id of the element its associeted with
#In reactpy this is renamed to html_for
from reactpy import component, html, run

@component
def html_for():
    return html.div(
        html.label({"html_for":"todo"}, "Todo"),
        html.input({"id":"todo", "type":"text"})
    )