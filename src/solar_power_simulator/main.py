from solar_power_simulator.calculations.electrical import (
    calculate_dc_power,
    calculate_installed_capacity,
)

print("Note: The input requires the panels that have same rated power per panel.")

number_of_panels = int(input("Enter the number of panels: "))
panel_rated_power = float(input("Enter the rated power per panel(W): "))

capacity = calculate_installed_capacity(number_of_panels, panel_rated_power)

irradiance = float(input("Enter solar irradiance (W/m²): "))

dc_power = calculate_dc_power(capacity, irradiance)

print(f"Installed capacity: {capacity / 1000} kW")
print(f"DC power: {dc_power / 1000} kW")
