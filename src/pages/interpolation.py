"""interpolation"""
from dash import html, dcc

layout = html.Div(children=[
    html.Div([
        html.H1('Interpolación'),
        html.P('''
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed maximus, quam vitae varius eleifend, augue lectus placerat massa, ut sollicitudin elit ipsum at tellus. Integer lobortis blandit purus, eu mollis tortor gravida et. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Integer non consectetur nibh. Sed et sapien sit amet lorem ultricies imperdiet ac non leo. Nunc vitae erat rhoncus, tempus sapien vitae, volutpat dui. In hac habitasse platea dictumst. Donec mattis aliquet justo vitae ornare. Pellentesque ut massa porttitor, gravida ante ut, iaculis arcu. Mauris eu facilisis arcu. Mauris maximus ac ex nec molestie. Nunc neque lorem, porttitor in pharetra eu, tincidunt ac justo. Maecenas dui metus, auctor ac convallis in, mattis at lectus. Nullam et eros eget nisl molestie iaculis. Suspendisse ornare in magna sed vestibulum. Maecenas eget sodales mi. Phasellus feugiat porta purus vitae tempus. Sed mauris quam, ornare eget nunc quis, tincidunt vulputate mauris. Vivamus tempor condimentum est. Quisque molestie lectus ac augue sodales pretium. Praesent non gravida turpis. Cras id lorem eu dui dapibus ultricies at at nisi. Donec scelerisque lectus ut dui aliquet, ac consectetur lectus tempus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Donec non libero sagittis, porttitor ante vitae, elementum quam.
            Nam ut justo elementum, egestas nunc semper, suscipit velit. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Interdum et malesuada fames ac ante ipsum primis in faucibus. Proin a facilisis nulla. Phasellus sit amet ullamcorper enim. Duis tortor eros, bibendum eu risus vel, auctor vestibulum ipsum. Nam quis augue pretium, dignissim est vitae, dictum ex. Fusce ornare eros ut velit volutpat, volutpat fermentum sem bibendum. Nullam egestas leo molestie, pharetra lorem ut, condimentum nisi. Phasellus eu elit hendrerit urna convallis aliquet. Aliquam aliquam ligula ac nisl aliquam sagittis. Duis fringilla, velit ut maximus aliquam, neque libero lobortis odio, sit amet congue ante tortor eget nisi.
            Vivamus convallis urna ut nulla pulvinar, placerat tincidunt sapien sodales. Curabitur finibus vitae mauris in ultrices. Donec sit amet volutpat felis, quis gravida libero. Suspendisse laoreet nisi quis hendrerit vestibulum. Morbi lacus nisl, pharetra non orci at, consectetur imperdiet nisi. Ut placerat hendrerit massa, at facilisis ex ultrices eu. Suspendisse eros sem, mattis in leo egestas, consequat venenatis felis. Proin rhoncus nibh elit, vel pellentesque nulla facilisis a.
            Proin gravida tristique nunc et placerat. Quisque ut venenatis enim, vel dictum quam. Etiam quis massa congue, dapibus augue at, pulvinar augue. Suspendisse sit amet congue enim. Phasellus sit amet sapien ante. Mauris libero lacus, cursus et lacus et, porttitor fringilla lorem. Vestibulum ornare odio finibus nunc luctus dignissim. Nam ultricies velit quam, sit amet malesuada elit viverra eget. Suspendisse nulla enim, vehicula sit amet interdum bibendum, maximus et diam. Curabitur feugiat fringilla magna sed feugiat. Integer porta consequat urna vel interdum. Pellentesque orci sapien, iaculis vel mauris eu, sodales vulputate urna. Nam eu scelerisque lectus. Cras quis consequat est. Proin imperdiet, metus ut volutpat volutpat, mauris nibh semper ipsum, sit amet rutrum nisi arcu vitae libero. Maecenas nulla nulla, malesuada et condimentum sed, rutrum id justo.
            ''',
            style={"textAlign": "justify"}
            ),
        html.H2('Sección'),
        dcc.Markdown('$$Area (m^{2})$$', mathjax=True),
        dcc.Markdown('$$x^{2} + 5x+ 2x_{0}$$', mathjax=True),
        dcc.Markdown('$$\\frac{4}{3}$$', mathjax=True),
        dcc.Markdown('$$\\frac{4}{3}$$', mathjax=True),
        dcc.Markdown('$$\\binom{n}{k}$$', mathjax=True),
        dcc.Markdown('$$\\int$$', mathjax=True),
        dcc.Markdown('$$\\mu$$', mathjax=True),
        dcc.Markdown('$$\\pi$$', mathjax=True),
        dcc.Markdown(
            '''$$
            f(x)= \\frac{1}{\\sigma \\sqrt{2 \\pi}} e^{\\frac{1}{2} \\frac{x - \\mu}{\\sigma}^2 }
            $$''',
            mathjax=True),
        dcc.Markdown('''$$
            \\begin{align}
            & \\text{Maximize: } 5.00 x_{1} + 7.50 x_{2} \\\\
            & \\text{Subject to:} \\\\
            & \\frac{x + 2}{x^3 + \\pi}
            \\end{align}
            $$''',
            mathjax=True),
        dcc.Markdown('''$$
            \\begin{equation}
            f(x) = a_{0} + a_{1} x + a_{2} x^{2} + \\ldots + a_{n} x^{n}
            \\end{equation}   
            $$''',
            mathjax=True)
    ])
])

def go_interpolation():
    """interpolation"""
    return layout
