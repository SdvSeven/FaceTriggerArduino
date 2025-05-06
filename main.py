import cv2
import serial
import time
import mediapipe as mp



# Подключение к Arduino
arduino = serial.Serial('COM№', 9600) #введите ваш COM порт
time.sleep(2)

# Загрузка обученной модели
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face_model.xml")

# Каскад Хаара для обнаружения лиц
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    command_sent = False

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_gray = cv2.resize(roi_gray, (200, 200))

        label, confidence = recognizer.predict(roi_gray)
        print(f"Label: {label}, Confidence: {confidence:.2f}")

        if label == 1 and confidence < 70:
            name = "YOU"
            arduino.write(b'1')
            color = (0, 255, 0)
        else:
            name = "NOT DETECT"
            arduino.write(b'0')
            color = (0, 0, 255)

        command_sent = True
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    if not command_sent:
        arduino.write(b'0')

    cv2.imshow('Face Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()