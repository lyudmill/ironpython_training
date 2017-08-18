import pytest
import json
import os.path
from fixture.application import WinApplication


fixture = None
target = None

@pytest.fixture()
def app(request):
    global fixture
    app_conf = load_config(request.config.getoption("--target"))['application']
    print("fixture app")
    if fixture is None:
        fixture = WinApplication(app_path=os.path.join(app_conf["path"],app_conf["name"]))
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
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


def pytest_addoption(parser):
    parser.addoption("--target", action="store", default="target.json")
