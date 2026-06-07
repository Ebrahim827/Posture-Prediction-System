import pandas as pd

df = pd.read_csv("posture_data.csv")

avg_distance = df["Distance"].mean()
min_distance = df["Distance"].min()
max_distance = df["Distance"].max()

too_close = df[df["Distance"] < 50]

percent_too_close = (
    len(too_close) / len(df)
) * 100

print()
print("SESSION STATISTICS")
print("------------------")
print(f"Average Distance : {avg_distance:.2f} cm")
print(f"Minimum Distance : {min_distance:.2f} cm")
print(f"Maximum Distance : {max_distance:.2f} cm")
print(f"Time Too Close   : {percent_too_close:.1f}%")

score = 100 - percent_too_close

if score < 0:
    score = 0

    print(f"Posture Score   : {score:.1f}/100")