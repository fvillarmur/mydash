"""navbar"""
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO

theme_switch = ThemeSwitchAIO(
    aio_id="theme", themes=[dbc.themes.COSMO, dbc.themes.DARKLY]
)

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.NavItem(dbc.NavLink("interpolation", href="/interpolation")),
        dbc.NavItem(dbc.NavLink("analytics", href="/analytics")),
        dbc.NavItem(dbc.NavLink(theme_switch))
    ],
    brand="NavbarSimple",
    brand_href="#",
    color="secondary",
    dark=True,
)

def get_navbar():
    """get navbar"""
    return navbar
