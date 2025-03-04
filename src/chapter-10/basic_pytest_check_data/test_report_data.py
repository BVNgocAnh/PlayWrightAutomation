from report_data import GenaratingReport
import json

def test_report_date():
    GenaratingReport.generate_report(
        "2025-3-4",
        "Passed",
        "TC-001 Covering test case example  "
    )

    with open("report.json") as file:
        data = json.load(file)
        assert type(data) == dict
        assert len(data) == 3

def test_report_data_key():
    GenaratingReport.generate_report(
        "2025-3-4",
        "Passed",
        "TC-001 Covering test case example  "
    )

    with open("report.json") as file:
            data = json.load(file)
            assert "timeStamp" in data
            assert "status" in data
            assert "testCaseId" in data

def test_report_data_value():
    GenaratingReport.generate_report(
        "2025-3-4",
        "Passed",
        "TC-001 Covering test case example"
    )

    with open("report.json") as file:
            data = json.load(file)
            assert "2025-3-4" == data['timeStamp']
            assert "Passed" == data['status']
            assert "TC-001 Covering test case example" == data['testCaseId']