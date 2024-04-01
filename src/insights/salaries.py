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

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        pass

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
