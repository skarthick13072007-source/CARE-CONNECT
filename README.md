# 🏥 Patient Assistance & Safety System
### AI-Powered Hand Gesture Recognition with Telegram Alerts

<p align="center">
  <strong>A low-cost, contactless patient communication and emergency alert system</strong><br>
  Designed for speech-impaired, mobility-impaired, paralyzed, and elderly patients
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv" alt="OpenCV">
  <img src="https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange" alt="MediaPipe">
  <img src="https://img.shields.io/badge/Telegram-Alerts-26A5E4?logo=telegram" alt="Telegram">
  <img src="https://img.shields.io/badge/Project-ECE-purple" alt="ECE Project">
</p>

---

## 📌 Project Overview

The **Patient Assistance & Safety System** is an ECE-focused assistive technology prototype that enables patients to communicate essential needs using simple **hand gestures**.

A webcam captures the patient's hand, **MediaPipe** detects hand landmarks, and the program counts the raised fingers. Each recognized gesture is mapped to a predefined request such as **HELP, WATER, FOOD, RESTROOM, or EMERGENCY**.

The selected request is then transmitted to the caregiver through a **Telegram bot**.

### 🔄 System Flow

```text
Patient
   │
   ▼
Hand Gesture
   │
   ▼
Webcam
   │
   ▼
OpenCV
   │
   ▼
MediaPipe Hand Landmark Detection
   │
   ▼
Finger Counting
   │
   ▼
Gesture → Patient Request
   │
   ▼
Telegram Bot API
   │
   ▼
Caregiver's Telegram
```

---

## 🎯 Problem Statement

Patients who are unable to speak or move freely may have difficulty communicating basic needs to caregivers.

Traditional communication methods can be:

- Difficult for speech-impaired patients
- Physically demanding for mobility-impaired patients
- Slow during urgent situations
- Dependent on continuous caregiver attention

This project provides a simple **contactless visual communication method** using predefined hand gestures.

---

## 💡 Proposed Solution

The system uses computer vision to recognize a patient's hand gesture and automatically send the corresponding request to a caregiver.

### Key capabilities

- ✋ Real-time hand gesture recognition
- 👁️ Computer-vision-based finger detection
- 🆘 Emergency alert generation
- 💧 Basic patient-need communication
- 📱 Telegram-based remote notification
- ⏱️ Message cooldown to prevent excessive repeated alerts
- 💻 Low-cost implementation using a normal webcam and computer

---

## ✋ Gesture Mapping

| Raised Fingers | Gesture Meaning | Telegram Alert |
|:---:|---|---|
| ☝️ **1** | Help | 🆘 HELP |
| ✌️ **2** | Water | 💧 WATER |
| 🤟 **3** | Food | 🍛 FOOD |
| 🖐️ **4** | Restroom | 🚻 RESTROOM |
| 🖐️ **5** | Emergency | 🚨 EMERGENCY |

> **Note:** The exact visual appearance of a gesture may vary depending on hand orientation and camera position. The current implementation uses finger counting and is intentionally simple for an educational prototype.

---

## 🧠 Technical Approach

### 1. Image Acquisition

The webcam continuously captures video frames using OpenCV.

### 2. Image Preprocessing

Each frame is:

- Flipped horizontally for a natural mirror view
- Converted from BGR to RGB
- Passed to the MediaPipe hand-processing pipeline

### 3. Hand Landmark Detection

MediaPipe detects hand landmarks and provides coordinates for key points on the hand.

The project uses the landmark positions to determine whether individual fingers are raised.

### 4. Finger Counting

The program checks:

- Thumb position using horizontal coordinates
- Other four fingers using vertical landmark positions

The number of detected raised fingers is then calculated.

### 5. Request Classification

The finger count is mapped to a predefined patient request.

```text
1 → HELP
2 → WATER
3 → FOOD
4 → RESTROOM
5 → EMERGENCY
```

### 6. Telegram Notification

When a valid request is detected, the program sends the corresponding message through the Telegram Bot API.

### 7. Cooldown Mechanism

A **5-second cooldown** prevents the same gesture from generating an excessive number of Telegram messages.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Main programming language |
| **OpenCV** | Webcam capture and display |
| **MediaPipe** | Hand landmark detection |
| **Requests** | Communication with Telegram Bot API |
| **Telegram Bot API** | Remote patient alerts |
| **Computer Vision** | Gesture recognition |

