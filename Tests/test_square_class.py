class TestSquareClass:

    def test_angles(self, create_square):
        assert create_square.angles() == 4

    def test_name(self, create_square):
        assert create_square.name() == "Square"

    def test_area(self, create_square):
        assert create_square.area() == 9

    def test_perimeter(self, create_square):
        assert create_square.perimeter() == 12

    def test_add_area(self, create_square, create_circle):
        assert create_square.area() + create_circle.area() == 37.27433388230814
