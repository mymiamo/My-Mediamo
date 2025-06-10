# My Mediamo

My Mediamo is a lightweight, browser-based remote media control app for your computer. It allows you to control media playback (play, pause, volume, next, previous) from any device connected to the same Wi-Fi network — no client-side installation required.

---

## ⚙️ Features

- Play / Pause your media remotely
- Control volume up/down
- Skip to next or previous track
- Works on any device with a browser (mobile, tablet, desktop)
- Local network only — privacy-friendly

---

## 🛠️ Installation

### Requirements
- Python 3.9 or above
- `pip` package manager

### Setup Steps

1. Download or clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/My-Mediamo.git
   cd My-Mediamo
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the server:
   ```bash
   py app.py
   ```

---

## 📱 Usage

1. Launch the app:
   ```bash
   py app.py
   ```

2. On your host machine, open `CMD` and type:
   ```bash
   ipconfig
   ```

3. Copy your **IPv4 Address** (e.g., `192.168.1.100`).

4. On another device (same Wi-Fi), open a browser and navigate to:
   ```
   http://192.168.1.100:5000
   ```

5. You're ready to control your media remotely!

---

## 🐞 Known Issues

- **SteelSeries Sonar:** Only controls "Gaming" audio; Media and other outputs are unaffected.

> **Found a bug?** Please [open an issue](https://github.com/YOUR_USERNAME/My-Mediamo/issues) and help improve the project.

---

## 🚧 Upcoming Updates

- Cover art display
- Enhanced player control bar (minutes, seconds)
- EXE version for Windows
- Mobile UI improvements
- QR-based device connection

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details.

---

Thank you for using My Mediamo! Contributions are welcome 🚀
