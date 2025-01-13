import shapes.shapes as shapes

def main():
    rect = shapes.Rectangle(x=0, y=0, width=10, height=5)
    print(f"Area del rectángulo: {rect.compute_area()}")
    print(f"Perimetro del rectángulo: {rect.compute_perimeter()}")

    square = shapes.Square(x=0, y=0, side_length=10)
    print(f"Area del cuadrado: {square.compute_area()}")
    print(f"Perimetro del cuadrado: {square.compute_perimeter()}")

    triangle_vertices = [shapes.Point(0, 0), shapes.Point(4, 0), shapes.Point(0, 3)]
    triangle = shapes.Triangle(triangle_vertices)
    print(f"Area del triangulo: {triangle.compute_area()}")
    print(f"Perimetro del triangulo: {triangle.compute_perimeter()}")

    trirectangle_vertices = [shapes.Point(0, 0), shapes.Point(3, 0), shapes.Point(0, 4)]
    trirectangle = shapes.TriRectangle(trirectangle_vertices)
    print(f"Area del triangulo rectángulo: {trirectangle.compute_area()}")
    print(f"Perimetro del triangulo rectangulo: {trirectangle.compute_perimeter()}")

if __name__ == "__main__":
    main()