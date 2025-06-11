import subprocess

def set_system_volume(level):  # 0.0 - 1.0
    subprocess.run(["python", "volume_worker.py", "set", str(level)], timeout=2)

def get_system_volume():
    result = subprocess.run(["python", "volume_worker.py", "get"], capture_output=True, text=True, timeout=2)
    return int(result.stdout.strip())

def volume_up():
    current = get_system_volume()
    new = min(current + 5, 100)
    set_system_volume(new / 100.0)

def volume_down():
    current = get_system_volume()
    new = max(current - 5, 0)
    set_system_volume(new / 100.0)
