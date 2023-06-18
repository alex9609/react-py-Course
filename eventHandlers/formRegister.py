import asyncio

from reactpy import component, html, run, use_state, event

@component
def App():
    name, set_name = use_state("")
    lastname, set_lastname = use_state("")
    phone, set_phone = use_state("")
    email, set_email = use_state("")
    university, set_university = use_state("")


    @event(prevent_default=True)
    async def handle_submit(event):
        set_name("")
        set_lastname("")
        set_phone("")
        set_email("")
        set_university("")
        print("About to send a form to...")
        await asyncio.sleep(0.5)
        print(f"Name: {name}")
        print(f"Lastname: {lastname}")
        print(f"Phone: {phone}")
        print(f"Email: {email}")
        print(f"University: {university}")

    return html.form(
        {"on_submit": handle_submit,"style": {"display": "inline-grid"}},
        html.input(
            {
                "type": "text",
                "placeholder": "name",
                "value": name,
                "on_change": lambda event: set_name(event["target"]["value"]),
            }
        ),
        html.input(
            {
                "type": "text",
                "placeholder": "lastname",
                "value": lastname,
                "on_change": lambda event: set_lastname(event["target"]["value"]),
            }
        ),
        html.input(
            {
                "type": "text",
                "placeholder": "phone",
                "value": phone,
                "on_change": lambda event: set_phone(event["target"]["value"]),
            }
        ),
        html.input(
            {
                "type": "text",
                "placeholder": "email",
                "value": email,
                "on_change": lambda event: set_email(event["target"]["value"]),
            }
        ),
        html.input(
            {
                "type": "text",
                "placeholder": "university",
                "value": university,
                "on_change": lambda event: set_university(event["target"]["value"]),
            }
        ),
        html.button({"type": "submit"}, "Send"),
    )

run(App)