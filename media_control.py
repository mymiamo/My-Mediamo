import win32api
import win32con

def play_pause():
    win32api.keybd_event(win32con.VK_MEDIA_PLAY_PAUSE, 0, 0, 0)

def next_track():
    win32api.keybd_event(win32con.VK_MEDIA_NEXT_TRACK, 0, 0, 0)

def prev_track():
    win32api.keybd_event(win32con.VK_MEDIA_PREV_TRACK, 0, 0, 0)

def stop():
    win32api.keybd_event(win32con.VK_MEDIA_STOP, 0, 0, 0)
