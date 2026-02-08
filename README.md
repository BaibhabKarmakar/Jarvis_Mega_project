# JARVIS - Voice Assistant
<p align="center">
  <img src="https://github.com/BaibhabKarmakar/Jarvis/raw/main/image.jpg" alt="JARVIS Banner" width="800"/>
</p>
A simple, offline-capable voice assistant inspired by Iron Man's JARVIS, built in Python.

Currently supports:
- Wake word detection ("Jarvis")
- Basic voice commands (open websites, play songs, get news headlines)
- Offline AI responses using **Llama 3.2 1B** via Ollama
- Text-to-speech using **gTTS** (Google TTS) + pygame playback
- Fallback TTS with **pyttsx3**

## Features

- Wake word: "Jarvis"
- Commands supported out-of-the-box:
  - "open google" / "open youtube" / "open facebook" / "open linkedin"
  - "play <song>" (from your personal `musicLibrary`)
  - "news" → reads top 5 Indian news headlines
  - Any other question/command → handled by local Llama 3.2 1B model
- Fully offline AI responses (after model is downloaded)
- Internet required only for: initial news fetch, gTTS audio generation, first-time model download

## Requirements

- Python 3.9 – 3.12
- Microphone (built-in or external)
- Internet connection (for first run + news + gTTS)
- Ollama installed and running with `llama3.2:1b` pulled

### Python Dependencies

```bash
pip install speechrecognition pyttsx3 gtts pygame requests ollama
```
## Setup Instructions
1. Install Ollama
  https://ollama.com/download
  Then run in terminal:
  ``` bash
  ollama pull llama3.2:1b
  ```
  (You can also try llama3.2:3b if your computer has more RAM)

2. Create music library (optional but recommended)
   Create a file called musicLibrary.py in the same folder:
   ``` bash
   music = {
    "bad guy": "https://www.youtube.com/watch?v=DyDfgMOUjCI",
    "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
    "levitating": "https://www.youtube.com/watch?v=TUVcZfQe-Kw",
    # add your favorite songs here (YouTube links)
    }
   ```
3. Replace NewsAPI key (optional)
   Get a free key from: https://newsapi.org
   Paste it into the variable newsapi = "your-key-here"

4. Run the Assistant :
   ``` bash
   python main.py
   ```
   Say "Jarvis" clearly → wait for "Ya" → give your command

## Project Structure : 
``` bash
Mega_Project JARVIS/
├── main.py               ← main voice assistant script
├── musicLibrary.py       ← your personal song links (create this file)
└── temp.mp3              ← temporary file created & deleted during speaking (gTTS)
```

## Current Limitations & Known Issues
1. Uses Google Speech Recognition by default → requires internet for voice → wake word & commands
2. gTTS also needs internet (generates MP3 from text)
3. Very small model (llama3.2:1b) → answers are short & sometimes not very smart
4. No offline speech recognition yet (you can replace with faster-whisper later)
5. pygame warning about pkg_resources → harmless, will be fixed in future pygame versions

## Planned Improvements (you can contribute!)
1. Add offline speech recognition (faster-whisper / Vosk)
2. Better song playing (pygame local mp3 instead of YouTube)
3. Add more commands (weather, time, jokes, calculations...)
4. Custom wake word sensitivity
5. Voice activity detection (VAD) to reduce false triggers
6. Better error handling & graceful exit

License
MIT License – feel free to use, modify, share!
Made with ❤️ in West Bengal, India
Started in 2025–2026 as a fun learning project
Happy hacking!
Say "Jarvis" and enjoy 🚀
