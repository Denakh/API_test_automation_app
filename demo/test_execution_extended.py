from time import sleep

import pytest

from demo.test_body_with_request_extended import main_test_function_extended

test_data_list = [
    {
        "case_name": "example",
        "url": "endpoint",
        "request_json": "auction_payload_json_with_cpmoverride_param",
        "headers": "headers",
        "request_type": "post",
        "expected_status_code": 200,
        "expected_json_part": {
            "seatbid": [
                {
                    "bid": [
                        {
                            "price": 5.15,
                        }
                    ]
                }
            ]
        },
        "validation_type": "value",
        "decimal_accuracy": 2,
        "expected_error_message": "",
        "execution_number": 2,
        "time_to_next_test": 10
    },
    {
        "case_name": "example",
        "url": "endpoint",
        "request_json": "auction_payload_json_with_cpmoverride_param",
        "headers": "headers",
        "request_type": "post",
        "expected_status_code": 200,
        "expected_json_part": {
            "seatbid": [
                {
                    "bid": [
                        {
                            "price": 5.15,
                        }
                    ]
                }
            ]
        },
        "validation_type": "value",
        "decimal_accuracy": 2,
        "expected_error_message": "",
        "execution_number": 5,
        "time_to_next_test": 1
    }
]


def get_test_data_list_reformat(test_data_list_int = test_data_list):
    new_test_data_list = []
    for test_data in test_data_list_int:
        for i in range(0, test_data["execution_number"]):
            new_test_data_list.append(test_data)
    return new_test_data_list


@pytest.fixture()
def extended_param_using(request, test_data):
    time_to_next_test = test_data["time_to_next_test"]

    def extended_param_using_teardown():
        sleep(time_to_next_test)

    request.addfinalizer(extended_param_using_teardown)


@pytest.mark.parametrize(
    "test_data",
    get_test_data_list_reformat()
)
def test_executor_extended(test_data, extended_param_using):
    main_test_function_extended(test_data)
