def calculate_installed_capacity(
    number_of_panels: int, panel_rated_power: float
) -> float:

    installed_capacity = number_of_panels * panel_rated_power

    return installed_capacity


def calculate_dc_power(installed_capacity: float, irradiance: float) -> float:

    dc_power = installed_capacity * (irradiance / 1000)

    return dc_power
