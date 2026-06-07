import serial
import pandas as pd
import joblib

PORT = "COM3"      # CHANGE IF NEEDED
BAUD = 9600

model = joblib.load("posture_model.pkl")

ser = serial.Serial(PORT, BAUD)

history = []

print("Future-risk prediction started...\n")

while True:

    try:

        line = ser.readline().decode().strip()

        if "," not in line:
            continue

        t, d = line.split(",")

        distance = float(d)

        history.append(distance)

        if len(history) < 30:
            print(f"Collecting history... {len(history)}/30")
            continue

        avg10 = sum(history[-10:]) / 10
        avg30 = sum(history[-30:]) / 30

        trend10 = history[-1] - history[-10]
        trend30 = history[-1] - history[-30]

        X = pd.DataFrame([[
            distance,
            avg10,
            avg30,
            trend10,
            trend30
        ]],
        columns=[
            "Distance",
            "Avg10",
            "Avg30",
            "Trend10",
            "Trend30"
        ])

        prediction = model.predict(X)[0]

        if prediction == 1:
            risk = "HIGH FUTURE RISK"
        else:
            risk = "LOW FUTURE RISK"

        print(
            f"Distance={distance:.1f} cm | "
            f"Trend30={trend30:.1f} | "
            f"{risk}"
        )

    except Exception:
        pass