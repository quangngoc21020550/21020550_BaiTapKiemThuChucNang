import numbers

def heathAnalyze(bmi):
    if not isinstance(bmi, numbers.Number):
        raise ValueError('Bmi have to be a positive number!')
    if bmi <=0:
        raise ValueError('Bmi have to be a positive number!')
    if bmi < 18:
        return "Underweight"
    elif bmi <= 25:
        return "Normal"
    else:
        return "Overweight"
