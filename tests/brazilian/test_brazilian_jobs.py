from src.pre_built.brazilian_jobs import read_brazilian_file
from unittest.mock import MagicMock, patch


def test_brazilian_jobs():
    test_data = [
        {"titulo": "Dev-Front", "salario": "R$5000", "tipo": "trainee"},
        {"titulo": "DevOps", "salario": "R$9000", "tipo": "trainee"},
    ]
    process_jobs_mock = MagicMock()
    process_jobs_mock.read.return_value = test_data
    process_jobs_mock.jobs_list = test_data

    with patch("src.pre_built.brazilian_jobs.ProcessJobs",
               return_value=process_jobs_mock,
               ):
        result = read_brazilian_file('tests/mocks/brazilian_jobs.csv')

    expected_result = [
        {"title": "Dev-Front", "salary": "R$5000", "type": "trainee"},
        {"title": "DevOps", "salary": "R$9000", "type": "trainee"},
    ]

    assert result == expected_result
