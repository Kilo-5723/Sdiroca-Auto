import win32gui

location = (0, 0)
size = (0, 0)
detected = False


def callback(hwnd, extra):
    global location, size, detected
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    if (win32gui.GetWindowText(hwnd) == extra):
        print("Window %s:" % win32gui.GetWindowText(hwnd))
        print("\tLocation: (%d, %d)" % (x, y))
        print("\t    Size: (%d, %d)" % (w, h))
        location = (x, y)
        size = (w, h)
        detected = True


def lock_window(name):
    win32gui.EnumWindows(callback, name)
    return detected


def to_window_position(position):
    return ((position[0]-location[0])/size[0], (position[1]-location[1])/size[1])


def to_global_position(position):
    return (int(location[0]+position[0]*size[0]), int(location[1]+position[1]*size[1]))
