import serial

ser = serial.Serial("COM3", 9600)   # replace COM3

with open("posture_data.csv", "w") as f:
    f.write("Time,Distance\n")

    while True:
        line = ser.readline().decode().strip()

        print(line)

        f.write(line + "\n")
        f.flush()