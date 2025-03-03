 # Hand Gesture Recognition for Gaming 🎮

A very simple python project that detects hand gestures using OpenCV and MediaPipe and maps them to **WASD** keyboard controls for gaming purposes.

## 📥 Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2️⃣ Create & Activate Virtual Environment
#### On Windows (PowerShell)
```powershell
python -m venv venv
venv\Scripts\Activate
```

#### On macOS/Linux
```sh
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

## 🚀 Running the Project
Make sure your webcam is connected, then run:
```sh
python hand_gesture.py
```
Press **c'** to exit.

## 🎮 Controls

| Gesture  | Action       | Keyboard Mapping |
|----------|-------------|------------------|
| 1 Finger | Move Left   | **A**            |
| 2 Fingers | Move Right  | **D**            |
| 3 Fingers | Move Backward | **S**       |
| 5 Fingers | Move Forward  | **W**       |

## 🛠 Dependencies
- OpenCV
- MediaPipe
- NumPy
- Keyboard

To manually install dependencies:
```sh
pip install opencv-python mediapipe numpy keyboard
```

## 📝 Notes
- This project uses **Python 3.10** (other versions may work).
- If `ModuleNotFoundError` occurs, ensure the virtual environment is activated.
- Adjust finger detection logic in `hand_gesture.py` to match specific game requirements.


## Demo

https://github.com/user-attachments/assets/1337d4fa-e7d4-48c5-a306-44abea639161





 
