import pytest

from main_code.test_body_with_request_helper import main_test_function

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
        "expected_error_message": ""
    }
]


@pytest.mark.parametrize(
    "test_data",
    test_data_list
)
def test_executor(test_data):
    main_test_function(test_data)
