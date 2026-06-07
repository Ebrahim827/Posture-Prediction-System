import serial
from collections import deque
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# CHANGE THIS
PORT = "COM3"

ser = serial.Serial(PORT, 9600)

times = deque(maxlen=100)
distances = deque(maxlen=100)

fig, ax = plt.subplots()

def update(frame):

    line = ser.readline().decode().strip()

    if "," not in line:
        return

    t, d = line.split(",")

    t = float(t)
    d = float(d)

    times.append(t)
    distances.append(d)

    ax.clear()
    ax.plot(times, distances)

    ax.set_title("Posture Monitor")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Distance (cm)")

ani = FuncAnimation(fig, update, interval=100)

plt.show()