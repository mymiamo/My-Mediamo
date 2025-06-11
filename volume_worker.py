import sys
from ctypes import cast, POINTER
import comtypes
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def set_volume(level):
    comtypes.CoInitialize()
    try:
        device = AudioUtilities.GetSpeakers()
        interface = device.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        level = float(level)
        level = min(max(level, 0.0), 1.0)

        if level == 0.0:
            volume.SetMute(1, None)
        else:
            volume.SetMute(0, None)
            volume.SetMasterVolumeLevelScalar(level, None)
    finally:
        comtypes.CoUninitialize()

def get_volume():
    comtypes.CoInitialize()
    try:
        device = AudioUtilities.GetSpeakers()
        interface = device.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current = volume.GetMasterVolumeLevelScalar()
        print(int(current * 100))  # stdout ile geri döner
    finally:
        comtypes.CoUninitialize()

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "set":
        set_volume(sys.argv[2])
    elif cmd == "get":
        get_volume()
