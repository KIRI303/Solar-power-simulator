from solar_power_simulator.calculations.electrical import (
    calculate_ac_power,
    calculate_dc_power,
    calculate_final_power,
    calculate_installed_capacity,
)

print("Note: The input requires the panels that have same rated power per panel.")

number_of_panels = int(input("Enter the number of panels: "))
panel_rated_power = float(input("Enter the rated power per panel(W): "))
irradiance = float(input("Enter solar irradiance (W/m²): "))
inverter_efficiency = float(input("Enter inverter efficiency (%): "))
system_losses = float(input("Enter the system losses (%: "))


capacity = calculate_installed_capacity(number_of_panels, panel_rated_power)


dc_power = calculate_dc_power(capacity, irradiance)

ac_power = calculate_ac_power(dc_power, inverter_efficiency)

final_power = calculate_final_power(ac_power, system_losses)


# Display results
print("\n--- Solar Power Plant Results ---")

print(f"Installed Capacity: {capacity:.5f} W ({capacity / 1000:.5f} kW)")
print(f"DC Power: {dc_power:.5f} W ({dc_power / 1000:52f} kW)")
print(f"AC Power: {ac_power:.5f} W ({ac_power / 1000:.5f} kW)")
print(f"Final Output Power: {final_power:.5f} W ({final_power / 1000:.5f} kW)")
