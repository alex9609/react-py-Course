import asyncio

from reactpy import component, html, run

@component
def ButtonWithDelay(display_text, delay):
    async def handle_click(event):
        await asyncio.sleep(delay)
        print(display_text)
    return html.button({"on_click":handle_click},display_text)

@component
def App():
    return html.div(
        ButtonWithDelay("Print 4 seconds later",4),
        ButtonWithDelay("Print inmediately",0),
    )

run(App)