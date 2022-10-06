import screen.locate as scr
import battle.read as bt
from pynput.mouse import Button, Controller
from PIL import Image
import win32gui
import win32api
import win32con
import time
# import pyautogui

# scr.view_all()

scr.lock_window("BlueStacks Keymap Overlay")

mouse = Controller()


def show(board):
    img = Image.new('RGB', (70, 20))
    for i in range(2):
        for j in range(7):
            for di in range(10):
                for dj in range(10):
                    img.putpixel((j*10+dj, i*10+di), board[i][j])
    img.show()


def check(board, x, y, pattern):
    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            if pattern[i][j] != -1 and pattern[i][j] != board[x+i][y+j]:
                return False
    return True


def exist(board, pattern):
    x = len(pattern)
    y = len(pattern[0])
    for i in range(3-x):
        for j in range(8-y):
            if check(board, i, j, pattern):
                return True
    return False


def click(pos):
    pos = scr.to_global_position(pos)
    # pyautogui.click(pos[0], pos[1])
    x = pos[0]
    y = pos[1]
    origin = win32api.GetCursorPos()

    # lParam = win32api.MAKELONG(pos[0], pos[1])

    # win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN,
    #                      win32con.MK_LBUTTON, lParam)
    # win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    win32api.SetCursorPos(origin)


def output(board):
    for i in range(2):
        for j in range(7):
            if board[i][j] == 0:
                print("\033[0;37;47m   ", end='')
            elif board[i][j] == 1:
                print("\033[0;37;44m   ", end='')
            elif board[i][j] == 2:
                print("\033[0;37;43m   ", end='')
        print("\033[0;37;40m")
    print()


while True:
    # print(scr.to_window_position(mouse.position), end='\r')
    # show(bt.read_board())
    board = bt.read_board()
    output(board)
    if not exist(board, [[2, 2, 2], [2, 2, 2]]):
        click((0.835, 0.808))
    time.sleep(0.5)
    # print(bt.read_board())
