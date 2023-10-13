Para ejecutar, desde la carpeta src, en consola,

python app.py

# Se implemento el método de simpson 1/3, para el caso de una distribución de probabilidad normal

<img width="436" alt="image" src="https://github.com/fvillarmur/mydash/assets/142535134/91aa03d9-55ee-43b1-9527-01f087729bfc">

Se consideran, 200000 segmentos 
https://github.com/fvillarmur/mydash/blob/4ddf810d80908ca30f3e2304d288a94ab7cdb430/src/utils/simpson_logic.py#L6

Usando la libreria numpy, partimos el espacio x en 200000 segmentos iguales
https://github.com/fvillarmur/mydash/blob/4ddf810d80908ca30f3e2304d288a94ab7cdb430/src/utils/simpson_logic.py#L50-L52

Usando las capacidades de álgebra lineal de numpy,
https://github.com/fvillarmur/mydash/blob/4ddf810d80908ca30f3e2304d288a94ab7cdb430/src/utils/simpson_logic.py#L10-L14
Se escribe la ecuación normal y se evalua para cada valor del array_x, mean es la media y sigma la desviación estándar.

https://github.com/fvillarmur/mydash/blob/4ddf810d80908ca30f3e2304d288a94ab7cdb430/src/utils/simpson_logic.py#L17-L29

Por último el método de simpson, al inicio se excluye el primero y el último elemento de array_fx.
Partimos los pares y los impares. De acuerdo a la ecuación, los pares se suman *2 y los impares *4.

np.sum, permite sumar todos los elementos de un numpy array. 

Se suma todo incluyendo el 1ero y el último elemento de array_fx.

_h representa la fracción que multiplica a la sumatoria.

Dando así, la aproximación, de la integral de la distribución gaussiana con el método de simpson 1/3.
