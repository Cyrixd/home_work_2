import pytest
import os


@pytest.fixture()
def clean_temp_file(request):
    def teardown():
        if os.path.isfile("./output_test.json"):
            os.remove("./output_test.json")
        print("success")

    request.addfinalizer(teardown)
    return "clean_temp_file"
