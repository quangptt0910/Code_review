# The vital_signs_analyzer script implements the following requirements:
# 1/ The system should accept heart rate (HR) and blood oxygen saturation (SpO2) readings. The values should be normalized into a 0-1 range using defined physiological limits.
# 2/ The system should detect the patient's status based on thresholds for normalized HR and SpO2.
# 3/ The user should be able to override the status with a manually set value.
# 4/ The system should support displaying the status (if enabled) and logging it to a file (if enabled).

tmp = None

# Constants for physiological limits
HR_MIN = 40
HR_MAX = 180
SPO2_MIN = 0
SPO2_MAX = 100
NORMALIZED_HR_CRITICAL_THRESHOLD = 0.7
NORMALIZED_SPO2_CRITICAL_THRESHOLD = 0.3
NORMALIZED_HR_WARNING_THRESHOLD = 0.4
SPO2_SEVERE = 88
HR_SEVERE = 200



def normalize_hr(hr):
    """
    Normalizes Heart Rate into a 0-1 range.

    Args:
        hr (float): Heart Rate.

    Returns:
        float: Normalized Heart Rate.
    """
    if hr < HR_MIN or hr > HR_MAX:
        raise ValueError("Invalid Heart rate range")

    if HR_MAX == HR_MIN:
        raise ValueError("HR_MAX and HR_MIN cannot be equal")
    return (hr - HR_MIN) / (HR_MAX - HR_MIN)


def normalize_spo2(spo2):
    """
    Normalizes SpO2 into a 0-1 range.

    Args:
        spo2 (float): Blood Oxygen Saturation.

    Returns:
        float: Normalized SpO2.
    """
    if spo2 < SPO2_MIN or spo2 > SPO2_MAX:
        raise ValueError("Invalid Spo2 range")

    if SPO2_MAX == SPO2_MIN:
        raise ValueError("SPO2_MAX and SPO2_MIN cannot be equal")
    return (spo2 - SPO2_MIN) / (SPO2_MAX - SPO2_MIN)


def analyze(hr, spo2, log=True, override_status=None, verbose=False):
    """
    Analyzes HR and SpO2 to determine patient status.

    Args:
        hr (float): Heart Rate.
        spo2 (float): Blood Oxygen Saturation.
        log (bool): Whether to log the result to a file.
        override_status (str): Manual status override.
        verbose (bool): Whether to print details.

    Returns:
        str: The determined status.
    """

    if verbose:
        print(f"Analyzing vital data: HR={hr}, SpO2={spo2}")

    try:
        n_hr = normalize_hr(hr)
        n_spo2 = normalize_spo2(spo2)
    except TypeError:
        print("Error: Invalid input types for HR or SpO2")
        return "ERROR"

    status = "OK"

    if override_status:
        status = override_status
    else:
        # Logic based on normalized thresholds
        # n_hr > 0.7 corresponds to HR > 138
        # n_spo2 < 0.3 corresponds to SpO2 < 30
        if n_hr > NORMALIZED_HR_CRITICAL_THRESHOLD and n_spo2 < NORMALIZED_SPO2_CRITICAL_THRESHOLD:
            status = "CRITICAL"
        elif n_hr > NORMALIZED_HR_WARNING_THRESHOLD:
            if spo2 < SPO2_SEVERE or hr > HR_SEVERE:
                status = "SEVERE"
            else:
                status = "WARNING"
        else:
            status = "OK"

    if log:
        try:
            with open("vitals_log.txt", "a", encoding="utf-8") as f:
                f.write(
                    f"HR={hr}, SpO2={spo2}, NormHR={n_hr:.2f}, NormSpO2={n_spo2:.2f}, STATUS={status}\n"
                )
        except IOError as e:
            print(f"Error writing to log file: {e}")

    if verbose:
        print(f"Status is: {status}")

    return status


if __name__ == "__main__":
    hr = 999
    spo2 = -3

    result = analyze(hr, spo2, log=True, override_status=None, verbose=True)

    print(f"Finished analysis, result: {result}")