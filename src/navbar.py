"""navbar"""
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO

theme_switch = ThemeSwitchAIO(
    aio_id="theme", themes=[dbc.themes.COSMO, dbc.themes.DARKLY]
)

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Sinopsis", href="/about")),
        dbc.NavItem(dbc.NavLink("Interpolación", href="/interpolation")),
        dbc.NavItem(dbc.NavLink("Simpson 1/3", href="/simpson")),
        dbc.NavItem(dbc.NavLink("Referencias", href="/reference")),
        dbc.NavItem(dbc.NavLink(theme_switch))
    ],
    brand="Probabilidad Gaussiana",
    brand_href="/",
    color="secondary",
    dark=True,
)


def get_navbar():
    """get navbar"""
    return navbar
