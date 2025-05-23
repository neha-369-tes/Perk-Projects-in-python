# Perk-Projects-in-python
A curated set of Python projects exploring fundamental programming logic and structure. This repository will expand with future additions.

# 🐍 Python Mini Projects Collection

This repository contains a collection of beginner-to-intermediate Python projects demonstrating real-world applications using various libraries and concepts. Each project is self-contained and well-documented for easy understanding and reuse.

---

## 📋 Project List

### 1. BMI Calculator

A console-based program that calculates Body Mass Index (BMI) from user-input height and weight and classifies it based on WHO standards.

**Features:**
- Input validation for height and weight
- Accurate BMI calculation
- Category classification (Underweight, Normal, Overweight, Obese)

**Run:**
  ```bash
  python bmi_calculator.py
```
### 2. Random Password Generator
Generates secure passwords based on user preferences: length, inclusion of uppercase/lowercase letters, digits, and symbols.

**Features:**

-Option to choose character types

-Ensures at least one character from each selected type

-Randomized and secure output

**Run:**

```bash

python password_generator.py
```
**Requirements:**

  Standard Python libraries: random, string
  
## 3. Weather App (Tkinter GUI + Open-Meteo API)
A desktop weather app that fetches current weather using city names via the Open-Meteo API.

**Features:**

  -Tkinter-based GUI

  -Geolocation using geopy

  -Real-time weather data via Open-Meteo

  -Error handling for invalid city names and API issues

**Run:**
```bash
   python weather_app.py
```
**Requirements:**
```bash
  pip install requests geopy
```

## 🛠️ Tools & Libraries Used
  Python 3.7+

  tkinter

  requests

  geopy

  Standard libraries: random, string, math

## 4. Client-Server Chat Application
A simple multi-client chat server and client built using Python's socket and threading libraries.

**Features:**

  -Server handles multiple clients simultaneously

  -Broadcasts messages to all connected clients except the sender

  -Clients can send and receive messages asynchronously

  -Clean connection handling and exit option

**Run Server:**

  ```bash

  python server.py
```
**Run Client:**

  ```bash

  python client.py
```
**Details:**

  -Server listens on all interfaces on port 12345

  -Client connects to 127.0.0.1 on port 12345

  -Type exit in client to disconnect

**Requirements**

  Standard Python libraries: socket, threading

## 5. Voice Assistant

A simple voice assistant that recognizes spoken commands and responds with speech using `speech_recognition` and `pyttsx3`. It can tell time, date, search Google, and respond to greetings.

### Features

- Speech-to-text recognition with error handling  
- Text-to-speech responses  
- Basic commands: greetings, time, date, Google search, and exit  
- Opens web browser for search queries  

### Run

```bash
python voice_assistant.py
```
Requirements
```bash

  pip install SpeechRecognition pyttsx3
```
**Additional dependencies**
  Microphone (hardware)
  Internet connection (for speech recognition API)



