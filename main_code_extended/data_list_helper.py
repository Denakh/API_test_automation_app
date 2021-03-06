from time import sleep

import pytest


def get_test_data_list_reformat(test_data_list_int):
    new_test_data_list = []
    for test_data in test_data_list_int:
        for i in range(0, test_data["execution_number"]):
            new_test_data_list.append(test_data)
    return new_test_data_list


@pytest.fixture(scope='function')
def extended_param_using(request, test_data):
    time_to_next_test = test_data["time_to_next_test"]

    def extended_param_using_teardown():
        sleep(time_to_next_test)

    request.addfinalizer(extended_param_using_teardown)
