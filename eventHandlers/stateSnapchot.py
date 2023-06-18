import asyncio

from reactpy import component, event, use_state, html, run

@component
def App():
    recipient, set_recipient = use_state("Alice")
    message, set_message = use_state("")

    @event(prevent_default=True)
    async def handle_submit(event):
        set_message("")
        print("About to send a message to...")
        await asyncio.sleep(0.5)
        print(f"Sent {message} to {recipient}")

    return html.form(
        {"on_submit": handle_submit,"style": {"display": "inline-grid"}},
        html.label(
            {},
            "To: ",
            html.select(
                {
                    "value": recipient,
                    "on_change": lambda event: set_recipient(event["target"]["value"]),
                },
                html.option({"value": "Alice"}, "Alice"),
                html.option({"value": "Bob"}, "Bob"),
                html.option({"value": "Carol"}, "Carol"),
            ),
        ),
        html.input(
            {
                "type": "text",
                "placeholder": "Message",
                "value": message,
                "on_change": lambda event: set_message(event["target"]["value"]),
            }
        ),
        html.button({"type": "submit"}, "Send"),
    )

run(App)