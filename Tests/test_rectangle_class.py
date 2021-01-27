class TestRectangleClass:

    def test_angles(self, create_rectangle):
        assert create_rectangle.angles() == 4

    def test_name(self, create_rectangle):
        assert create_rectangle.name() == "Rectangle"

    def test_area(self, create_rectangle):
        assert create_rectangle.area() == 12

    def test_perimeter(self, create_rectangle):
        assert create_rectangle.perimeter() == 24

    def test_add_area(self, create_rectangle, create_triangle):
        assert create_rectangle.area() + create_triangle.area() == 17.562148865321745