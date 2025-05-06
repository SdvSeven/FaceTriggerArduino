# Убедись, что у тебя установлена версия opencv-contrib-python
# pip install opencv-contrib-python

import cv2
import os
import numpy as np

# Папка с изображениями эталонного лица
data_path = r'...' 
faces = []
labels = []

for img_name in os.listdir(data_path):
    img_path = os.path.join(data_path, img_name)
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        continue
    img = cv2.resize(img, (200, 200))  # приведение всех изображений к одному размеру
    faces.append(img)
    labels.append(1)  # Метка 1 для известного человека

# Проверка наличия лиц
if len(faces) == 0:
    print("Нет изображений для обучения!")
    exit()

# Создание и обучение модели
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, np.array(labels))
recognizer.save("face_model.xml")

print("Обучение завершено. Модель сохранена как face_model.xml")