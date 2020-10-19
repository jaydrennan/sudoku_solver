def show(all_values):
    grid_representation = "\n~~~~~~~~~~~~~~~~~~~~~\n"
    for i, val in enumerate(all_values):
        grid_representation += str(val)
        if i % 3 == 2:
            grid_representation += "|"
        if i % 9 == 8:
            grid_representation += "\n"
        if i % 27 == 26:
            grid_representation += "---------------------------\n"
        if i == 80:
            grid_representation += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    return grid_representation
