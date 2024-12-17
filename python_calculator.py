def calculate(operator, num1, num2):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
        return (round(result,3))
    else:
        raise ValueError(f'{operator} is not a valid operator')
    return result

        
      
       
    