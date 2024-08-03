def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

temperature_conversions = {
    ('celsius', 'fahrenheit'): celsius_to_fahrenheit,
    ('celsius', 'kelvin'): celsius_to_kelvin,
    ('fahrenheit', 'celsius'): fahrenheit_to_celsius,
    ('fahrenheit', 'kelvin'): fahrenheit_to_kelvin,
    ('kelvin', 'celsius'): kelvin_to_celsius,
    ('kelvin', 'fahrenheit'): kelvin_to_fahrenheit
}

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if (from_unit, to_unit) in temperature_conversions:
        return temperature_conversions[(from_unit, to_unit)](value)
    else:
        raise ValueError(f"Conversion from '{from_unit}' to '{to_unit}' is not supported.")

# Example usage
print(convert_temperature(25, 'celsius', 'fahrenheit'))
print(convert_temperature(77, 'fahrenheit', 'celsius'))
print(convert_temperature(300, 'kelvin', 'celsius'))
print(convert_temperature(0, 'celsius', 'kelvin'))
print(convert_temperature(100, 'kelvin', 'fahrenheit'))
print(convert_temperature(32, 'fahrenheit', 'kelvin'))
