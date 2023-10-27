import reflex as rx

from app import style
from app.state import State




def chat() -> rx.Component:
    return rx.box(
        rx.text(State.chat_history, style=style.question_style)
        #rx.foreach(
        #    State.chat_history,
        #    lambda messages: qa(messages[0], messages[1]),
        #)
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.question,
            placeholder="Put in a review...",
            on_change=State.set_question,
            style=style.input_style,
        ),
        rx.button(
            "Ask",
            on_click=State.answer,
            style=style.button_style,
        ),
    )
color = "rgb(107,99,246)"

#def upload():
#    """The main view."""
#    return rx.vstack(
#        rx.upload(
#            rx.vstack(
#                rx.button(
#                    "Select File",
#                    color=color,
#                    bg="white",
#                    border=f"1px solid {color}",
#                ),
#                rx.text(
#                    "Drag and drop files here or click to select files"
#                ),
#            ),
#            border=f"1px dotted {color}",
#            padding="5em",
#        ),
#        rx.hstack(rx.foreach(rx.selected_files, rx.text)),
#        rx.button(
#            "Upload",
#            on_click=lambda: State.handle_upload(
#               rx.upload_files()
#            ),
#        ),
#        rx.button(
#            "Clear",
#            on_click=rx.clear_selected_files,
#        ),
#        rx.foreach(
#            State.img, lambda img: rx.image(src=img)
#        ),
#        padding="5em",
#    )

def index() -> rx.Component:
    return rx.container(
        action_bar(),
        chat(),
    )


app = rx.App()
app.add_page(index)
app.compile()





