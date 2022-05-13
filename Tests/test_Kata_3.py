from Kata_3_6kyu import solution
import pytest


@pytest.mark.parametrize("a, expected_result", [(4, 3), (6, 8), (16, 60), (3, 0),
                                                (15, 45), (200, 9168,)])
def test_solution_kata3(a, expected_result):
    assert solution(a) == expected_result
    assert solution(a) == expected_result
    assert solution(a) == expected_result
    assert solution(a) == expected_result
    assert solution(a) == expected_result
    assert solution(a) == expected_result
