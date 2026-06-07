import pandas as pd

try:

    df = pd.read_csv("posture_data.csv")

    if len(df) < 30:
        print("Need at least 30 readings.")
        exit()

    distance = df["Distance"]

    current = distance.iloc[-1]

    avg10 = distance.tail(10).mean()
    avg30 = distance.tail(30).mean()

    first30 = distance.tail(30).iloc[0]
    last30 = distance.tail(30).iloc[-1]

    trend = last30 - first30

    below50 = len(df[df["Distance"] < 50])
    percent_below50 = (below50 / len(df)) * 100

    print("\nPOSTURE PREDICTION REPORT")
    print("-------------------------")

    print(f"Current Distance      : {current:.1f} cm")
    print(f"10-Reading Average    : {avg10:.1f} cm")
    print(f"30-Reading Average    : {avg30:.1f} cm")
    print(f"30-Reading Trend      : {trend:.1f} cm")
    print(f"Time Below 50 cm      : {percent_below50:.1f}%")

    risk_score = 0

    if current < 50:
        risk_score += 3

    if avg10 < 55:
        risk_score += 2

    if avg30 < 60:
        risk_score += 1

    if trend < -5:
        risk_score += 2

    if percent_below50 > 20:
        risk_score += 2

    print()

    if risk_score >= 7:
        print("Prediction: HIGH POSTURE RISK")

    elif risk_score >= 4:
        print("Prediction: MEDIUM POSTURE RISK")

    else:
        print("Prediction: LOW POSTURE RISK")

except FileNotFoundError:
    print("posture_data.csv not found.")