def calculate_installed_capacity(
    number_of_panels: int, panel_rated_power: float
) -> float:

    installed_capacity = number_of_panels * panel_rated_power

    return installed_capacity
