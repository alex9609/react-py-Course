from reactpy import component, html, run



@component
def photo(alt_text,image_id):
    return html.img(
        {
            "src": f"https://picsum.photos/id/{image_id}/500/300",
            "style": {"width":"50%"},
            "alt": alt_text,
        }
    )

@component
def Gallery():
    return html.section(
        html.h1("Gallery"),
        photo("Landscape",image_id=830),
        photo("City",image_id=274),
        photo("Puppy",image_id=237)
    )

run(Gallery)