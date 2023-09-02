def test_basic_math_operation():
    assert basic_math_operation('add', 5, 3) == 8
    assert basic_math_operation('subtract', 10, 4) == 6
    assert basic_math_operation('multiply', 6, 2) == 12
    assert basic_math_operation('divide', 8, 2) == 4.0
    assert basic_math_operation('divide', 10, 0) == "Cannot divide by zero"
    assert basic_math_operation('power', 2, 3) == "Invalid operation"

test_basic_math_operation()
