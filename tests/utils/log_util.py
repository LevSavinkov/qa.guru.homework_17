import allure


def log_response(response):
    allure.attach(
        body=str(response.status_code),
        name="HTTP Status Code",
        attachment_type=allure.attachment_type.TEXT
    )
    allure.attach(
        body=response.text,
        name="Response Body",
        attachment_type=allure.attachment_type.JSON
    )
