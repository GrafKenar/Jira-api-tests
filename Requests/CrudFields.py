import requests
from Methods import FormingJsonData
from Methods.FormingJsonData import FormingJsonData
from Settings import Settings


class CrudFields:
    base_url = Settings.BaseUrl
    headers = Settings.headers
    auth = Settings.auth

    def create_custom_field(self, name, test_data):
        payload_creation = FormingJsonData(test_data)
        url = self.base_url + f'/field'
        formed_json = payload_creation.form_json_for_field(summary=name)
        response = requests.post(url, data=formed_json, headers=self.headers, auth=self.auth)
        return response

    def delete_custom_field(self, field_id):
        url = self.base_url + f'/field/{field_id}'
        response = requests.delete(url, auth=self.auth)
        return response

    def add_field_to_default_screen(self, field_id):
        url = self.base_url + f'/screens/addToDefault/{field_id}'
        response = requests.post(url, headers=self.headers, auth=self.auth)
        return response
