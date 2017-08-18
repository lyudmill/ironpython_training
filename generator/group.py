from model.group import Group
import random
import string
import os.path
import getopt
import sys
import time
#virt machine .Net
import clr
clr.AddReferenceByName('Microsoft.Office.Interop.Excel, Version=15.0.0.0, Culture=neutral, PublicKeyToken=71E9BCE111E9429C')
from Microsoft.Office.Interop import Excel


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:p:", ["number of groups", "file"])
    print(opts)
    print(args)
except getopt.GetoptError as err:
#    getopt.usage()
    print(err)
    sys.exit(2)

n = 5
f = "data/groups.xlsx"
p = ""

for o,a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a
    elif o == "-p":
        p = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group(name="")] + [
    Group(name=random_string("%sname"%p, 10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

excel = Excel.ApplicationClass()
excel.Visible = True
workbook = excel.Workbooks.Add()
sheet = workbook.ActiveSheet

for i in range(len(testdata)):
    sheet.Range["A%s" % (i+1)].value2 = testdata[i].name

workbook.SaveAs(file)
time.sleep(10)
excel.Quit