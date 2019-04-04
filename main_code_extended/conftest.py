from time import sleep

import pytest


@pytest.fixture()
def extended_param_using(request, test_data):
    time_to_next_test = test_data["time_to_next_test"]

    def extended_param_using_teardown():
        sleep(time_to_next_test)

    request.addfinalizer(extended_param_using_teardown)