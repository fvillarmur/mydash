"""about"""
from dash import html, dcc

layout = html.Div([
    html.P('''El método de integración numérica Simpson 1/3 con aplicación múltiple,
        es implementado para el caso de una distribución normal.'''),
    html.P('''La distribución normal es trascendental por sus diversas
           aplicaciones en estadística.'''),
    html.P('''En este contexto, la integral de la distribución normal es relevante,
           dado que no tiene solución analitica.'''),
    html.P('''Esta integral representa la probabilidad de la variable aleatoria x
           dentro de un intervalo.'''),
    dcc.Markdown('''$$
                \\begin{equation}
                f(x) = \\frac{1}{\\sigma \\sqrt{2 \\pi}} e^{-\\frac{1}{2} \\frac{(x - \\mu)^2}{\\sigma^2}}
                \\end{equation}   
                 $$''', mathjax=True, className="myMath"),
    dcc.Markdown('''$$
            \\begin{equation}
            P(x_{0} \\geq x \\leq x_{n}) = \\int_{x_{0}}^{x_{n}} \\frac{1}{\\sigma \\sqrt{2 \\pi}} e^{- \\frac{1}{2} \\frac{(x - \\mu)^2}{\\sigma^2}} dx
            \\end{equation}   
            $$''', mathjax=True, className="myMath"),
    html.P('''En las secciones Interpolación y Simpson 1/3, se expone la deducción
           del método de Simpson 1/3, partiendo del concepto de los polinomios de 
           interpolación.'''),
    html.P([
        html.A(
            html.I(' El repositorio', className="fa-brands fa-github"),
            href='https://github.com/fvillarmur/mydash', target="_blank"),
        ' con el código'])
])


def go_about():
    """about"""
    return layout
