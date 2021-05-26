def add_viewer(name, fan_list=None):
    if fan_list is None:
        fan_list = [name]
    else:
        fan_list.append(name)
    return fan_list
