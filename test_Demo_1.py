import Demo_1

def test_area1():
    result = Demo_1.area1(10, 20)
    assert result <= 30

def test_area2():
    result = Demo_1.area2(2, 2)
    assert result >= 20
