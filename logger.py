import serial

PORT = "COM3"      # CHANGE THIS
BAUD = 9600

ser = serial.Serial(PORT, BAUD)

with open("posture_data.csv", "w") as f:

    f.write("Time,Distance\n")

    print("Logging started...")

    while True:

        line = ser.readline().decode().strip()

        if "," not in line:
            continue

        print(line)

        f.write(line + "\n")
        f.flush()