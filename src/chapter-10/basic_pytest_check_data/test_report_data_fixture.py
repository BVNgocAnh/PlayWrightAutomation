from report_data import GenaratingReport
import json
import pytest

@pytest.fixture()
def report_data():
    print("\n Generate report in pytest fixture")
    GenaratingReport.generate_report(
        "2025-3-4",
        "Passed",
        "TC-001 Covering test case example"
    )
    with open("report.json") as file:
        return json.load(file)

def test_report_date(report_data):
    print("\n Verify Test Case 01")
    assert type(report_data) == dict
    assert len(report_data) == 3

def test_report_data_key(report_data):
    print("\n Verify Test Case 02")
    assert "timeStamp" in report_data
    assert "status" in report_data
    assert "testCaseId" in report_data

def test_report_data_value(report_data):
    print("\n Verify Test Case 03")
    assert "2025-3-4" == report_data['timeStamp']   
    assert "Passed" == report_data['status']
    assert "TC-001 Covering test case example" == report_data['testCaseId']