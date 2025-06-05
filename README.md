# 🤖 Shinrai - Your Personal AI Voice Assistant

Shinrai (信頼) means **"trust"** in Japanese — and that's exactly what this assistant is designed for.  
Built with Python and powered by OpenRouter AI (LLaMA 4 Maverick), Shinrai is your terminal-based voice assistant that can:

- 🧠 Chat using LLaMA-4-Maverick (via OpenRouter)
- 🎤 Speak responses with gTTS + mpv
- 🌐 Open websites like YouTube, Google, Reddit, etc.
- 📁 Maintain and show chat history
- 🧹 Clear screen and history
- 🔍 Search Google via commands

---

## 📦 Features

- **Voice Interaction** using `gTTS` and `mpv`
- **Chat with LLaMA 4** via OpenRouter API
- **Command Support** (open sites, search, clear, help)
- **History Logging** and Review

---

## 🚀 Installation
1. Clone the Repository
```bash
git clone https://github.com/DevManoj96/Shinrai_AI-Assistant_v1.git
cd Shinrai_AI-Assistant_v1
```

2. Install THe Requirements
```bash
pip install -r requirements.txt
```

3. Run The Program
```bash
python3 main.py
```
---

## 🛠 Requirements
- Python 3.7+
- openai (OpenRouter client)
- gTTS
- mpv (for audio playback)
  Debian / Ubuntu / Linux Mint:
  ```bash
  sudo apt update
  sudo apt install mpv -y
  ```
  
  Arch / Manjaro:
  ```bash
  sudo pacman -S mpv
  ```

  Fedora / RHEL / CentOS (with EPEL):
  ```bash
  sudo dnf install mpv
  ```


---

## 🔐 API Key
Get Your API KEY from http://openrouter.ai/ and Update API KEY in the Assistant

```bash
API_KEY = "ENTER YOUR API KEY HERE"
```
---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Contact
- Created by Manoj Meghwal.
- Feel free to open issues or submit pull requests.