---

## 📂 Project Structure

```text
patient-monitoring-system/
│
├── patient_monitor.py      # Main application
├── requirements.txt        # Python dependencies
├── .env.example            # Telegram configuration template
├── .gitignore              # Prevents sensitive/local files from Git
└── README.md               # Project documentation
```

---

# 🚀 Installation & Setup

## 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd patient-monitoring-system
```

Or download the repository as a ZIP file and extract it.

---

## 2. Check Python

Recommended Python version:

```text
Python 3.9 – 3.12
```

Check your installed version:

```bash
python --version
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If required:

```bash
python -m pip install --upgrade pip
```

---

# 📱 Telegram Bot Configuration

### Important Security Principle

**Do not use the developer's Telegram credentials.**

Every person who downloads this project should create and configure **their own Telegram bot**.

The source code intentionally does **not** contain a real bot token or chat ID.

---

## Step 1 — Create Your Telegram Bot

Open Telegram and search for:

**@BotFather**

Create a new bot using:

```text
/newbot
```

Follow the instructions provided by BotFather.

You will receive a bot token similar to:

```text
123456789:ABCDEF_your_bot_token
```

### 🔐 Keep this token private.

Never publish your real bot token in:

- GitHub
- README files
- Screenshots
- Public messages
- Source code

---

## Step 2 — Start Your Bot

Search for your newly created bot in Telegram and press:

**START**

Send it a test message such as:

```text
Hello
```

---

## Step 3 — Get Your Chat ID

The Telegram Bot API requires the destination **chat ID**.

Use a trusted method to obtain the chat ID associated with the chat where your bot will send alerts.

It will typically look like:

```text
123456789
```

Remember:

```text
Bot Token ≠ Chat ID
```

The **bot token** identifies the bot.

The **chat ID** identifies where the message should be delivered.

---

# 🔐 Configure Telegram Credentials

The program reads credentials from environment variables:

```text
TELEGRAM_BOT_TOKEN
TELEGRAM_CHAT_ID
```

## Windows PowerShell

```powershell
$env:TELEGRAM_BOT_TOKEN="YOUR_BOT_TOKEN"
$env:TELEGRAM_CHAT_ID="YOUR_CHAT_ID"
```

Example:

```powershell
$env:TELEGRAM_BOT_TOKEN="123456789:ABCDEF..."
$env:TELEGRAM_CHAT_ID="123456789"
```

Then run:

```powershell
python patient_monitor.py
```

---

## Windows Command Prompt

```cmd
set TELEGRAM_BOT_TOKEN=YOUR_BOT_TOKEN
set TELEGRAM_CHAT_ID=YOUR_CHAT_ID
python patient_monitor.py
```

---

## Linux / macOS

```bash
export TELEGRAM_BOT_TOKEN="YOUR_BOT_TOKEN"
export TELEGRAM_CHAT_ID="YOUR_CHAT_ID"
```

Then:

```bash
python patient_monitor.py
```

---

# ▶️ Run the Application

Start the program:

```bash
python patient_monitor.py
```

The webcam window will open.

Show one of the supported hand gestures to the camera.

For example:

```text
☝️  1 finger
      ↓
🆘 HELP
      ↓
Telegram
```

Press:

```text
q
```

to close the application.

---

# 📲 Example Telegram Workflow

```text
Patient raises 2 fingers
        ↓
MediaPipe detects hand
        ↓
Finger counter = 2
        ↓
Message = 💧 WATER
        ↓
Telegram Bot API
        ↓
Caregiver receives:
💧 WATER
```

---

# ⚙️ Configuration

The main settings are located in:

```text
patient_monitor.py
```

### Message mapping

```python
messages = {
    1: "🆘 HELP",
    2: "💧 WATER",
    3: "🍛 FOOD",
    4: "🚻 RESTROOM",
    5: "🚨 EMERGENCY"
}
```

### Telegram configuration

The project intentionally uses:

```python
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
```

This allows every user to configure their own Telegram account without modifying the core application.

### Message cooldown

The current cooldown is:

```python
cooldown = 5
```

This means the same recognized request will not continuously send messages during every video frame.

---

# 🧪 Example Output

### Computer Screen

