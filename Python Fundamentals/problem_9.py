"""
Traffic Signal Program
"""

signal = input("Enter signal colour: ").lower()

if signal == "green":
    print("GO")

elif signal == "red":
    print("STOP")

elif signal == "yellow":
    print("READY / SLOW DOWN")

else:
    print("SIGNAL IS BROKEN, DRIVE SLOW")