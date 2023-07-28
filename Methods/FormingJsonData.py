import json


class FormingJsonData:
    def __init__(self, test_data):
        self.test_data = test_data

    def form_json_for_issue(self, summary, custom_field_id='', custom_field_data=''):
        formed_json = {
          "fields": {
            "assignee": {"id": self.test_data["assignee"]},
            "issuetype": {"id": self.test_data["issuetype_id"]},
            "labels": self.test_data["labels"],
            "project": {"id": self.test_data["project_id"]},
            "reporter": {"id": self.test_data["reporter_id"]},
            "summary": summary
          },
          "update": {}
        }

        if custom_field_id != '':
            formed_json["fields"][custom_field_id] = custom_field_data

        payload = json.dumps(formed_json)
        return payload

    def form_json_for_field(self, summary):
        formed_json = {
          "description": self.test_data["description"],
          "name": summary,
          "searcherKey": self.test_data["searcherKey"],
          "type": self.test_data["type"]
        }

        payload = json.dumps(formed_json)
        return payload
