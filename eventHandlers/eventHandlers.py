from reactpy import component, html, run


@component
def PrintButton(display_text,message_text):
    def handle_event(event):
        print(message_text)
    return html.div(
        html.button({"on_click":handle_event},display_text)
    )

@component
def LambdaButton(display_text,message_text):
    return html.div(
        html.button({"on_click":lambda event:print(message_text)},display_text)
    )

@component
def App():
    return html.div(
        PrintButton("Play","Playing"),
        PrintButton("Pause","Pause"),
        LambdaButton("Play lambda","LambdaButton Playing"),
    )


run(App)