import pytest
from Requests.CrudFields import CrudFields
from Methods.AdditionalMethods import new_random_value
import json

from Requests.CrudIssues import CrudIssues
from TestData.TestData import test_set_1


@pytest.fixture
def new_issue_id():
    summary = new_random_value()
    ci = CrudIssues()
    created_issue = ci.create_issue(summary,
                                    test_data=test_set_1)
    new_issue_id = json.loads(created_issue.text)['id']
    yield new_issue_id
    ci.delete_issue(new_issue_id)


@pytest.fixture
def delete_issue(request):
    yield
    ci = CrudIssues()
    issue_id = getattr(request.function, "id")
    ci.delete_issue(issue_id)


@pytest.fixture
def new_custom_field():
    name = new_random_value()
    cf = CrudFields()
    created_field = cf.create_custom_field(name,
                                           test_data=test_set_1)
    new_field_id = json.loads(created_field.text)['id']
    cf.add_field_to_default_screen(new_field_id)
    yield new_field_id
    cf.delete_custom_field(new_field_id)


@pytest.fixture
def new_issue_id_with_field(new_custom_field):
    summary = new_random_value()
    ci = CrudIssues()
    created_issue = ci.create_issue(summary,
                                    custom_field_id=new_custom_field,
                                    custom_field_data=new_random_value(),
                                    test_data=test_set_1)
    new_issue_id = json.loads(created_issue.text)['id']
    data = {"issue_id": new_issue_id, "field_id": new_custom_field}
    yield data
    ci.delete_issue(new_issue_id)
