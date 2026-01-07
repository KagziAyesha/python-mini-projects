# 😊 Live Emotion Detection using OpenCV (No ML Model)

This project is a **real-time emotion detection system** built using **Python and OpenCV**.  
It detects **faces, eyes, and smiles** from a webcam feed and predicts basic emotions **without using any machine learning or deep learning model**.

---

## 🎯 Features
- 📷 Real-time webcam face detection  
- 👀 Eye detection  
- 😊 Smile detection  
- 🧠 Rule-based emotion prediction  
- 🟢 Emotion label displayed on face  
- ❌ No training or dataset required  

---

## 🧠 Emotions Detected
| Condition | Emotion |
|---------|--------|
| Smile detected | 😄 Happy |
| Many eyes detected | 😮 Surprised |
| Few or no eyes | 😠 Angry |
| Default | 😐 Neutral |

---

## 🛠 Technologies Used
- Python 3
- OpenCV (`cv2`)
- Haar Cascade Classifiers

---

## ▶ How to Run
1.Clone or download the project
2.Open terminal / command prompt
3.Run the file:
python emotion_detection.py
4.Webcam will open
5.Press q to exit

## 📸 Output
Detects face in real time
Displays emotion label above face
Draws bounding box around face

## ⚠ Limitations
Emotion detection is rule-based, not AI-trained
Accuracy depends on lighting and camera quality
Haar cascades are not as accurate as deep learning models

## 🚀 Future Improvements
Use Deep Learning (CNN) for accurate emotion detection
Train model with real emotion datasets
Add GUI using Tkinter or PyQt
Save detected emotions to a file

``` bash
python emotion_detection.py
```

##📂 Project Structure
Emotion-Detection/ 
│ ├── emotion_detection.py 
    ├── README.md

##👩‍💻 Author
Ayesha Kagzi
BCA (AI) Student
Python & AI Enthusiast