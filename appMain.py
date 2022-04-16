from dash import Dash, dcc, html, Input, Output, callback
# hello

import pageInfo, pagePlots, pageHome
import dash_bootstrap_components as dbc

from pageHome import createpage_home
from pageInfo import createpage_info
from pagePlots import createpage_plots

import pandas as pd

import os
from config.definitions import ROOT_DIR

app = Dash(__name__, suppress_callback_exceptions=True,external_stylesheets=[dbc.themes.BOOTSTRAP])
#app = dash.Dash(...)
#server = app.server



app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':           # page root is home page
        # pageHome.layout
        return createpage_home()
    elif pathname == '/page1':    # page 1 is info page
        #return pageInfo.layout    #  with   return   file . laout  the full page loads (not inside)
        return createpage_info()
    elif pathname == '/page2':    # page 2 is plots page
        #return pagePlots.layout
        return createpage_plots()
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)

