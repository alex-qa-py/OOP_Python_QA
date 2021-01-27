class TestTriangleClass:

    def test_angles(self, create_triangle):
        assert create_triangle.angles() == 3

    def test_name(self, create_triangle):
        assert create_triangle.name() == "Triangle"

    def test_area(self, create_triangle):
        assert create_triangle.area() == 5.562148865321747

    def test_perimeter(self, create_triangle):
        assert create_triangle.perimeter() == 11

    def test_add_area(self, create_triangle, create_circle):
        assert create_triangle.area() + create_circle.area() == 33.83648274762989