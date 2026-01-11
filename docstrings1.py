
MINOR_AGE_THRESHOLD = 12
DOSE_PROPORTION_FOR_MINOR_AGE = 0.8

def calcMed(weight_kg, age, drug_name, urgent=False):
    """
    Calculates medication dose based on weight.

    Args:
        weight_kg (float): patient body mass in kg
        age (int): years
        drug_name (str): name of drug: "amox", "ibup", etc.
        urgent (boolean): optional flag for EMERGENCY USE ONLY dose
    Returns:
        dose in mg

    Notes:
    - This function does not check for allergies
    - Based on hospital guidelines 2025
    - If weight or age is negative then raise a valueError
    """

    if weight_kg <= 0:
        raise ValueError("Weight must be positive")

    if age < 0:
        raise ValueError("Age cannot be negative")

    dose_per_kilo = {     # describes how absorbed radiation dose is distributed in a medium
        "DRUG_A": 2.0,   # fictional mg/kg
        "DRUG_B": 0.5,   # fictional mg/kg
        "DRUG_C": 1.2    # fictional mg/kg
    }

    if drug_name not in dose_per_kilo:
        raise ValueError(f"Unknown drug name: {drug_name}")

    base_dose = weight_kg * dose_per_kilo[drug_name]

    if age < MINOR_AGE_THRESHOLD:
        base_dose *= DOSE_PROPORTION_FOR_MINOR_AGE

    return round(base_dose, 2)
