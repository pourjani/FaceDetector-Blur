# Real_time_face_detection
This project demonstrates how to use OpenCV and Haar Cascades to perform real-time face detection via webcam.
## 🔍 Features

- 🎥 Real-time webcam access (via OpenCV)
- 😃 Face detection using Haar cascades
## 🚀 Getting Started

### 🔧 Requirements

Make sure you have the following installed:

- Python 3.x
- OpenCV (`opencv-python`)
- NumPy
- Jupyter Notebook
# 🤖 Real-Time Face Blur with OpenCV DNN

This project detects human faces in real-time using OpenCV's Deep Neural Network (DNN) module and applies a Gaussian blur to those regions. It's useful for protecting privacy in images or webcam video streams.

---

## 📌 Features

- ✅ Real-time face detection using a pre-trained DNN model
- ✅ Gaussian blur applied only to detected face areas
- ✅ Supports both images and webcam streams
- ✅ Lightweight and easy to integrate

---

## 🎥 Demo

Here's a real-time demonstration of the face blur in action:

![Face Blur Demo](demo.gif)

---

## 🧠 How It Works

1. The image is passed through a pre-trained DNN face detector.
2. A binary mask is created for detected face areas.
3. Gaussian blur is applied only to the masked (face) regions.
4. The blurred regions are merged with the original background.

---

## 🛠 Requirements

- Python 3.x
- `opencv-python`
- `numpy`
