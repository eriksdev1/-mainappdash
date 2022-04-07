import dash_bootstrap_components as dbc
from dash import Dash, html, dcc

#def create_navbar():
#    navbar = dbc.NavbarSimple(
#        children=[
#            dbc.DropdownMenu(
#                nav=True,
#                in_navbar=True,
#                label="Menu",
#                children=[
#                    dbc.DropdownMenuItem("Home", href='/'),
#                    dbc.DropdownMenuItem(divider=True),
#                    dbc.DropdownMenuItem("Page 2", href='/page-2'),
#                    dbc.DropdownMenuItem("Page 3", href='/page-3'),
#                ],
#            ),
#        ],
#        brand="Home",
#        brand_href="/",
#        sticky="top",
#        color="dark",  # Change this to change color of the navbar e.g. "primary", "secondary" etc.
#        dark=True,  # Change this to change color of text within the navbar (False for dark text)
#    )
#
#    return navbar




nav_item1 = dbc.NavItem(dbc.NavLink("Info page", class_name='ms-4', href="/page1"))
nav_item2 = dbc.NavItem(dbc.NavLink("Plots", class_name='ms-4', href="/page2"))


dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Entry 1"),
        dbc.DropdownMenuItem("Entry 2"),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("Entry 3"),
    ],
    nav=True,
    in_navbar=True,
    class_name='ms-4',
    label="Menu",
)





def create_mynavbar():
    logonav1 = dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    # Use row and col to control vertical alignment of logo / brand
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src='/assets/logosmall.png', height="70px")),
                            dbc.Col(dbc.NavbarBrand("Hackaton 2022", className="ms-4")),
                        ],
                        align="center",
                        className="g-0",
                    ),
                    href="/",
                    style={"textDecoration": "none"},
                ),
                dbc.NavbarToggler(id="navbar-toggler2", n_clicks=0),
                dbc.Collapse(
                    dbc.Nav(
                        [nav_item1, nav_item2, dropdown],
                        className="mr-auto", # mr-auto aligns to left
                        navbar=True,
                    ),
                    id="navbar-collapse2",
                    navbar=True,
                ),
            ],
        ),
        color="dark",
        dark=True,
        className="mb-5",
    )
    return logonav1




