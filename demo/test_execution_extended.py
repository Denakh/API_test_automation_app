
import pytest

from demo.data_list_helper import get_test_data_list_reformat
from demo.test_body_with_request_extended_helper import main_test_function_extended

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


@pytest.mark.parametrize(
    "test_data",
    get_test_data_list_reformat(test_data_list)
)
def test_executor_extended(test_data, extended_param_using):
    main_test_function_extended(test_data)
