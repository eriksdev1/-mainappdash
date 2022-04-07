from click import style
from dash import dcc, html, Input, Output, callback
from pageNavbar import create_mynavbar
import dash_bootstrap_components as dbc
import plotly.express as px
from datetime import datetime as dt

import pandas as pd

import os
from config.definitions import ROOT_DIR


df = pd.read_csv(os.path.join(ROOT_DIR, 'data', 'data_33.csv'))

thenav = create_mynavbar()

dff = df
#dff['Date'] = pd.to_datetime(dff['Date'])
myscatter = px.scatter(dff, x='Date', y='CMP_SPEED', color='POWER')




@callback(
    Output('page-2-display-value', 'children'),
    Input('page-2-dropdown', 'value'))
def display_value(value):
    return f'You have selected {value}'




def createpage_plots():
    
    #layout = html.Div(
    #    [
    #    thenav,
    #    html.H3('Page ----- plots'),
    #    dcc.Dropdown(
    #        {f'Page dddd - {i}': f'{i}' for i in ['neeeee 1', 'Place 2', 'Place 3']},
    #        id='page-2-dropdown'
    #    ),
    #    html.Div(id='page-2-display-value'),
    #    dcc.Link('Go to Home', href='/')
    #]
    #)









    layout2 = dbc.Row(
        [thenav,

            dbc.Col(
                html.Div('''
                long description
                
                ''' 
                    
                ), md=8, class_name="h-50", className='ms-4',
                        style={
                        'color':'#000000',
                        'text-align':'justify','margin-left':'5%',
                        }
            ), html.Br(),html.Br(),

            html.Div(children=[
            html.Label('Filter by date (M-D-Y):'),html.Br(),

            dcc.DatePickerRange(
                id='input_date',
                number_of_months_shown=2,
                persistence=True,
                month_format='DD/MM/YYYY',
                show_outside_days=True,
                minimum_nights=0,
                initial_visible_month=dt(2017, 1, 1),
                min_date_allowed=dt(2016, 1, 1),
                max_date_allowed=dt(2018, 12, 31),
                start_date=dt.strptime("2018-06-01", "%Y-%m-%d").date(),
                end_date=dt.strptime("2018-12-31", "%Y-%m-%d").date()
            ), ], style={'margin-left':'5%'}),


            dbc.Col(
                
                dcc.Graph(figure=myscatter, id='graph_1'), md=6


            ),
            dbc.Col(
                dcc.Graph(id='graph_2'), md=6
            )
        ]
    )


    return [layout2]




#def update_graph_1():
#    dff = df
#    myscatter = px.scatter(dff, x='Date', y='CMP_SPEED', color='POWER')
#
#
#    return myscatter







#layout = html.Div([
#    html.H3('Page 2'),
#    dcc.Dropdown(
#        {f'Page 2 - {i}': f'{i}' for i in ['London', 'Berlin', 'Paris']},
#        id='page-2-dropdown'
#    ),
#    html.Div(id='page-2-display-value'),
#    dcc.Link('Go to Page 1', href='/page1')
#])


