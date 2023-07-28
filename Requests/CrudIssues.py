import requests
from Methods.FormingJsonData import FormingJsonData
from Settings import Settings


class CrudIssues:
    base_url = Settings.BaseUrl
    headers = Settings.headers
    auth = Settings.auth

    def create_issue(self, summary, test_data, custom_field_id='', custom_field_data=''):
        payload_creation = FormingJsonData(test_data)
        formed_json = payload_creation.form_json_for_issue(summary=summary,
                                                           custom_field_id=custom_field_id,
                                                           custom_field_data=custom_field_data)
        url = self.base_url+"/issue"
        response = requests.post(url, data=formed_json, headers=self.headers, auth=self.auth)
        return response

    def get_issue_info(self, issue_id):
        url = self.base_url+f'/issue/{issue_id}'
        response = requests.get(url, auth=self.auth)
        return response

    def delete_issue(self, issue_id):
        url = self.base_url+f'/issue/{issue_id}'
        response = requests.delete(url, auth=self.auth)
        return response

    def edit_issue(self, issue_id, test_data, custom_field_id='', custom_field_data='', summary='stub'):
        payload_creation = FormingJsonData(test_data)
        formed_json = payload_creation.form_json_for_issue(summary=summary,
                                                           custom_field_id=custom_field_id,
                                                           custom_field_data=custom_field_data)
        url = self.base_url + f"/issue/{issue_id}"
        response = requests.put(url, data=formed_json, headers=self.headers, auth=self.auth)
        return response
