def calculate_installed_capacity(
    number_of_panels: int, panel_rated_power: float
) -> float:

    installed_capacity = number_of_panels * panel_rated_power

    return installed_capacity


def calculate_dc_power(installed_capacity: float, irradiance: float) -> float:

    dc_power = installed_capacity * (irradiance / 1000)

    return dc_power


def calculate_ac_power(dc_power: float, inverter_efficiency: float) -> float:

    ac_power = dc_power * (inverter_efficiency / 100)

    return ac_power


def calculate_final_power(ac_power: float, system_losses: float) -> float:

    final_power = ac_power * (1 - (system_losses / 100))

    return final_power
