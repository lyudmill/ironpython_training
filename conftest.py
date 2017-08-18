import pytest
import json
import os.path
from fixture.application import WinApplication


fixture = None
target = None

@pytest.fixture()
def app(request):
    global fixture
    config = load_config(request.config.getoption("--target"))
    if fixture is None:
        fixture = WinApplication(app_path=os.path.join(config['application']["path"],config['application']["name"]))
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        if fixture is not None:
            fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def load_config(file):
    global target
    print("load config")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        print("load config2")
        print(config_file)
        with open(config_file) as f:
            target = json.load(f)
            print("load config3")
            print(target)
    return target


def pytest_addoption(parser):
    parser.addoption("--target", action="store", default="target.json")
