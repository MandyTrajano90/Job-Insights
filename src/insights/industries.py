from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        self.jobs_list = list()
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        unique_industry = set()
        for row in self.jobs_list:
            industry = row['industry']
            if industry and industry not in unique_industry:
                unique_industry.add(industry)
        return list(unique_industry)
