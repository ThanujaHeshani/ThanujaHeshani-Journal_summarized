# Thermal Power Plant Exergy Calculation


# Get energy input from coal (in MW)
coal_input_energy = float(input("Energy input from coal (MW): "))

# Get efficiency values (as percentages) and convert to decimal
boiler_efficency = float(input("Boiler efficiency (%): ")) / 100
turbine_efficency = float(input("Turbine efficiency (%): ")) / 100
aux_power_percentage = float(input("Auxiliary consumption (% of turbine output): ")) / 100


# Boiler process
boiler_output = coal_input_energy * boiler_efficency
boiler_loss = coal_input_energy - boiler_output
print(f"Boiler Output: {boiler_output:.2f} MW")
print(f"Boiler Loss: {boiler_loss:.2f} MW\n")

# Turbine process
turbine_output = boiler_output * turbine_efficency
turbine_loss = boiler_output - turbine_output
print(f"Turbine Output: {turbine_output:.2f} MW")
print(f"Turbine Loss: {turbine_loss:.2f} MW\n")

# Auxiliary power consumption
aux_power = turbine_output * aux_power_percentage
net_output = turbine_output - aux_power
print(f"Auxiliary Power Consumption: {aux_power:.2f} MW")
print(f"Net Electric Output: {net_output:.2f} MW\n")

# Summary
print("SUMMARY")

print(f"Total Coal Energy Input: {coal_input_energy:.2f} MW")
print(f"Boiler Efficiency: {boiler_efficency*100:.1f}%")
print(f"Turbine Efficiency: {turbine_efficency*100:.1f}%")
print(f"Auxiliary Consumption: {aux_power_percentage*100:.1f}% of turbine output")
print(f"Final Net Output: {net_output:.2f} MW")
