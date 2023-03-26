import dash
from dash import html

app = dash.Dash(__name__)
server = app.server


app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children=['''
        html.Div is intuitive enough to understand that it adds a html div element.''' ,
             html.A("More here", href='https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div', target='_blank')]),


    html.Div(children='''
        The above example also has a 'a' tag for creating an external link too! 
    '''),

    html.A("More here", href='https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a', target='_blank'),

    html.P('''Important thing to note is that you did not have to use HTML 
    instead used the Dash elements that are named similarly to get your job done. BTW this is a paragraph (p) element. 
    Follow the same documentation to learn more''')

])

if __name__ == '__main__':
    app.run_server(debug=True, port=8080)
