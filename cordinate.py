# BEGIN (write your solution here
def is_degenerated(cordinate):
    if cordinate[0][1] == cordinate[1][1] and cordinate[0][0] == cordinate[1][0]:
        return True
    return False


def is_vertical(cordinate):
    if cordinate[0][0] == cordinate[1][0] and cordinate[0][1] != cordinate[1][1]:
        return True
    return False


def is_horizontal(cordinate):
    if cordinate[0][1] == cordinate[1][1] and cordinate[0][0] != cordinate[1][0]:
        return True
    return False


def is_inclined(cordinate):
    if cordinate[0][1] != cordinate[1][1] and cordinate[1][0] != cordinate[0][0]:
        return True
    return False
# END
