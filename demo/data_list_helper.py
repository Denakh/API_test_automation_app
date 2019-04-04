from time import sleep

import pytest


def get_test_data_list_reformat(test_data_list_int):
    new_test_data_list = []
    for test_data in test_data_list_int:
        for i in range(0, test_data["execution_number"]):
            new_test_data_list.append(test_data)
    return new_test_data_list
