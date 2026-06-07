# Posture-Prediction-System
# AI-Based Posture Monitoring and Prediction System

## Overview

This project is an Arduino and Python based posture monitoring system designed to track a user's sitting distance from a workstation and predict posture deterioration using machine learning.

The system uses an ultrasonic sensor connected to an Arduino to continuously measure the distance between the user and the sensor. Distance data is transmitted to Python, where it is logged, analyzed, visualized, and used to train a machine learning model.

The goal is not only to detect poor posture but also to identify patterns that may indicate future posture degradation.

---

## Features

- Real-time distance measurement using an HC-SR04 ultrasonic sensor
- LED and buzzer feedback for poor posture
- Serial communication between Arduino and Python
- Automatic data logging to CSV
- Live distance visualization
- Statistical posture analysis
- Machine learning model training using historical posture data
- Real-time posture risk prediction

---

## Hardware Used

- Arduino Uno
- HC-SR04 Ultrasonic Sensor
- Passive Buzzer
- LED
- Jumper Wires
- Breadboard

---

## Software Used

- Python 3
- Arduino IDE
- Pandas
- Scikit-learn
- PySerial

---

## Dataset

The dataset was collected by me doing a 20 minutes study session where it measured the lengths between my chest and top of laptop where i had placed it.

Recorded features include:

- Distance
- Moving averages
- Distance trends over time

Dataset size:

- 1200+ sensor readings

---

## Machine Learning

The project uses a Random Forest Classifier trained on time-series posture data.

Engineered features:

- Current Distance
- 10-sample Moving Average
- 30-sample Moving Average
- 10-sample Trend
- 30-sample Trend

Model performance:

- Accuracy: ~92%


---

## Future Improvements

- Additional posture sensors
- Personalized posture models
- Larger training dataset

---

## Author

Muhammad Ebrahim Imran

Artificial Intelligence Undergraduate Student

National University of Sciences and Technology (NUST)
