import json
import uuid


def new_random_value():
    return uuid.uuid4().hex


def check_that_status_code_is_success(sent_request):
    assert sent_request.status_code in (201, 204)


def check_that_issue_deleted(sent_request):
    assert sent_request.status_code == 404


def get_id_of_created_issue(created_issue):
    return json.loads(created_issue.text)['id']


def check_that_issue_has_correct_name(issue_info, issue_name):
    assert str(json.loads(issue_info.text)["fields"]["summary"]) == issue_name


def check_that_custom_field_value_is_correct(issue_info, custom_field, custom_field_value):
    assert str(json.loads(issue_info.text)["fields"][custom_field]) == custom_field_value
