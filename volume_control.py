import comtypes
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def with_com(func):
    def wrapper(*args, **kwargs):
        comtypes.CoInitialize()
        try:
            return func(*args, **kwargs)
        finally:
            comtypes.CoUninitialize()
    return wrapper

@with_com
def get_volume_interface():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    return cast(interface, POINTER(IAudioEndpointVolume))

@with_com
def volume_up():
    volume = get_volume_interface()
    current = volume.GetMasterVolumeLevelScalar()
    volume.SetMasterVolumeLevelScalar(min(current + 0.05, 1.0), None)

@with_com
def volume_down():
    volume = get_volume_interface()
    current = volume.GetMasterVolumeLevelScalar()
    volume.SetMasterVolumeLevelScalar(max(current - 0.05, 0.0), None)

@with_com
def set_system_volume(level):  # level: 0.0 - 1.0
    level = float(level)
    level = min(max(level, 0.0), 1.0)
    volume = get_volume_interface()

    if level == 0.0:
        volume.SetMute(1, None)  # Sessize al
    else:
        volume.SetMute(0, None)  # Sessizden çıkar
        volume.SetMasterVolumeLevelScalar(level, None)


@with_com
def get_system_volume():
    volume = get_volume_interface()
    return int(volume.GetMasterVolumeLevelScalar() * 100)
