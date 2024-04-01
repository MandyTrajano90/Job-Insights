from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        salaries = [
            int(row['max_salary'])
            for row in self.jobs_list
            if row['max_salary'] and row['max_salary'].isdigit()
        ]
        return max(salaries)

    def get_min_salary(self) -> int:
        salaries = [
            int(row['min_salary'])
            for row in self.jobs_list
            if row['min_salary'] and row['min_salary'].isdigit()
        ]
        return min(salaries)

    def verify_salary(self, value: int | float | str) -> float:
        if value is None or not isinstance(value, (int, float, str)):
            raise ValueError('Invalid salary value')
        return float(value)

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        if 'min_salary' not in job or 'max_salary' not in job:
            raise ValueError('Salary range not found')
        min_salary = self.verify_salary(job['min_salary'])
        max_salary = self.verify_salary(job['max_salary'])
        if min_salary > max_salary:
            raise ValueError('Invalid salary range')
        salary = self.verify_salary(salary)
        return min_salary <= salary <= max_salary

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
