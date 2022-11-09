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
    jobs_list = list()

    for job in jobs:
        if job["industry"] == industry:
            jobs_list.append(job)
    return jobs_list


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
    min_salary = list()

    for salary in jobs_list:
        if salary["min_salary"] and salary["min_salary"].isdigit():
            min_salary.append(salary["min_salary"])
            lower_salary = int(min(min_salary, key=int))
    return lower_salary


def matches_salary_range(job, salary):
    if "min_salary" not in job.keys() or "max_salary" not in job.keys():
        raise ValueError("invalid salary")
    if type(job["max_salary"]) != int or type(job["min_salary"]) != int:
        raise ValueError("job salary is not a number")
    if job["max_salary"] < job["min_salary"]:
        raise ValueError("salary is lower than expected")
    if type(salary) != int:
        raise ValueError("salary is not a number")
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    filtered_jobs = list()

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError as error:
            print(error)

    return filtered_jobs
