"""interpolation"""
from dash import html, dcc

def latext(text):
    """return a mathjax markdown"""
    return dcc.Markdown(text, mathjax=True)

layout = html.Div(children=[
    html.Div([
        html.H3('Interpolación'),
        latext('''
            Dados $n+1$ puntos, hay un solo polinomio de grado $n$ que pasa a traves de todos los puntos.
            Por ejemplo, si se trata de dos puntos, para unirlos necesitas una línea recta. 
            En otras palabras, necesitas un polinomio de grado uno para unir dos puntos.
            La forma general de un polinomio de n-ésimo grado es,
            '''),
        latext('''$$
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
            f_{n}(x) = b_{0} + b_{1}(x-x_{0}) + \\ldots + b_{n}(x-x_{0})(x-x_{1})\\ldots(x-x_{n-1})
            \\end{equation}
            $$'''),
        html.P('donde'),
        latext('''$$
            \\begin{equation}
            [x_{0}, f(x_{0})],[x_{1}, f(x_{1})],[x_{2}, f(x_{2})] \\ldots [x_{n}, f(x_{n})]
            \\end{equation}
            $$'''),
        latext('representan los $n$ puntos. Los coeficientes,'),
        latext('''$$
            \\begin{equation}
            b_{0}, b_{1}, \\ldots, b_{n}
            \\end{equation}
            $$'''),
        html.P('corresponden a,'),
        latext('''$$
            \\begin{align}
            b_{0} &= f(x_{0}) \\\\
            b_{1} &= f[x_{1},x_{0}] \\\\
            b_{2} &= f[x_{2},x_{1},x_0] \\\\
            &\\;\\; \\vdots \\notag \\\\
            b_{n} &= f[x_{n},x_{n-1},\\ldots,x_{1},x_{0}]
            \\end{align}
            $$'''),
        html.P('''las evaluaciones de las funciones entre corchetes,
               son las diferencias divididas finitas.
               La primera diferencia finita dividida,'''),
        latext('''$$
            \\begin{equation}
            f[x_{i},x_{j}] = \\frac{f(x_{i}) - f(x_{j})}{x_{i}-x_{j}}
            \\end{equation}
            $$'''),
        html.P('La segunda diferencia dividida finita,'),
        latext('''$$
            \\begin{equation}
            f[x_{i},x_{j},x_{k}] = \\frac{f[x_{i},x_{j}] - f[x_{j},x_{k}] }{x_{i}-x_{k}}
            \\end{equation}
            $$'''),
        html.P('por lo tanto, la n-ésima diferencia dividida finita es,'),
        latext('''$$
            \\begin{equation}
            f[x_{n},x_{n-1},_{\\ldots},x_{1},x_{0}] = \\frac{f[x_{n},x_{n-1},_{\\ldots},x_{1}] - f[x_{n-1},x_{n-2},_{\\ldots},x_{0}]}{x_{n}-x_{0}}
            \\end{equation}
            $$'''),
        html.P('sustituyendo los coeficientes,'),
        latext('''$$
            \\begin{align}
            f_{n}(x) &= f(x_{0}) + (x-x_{0})f[x_{1},x_{0}] + (x-x_{0})(x-x_{1})f[x_{2},x_{1},x_{0}] \\\\
            &+ \\ldots + (x-x_{0})(x-x_{1}) \\ldots (x-x_{n-1}) f[x_{n},x_{n-1},_{\\ldots},x_{0}] \\notag
            \\end{align}
            $$'''),
        html.H3('Polinomio de interpolación de Lagrange'),
        html.P('''
            El polinomio de interpolación de Lagrange es una reformulación del polinomio de interpolación de Newton, 
            donde se evita el cálculo de las diferencias divididas.
            El polinomio de Lagrande es definido como,
            '''),
        latext('''$$
            \\begin{equation}
            f_{n}(x) = \\sum_{i=0}^{n} L_{i}(x) f(x_{i})
            \\end{equation}
            $$'''),
        html.P('donde'),
        latext('''$$
            \\begin{equation}
            L_{i}(x) = \\prod^{n}_{j = 0, j \\neq i} \\frac{x - x_{j}}{x_{i} - x_{j}}
            \\end{equation}
            $$'''),
        latext('''donde, $\\prod$ representa multiplicaciones sucesivas.
               Por lo tanto para la versión $n = 1$,'''),
        latext('''$$
            \\begin{equation}
            f_{1} (x) = \\frac{x - x_{1}}{x_{0} - x_{1}} f(x_{0}) + \\frac{x - x_{0}}{x_{1} - x_{0}} f(x_{1})
            \\end{equation}
            $$'''),
        latext('y la versión $n = 2$'),
        latext('''$$
            \\begin{align}
            f_{2} (x) &= \\frac{ (x - x_{1}) (x - x_{2}) }{(x_{0} - x_{1}) (x_{0} - x_{2})} f(x_{0}) + 
            \\frac{ (x - x_{0}) (x - x_{2}) }{(x_{1} - x_{0}) (x_{1} - x_{2})} f(x_{1}) \\\\
            &+ \\frac{ (x - x_{0}) (x - x_{1}) }{(x_{2} - x_{0}) (x_{2} - x_{1})} f(x_{2}) \\notag
            \\end{align}
            $$'''),
        latext('''
            La ecuación (16) se conoce como el polinomio de  interpolación de Lagrange de grado 2. 
            El cual, une los tres puntos, $[x_{0}, f(x_{0})],[x_{1}, f(x_{1})],[x_{2}, f(x_{2})]$
            '''),
        latext('''
            A continuación se probara, que a partir del polinomio de interpolación de Newton es posible 
            deducir el polinomio de interpolación de Lagrange. Procesando la ecuación (9), de la siguiente manera,
            '''),
        latext('''$$
            \\begin{equation}
            f[x_{1},x_{0}] = \\frac{f(x_{1})}{x_{1}-x_{0}} - \\frac{f(x_{0})}{x_{1}-x_{0}} 
            \\end{equation}
            $$'''),
        html.P('considerando la ecuación (2), llegamos a la forma,'),
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
            f_{1}(x) = \\frac{x_{1} - x}{x_{1}-x_{0}} f(x_{0}) + \\frac{x - x_{0}}{x_{1}-x_{0}} f(x_{1})
            \\end{equation}
            $$'''),
        latext('''$$
            \\begin{equation}
            \\frac{x_{1} - x}{x_{1}-x_{0}} f(x_{0}) = \\frac{x-x_{1}}{x_{0}-x_{1}} \\left( \\frac{-1}{-1} \\right) f(x_{0}) =  \\frac{x-x_{1}}{x_{0}-x_{1}} f(x_{0}) 
            \\end{equation}
            $$'''),
        html.P('demostrando así el origen de la ecuación (15)'),
        html.P('Para demostrar el origen de (16), dado que la primera diferencia finita dividida,'),
        latext('''$$
            \\begin{equation}
            f[x_{2},x_{1}] = \\frac{f(x_{2})}{x_{2}-x_{1}} - \\frac{f(x_{1})}{x_{2}-x_{1}} 
            \\end{equation}
            $$'''),
        html.P('considerando las ecuaciones (17) y (eqn:22) en (10}, obtenemos,'),
        latext('''$$
            \\begin{align}
            &f[x_{2},x_{1},x_{0}] = \\frac{f[x_{2},x_{1}] - f[x_{1},x_{0}] }{x_{2}-x_{0}} \\\\
            &= \\frac{f(x_{2})-f(x_{1})}{(x_{2}-x_{1})(x_{2}-x_{0})} +  \\frac{f(x_{0})-f(x_{1})}{(x_{1}-x_{0})(x_{2}-x_{0})} \\notag \\\\
            &= \\frac{(x_{1}-x_{0})(f(x_{2})-f(x_{1})) + (x_{2}-x_{1})(f(x_{0})-f(x_{1}))}{(x_{2}-x_{1})(x_{2}-x_{0})(x_{1}-x_{0})} \\notag \\\\
            &= \\frac{(x_{1}-x_{0})f(x_{2}) - (x_{1}-x_{0} + x_{2} - x_{1})f(x_{1}) + (x_{2}-x_{1})f(x_{0})}{(x_{2}-x_{1})(x_{2}-x_{0})(x_{1}-x_{0})} \\notag \\\\
            &= \\frac{(x_{1}-x_{0})f(x_{2}) - (x_{2} - x_{0})f(x_{1}) + (x_{2}-x_{1})f(x_{0})}{(x_{2}-x_{1})(x_{2}-x_{0})(x_{1}-x_{0})} \\notag \\\\
            &= \\frac{f(x_{2})}{(x_{2}-x_{1})(x_{2}-x_{0})} + \\frac{f(x_{1})}{(x_{1}-x_{2})(x_{1}-x_{0})} + \\frac{f(x_{0})}{(x_{2}-x_{0})(x_{1}-x_{0})} \\notag
            \\end{align}
            $$'''),
        html.P('Dado que en (eqn:12) se sabe que,'),
        latext('''$$
            \\begin{equation}
            f_{2}(x) = f(x_{0}) + (x-x_{0})f[x_{1},x_{0}] + (x-x_{0})(x-x_{1})f[x_{2},x_{1},x_{0}]
            \\end{equation}
            $$'''),
        html.P('dado, (17) y (23)'),
        latext('''$$
            \\begin{align}
            f_{2}(x) &= f(x_{0}) + (x-x_{0})\\left[\\frac{f(x_{1})}{x_{1}-x_{0}} - \\frac{f(x_{0})}{x_{1}-x_{0}} \\right] \\\\
            &+ (x-x_{0})(x-x_{1}) \\left[ \\frac{f(x_{2})}{(x_{2}-x_{1})(x_{2}-x_{0})} + \\frac{f(x_{1})}{(x_1-x_2)(x_{1}-x_{0})} + \\frac{f(x_{0})}{(x_{2}-x_{0})(x_{1}-x_{0})} \\right] \\notag \\\\
            &= f(x_{0}) + (x-x_{0})\\left[\\frac{f(x_{1})}{x_{1}-x_{0}} - \\frac{f(x_{0})}{x_{1}-x_{0}} \\right] \\notag \\\\
            &+ (x-x_{0})(x-x_{1}) \\left[ \\frac{f(x_{2})}{(x_{2}-x_{1})(x_{2}-x_{0})} + \\frac{f(x_{1})}{(x_1-x_2)(x_{1}-x_{0})} + \\frac{f(x_{0})}{(x_{2}-x_{0})(x_{1}-x_{0})} \\right] \\notag
            \\end{align}
            $$'''),
        latext('''Se van a analizar los terminos de (25) por partes,
               agrupando lo relacionado a $f(x_0)$)'''),
        latext('''$$
            \\begin{align}
            & \\frac{f(x_{0})(x - x_0)}{x_1 - x_0} \\left[ \\frac{x_1 - x_0}{x - x_0} - 1 + \\frac{x-x_1}{x_{2}-x_{0}} \\right] \\notag \\\\
            & \\frac{f(x_{0})(x - x_0)}{x_1 - x_0} \\left[ \\frac{(x_{2}-x_{0})(x_1 - x_0) - (x - x_0)(x_{2}-x_{0}) + (x-x_1)(x-x_0)  }{(x - x_0)(x_{2}-x_{0})} \\right] \\notag \\\\
            & \\frac{f(x_{0})(x - x_0)}{x_1 - x_0} \\left[ \\frac{(x_{2}-x_{0})(x_1 - x ) + (x-x_1)(x-x_0) }{(x - x_0)(x_{2}-x_{0})} \\right] \\notag \\\\
            & \\frac{f(x_{0})}{x_1 - x_0} \\left[ \\frac{(x_{0}-x_{2})(x - x_{1} ) + (x-x_1)(x-x_0)   }{(x_{2}-x_{0})} \\right] \\notag \\\\
            & \\frac{f(x_{0})}{x_1 - x_0} \\left[ \\frac{(x-x_1)(x_{0}-x_{2} + x-x_0) }{(x_{2}-x_{0})} \\right] \\notag \\\\
            & \\frac{f(x_{0})}{x_1 - x_0} \\left[ \\frac{(x-x_1)(x-x_{2}) }{(x_{2}-x_{0})} \\right] \\notag \\\\
            & \\frac{(x-x_1)(x-x_{2}) }{(x_{2}-x_{0})(x_1 - x_0)} f(x_{0}) = \\frac{(x-x_1)(x-x_{2}) }{(x_{0}-x_{2})(-1)(x_1 - x_0)}f(x_{0}) \\notag \\\\
            & \\frac{(x-x_1)(x-x_{2}) }{(x_{0}-x_{2})(x_0 - x_1)}f(x_{0})
            \\end{align}
            $$'''),
        latext('Analizando los terminos relacionados a $f(x_1)$'),
        latext('''$$
            \\begin{align}
            & \\frac{f(x_{1})(x - x_0)}{x_1 - x_0} \\left[ 1 + \\frac{x-x_1}{x_1-x_2} \\right] \\\\
            & \\frac{f(x_{1})(x - x_0)}{x_1 - x_0} \\left[ \\frac{x_1-x_2 + x - x_1 }{x_1-x_2} \\right] \\notag \\\\
            & \\frac{(x-x_2)(x - x_0)}{(x_1 - x_0)(x_1-x_2)} f(x_1) \\notag
            \\end{align}
            $$'''),
        latext('Por último, los terminos relacionados a $f(x_2)$,'),
        latext('''$$
            \\begin{equation}
            \\frac{(x-x_{0})(x-x_{1})}{(x_{2}-x_{1})(x_{2}-x_{0})} f(x_{2})
            \\end{equation}
            $$'''),
        html.P('''Las ecuaciones (26), (27) y (28), permiten concluir que la ecuación
            (25) es equivalente a la ecuación (16). Demostrando el origen de (16), a partir 
            del polinomio de interpolación de Newton.'''),
        html.H3('Regla de Simpson 1/3'),
        html.P('''La regla de Simpson 1/3, consiste en la idea de aproximar una función usando un
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
            &+ \\int_{x_0}^{x_2} \\left[ \\frac{ (x - x_{0}) (x - x_{1}) }{(x_{2} - x_{0}) (x_{2} - x_{1})} f(x_{2}) \\right] dx \\notag
            \\end{align}
            $$'''),
        html.P('Teniendo en cuenta que,'),
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
        latext('''$$
            \\begin{equation}
            x
            \\end{equation}
            $$'''),
        latext('''$$
            \\begin{align}
            y
            \\end{align}
            $$''')
    ])
])

def go_interpolation():
    """interpolation"""
    return layout
