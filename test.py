import comtypes
comtypes.CoInitialize()

from pycaw.pycaw import AudioUtilities

sessions = AudioUtilities.GetAllSessions()

for session in sessions:
    if session.Process:
        print(f"App: {session.Process.name()}")
        print(f"  Volume: {session.SimpleAudioVolume.GetMasterVolume():.2f}")
        print(f"  Mute: {session.SimpleAudioVolume.GetMute()}")