```text
┌──────────────────────────────────────┐
│ Fingers : 1                          │
│ 🆘 HELP                              │
└──────────────────────────────────────┘
```

### Telegram

```text
🆘 HELP
```

The terminal also reports:

```text
Sent: 🆘 HELP
```

---

# 🛡️ Security & GitHub Guidelines

## ❌ Never commit real credentials

Do not write:

```python
BOT_TOKEN = "REAL_BOT_TOKEN"
CHAT_ID = "REAL_CHAT_ID"
```

inside the public repository.

Do not upload:

```text
.env
```

The repository contains:

```text
.env.example
```

only as a template.

The `.gitignore` also excludes `.env`.

---

## 🚨 If You Accidentally Expose a Bot Token

If a real Telegram bot token is ever posted publicly:

1. Open BotFather.
2. Revoke/regenerate the exposed token.
3. Replace the token in your local environment.
4. Check Git history if the token was committed to GitHub.

**Deleting the token from the latest file does not necessarily remove it from Git history.**

---

# 🐛 Troubleshooting

### Camera does not open

Try another camera index:

```python
cap = cv2.VideoCapture(1)
```

instead of:

```python
cap = cv2.VideoCapture(0)
```

Also make sure another application is not using the webcam.

---

### Telegram message is not received

Check:

- Bot token is correct.
- Chat ID is correct.
- You pressed **START** on your bot.
- The computer has internet access.
- Environment variables were configured in the same terminal used to run Python.

---

### Telegram credentials are missing

You may see an error explaining that:

```text
TELEGRAM_BOT_TOKEN
TELEGRAM_CHAT_ID
```

are missing.

Set both variables and run the program again.

---

### Dependencies fail to install

Try:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If MediaPipe has compatibility issues, verify that your Python version is supported by the MediaPipe release you are installing.

---

# 📈 Future Enhancements

Possible improvements for a more advanced version include:

- [ ] Custom trained gesture classification
- [ ] Two-hand gesture recognition
- [ ] Voice feedback for caregivers
- [ ] OLED/LED local status indicators
- [ ] ESP32/ESP8266 integration
- [ ] GSM/SMS emergency fallback
- [ ] Multiple caregiver Telegram accounts
- [ ] Web dashboard for patient status
- [ ] Event logging and timestamps
- [ ] Database integration
- [ ] Patient-specific gesture configuration
- [ ] Improved hand-orientation handling
- [ ] Emergency escalation workflow

---

# 🎓 ECE / SIH Relevance

This project demonstrates the integration of multiple engineering domains:

```text
Electronics & Communication
          │
          ├── Embedded-system integration
          ├── IoT communication
          ├── Wireless notification
          │
          └── Computer Vision / AI
                    │
                    ├── Image Processing
                    ├── Hand Landmark Detection
                    └── Gesture Recognition
```

### Relevant ECE concepts

- Computer vision
- Digital image processing
- Human-machine interaction
- IoT communication
- Wireless data transmission
- Embedded-system integration
- Assistive technology
- Real-time systems

---

# 🌍 Social Impact

The system is intended to support patients who may have difficulty communicating verbally.

Potential use cases include:

- 🏥 Hospitals
- 🏠 Home healthcare
- 👵 Elderly care
- ♿ Assistive-care environments
- 🚑 Emergency assistance
- 🧑‍⚕️ Patient-care monitoring

The goal is to provide a **simple, low-cost, contactless communication interface** that can be extended with embedded hardware and additional AI capabilities.

---

# ⚠️ Disclaimer

This project is an **educational and research prototype**.

It is not a certified medical device and should not be used as the sole method of emergency communication or patient monitoring in a real clinical environment.

---

# 👨‍💻 Contributing

Contributions and improvements are welcome.

A typical workflow is:

```bash
git fork
git clone
git checkout -b feature-name
```

Make your changes, test them, and submit a pull request.

Please do not include real Telegram credentials in commits or pull requests.

---

# 📄 License

Choose an appropriate open-source license before publishing the repository, such as the **MIT License**, if you want others to freely use and modify the project.

---

## ⭐ Project Summary

> **A computer-vision-based patient assistance system that converts simple hand gestures into predefined Telegram alerts, providing a low-cost and contactless communication mechanism for patients who have difficulty communicating verbally.**

<p align="center">
  <strong>Built as an ECE assistive-technology project 🚀</strong>
</p>
