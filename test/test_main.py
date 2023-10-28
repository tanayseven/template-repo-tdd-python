from src.main import add


def test_main_add():
    actual_sum = add(1, 2)

    expected_sum = 3

    assert actual_sum == expected_sum
