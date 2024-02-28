import math
import matplotlib.pyplot as plt

# data comes from https://www.automobile-catalog.com/curve/2013/1600490/honda_civic_lx_sedan.html#gsc.tab=0


# initialize empty lists for graph values
RPM_X = []
Torque_Y = []
Power_Y2 = []

# open the file with the corresponding car data
with open ("car_data.txt", "r") as file:
    # this line will determine the number of lines in the file
    lines = file.readlines()

    # split = lines[0].split()
    # print(split[0])

    # iterate thru each line
    for line in lines:
        # this function will split each value in the line like this
        # ["1000" "rpm:" "80.9" "Nm" "59.7" "lb-ft" "8.5" "kW" "11.5" "PS" "11.4" "hp"]
        split = line.split()

        # will grab 1000 from the split line 
        RPM_X.append(int(split[0]))

        # will grab 80.9 from the split line
        Torque_Y.append(float(split[2]))

        # will grab 11.4 from the split line
        Power_Y2.append(float(split[10]))
# print(RPM_X)
# print(Torque_Y)
# print(Power_Y2)



# will create the torque and power map
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
line1 = ax1.plot(RPM_X, Torque_Y, color = "red", label = "Torque")
ax1.set_ylabel("Engine Torque Nm")
ax1.set_ylim(0, 180)
ax2.set_ylim(0, 180)
line2 = ax2.plot(RPM_X, Power_Y2, color = "blue", label = "Power")
ax2.set_ylabel("Engine Power HP")
ax1.set_xlabel("Engine RPM")
plt.title("Engine Torque map at full load")
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels)
ax1.grid(True)
plt.show()