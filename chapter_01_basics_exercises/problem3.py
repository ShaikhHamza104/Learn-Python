"""
📚 Topic: External Libraries & Audio Synthesis (pyttsx3)

This exercise demonstrates initializing an external text-to-speech engine
using the `pyttsx3` library, queueing spoken utterances, and processing audio.

💡 Key points:
    1️⃣ Initializing the TTS engine using `pyttsx3.init()`
    2️⃣ Queuing speech commands with `engine.say()`
    3️⃣ Flushing and executing the speech queue with `engine.runAndWait()`

🧠 Beginner tip:
    `pyttsx3` operates offline and works across Windows, macOS, and Linux
    without requiring an internet connection or external API keys.
"""


import pyttsx3

engine = pyttsx3.init()
engine.say("Hi i am good")
engine.runAndWait()
