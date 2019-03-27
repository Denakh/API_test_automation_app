
test_data_list =   [
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
       "expected_error_message": "error"
    }
 ]


def main_test_function(test_data_list):
    for test_data in test_data_list:
        print(test_data["case_name"])
        assert test_data["actual_status_code"] == test_data["expected_status_code"]
        if test_data["expected_error_message"] != "":
            if test_data["validation_type"] == "value":
                assert check_subdictionary_using_param_values(test_data["actual_json"], test_data["expected_json_part"]) is True

def check_subdictionary_using_param_values(int_dict_whole, int_dict_part):
    int_dpk_list = int_dict_part.keys()
    #print(int_dpk_list)
    for key in int_dpk_list:
        if not int_dict_whole.has_key(key):
            return False
        else:
            if type(int_dict_part[key]) == dict and type(int_dict_whole[key]) == dict:
                subdict_p = int_dict_part[key]
                subdict_w = int_dict_whole[key]
                if check_subdictionary_using_param_values(subdict_w, subdict_p) is False:
                    return False
            else:
                if int_dict_part[key] != int_dict_whole[key]:
                    return False
    return True


def check_subdictionary_using_param_types(int_dict_whole, int_dict_part):
    int_dpk_list = int_dict_part.keys()
    #print(int_dpk_list)
    for key in int_dpk_list:
        if not int_dict_whole.has_key(key):
            return False
        else:
            if type(int_dict_part[key]) == dict and type(int_dict_whole[key]) == dict:
                subdict_p = int_dict_part[key]
                subdict_w = int_dict_whole[key]
                if check_subdictionary_using_param_types(subdict_w, subdict_p) is False:
                    return False
            else:
                if not isinstance(int_dict_part[key], type(int_dict_part[key])):
                    return False
    return True
