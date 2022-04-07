from ctypes import alignment
from tkinter import Image
import dash as dash
#import dash_core_components as dcc # old
from dash import html as html
#import dash_html_components as html # old
from dash import dcc as dcc

from dash.dependencies import Input, Output
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from pageNavbar import create_mynavbar



nav = create_mynavbar()

header = html.H3('Welcome to home page!')


def createpage_home():
    layout = html.Div([
        nav,
        header,
    ])
    return layout








##logoimg = app.get_asset_url("logosmall.png")
#
#nav_item = dbc.NavItem(dbc.NavLink("Link", href="/page1"))
#
#
#dropdown = dbc.DropdownMenu(
#    children=[
#        dbc.DropdownMenuItem("Entry 1"),
#        dbc.DropdownMenuItem("Entry 2"),
#        dbc.DropdownMenuItem(divider=True),
#        dbc.DropdownMenuItem("Entry 3"),
#    ],
#    nav=True,
#    in_navbar=True,
#    label="Menu",
#)
## ------------------------------------------- navbar
#
#logonav1 = dbc.Navbar(
#    dbc.Container(
#        [
#            html.A(
#                # Use row and col to control vertical alignment of logo / brand
#                dbc.Row(
#                    [
#                        dbc.Col(html.Img(src='/assets/logosmall.png', height="70px")),
#                        dbc.Col(dbc.NavbarBrand("Logo", className="ms-2")),
#                    ],
#                    align="center",
#                    className="g-0",
#                ),
#                href="/",
#                style={"textDecoration": "none"},
#            ),
#            dbc.NavbarToggler(id="navbar-toggler2", n_clicks=0),
#            dbc.Collapse(
#                dbc.Nav(
#                    [nav_item, dropdown],
#                    className="mr-auto",
#                    navbar=True,
#                ),
#                id="navbar-collapse2",
#                navbar=True,
#            ),
#        ],
#    ),
#    color="dark",
#    dark=True,
#    className="mb-5",
#)
#
#
#
#
#
#
## ------------------------------------------- navbar
#
#row = html.Div(
#    [
#
#
#
#        dbc.Row(dbc.Col(html.Div(
#            
#            
#            "A single column", className="text-center"
#            
#            
#            
#            ))),
#        dbc.Row(
#            [
#                dbc.Col(html.Div("One of three columns")),
#                dbc.Col(html.Div("One of three columns")),
#                dbc.Col(html.Div("One of three columns")),
#            ]
#        ),
#
#
#
#
#
#    ]
#)
#
#
#
#
#
#
#
#
#
#
#
#
##layout = dbc.Container(row, fluid=True)
##app.layout = html.Div(
##    [default, custom_default, logo, search_navbar, dashboard]
##)
#
##layout = dbc.Container(logonav1, row, fluid=True)
#
#layout = html.Div(
#   [logonav1, row]
#)





