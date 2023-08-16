

def calculate_bmi_value(weight, height):
    # BMI Formula: weight (kg) / (height (m) ** 2)
    if weight == '' or weight is None:
        raise ValueError('Weight Parameter is missing')
    
    if height == '' or weight is None:
        raise ValueError('Height Parameter is missing')
    
    try:
        weight = float(weight)
        height = float(height)/100

    except Exception as e:
        raise ValueError('Invalid data for Weight or Height')

    bmi = weight / (height ** 2)
    bmi = round(bmi, 2)
    return bmi