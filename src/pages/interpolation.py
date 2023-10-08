"""interpolation"""
from dash import html, dcc


def latext(text):
    """return a mathjax markdown"""
    return dcc.Markdown(text, mathjax=True, className="myMath")


layout = html.Div([
    html.H3('Interpolación'),
    latext('''
            Dados $n+1$ puntos, hay un solo polinomio de grado $n$ que pasa a traves de todos los puntos.
            Por ejemplo, si se trata de dos puntos, para unirlos necesitas una línea recta. 
            En otras palabras, necesitas un polinomio de grado uno para unir dos puntos.
            La forma general de un polinomio de n-ésimo grado es,
            '''),
    latext('''$$
            \\tag{1}
            \\begin{equation}
            f(x) = a_{0} + a_{1} x + a_{2} x^{2} + \\ldots + a_{n} x^{n}
            \\end{equation}
            $$'''),
    latext('''
            La interpolación polinomial consiste en encontrar un polinomio de grado $n$ que una $n+1$ puntos.
            Existen distintas formas de calcular este polinomio. Entre ellas, el polinomio de interpolación de Newton y el polinomio de interpolacion de Lagrange.
            '''),
    html.H3('Forma general de los polinomios de interpolación de Newton'),
    html.P('La forma general corresponde a,'),
    latext('''$$
            \\begin{equation}
            \\tag{2}
            f_{n}(x) = b_{0} + b_{1}(x-x_{0}) + \\ldots + b_{n}(x-x_{0})(x-x_{1})\\ldots(x-x_{n-1})
            \\end{equation}
            $$'''),
    html.P('donde'),
    latext('''$$
            \\begin{equation}
            \\tag{3}
            [x_{0}, f(x_{0})],[x_{1}, f(x_{1})],[x_{2}, f(x_{2})] \\ldots [x_{n}, f(x_{n})]
            \\end{equation}
            $$'''),
    latext('representan los $n + 1$ puntos. Los coeficientes,'),
    latext('''$$
            \\begin{equation}
            \\tag{4}
            b_{0}, b_{1}, \\ldots, b_{n}
            \\end{equation}
            $$'''),
    html.P('corresponden a,'),
    latext('''$$
            \\begin{align}
            b_{0} &= f(x_{0}) \\\\
            b_{1} &= f[x_{1},x_{0}] \\\\
            b_{2} &= f[x_{2},x_{1},x_0] \\\\
            &\\;\\; \\vdots  \\\\
            b_{n} &= f[x_{n},x_{n-1},\\ldots,x_{1},x_{0}] \\tag{5}
            \\end{align}
            $$'''),
    html.P('''las evaluaciones de las funciones entre corchetes,
               son las diferencias divididas finitas.
               La primera diferencia finita dividida,'''),
    latext('''$$
            \\begin{equation}
            \\tag{6}
            f[x_{i},x_{j}] = \\frac{f(x_{i}) - f(x_{j})}{x_{i}-x_{j}}
            \\end{equation}
            $$'''),
    html.P('La segunda diferencia dividida finita,'),
    latext('''$$
            \\begin{equation}
            \\tag{7}
            f[x_{i},x_{j},x_{k}] = \\frac{f[x_{i},x_{j}] - f[x_{j},x_{k}] }{x_{i}-x_{k}}
            \\end{equation}
            $$'''),
    html.P('por lo tanto, la n-ésima diferencia dividida finita es,'),
    latext('''$$
            \\begin{equation}
            \\tag{8}
            f[x_{n},x_{n-1},_{\\ldots},x_{1},x_{0}] = \\frac{f[x_{n},x_{n-1},_{\\ldots},x_{1}] - f[x_{n-1},x_{n-2},_{\\ldots},x_{0}]}{x_{n}-x_{0}}
            \\end{equation}
            $$'''),
    html.P('sustituyendo los coeficientes,'),
    latext('''$$
            \\begin{align}
            \\tag{9}
            f_{n}(x) &= f(x_{0}) + (x-x_{0})f[x_{1},x_{0}] + (x-x_{0})(x-x_{1})f[x_{2},x_{1},x_{0}] \\\\
            &+ \\ldots + (x-x_{0})(x-x_{1}) \\ldots (x-x_{n-1}) f[x_{n},x_{n-1},_{\\ldots},x_{0}] \\notag
            \\end{align}
            $$'''),
    html.H3('Polinomio de interpolación de Lagrange'),
    html.P('''
            El polinomio de interpolación de Lagrange es una reformulación del polinomio de interpolación de Newton, 
            donde se evita el cálculo de las diferencias divididas.
            El polinomio de Lagrange es definido como,
            '''),
    latext('''$$
            \\begin{equation}
            \\tag{10}
            f_{n}(x) = \\sum_{i=0}^{n} L_{i}(x) f(x_{i})
            \\end{equation}
            $$'''),
    html.P('donde'),
    latext('''$$
            \\begin{equation}
            \\tag{11}
            L_{i}(x) = \\prod^{n}_{j = 0, j \\neq i} \\frac{x - x_{j}}{x_{i} - x_{j}}
            \\end{equation}
            $$'''),
    latext('''donde, $\\prod$ representa multiplicaciones sucesivas.
               Por lo tanto para la versión $n = 1$,'''),
    latext('''$$
            \\begin{equation}
            \\tag{12}
            f_{1} (x) = \\frac{x - x_{1}}{x_{0} - x_{1}} f(x_{0}) + \\frac{x - x_{0}}{x_{1} - x_{0}} f(x_{1})
            \\end{equation}
            $$'''),
    latext('y la versión $n = 2$'),
    latext('''$$
            \\begin{align}
            \\tag{13}
            f_{2} (x) &= \\frac{ (x - x_{1}) (x - x_{2}) }{(x_{0} - x_{1}) (x_{0} - x_{2})} f(x_{0}) + 
            \\frac{ (x - x_{0}) (x - x_{2}) }{(x_{1} - x_{0}) (x_{1} - x_{2})} f(x_{1}) \\\\
            &+ \\frac{ (x - x_{0}) (x - x_{1}) }{(x_{2} - x_{0}) (x_{2} - x_{1})} f(x_{2})
            \\end{align}
            $$'''),
    latext('''
            La ecuación (13) se conoce como el polinomio de  interpolación de Lagrange de grado 2. 
            El cual, une los tres puntos, $[x_{0}, f(x_{0})],[x_{1}, f(x_{1})],[x_{2}, f(x_{2})]$
            '''),
    latext('''
            A continuación se probara, que a partir del polinomio de interpolación de Newton es posible 
            deducir el polinomio de interpolación de Lagrange.
            '''),
    html.P('Para probar el origen de (12), se considera la ecuación (6),'),
    latext('''$$
            \\begin{equation}
            \\tag{14}
            f[x_{1},x_{0}] = \\frac{f(x_{1})}{x_{1}-x_{0}} - \\frac{f(x_{0})}{x_{1}-x_{0}} 
            \\end{equation}
            $$'''),
    html.P('de la ecuación (9), llegamos a la forma,'),
    latext('''$$
            \\begin{equation}
            f_{1}(x) = f(x_{0}) + (x - x_{0}) \\left( \\frac{f(x_{1})}{x_{1}-x_{0}} - \\frac{f(x_{0})}{x_{1}-x_{0}} \\right)
            \\end{equation}
            $$'''),
    latext('$\\therefore$'),
    latext('''$$
            \\begin{equation}
            f_{1}(x) = \\frac{(x_{1}-x_{0})f(x_{0})}{x_{1}-x_{0}} + \\frac{(x - x_{0})f(x_{1})}{x_{1}-x_{0}} - \\frac{(x - x_{0})f(x_{0})}{x_{1}-x_{0}} 
            \\end{equation}
            $$'''),
    latext('''$$
            \\begin{equation}
            \\tag{15}
            f_{1}(x) = \\frac{x_{1} - x}{x_{1}-x_{0}} f(x_{0}) + \\frac{x - x_{0}}{x_{1}-x_{0}} f(x_{1})
            \\end{equation}
            $$'''),
    latext('''$$
            \\begin{equation}
            \\frac{x_{1} - x}{x_{1}-x_{0}} f(x_{0}) = \\frac{x-x_{1}}{x_{0}-x_{1}} \\left( \\frac{-1}{-1} \\right) f(x_{0}) =  \\frac{x-x_{1}}{x_{0}-x_{1}} f(x_{0}) 
            \\end{equation}
            $$'''),
    html.P(
        'dado que (15) es equivalente a (12), se demuestra el origen de la ecuación (12)'),
    html.P('Para demostrar el origen de (13), de (6) se entiende que,'),
    latext('''$$
            \\begin{equation}
            \\tag{16}
            f[x_{2},x_{1}] = \\frac{f(x_{2})}{x_{2}-x_{1}} - \\frac{f(x_{1})}{x_{2}-x_{1}} 
            \\end{equation}
            $$'''),
    html.P('considerando las ecuaciones (14) y (16) en (7), obtenemos,'),
    latext('''$$
            \\begin{align}
            &f[x_{2},x_{1},x_{0}] = \\frac{f[x_{2},x_{1}] - f[x_{1},x_{0}] }{x_{2}-x_{0}} \\\\
            &= \\frac{f(x_{2})-f(x_{1})}{(x_{2}-x_{1})(x_{2}-x_{0})} +  \\frac{f(x_{0})-f(x_{1})}{(x_{1}-x_{0})(x_{2}-x_{0})} \\notag \\\\
            &= \\frac{(x_{1}-x_{0})(f(x_{2})-f(x_{1})) + (x_{2}-x_{1})(f(x_{0})-f(x_{1}))}{(x_{2}-x_{1})(x_{2}-x_{0})(x_{1}-x_{0})} \\notag \\\\
            &= \\frac{(x_{1}-x_{0})f(x_{2}) - (x_{1}-x_{0} + x_{2} - x_{1})f(x_{1}) + (x_{2}-x_{1})f(x_{0})}{(x_{2}-x_{1})(x_{2}-x_{0})(x_{1}-x_{0})} \\notag \\\\
            &= \\frac{(x_{1}-x_{0})f(x_{2}) - (x_{2} - x_{0})f(x_{1}) + (x_{2}-x_{1})f(x_{0})}{(x_{2}-x_{1})(x_{2}-x_{0})(x_{1}-x_{0})} \\notag \\\\
            &= \\frac{f(x_{2})}{(x_{2}-x_{1})(x_{2}-x_{0})} + \\frac{f(x_{1})}{(x_{1}-x_{2})(x_{1}-x_{0})} + \\frac{f(x_{0})}{(x_{2}-x_{0})(x_{1}-x_{0})} \\tag{17}
            \\end{align}
            $$'''),
    html.P('Dado que en (9) se sabe que,'),
    latext('''$$
            \\begin{equation}
            \\tag{18}
            f_{2}(x) = f(x_{0}) + (x-x_{0})f[x_{1},x_{0}] + (x-x_{0})(x-x_{1})f[x_{2},x_{1},x_{0}]
            \\end{equation}
            $$'''),
    html.P('sustituyendo (14) y (17) en (18)'),
    latext('''$$
            \\begin{align}
            f_{2}(x) &= f(x_{0}) + (x-x_{0})\\left[\\frac{f(x_{1})}{x_{1}-x_{0}} - \\frac{f(x_{0})}{x_{1}-x_{0}} \\right] \\\\
            &+ (x-x_{0})(x-x_{1}) \\left[ \\frac{f(x_{2})}{(x_{2}-x_{1})(x_{2}-x_{0})} + \\frac{f(x_{1})}{(x_1-x_2)(x_{1}-x_{0})} + \\frac{f(x_{0})}{(x_{2}-x_{0})(x_{1}-x_{0})} \\right] \\notag \\\\
            &= f(x_{0}) + (x-x_{0})\\left[\\frac{f(x_{1})}{x_{1}-x_{0}} - \\frac{f(x_{0})}{x_{1}-x_{0}} \\right] \\notag \\\\
            &+ (x-x_{0})(x-x_{1}) \\left[ \\frac{f(x_{2})}{(x_{2}-x_{1})(x_{2}-x_{0})} + \\frac{f(x_{1})}{(x_1-x_2)(x_{1}-x_{0})} + \\frac{f(x_{0})}{(x_{2}-x_{0})(x_{1}-x_{0})} \\right] \\tag{19}
            \\end{align}
            $$'''),
    latext('''Se van a analizar los terminos de (19) por partes,
               agrupando lo relacionado a $f(x_0)$'''),
    latext('''$$
            \\begin{align}
            & \\frac{f(x_{0})(x - x_0)}{x_1 - x_0} \\left[ \\frac{x_1 - x_0}{x - x_0} - 1 + \\frac{x-x_1}{x_{2}-x_{0}} \\right] \\notag \\\\
            & \\frac{f(x_{0})(x - x_0)}{x_1 - x_0} \\left[ \\frac{(x_{2}-x_{0})(x_1 - x_0) - (x - x_0)(x_{2}-x_{0}) + (x-x_1)(x-x_0)  }{(x - x_0)(x_{2}-x_{0})} \\right] \\notag \\\\
            & \\frac{f(x_{0})(x - x_0)}{x_1 - x_0} \\left[ \\frac{(x_{2}-x_{0})(x_1 - x ) + (x-x_1)(x-x_0) }{(x - x_0)(x_{2}-x_{0})} \\right] \\notag \\\\
            & \\frac{f(x_{0})}{x_1 - x_0} \\left[ \\frac{(x_{0}-x_{2})(x - x_{1} ) + (x-x_1)(x-x_0)   }{(x_{2}-x_{0})} \\right] \\notag \\\\
            & \\frac{f(x_{0})}{x_1 - x_0} \\left[ \\frac{(x-x_1)(x_{0}-x_{2} + x-x_0) }{(x_{2}-x_{0})} \\right] \\notag \\\\
            & \\frac{f(x_{0})}{x_1 - x_0} \\left[ \\frac{(x-x_1)(x-x_{2}) }{(x_{2}-x_{0})} \\right] \\notag \\\\
            & \\frac{(x-x_1)(x-x_{2}) }{(x_{2}-x_{0})(x_1 - x_0)} f(x_{0}) = \\frac{(x-x_1)(x-x_{2}) }{(x_{0}-x_{2})(-1)(x_1 - x_0)}f(x_{0}) \\notag \\\\
            & \\frac{(x-x_1)(x-x_{2}) }{(x_{0}-x_{2})(x_0 - x_1)}f(x_{0}) \\tag{20}
            \\end{align}
            $$'''),
    latext('Analizando los terminos relacionados a $f(x_1)$'),
    latext('''$$
            \\begin{align}
            & \\frac{f(x_{1})(x - x_0)}{x_1 - x_0} \\left[ 1 + \\frac{x-x_1}{x_1-x_2} \\right] \\\\
            & \\frac{f(x_{1})(x - x_0)}{x_1 - x_0} \\left[ \\frac{x_1-x_2 + x - x_1 }{x_1-x_2} \\right] \\notag \\\\
            & \\frac{(x-x_2)(x - x_0)}{(x_1 - x_0)(x_1-x_2)} f(x_1) \\tag{21}
            \\end{align}
            $$'''),
    latext('Por último, los terminos relacionados a $f(x_2)$,'),
    latext('''$$
            \\begin{equation}
            \\frac{(x-x_{0})(x-x_{1})}{(x_{2}-x_{1})(x_{2}-x_{0})} f(x_{2}) \\tag{22}
            \\end{equation}
            $$'''),
    html.P('''Las ecuaciones (20), (21) y (22), permiten concluir que la ecuación
            (18) es equivalente a la ecuación (13). Demostrando el origen de (13), a partir 
            del polinomio de interpolación de Newton.''')
])


def go_interpolation():
    """interpolation"""
    return layout
