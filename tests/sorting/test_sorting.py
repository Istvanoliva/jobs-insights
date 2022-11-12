from src.sorting import sort_by
from src.jobs import read
from src.insights import get_max_salary, get_min_salary


def test_sort_by_criteria():
    path = "src/jobs.csv"
    jobs_list = read(path)

    sort_by(jobs_list, "min_salary")
    expected = get_min_salary(path)
    result = jobs_list[0]["min_salary"]
    assert result == str(expected)

    sort_by(jobs_list, "max_salary")
    expected = get_max_salary(path)
    result = jobs_list[0]["max_salary"]
    assert result == str(expected)
