
def test_add_group(app):
    old_list = app.group.get_group_list()
    app.group.open_group_window()
    app.group.add_new_group("new_group1")
    app.group.close_group_window()
    new_list = app.group.get_group_list()
    old_list.append("new_group1")
    assert sorted(old_list) == sorted(new_list)
    print("OK")
