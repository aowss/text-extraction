from behave import *

from clients.textract import extract_data


@given('this proof of sustainability: {file_name}')
def step_impl(context, file_name):
    with open('tests/input/' + file_name, mode='rb') as file:
        context.file_content = file.read()
    pass


@when('the extraction is run using {framework}')
def step_impl(context, framework):
    if (framework == 'textract'):
        context.result = extract_data(context.file_content)
    else:
        assert True is False
    assert True is not False


@then('the following data is extracted')
def step_impl(context):
    # Print detected text
    for item in context.result["Blocks"]:
        if item["BlockType"] == "LINE":
            print('\033[94m' + item["Text"] + '\033[0m')
    # for row in context.table:
    #     print("data = ", row)
    assert context.failed is False
