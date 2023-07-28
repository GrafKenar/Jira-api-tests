from Methods.AdditionalMethods import *
import json

from Requests.CrudIssues import CrudIssues
from TestData.TestData import test_set_1


def test_creating_issue(delete_issue):
    issue_name = new_random_value()
    ci = CrudIssues()
    created_issue = ci.create_issue(summary=issue_name,
                                    test_data=test_set_1)
    check_that_status_code_is_success(created_issue)
    issue_id = test_creating_issue.id = get_id_of_created_issue(created_issue)
    issue_info = ci.get_issue_info(issue_id)
    check_that_issue_has_correct_name(issue_info, issue_name)


def test_updating_issue_summary(new_issue_id):
    new_name = new_random_value()
    ci = CrudIssues()
    updated_issue = ci.edit_issue(new_issue_id,
                                  summary=new_name,
                                  test_data=test_set_1)
    check_that_status_code_is_success(updated_issue)
    issue_info = ci.get_issue_info(new_issue_id)
    check_that_issue_has_correct_name(issue_info, new_name)


def test_delete_issue(new_issue_id):
    ci = CrudIssues()
    deleted_issue = ci.delete_issue(new_issue_id)
    check_that_status_code_is_success(deleted_issue)
    issue_info = ci.get_issue_info(new_issue_id)
    check_that_issue_deleted(issue_info)


def test_creating_issue_with_custom_field(delete_issue, new_custom_field):
    issue_name, custom_field_value = new_random_value(), new_random_value()
    ci = CrudIssues()
    created_issue = ci.create_issue(summary=issue_name,
                                    custom_field_id=new_custom_field,
                                    custom_field_data=custom_field_value,
                                    test_data=test_set_1)
    check_that_status_code_is_success(created_issue)
    issue_id = test_creating_issue_with_custom_field.id = json.loads(created_issue.text)['id']
    issue_info = ci.get_issue_info(issue_id)
    check_that_custom_field_value_is_correct(issue_info, new_custom_field, custom_field_value)


def test_updating_issue_custom_field_value(new_issue_id_with_field):
    ci = CrudIssues()
    issue_id, field_id = new_issue_id_with_field["issue_id"], new_issue_id_with_field["field_id"]
    new_field_value = new_random_value()
    updated_issue = ci.edit_issue(issue_id=issue_id,
                                  custom_field_id=field_id,
                                  custom_field_data=new_field_value,
                                  test_data=test_set_1)
    check_that_status_code_is_success(updated_issue)
    issue_info = ci.get_issue_info(issue_id)
    check_that_custom_field_value_is_correct(issue_info, field_id, new_field_value)
