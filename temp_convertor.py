
print('Welcome of Temperature Convertor App')

#Gather user input
temp_f = float(input('What is the given temperature in degrees fahrenheit'))

#Formulae
temp_c = (5/9)*(temp_f-32)
temp_k = temp_c + 273.15

#round temps
temp_f = round(temp_f, 4)
temp_c = round(temp_c, 4)
temp_k = round(temp_k, 4)

#Summary/OUTPUT Table
print('\nDegrees Fahrenheit:\t' + str(temp_f))
print('Degrees Celsius:' + str(temp_c))
print('Degrees Kelvin:\t' + str(temp_k))
