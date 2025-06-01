from dash import Dash, Input, Output, html, dcc, callback, State

import back

app = Dash()

app.layout = html.Div(
    [
        html.Div(
            [html.H1("Мой проект по проверке цены БИТКОИНА", id="label_text")],
            id="label"
        ),
        html.Div(children=[f"Цена сейчас {back.back_main()} долларов"])
    ], id="main"
)

if __name__ == "__main__":
    app.run(debug="True")
