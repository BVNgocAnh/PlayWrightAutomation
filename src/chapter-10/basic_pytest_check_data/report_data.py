import json
import os

class GenaratingReport:
    def delete_report_file(file_path):
        if os.path.exists(file_path):
            os.remove(file_path)
            print("Delete report successfully!")
        else:
            print("The report file doesn't not existing")

    def generate_report(timeStamp: str, status: str, testCaseId: str):
        GenaratingReport.delete_report_file("report.json")
        result_data = {
            "timeStamp": timeStamp,
            "status": status,
            "testCaseId": testCaseId
        }

        with open('report.json', 'w') as file:
            return json.dump(result_data, file, indent = 3)
        