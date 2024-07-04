def convert_temperature_to_f(c):
    resc = c * 9.0 / 5.0 + 32.0
    return f'Converted to Fahrenheit: {resc}'
def convert_to_kelvin(c):
    res = c + 273.15
    return f'Converted to Kelvin: {res}'

while True:
    typetemp = input('Write to what temperature to convert Celsius-> \nf (Fahrenheit),\nk (kelvin): ')
    if typetemp == 'f':
        c = float(input('Write temperature in Celsius: '))
        result = convert_temperature_to_f(c)
        print(result)
    elif typetemp == 'k':
        c = float(input('Write temperature in Kelvin: '))
        result1 = convert_to_kelvin(c)
        print(result1)
    else:
        print('Write only letter f or k')