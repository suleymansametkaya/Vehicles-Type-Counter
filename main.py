import cv2
from sort import *
import math
import numpy as np
from ultralytics import YOLO
import cvzone
import torch
import time
from database import send_values, databese_create



databese_create()  # Eger database yoksa olusturur 

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"Using device: {device}")  # Modelin GPU mu CPU mu kullandigini gosterir 

cap = cv2.VideoCapture('sources/trafic3.mp4')
model = YOLO('models/vehicles_best2.pt')

classNames = ['otomobil', 'bisiklet', 'otobus', 'minibus', 'motor', 'kamyon']  # Modelimizdeki sinif isimleri

tracker = Sort(max_age=20) # Sort algoritmasi ile nesneleri takip eder
line = [0, 400, 1920, 400] # Gecis hattinin koordinatlari

# Her sınıf için ayrı bir counter listesi
counter_otomobil = []
counter_bisiklet = []
counter_otobus = []
counter_minibus = []
counter_motor = []
counter_kamyon = []

while 1:
    start = time.perf_counter()

    ret, frame = cap.read()
    
    if not ret:
        break
    
    detections = np.empty((0, 5)) #
    
    result = model(frame, stream=1, conf=0.7, verbose=False, show=False, device=device)
    
    for info in result:
        
        boxes = info.boxes
        
        for box in boxes:
            
            # Tespit edilen nesnelerin koordinatlarını ve sınıfını alıyoruz
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1
            conf = box.conf[0]
            classindex = box.cls[0]
            conf = math.ceil(conf * 100)
            classindex = int(classindex)
            objectdetect = classNames[classindex]
            
            # Tespit edilen nesneleri ekrana yazdirma ve cizme
            if objectdetect in ['otomobil', 'bisiklet', 'otobus', 'minibus', 'motor', 'kamyon'] and conf > 60:
                new_detections = np.array([x1, y1, x2, y2, conf])
                detections = np.vstack((detections, new_detections))
                color = (0, 255, 0)
                cvzone.cornerRect(frame, (x1, y1, w, h), colorC=color, colorR=color)
                cvzone.putTextRect(frame, f'{classNames[classindex].upper()} {int(conf)}%', (max(0, x1), max(35, y1)),
                                   scale=1, thickness=2, colorR=color, colorB=color)

    # Tespit edilen nesneleri takip etme
    track_result = tracker.update(detections)
    cv2.line(frame, (line[0], line[1]), (line[2], line[3]), (0, 255, 255), 5)

    # Tespit edilen nesnelerin koordinatlarını ve sınıfını alıyoruz
    for results in track_result:
        x1, y1, x2, y2, id = results
        x1, y1, x2, y2, id = int(x1), int(y1), int(x2), int(y2), int(id)

        w, h = x2 - x1, y2 - y1
        cx, cy = x1 + w // 2, y1 + h // 2

        # Tespit edilen nesnelerin merkez noktasini cizme
        cv2.circle(frame, (cx, cy), 6, (0, 0, 255), -1)
        color = (0, 255, 0)

        # Tespit edilen nesne cizgiyi gecip gecmedigini kontrol etme
        if line[0] < cx < line[2] and line[1] -20 < cy < line[1] + 20:
            cv2.line(frame, (line[0], line[1]), (line[2], line[3]), (0, 0, 255), 7)

            # Tespit edilen nesnenin sinifini kontrol etme ve counter listesine eklemek
            objectdetect = classNames[classindex]
            if objectdetect == 'otomobil' and counter_otomobil.count(id) == 0:
                counter_otomobil.append(id)
            elif objectdetect == 'bisiklet' and counter_bisiklet.count(id) == 0:
                counter_bisiklet.append(id)
            elif objectdetect == 'otobus' and counter_otobus.count(id) == 0:
                counter_otobus.append(id)
            elif objectdetect == 'minibus' and counter_minibus.count(id) == 0:
                counter_minibus.append(id)
            elif objectdetect == 'motor' and counter_motor.count(id) == 0:
                counter_motor.append(id)
            elif objectdetect == 'kamyon' and counter_kamyon.count(id) == 0:
                counter_kamyon.append(id)

    # Tespit edilen nesnelerin sayisini ekrana yazdirma
    cvzone.putTextRect(frame, f'Otomobil = {len(counter_otomobil)}', [10, 74], thickness=2, scale=1.5, border=2)
    cvzone.putTextRect(frame, f'Bisiklet = {len(counter_bisiklet)}', [10, 114], thickness=2, scale=1.5, border=2)
    cvzone.putTextRect(frame, f'Otobus = {len(counter_otobus)}', [10, 154], thickness=2, scale=1.5, border=2)
    cvzone.putTextRect(frame, f'Minibus = {len(counter_minibus)}', [10, 194], thickness=2, scale=1.5, border=2)
    cvzone.putTextRect(frame, f'Motor = {len(counter_motor)}', [10, 234], thickness=2, scale=1.5, border=2)
    cvzone.putTextRect(frame, f'Kamyon = {len(counter_kamyon)}', [10, 274], thickness=2, scale=1.5, border=2)

    end = time.perf_counter()
    total_time = end - start
    fps = 1 / total_time

    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow("Vehicles Type Counter", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tespit edilen nesnelerin sayisini database'e gonderme
send_values(len(counter_otomobil), len(counter_otobus), len(counter_minibus), len(counter_bisiklet), len(counter_motor), len(counter_kamyon))

cap.release()
cv2.destroyAllWindows()
