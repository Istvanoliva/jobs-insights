from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    unique_jobs = set()

    for job in jobs_list:
        unique_jobs.add(job["job_type"])
    return unique_jobs


def filter_by_job_type(jobs, job_type):
    jobs_list = list()

    for job in jobs:
        if job["job_type"] == job_type:
            jobs_list.append(job)
    return jobs_list


def get_unique_industries(path):
    jobs_list = read(path)
    unique_industries = set()

    for job in jobs_list:
        if job["industry"]:
            unique_industries.add(job["industry"])
    return unique_industries


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


def get_max_salary(path):
    jobs_list = read(path)
    max_salary = 0

    for job in jobs_list:
        if (
            job["max_salary"].isdigit()
            and int(job["max_salary"]) > max_salary
        ):
            max_salary = int(job["max_salary"])
    return max_salary


def get_min_salary(path):
    jobs_list = read(path)
    min_salary = []

    for salary in jobs_list:
        if salary["min_salary"] and salary["min_salary"].isdigit():
            min_salary.append(salary["min_salary"])
            lower_salary = int(min(min_salary, key=int))
    return lower_salary


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
