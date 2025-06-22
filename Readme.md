# EchoDex – Intelligent Voice-Powered Desktop Assistant
> Transform your desktop experience with natural voice commands and AI-powered automation

EchoDex is a sophisticated, modular desktop assistant that brings the power of voice interaction to your computer. Using deep learning and seamless API integrations, it understands natural speech patterns, executes complex system operations, retrieves real-time information, and responds with dynamic voice output.

---

## Features

- **Natural Voice Interaction** 
- **Intent Recognition** 
- **Real-Time Information Access**
- **Email Automation**
- **System Control**
- **Note-Taking**
- **AI Image Generation**
- **Enhanced Web Navigation**
- **Persistent Memory**
- **Email Automation**

---

## Tech Stack

- **Python** – Core application logic and orchestration
- **TensorFlow/Keras** – Intent recognition modeling 
- **SpeechRecognition + win32com** – Voice input/output pipeline
- **Regex & Requests** – Text processing and API communication
- **AppOpener & pynput** – System and application automation
- **SQLite** – Query data persistance
- **Git** – Version control 

---

## Project Structure

```
EchoDex/
│
├── Data/
│   ├── .env                    # API keys and credentials storage
│   ├── chat_model              # Pre-trained intent recognition model
│   ├── tokenizer.pickle        # Trained tokenizer for text processing
│   ├── label_encoder.pickle    # Intent classification label encoder
│   ├── intents.json            # Intent-recognition training dataset
│   └── chats.db                # SQLite database for conversation history
│
├── Plugins/
│   ├── main.py                     # Application entry point and core logic
│   ├── API_functionalities.py      # Weather, news, calculations, and data APIs
│   ├── browsing_functionalities.py # Web navigation and search capabilities
│   ├── gmail.py                    # Email automation 
│   ├── image_generation.py         # AI-powered image generation module
│   ├── model_training.py           # Intent recognition model training pipeline
│   ├── system_operations.py        # System-level automation and control
│   ├── database.py                 # Chat history 
│   └── websites.py                 # Website mapping 
│
├── requirements.txt            # Python dependency specifications
└── setup.py                    # Automated dependency installation and DB configuration
```

---

## Getting Started
---

1. **Clone the repository**
```
$ git clone https://github.com/nogi2k2/EchoDex.git
$ cd EchoDex
```

2. **Set Up Virtual Environment (Windows-bash)**
```
$ python -m venv echodex-env
$ echodex-env\Scripts\activate  
```

3. **Install Dependencies and Setup DB**
```
$ python setup.py
```

4. **Launch EchoDex**
```
$ cd Plugins
$ python main.py
```

---
