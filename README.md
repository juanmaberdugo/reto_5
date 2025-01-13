# reto_5
Para el reto 5, se proponen dos formas para utilizar módulos y paquetes.

## Opcion 1
- A unique module inside of package Shape
```bash
└── Shapes/ 
    ├── __init__.py
    ├── shape.py 
├── main.py
```
Para esta opción, se crea un paquete que contiene un único módulo, en el cual se incluyen las clases necesarias para ejecutar el archivo main.py

## Opcion 2
- Individual modules that import Shape in inheritates from it.
```bash
└── Shapes/ 
    ├── __init__.py
    ├── equilateral.py
    ├── isoseceles.py
    ├── line.py
    ├── point.py
    ├── rectangle.py
    ├── scalene.py
    ├── shapes.py
    ├── triangle.py
    ├── trirectangle.py 
├── main.py
```
Para esta segunda opción, se consideraron todas las clases relacionadas con la clase Shape, agrupándolas en varios módulos. De esta manera, es posible visualizar las relaciones de herencia entre las clases mediante el uso de módulos.
