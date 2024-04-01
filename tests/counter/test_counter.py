from src.pre_built.counter import count_ocurrences


def test_counter():
    python_ocurrences = count_ocurrences("data/jobs.csv", "Python")
    js_ocurrences = count_ocurrences("data/jobs.csv", "JavaScript")
    assert python_ocurrences == 1639
    assert js_ocurrences == 122