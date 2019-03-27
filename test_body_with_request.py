import json

from pip._vendor import requests


def main_test_function(test_data):
    print()
    print(test_data["case_name"] + ":")

    url = test_data["url"]
    payload = test_data["request_json"]
    headers = test_data["headers"]

    response = ""
    if test_data["request_type"] == "post":
        response = requests.post(url, data=payload, headers=headers)

    response_body = json.loads(response.text)
    actual_status_code = response.status_code

    assert actual_status_code == test_data["expected_status_code"], \
        "actual status code doesn't match expected"
    if test_data["expected_error_message"] == "":
        if test_data["validation_type"] == "value":
            assert check_dictionary_using_param_values(response_body, test_data["expected_json_part"]), \
                "actual JSON param value(s) doesn't match expected"
        else:
            assert check_dictionary_using_param_types(response_body, test_data["expected_json_part"]), \
                "actual JSON param type(s) doesn't match expected"
    else:
        assert test_data["actual_error_message"] == test_data["expected_error_message"], \
            "actual error message doesn't match expected"
    print("PASSED ;")


def check_dictionary_using_param_values(dict_whole, dict_part):
    int_dpk_list = dict_part.keys()
    for key in int_dpk_list:
        if key not in dict_whole:
            return False
        else:
            if type(dict_part[key]) == dict and type(dict_whole[key]) == dict:
                subdict_p = dict_part[key]
                subdict_w = dict_whole[key]
                if check_dictionary_using_param_values(subdict_w, subdict_p) is False:
                    return False
            elif type(dict_part[key]) == list and type(dict_whole[key]) == list:
                int_list_part = dict_part[key]
                int_list_whole = dict_whole[key]
                if check_list_using_param_values(int_list_whole, int_list_part) is False:
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
            else:
                if not isinstance(dict_part[key], type(dict_whole[key])):
                    return False
    return True


def check_list_using_param_values(list_whole, list_part):
    sub_list_w = []
    sub_list_p = []
    for param in list_part:
        if type(param) == dict:
            sub_list_p.append(param)
    for param in list_whole:
        if type(param) == dict:
            sub_list_w.append(param)
    if len(sub_list_p) > len(sub_list_w):
        return False
    i = 0
    l = 0
    while i < len(sub_list_p):
        mark = False
        j = l+1
        while j < len(sub_list_w):
            if check_dictionary_using_param_values(sub_list_w[j], sub_list_p[i]):
                mark = True
                l = j
                break
            j += 1
        if mark is False:
            return False



