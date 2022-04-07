from dash import dcc, html, Input, Output, callback
from pageNavbar import create_mynavbar

thenav = create_mynavbar()

header = html.H3('Welcome to info page!')


def createpage_info():

    
 #   layout = html.Div([
 #       nav,
 #       header,
 #   ])

    layout = html.Div([thenav,
        html.H3('Page 1'),
        dcc.Dropdown(
            {f'Page 1 - {i}': f'{i}' for i in ['New York City', 'Montreal', 'Los Angeles']},
            id='page-1-dropdown'
        ),
        html.Div(id='page-1-display-value'),
        dcc.Link('Go to Page 2', href='/page2')
    ])


    @callback(
        Output('page-1-display-value', 'children'),
        Input('page-1-dropdown', 'value'))
    def display_value(value):
        return f'You have selected {value}'




    return layout






#layout = html.Div([
#    html.H3('Page 1'),
#    dcc.Dropdown(
#        {f'Page 1 - {i}': f'{i}' for i in ['New York City', 'Montreal', 'Los Angeles']},
#        id='page-1-dropdown'
#    ),
#    html.Div(id='page-1-display-value'),
#    dcc.Link('Go to Page 2', href='/page2')
#])


#@callback(
#    Output('page-1-display-value', 'children'),
#    Input('page-1-dropdown', 'value'))
#def display_value(value):
#    return f'You have selected {value}'