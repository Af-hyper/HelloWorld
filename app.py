
early_temp = int(input("Early Temperature:  "))
last_temp = int(input("Last Temperature:  "))
change_in_temp = int(last_temp - early_temp)
alpha_aluminium = float(0.0000128)
L = int(input("L: "))
thermal_expansion = (alpha_aluminium * L * change_in_temp )
print(f"Thermal expansion is: {thermal_expansion} mm ")