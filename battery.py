def battery_charge(num):
    rond = round(num / 10)
    print("[" + "[" * rond + " " * (10 - rond) + "]" + "\n" + str(num) + "%")


battery_charge(52)
