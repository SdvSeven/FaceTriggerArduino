# FaceTriggerArduino
**The program operates on the principle of recognizing the operator's face. When the face is detected, the program highlights it and displays the operator's name. Upon identifying the operator, the program sends a signal to rotate the servo motor by 180 degrees. If the operator is not recognized, the program highlights the face in red with the label "NO FACE," and the servo motor returns to the 0-degree position.**

---

## 📌 Features

- Detects and recognizes a specific face from a webcam.
- Trained on a sample image or folder of known face images.
- Sends `1` to Arduino when the face is detected.
- Sends `0` if no match is found.

---

## 🧠 Technologies Used

- OpenCV
- OpenCV-Contrib
- Python 3.x
- Serial communication (optionally via `pyserial`)

---

## 🛠️ Installation

```
pip install opencv-contrib-python
```

## 📁 Step 1: Train the Model

**Script:** `train_model.py`

- Place grayscale face images in a folder (e.g., `face_images/`)
- Each image will be assigned label `1` for known face.

```
python train_model.py
```

## 🎯 Step 2: Run Recognition

**Script:** 'face_recognition_serial.py'

-Set the correct serial port (COM#)
-Ensure face_model.xml is in the same directory


🔌 Arduino Sketch Example
```
#include <Servo.h>

Servo myServo;

void setup() {
  Serial.begin(9600);
  myServo.attach(9); // Подключен к пину 9
  myServo.write(0);  // Начальная позиция
}

void loop() {
  if (Serial.available()) {
    char command = Serial.read();
    if (command == '1') {
      myServo.write(180); // Лицо известно
    } else if (command == '0') {
      myServo.write(0); // Лицо неизвестно
    }
  }
}
```

📄 License
MIT — free to use, modify, and share.
