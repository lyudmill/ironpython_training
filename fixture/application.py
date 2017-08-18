import clr
import sys
import os.path

project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(project_dir, "..", "Castle.Core.3.3.0\\lib\\net40-client\\"))
sys.path.append(os.path.join(project_dir, "..", "TestStack.White.0.13.3\\lib\\net40\\"))

clr.AddReferenceByName('TestStack.White')

from TestStack.White import Application
from TestStack.White.InputDevices import Keyboard
from TestStack.White.WindowsAPI import KeyboardInput
from TestStack.White.UIItems.Finders import *

clr.AddReferenceByName('UIAutomationTypes, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35')
from System.Windows.Automation import *

from fixture.group import GroupHelper

class WinApplication:
    def __init__(self, app_path):
        print("WinApp init")
        self.path = app_path
        self.app = Application.Launch(app_path)
        self.main_window = self.app.GetWindow("Free Address Book")
        self.group = GroupHelper(self)

    def destroy(self):
        if self.main_window is not None:
            self.main_window.Get(SearchCriteria.ByAutomationId("uxExitAddressButton")).Click()
