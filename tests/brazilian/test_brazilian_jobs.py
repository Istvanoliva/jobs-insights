from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    brazilian_file = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    assert brazilian_file[0].get('title')
