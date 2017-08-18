import clr
clr.AddReferenceByName('TestStack.White')

from TestStack.White import Application
from TestStack.White.InputDevices import Keyboard
from TestStack.White.WindowsAPI import KeyboardInput
from TestStack.White.UIItems.Finders import *

clr.AddReferenceByName('UIAutomationTypes, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35')
from System.Windows.Automation import *



class GroupHelper:
    def __init__(self, app):
        self.app = app
        self.modal = None

    def add_new_group(self, name):
        self.modal.Get(SearchCriteria.ByAutomationId("uxNewAddressButton")).Click()
        self.modal.Get(SearchCriteria.ByControlType(ControlType.Edit)).Enter(name)
        Keyboard.Instance.PressSpecialKey(KeyboardInput.SpecialKeys.RETURN)


    def close_group_window(self):
        self.modal.Get(SearchCriteria.ByAutomationId("uxCloseAddressButton")).Click()
        self.modal = None


    def open_group_window(self):
        if self.modal is None:
            main_window = self.app.main_window
            main_window.Get(SearchCriteria.ByAutomationId("groupButton")).Click()
            self.modal = self.app.main_window.ModalWindow("Group editor")

    def get_group_list(self):
        self.open_group_window()
        tree = self.modal.Get(SearchCriteria.ByAutomationId("uxAddressTreeView"))
        root = tree.Nodes[0]
        l = [node.Text for node in root.Nodes]
        self.close_group_window()
        return l