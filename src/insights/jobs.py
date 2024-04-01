from typing import List, Dict, Union
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        with open(path, encoding="utf-8") as job_file:
            reader = csv.DictReader(job_file, delimiter=",", quotechar='"')
            self.jobs_list = [row for row in reader]

    def get_unique_job_types(self) -> List[str]:
        unique_job = set()
        for row in self.jobs_list:
            job_type = row["job_type"]
            if job_type and job_type not in unique_job:
                unique_job.add(job_type)
        return list(unique_job)

    def filter_by_multiple_criteria(
            self,
            jobs: List[Dict[str, str]],
            filter_criteria: Dict[str, Union[str, List[str]]],
            ) -> List[dict]:
        if not isinstance(filter_criteria, dict):
            raise TypeError("filter_by_multiple_criteria must be a dictionary")
        filtered_jobs = []
        for job in jobs:
            if all(
                job.get(key) in value for key, value in filter_criteria.items()
            ):
                filtered_jobs.append(job)
        return filtered_jobs
