import pytest

import test_body

test_data_list_ex = [
    {
       "case_name": "success request",
       "actual_status_code": 200,
       "actual_json": {
         "param1": 1,
         "param1_a": "aaa",
         "param2": {
           "param3": "value",
           "param4": ["a", "b", "c"],
           "param4_a": 111
          }
       },
       "actual_error_message": "",
       "expected_status_code": 200,
       "expected_json_part": {
         "param2": {
           "param3": "value",
           "param4": ["a", "b", "c"]
          }
       },
       "validation_type": "type",
       "decimal_accuracy": 2,
       "expected_error_message": ""
    },
    {
       "case_name": "unsuccess request",
       "actual_status_code": 400,
       "actual_json": {},
       "actual_error_message": "error",
       "expected_status_code": 400,
       "expected_json_part": {},
       "validation_type": "",
       "decimal_accuracy": 2,
       "expected_error_message": "error"
    }
 ]


@pytest.mark.parametrize(
    "test_data_list",
    test_data_list_ex
)
def test_execution(test_data_list):
    test_body.main_test_function(test_data_list)
