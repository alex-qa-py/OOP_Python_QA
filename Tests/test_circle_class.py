class TestCircleClass:

    def test_angles(self, create_circle):
        assert create_circle.angles() == 0

    def test_name(self, create_circle):
        assert create_circle.name() == "Circle"

    def test_area(self, create_circle):
        assert create_circle.area() == 28.274333882308138

    def test_perimeter(self, create_circle):
        assert create_circle.perimeter() == 18.84955592153876

    def test_add_area(self, create_circle, create_square):
        assert create_circle.area() + create_square.area() == 37.27433388230814