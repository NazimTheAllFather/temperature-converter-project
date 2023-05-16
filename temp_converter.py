import math

def is_real_number(user_input):  
    leading_sign = ''
    decimal_point_index = -1
    length = len(user_input)
    ord_value = 0

    #Using an if-else statement to ensure that users enters at least one character
    if (length < 1):
        return False
    else:
        #If user_input has more than 1 character, leading_sign is given the first element
        leading_sign = user_input[0]

    #Detecting leading positve or negative signs
    if (leading_sign == '+' or leading_sign == '-') and length > 1:
        user_input = user_input[1:]
        length = len(user_input) 

    #Determining the index of the radix point     
    for i in range(length): 
        if user_input[i] == '.':
            decimal_point_index = i
            break

    #Using a loop to determine if user_input's characters are within an acceptable ASCII range 
    for i in range(length): 
        #if radix point has been found just continue
        if i == decimal_point_index: 
            continue
        #check if character is not within an acceptable number range 
        ord_value = ord(user_input[i]) 
        if ord_value < 48 or ord_value > 57: #48 and 57 represent the ordinal numbers for ASCII character 0 and 9
            return False
    
    return True
def string_to_real(valid_number_string):
    fractional_string = ''
    interger_string = ''
    real_fraction = 0.0
    integer_part = 0
    has_fraction = False
    leading_sign = valid_number_string[0] 
    index = 1
    is_negative = False
    return_real_number = 0.0
    int_string_length = 0
    
    #if loop to check if it is a real number
    if is_real_number(valid_number_string):  
        #checking if has been entered as a positive or negative number 
        if leading_sign == '+':
            valid_number_string = valid_number_string[1:]   
        elif leading_sign == '-':
            is_negative = True
            valid_number_string = valid_number_string[1:]  
        
        #a for loop to perform the opreation of extracting integer and fractional parts as string characters
        for i in valid_number_string: 
            if i == '.':
                has_fraction = True
                continue
            if not has_fraction:
                interger_string += i
            else:
                fractional_string += i
                
        #Converting the integer string to a real number
        int_string_length = len(interger_string)
        for i in range(int_string_length):  
            integer_part += (ord(interger_string[i]) - 48) * (10 ** (int_string_length -1))
            int_string_length -= 1
            
        #Converting the fractional string into a real number
        fractional_string = '.' + fractional_string  

        for index in range(index, len(fractional_string), 1):
            real_fraction += (ord(fractional_string[index]) - 48) * (10 ** (index * -1))  
        
        #Assiging the return value and ensuring that all negative values are returned as negative
        return_real_number = integer_part + real_fraction  
        if is_negative:
            return_real_number *= -1
        
        #returns valid_number_string as a valid real_number of float type
        return return_real_number 

def get_temp_scale(input_or_target):
    #Accepting temprature scale and validating it 
    temp_scale = ''
    valid_temps = ['fahrenheit', 'celsius', 'kelvin', 'rankine', 'delisle', 'newton', 'roaumur', 'romer']

    while True:
        print('\n----\t', end= '')
        print('Fahrenheit, Celsius, Kelvin, Rankine, Delisle, Newton, Roaumur, or Romer', end= ' ')
        print('----\t')
        temp_scale = input(f'Enter your "{input_or_target}" temprature scale (Select an option from the above list!!): ')


        if temp_scale.lower() in valid_temps:
            break
 
    return temp_scale
def to_inter_temp_scale(temprature, temprature_scale):
    #The selected intermediate scale is Celsius
    # if-elif statments that take in temprature and based on the scale convert it to the selected intermediate scale (Celsius)
    celsius_scale = 0
    if temprature_scale.lower() == 'fahrenheit':
        celsius_scale = (temprature - 32) / (9.0/5.0)
    elif temprature_scale.lower() == 'celsius':
        celsius_scale = temprature
    elif temprature_scale.lower() == 'kelvin':
        celsius_scale = temprature - 273.15
    elif temprature_scale.lower() == 'rankine':
        celsius_scale = (temprature - 491.67) * 5.0/9.0
    elif temprature_scale.lower() == 'delisle':
        celsius_scale = 100 - (temprature * 2.0/3.0)
    elif temprature_scale.lower() == 'newton':
        celsius_scale = temprature * 100.0/33.0
    elif temprature_scale.lower() == 'roaumur':
        celsius_scale = temprature * 5.0/4.0
    elif temprature_scale.lower() == 'romer':
        celsius_scale = (temprature - 7.5) * 40.0/21.0

    return celsius_scale
