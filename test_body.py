def main_test_function(test_data):
    print()
    print(test_data["case_name"] + ":")
    assert test_data["actual_status_code"] == test_data["expected_status_code"], \
        "actual status code doesn't match expected"
    if test_data["expected_error_message"] == "":
        if test_data["validation_type"] == "value":
            assert check_subdictionary_using_param_values(test_data["actual_json"], test_data["expected_json_part"]), \
                "actual JSON param value(s) doesn't match expected"
        else:
            assert check_subdictionary_using_param_types(test_data["actual_json"], test_data["expected_json_part"]), \
                "actual JSON param type(s) doesn't match expected"
    else:
        assert test_data["actual_error_message"] == test_data["expected_error_message"], \
            "actual error message doesn't match expected"
    print("PASSED ;")


def check_subdictionary_using_param_values(int_dict_whole, int_dict_part):
    int_dpk_list = int_dict_part.keys()
    for key in int_dpk_list:
        if key not in int_dict_whole:
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
    for key in int_dpk_list:
        if key not in int_dict_whole:
            return False
        else:
            if type(int_dict_part[key]) == dict and type(int_dict_whole[key]) == dict:
                subdict_p = int_dict_part[key]
                subdict_w = int_dict_whole[key]
                if check_subdictionary_using_param_types(subdict_w, subdict_p) is False:
                    return False
            else:
                print()
                if not isinstance(int_dict_part[key], type(int_dict_whole[key])):
                    return False
    return True


"""
def main_test_function(test_data_list = test_data_list_ex):
    for test_data in test_data_list:
        print()
        print(test_data["case_name"])
        assert test_data["actual_status_code"] == test_data["expected_status_code"], \
            "actual status code doesn't match expected"
        if test_data["expected_error_message"] == "":
            if test_data["validation_type"] == "value":
                assert check_subdictionary_using_param_values(test_data["actual_json"], test_data["expected_json_part"]), \
                    "actual JSON param value(s) doesn't match expected"
            else:
                assert check_subdictionary_using_param_types(test_data["actual_json"], test_data["expected_json_part"]), \
                    "actual JSON param type(s) doesn't match expected"
        else:
            assert test_data["actual_error_message"] == test_data["expected_error_message"], \
                "actual error message doesn't match expected"
        print("Passed")
"""
