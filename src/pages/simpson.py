"""simpson"""
from dash import html, dcc


def latext(text):
    """return a mathjax markdown"""
    return dcc.Markdown(text, mathjax=True, className="myMath")


layout = html.Div([
    html.H3('Regla de Simpson 1/3'),
    html.P('''La regla de Simpson 1/3 es un método de integración numperica,
            donde la idea es aproximar una función usando un
            polinomio de interpolación de Lagrange de segundo grado,'''),
    latext('''$$
            \\begin{equation}
            I = \\int_{a}^{b} f(x) dx \\cong \\int_{a}^{b} f_{2}(x) dx
            \\end{equation}
            $$'''),
    latext('donde $f_{2}(x)$ es,'),
    latext('''$$
            \\begin{align}
            f_{2} (x) &= \\frac{ (x - x_{1}) (x - x_{2}) }{(x_{0} - x_{1}) (x_{0} - x_{2})} f(x_{0}) +
            \\frac{ (x - x_{0}) (x - x_{2}) }{(x_{1} - x_{0}) (x_{1} - x_{2})} f(x_{1}) \\\\
            &+ \\frac{ (x - x_{0}) (x - x_{1}) }{(x_{2} - x_{0}) (x_{2} - x_{1})} f(x_{2}) \\notag
            \\end{align}
            $$'''),
    latext('Designando $a$ y $b$ como $x_0$ y $x_2$ $\\therefore$,'),
    latext('''$$
            \\begin{align}
            I  &=  \\int_{x_0}^{x_2}  \\left[ \\frac{ (x - x_{1}) (x - x_{2})}{(x_{0} - x_{1}) (x_{0} - x_{2})} f(x_{0}) \\right] dx \\\\ \\notag
            &+ \\int_{x_0}^{x_2} \\left[ \\frac{ (x - x_{0}) (x - x_{2}) }{(x_{1} - x_{0}) (x_{1} - x_{2})} f(x_{1}) \\right] dx \\\\ \\notag
            &+ \\int_{x_0}^{x_2} \\left[ \\frac{ (x - x_{0}) (x - x_{1}) }{(x_{2} - x_{0}) (x_{2} - x_{1})} f(x_{2}) \\right] dx \\tag{1}
            \\end{align}
            $$'''),
    latext('''Teniendo en cuenta que, $x_0$, $x_1$ y $x_2$ son tres puntos
               consecutivos en incrementos iguales,'''),
    latext('''$$
            \\begin{align}
            x_{1} &= x_{0} + \\Delta \\notag \\\\
            x_{2} &= x_{0} + 2\\Delta \\notag \\\\
            \\Delta &= \\frac{x_2 - x_0}{3} \\notag
            \\end{align}
            $$'''),
    html.P('Resolviendo las tres integrales,'),
    latext('''$$
            \\begin{align}
            &\\int_{x_0}^{x_2}  \\left[ \\frac{ (x - x_{1}) (x - x_{2})}{(x_{0} - x_{1}) (x_{0} - x_{2})} f(x_{0}) \\right] dx \\notag \\\\ \\notag
            &\\frac{f(x_{0})}{2 \\Delta^2} \\int_{x_0}^{x_{0} + 2 \\Delta} (x - (x_0 + \\Delta)) (x - (x_0 + 2 \\Delta)) dx \\\\ \\notag
            &\\frac{f(x_{0})}{2 \\Delta^2} \\left[ \\frac{x^3}{3} - \\frac{x^2}{2}(2x_0 + 3 \\Delta) + (x_0 + \\Delta)(x_0 + 2\\Delta)x \\right] \\Bigg|_{x_0}^{x_{0} + 2 \\Delta} \\\\ \\notag
            \\end{align}
            $$'''),
    latext('$\\therefore$'),
    latext('''$$
            \\begin{align}
            &\\frac{f(x_{0})}{2 \\Delta^2} \\left( \\frac{(x_{0} + 2 \\Delta)^3}{3} - \\frac{(x_{0} + 2 \\Delta)^2}{2}(2x_0 + 3 \\Delta) + (x_0 + \\Delta)(x_0 + 2\\Delta)(x_{0} + 2 \\Delta) \\right) \\notag \\\\
            &- \\frac{f(x_{0})}{2 \\Delta^2} \\left( \\frac{(x_{0})^3}{3} - \\frac{(x_{0})^2}{2}(2x_0 + 3 \\Delta) + (x_0 + \\Delta)(x_0 + 2\\Delta)(x_{0}) \\right) \\notag
            \\end{align}
            $$'''),
    latext('$\\therefore$'),
    latext('''$$
            \\begin{align}
            &\\frac{f(x_{0})}{2 \\Delta^2} \\left( \\frac{(x_{0} + 2 \\Delta)^3}{3} - \\frac{(x_{0} + 2 \\Delta)^2}{2}(2x_0 + 3 \\Delta) + (x_0 + \\Delta)(x_0 + 2\\Delta)(x_{0} + 2 \\Delta) \\right) \\notag \\\\
            &- \\frac{f(x_{0})}{2 \\Delta^2} \\left( \\frac{(x_{0})^3}{3} - \\frac{(x_{0})^2}{2}(2x_0 + 3 \\Delta) + (x_0 + \\Delta)(x_0 + 2\\Delta)(x_{0}) \\right) \\notag
            \\end{align}
            $$'''),
    latext('$\\therefore$'),
    latext('''$$
            \\begin{align}
            &\\frac{f(x_{0})}{2 \\Delta^2} \\left( \\frac{6x_{0}^2 \\Delta + 12 \\Delta^2 x_0 + 8\\Delta^3}{3} - \\frac{(4x_0 \\Delta + 4 \\Delta^2)}{2}(2x_0 + 3 \\Delta) + (x_0 + \\Delta)(x_0 + 2\\Delta)(2 \\Delta) \\right) \\notag \\\\
            &\\frac{f(x_{0})}{\\Delta} \\left( x_{0}^2  + 2\\Delta x_0 + \\frac{4\\Delta^2}{3} - (x_0 + \\Delta)(2x_0 + 3 \\Delta) + (x_0 + \\Delta)(x_0 + 2\\Delta) \\right) \\notag \\\\
            &\\frac{f(x_{0})}{\\Delta} \\left( 2\\Delta x_0 + \\frac{4\\Delta^2}{3} - 2 \\Delta x_0 - \\Delta^2 \\right) \\notag \\\\
            &\\frac{f(x_{0})}{\\Delta} \\left(\\frac{4\\Delta^2 - 3\\Delta^2}{3} \\right) =  \\frac{f(x_{0}) \\Delta}{3} = \\frac{f(x_{0}) (x_2 - x_0)}{6}\\notag \\\\ \\notag
            \\end{align}
            $$'''),
    latext('Resolviendo para $f(x_1)$'),
    latext('''$$
            \\begin{align}
            &\\int_{x_0}^{x_2} \\left[ \\frac{ (x - x_{0}) (x - x_{2}) }{(x_{1} - x_{0}) (x_{1} - x_{2})} f(x_{1}) \\right] dx \\notag \\\\
            &-\\frac{f(x_{1})}{\\Delta^2} \\int_{x_0}^{x_{0} + 2 \\Delta} (x - x_0) (x - (x_0 + 2 \\Delta)) dx \\notag \\\\
            &-\\frac{f(x_{1})}{\\Delta^2} \\left[ \\frac{x^3}{3} - \\frac{x^2}{2}(2x_0 + 2 \\Delta) + (x_0^2 + 2\\Delta x_0)x \\right] \\Bigg|_{x_0}^{x_{0} + 2 \\Delta} \\notag
            \\end{align}
            $$'''),
    latext('''$$
            \\begin{align}
            &-\\frac{f(x_{1})}{\\Delta^2} \\left( \\frac{(x_0+2\\Delta)^3}{3} - \\frac{(x_0+2\\Delta)^2}{2}(2x_0 + 2 \\Delta) + (x_0^2 + 2\\Delta x_0)(x_0+2\\Delta) \\right)
            \\notag \\\\
            &+ \\frac{f(x_{1})}{\\Delta^2} \\left( \\frac{x_0^3}{3} - \\frac{x_0^2}{2}(2x_0 + 2 \\Delta) + (x_0^2 + 2\\Delta x_0)(x_0) \\right) \\notag
            \\end{align}
            $$'''),
    latext('''$$
            \\begin{align}
            &-\\frac{f(x_{1})}{\\Delta^2} \\left( 2x_0^{2}\\Delta + 4x_0 \\Delta^2 + \\frac{8}{3}\\Delta^3 - (4x_0 \\Delta + 4\\Delta^2)(x_0 + \\Delta) + 2\\Delta x_0^2 + 4\\Delta^2 x_0 \\right) \\notag \\\\
            &-\\frac{f(x_{1})}{\\Delta^2} \\left(  -\\frac{4}{3} \\Delta^3 \\right) = \\frac{4 f(x_{0}) \\Delta }{3} = \\frac{4f(x_1)(x_2 - x_0)}{6} \\notag
            \\end{align}
            $$'''),
    latext('Resolviendo para $f(x_2)$'),
    latext('''$$
            \\begin{align}
            &\\int_{x_0}^{x_2} \\left[ \\frac{ (x - x_{0}) (x - x_{1}) }{(x_{2} - x_{0}) (x_{2} - x_{1})} f(x_{2}) \\right] dx \\notag \\\\
            &\\frac{f(x_{2})}{2\\Delta^2} \\int_{x_0}^{x_{0} + 2 \\Delta} (x - x_0) (x - (x_0 + \\Delta)) dx \\notag \\\\
            &\\frac{f(x_{2})}{2\\Delta^2} \\left[ \\frac{x^3}{3} - \\frac{x^2}{2}(2x_0 + \\Delta) + (x_0^2 + \\Delta x_0)x \\right] \\Biggr|_{x_0}^{x_{0} + 2 \\Delta} \\notag
            \\end{align}
            $$'''),
    latext('''$$
            \\begin{align}
            &\\frac{f(x_{2})}{2\\Delta^2} \\left( 2x_0^{2}\\Delta + 4x_0 \\Delta^2 + \\frac{8}{3}\\Delta^3 - (2x_0 \\Delta + 2\\Delta^2)(2x_0 + \\Delta) + 2\\Delta x_0^2 + 2\\Delta^2 x_0 \\right) \\notag \\\\
            &\\frac{f(x_{2})}{2\\Delta^2} \\left( \\frac{8}{3}\\Delta^3 - 2\\Delta^3 \\right) \\notag \\\\
            &\\frac{f(x_{2})}{2} \\left( \\frac{2\\Delta}{3} \\right) = \\frac{f(x_{2})\\Delta}{3} = \\frac{f(x_{2})(x_2 - x_1) }{6}
            \\end{align}
            $$'''),
    html.P('Una vez resuelta la integral de (1), juntando las tres partes,'),
    latext('''$$
               \\begin{equation}
               \\tag{2}
                I = (x_2 - x_0) \\frac{f(x_{0}) + 4 f(x_{1}) + f(x_{2})}{6}
               \\end{equation}
               $$'''),
    html.P('La ecuación (2) es conocida como la regla de Simpson 1/3'),
    html.H3('Regla de simpson 1/3 con aplicación múltiple'),
    html.P('''Este método es más exacto, porque divide el intervalo de
               integración en segmentos de un mismo tamaño,'''),
    latext('''$$
            \\begin{equation}
            h = \\frac{x_n - x_0}{n}
            \\end{equation}
            $$'''),
    latext('donde $n$ es un número par.'),
    latext('$\\therefore$'),
    latext('''$$
            \\begin{align}
            h &= x_1 - x_0 \\\\
            h &= x_2 - x_1 \\\\
            &\\vdots \\\\
            h &= x_n - x_{n-1}
            \\end{align}
            $$'''),
    latext('esto implica que la distancia $\\Delta$ sea,'),
    latext('''$$
            \\begin{equation}
            \\Delta = \\frac{2h}{3}
            \\end{equation}
            $$'''),
    html.P('Plasmando la idea, la integral de la función se aproxima,'),
    latext('''$$
            \\begin{equation}
            I = \\int_{x_{0}}^{x_2} f(x) dx + \\int_{x_{2}}^{x_4} f(x) dx + \\ldots + \\int_{x_{n}}^{x_{n-2}} f(x) dx
            \\end{equation}
            $$'''),
    html.P('aplicando la regla de simpson 1/3 (ecuación 2) a cada integral'),
    latext('$\\therefore$'),
    latext('''$$
            \\begin{align}
            I &\\cong 2h \\frac{f(x_{0}) + 4f(x_{1}) + f(x_{2})}{6} + 2h \\frac{f(x_{2}) + 4f(x_{3}) + f(x_{4})}{6} \\\\
            & + \\ldots + 2h \\frac{f(x_{n-2}) + 4f(x_{n-1}) + f(x_{n})}{6}
            \\end{align}
            $$'''),
    latext('''dada la naturaleza de esta serie, los terminos impares están multiplicados
               por 4 y los pares cuentan por 2. Sustituyendo $h$ se llega a,'''),
    latext('''$$
            \\begin{equation}
            I \\cong (x_n - x_0) \\left[ \\frac{f(x_0) + 4 \\sum_{i = 1,3,5...}^{n-1} f(x_{i}) + \\sum_{j = 2,4,6...}^{n-2} f(x_{j}) + f(x_n)}{3n} \\right]
            \\end{equation}
            $$'''),
    html.P(
        '''Esta ecuación es conocida como la regla de Simpson 1/3 de aplicación múltiple.''')
])


def go_simpson():
    """simpson"""
    return layout