def to_target_temp_scale(temprature, temprature_scale):
    return_temprature = 0
    #Using a number of if-elif statements to convert the intermediate scale to the target one 
    if temprature_scale.lower() == 'fahrenheit':
        return_temprature = temprature * (9.0/5.0) + 32
    elif temprature_scale.lower() == 'celsius':
        return_temprature = temprature
    elif temprature_scale.lower() == 'kelvin':
        return_temprature = temprature + 273.15
    elif temprature_scale.lower() == 'rankine':
        return_temprature = (temprature + 273) * 9.0/5.0
    elif temprature_scale.lower() == 'delisle':
        return_temprature = 100 - (temprature * 3.0/2.0)
    elif temprature_scale.lower() == 'newton':
        return_temprature = temprature * 100.0/33.0
    elif temprature_scale.lower() == 'roaumur':
        return_temprature = temprature * 4.0/5.0
    elif temprature_scale.lower() == 'romer':
        return_temprature = (temprature * 21.0/40.0) + 7.5
    return return_temprature
def sub_zero_detector(temprature_value):
    #Using an if statement to ensure that temprature_value is never less than the sub zero value of the designated 
    # intermediate scale (Celsius)
        if temprature_value < -273.15:
            return True
        return False

    
#Declaring the program's variables
input_temp_as_string = ''
input_temp_as_real = 0.0
target_temp_as_real = 0.0
input_temp_scale = ''
target_temp_scale = ''
yes_no = ''
intermediate_val_holder = 0

print('\t\t\t------------')
print('\t\t\t  Welcome!\n')

while True:
    # Accepting input temprature and validating it 
    while True:
        input_temp_as_string = input('Enter your desired temprature: ')
        #checking if input_temp_as_String is a real number and if so converting it by calling string_to_Real
        if (is_real_number(input_temp_as_string)):
            input_temp_as_real = string_to_real(input_temp_as_string)
            break
        
    #Accepting input temprature scale and validating it 
    input_temp_scale = get_temp_scale('initial')
    
    #Checking if the input is below subzero
    if sub_zero_detector(to_inter_temp_scale(input_temp_as_real, input_temp_scale)):
        print('\nThat temperature is below absolute zero, and therefore is invalid.')
        print('You need to enter a temperature that is greater than or equal to absolute zero!!!\n')
        continue

    #Accepting target temprature scale and validating it  
    target_temp_scale = get_temp_scale('target')

    #Using an if-else statment to check checking if the uesr's input scale and target scale are the same or not
    if input_temp_scale == target_temp_scale:
        target_temp_as_real = input_temp_as_real
    else:    
        intermediate_val_holder = to_inter_temp_scale(input_temp_as_real, input_temp_scale)
        target_temp_as_real = to_target_temp_scale(intermediate_val_holder, target_temp_scale)
    
    #Displaying results
    print(f'\nYou entered {input_temp_as_real} degrees {input_temp_scale}, which is equal to {target_temp_as_real:.2f} degrees ' 
          +f'{target_temp_scale}!')
    
    #Asking the user if they want to conintue
    # An inner loop to make sure the user only enters y or n
    while True:
        yes_no = input('\nWould you like to enter another temperature? (Y/N) ')
        if (yes_no.lower() == 'n') or (yes_no.lower() == 'y'):
            break
        else:
            continue
    #Using an if statment to check if y was entered. if so we continue, otherwise we exit the loop
    if yes_no == 'y':
        continue
    else:
        break

print('\nGoodbye!')
        
