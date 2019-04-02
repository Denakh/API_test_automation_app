import json

from pip._vendor import requests


def main_test_function(test_data):
    print()
    print(test_data["case_name"] + ":")

    url = test_data["url"]
    payload = test_data["request_json"]
    headers = test_data["headers"]
    decimal_accuracy = test_data["decimal_accuracy"]

    response = ""
    if test_data["request_type"] == "post":
        response = requests.post(url, data=payload, headers=headers)

    response_body = json.loads(response.text)
    actual_status_code = response.status_code

    assert actual_status_code == test_data["expected_status_code"], \
        "actual status code doesn't match expected"
    if test_data["expected_error_message"] == "":
        if test_data["validation_type"] == "value":
            assert check_dictionary_using_param_values(response_body, test_data["expected_json_part"], decimal_accuracy), \
                "actual JSON param value(s) doesn't match expected"
        else:
            assert check_dictionary_using_param_types(response_body, test_data["expected_json_part"]), \
                "actual JSON param type(s) doesn't match expected"
    else:
        assert test_data["actual_error_message"] == test_data["expected_error_message"], \
            "actual error message doesn't match expected"
    print("PASSED ;")


def check_dictionary_using_param_values(dict_whole, dict_part, decimal_accuracy):
    int_dpk_list = dict_part.keys()
    for key in int_dpk_list:
        if key not in dict_whole:
            return False
        else:
            if type(dict_part[key]) == dict and type(dict_whole[key]) == dict:
                subdict_p = dict_part[key]
                subdict_w = dict_whole[key]
                if check_dictionary_using_param_values(subdict_w, subdict_p, decimal_accuracy) is False:
                    return False
            elif type(dict_part[key]) == list and type(dict_whole[key]) == list:
                int_list_part = dict_part[key]
                int_list_whole = dict_whole[key]
                if check_list_using_param_values(int_list_whole, int_list_part, decimal_accuracy) is False:
                    return False
            else:
                if type(dict_whole[key]) == float:
                    if round(dict_whole[key], decimal_accuracy) != dict_part[key]:
                        return False
                else:
                    if dict_part[key] != dict_whole[key]:
                        return False
    return True


def check_dictionary_using_param_types(dict_whole, dict_part):
    int_dpk_list = dict_part.keys()
    for key in int_dpk_list:
        if key not in dict_whole:
            return False
        else:
            if type(dict_part[key]) == dict and type(dict_whole[key]) == dict:
                subdict_p = dict_part[key]
                subdict_w = dict_whole[key]
                if check_dictionary_using_param_types(subdict_w, subdict_p) is False:
                    return False
            elif type(dict_part[key]) == list and type(dict_whole[key]) == list:
                int_list_part = dict_part[key]
                int_list_whole = dict_whole[key]
                if check_list_using_param_types(int_list_whole, int_list_part) is False:
                    return False
            else:
                if not isinstance(dict_part[key], type(dict_whole[key])):
                    return False
    return True


def check_list_using_param_values(list_whole, list_part, decimal_accuracy):
    for i in range(0, len(list_part)):
        if list_part[i] != {}:
            if type(list_part[i]) == dict and type(list_whole[i]) == dict:
                subdict_p = list_part[i]
                subdict_w = list_whole[i]
                if check_dictionary_using_param_values(subdict_w, subdict_p, decimal_accuracy) is False:
                    return False
            elif type(list_part[i]) == list and type(list_whole[i]) == list:
                int_list_part = list_part[i]
                int_list_whole = list_whole[i]
                if check_list_using_param_values(int_list_whole, int_list_part, decimal_accuracy) is False:
                    return False
            else:
                if type(list_whole[i]) == float:
                    if round(list_whole[i], decimal_accuracy) != list_part[i]:
                        return False
                else:
                    if list_part[i] != list_whole[i]:
                        return False
    return True


def check_list_using_param_types(list_whole, list_part):
    for i in range(0, len(list_part)):
        if list_part[i] != {}:
            if type(list_part[i]) == dict and type(list_whole[i]) == dict:
                subdict_p = list_part[i]
                subdict_w = list_whole[i]
                if check_dictionary_using_param_types(subdict_w, subdict_p) is False:
                    return False
            elif type(list_part[i]) == list and type(list_whole[i]) == list:
                int_list_part = list_part[i]
                int_list_whole = list_whole[i]
                if check_list_using_param_types(int_list_whole, int_list_part) is False:
                    return False
            else:
                if not isinstance(list_part[i], type(list_whole[i])):
                    return False
    return True
