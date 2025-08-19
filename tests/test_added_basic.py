def test_truth():
    assert True

def test_arithmetic():
    assert 1 + 1 == 2

def test_string_upper():
    assert "hello".upper() == "HELLO"

def test_list_reverse():
    assert [1, 2, 3][::-1] == [3, 2, 1]
