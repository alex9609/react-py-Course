from reactpy import component, hooks, html, run

from pathlib import Path
import json

HERE = Path(__file__)
DATA = HERE.parent / "data.json"
sculptures = json.loads(DATA.read_text())


@component
def Gallery():
    index, set_index = hooks.use_state(0)

    def handle_click(event):
        set_index(index + 1)

    print(index)
    bound_index = index % len(sculptures)
    print(bound_index)
    sculpture = sculptures[bound_index]
    print(sculpture)
    alt = sculpture["alt"]
    artist = sculpture["artist"]
    description = sculpture["description"]
    name = sculpture["name"]
    ulr = sculpture["url"]

    return html.div(
        html.button({"on_click": handle_click}, "Next"),
        html.h2(name, " by ", artist),
        html.p(f"({bound_index + 1} of {len(sculptures)})"),
        html.img({"src": ulr, "alt": alt, "style": {"height": "200px"},}),
        html.p(description),
    )

run(Gallery)