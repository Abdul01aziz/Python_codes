def int(value):
    if type(value) is str:
        return str_to_int(value)
    elif type(value) is float:
        return float_to_int(value)
    elif type(value) is bool:
        return bool_to_int(value)
    elif type(value) is int:
        return value

def str_to_int(str_value):
       '''pick characters one by one from left check character is in between '0' and '9'
       if no raise valueerror if yes convert character to integer and add to result.
       suppose character is '3' then ord('3') - ord('0') = 51 - 48 = 3.'''
       x=0
       for y in str_value:
           if y<'0' or y>'9':
               raise ValueError("not an integer")
           digit = ord(y) - ord('0')
           x = x * 10 + digit
       return x

def float_to_int(float_value):
    '''if number is positive start from result =0 and keep adding 1 until the result is
      less than the number, once you fail condition means result > float_value.
      stop and return the current result. If number is negative
     start from result =0 and keep subtracting 1 until the result is greater than the float_value,
     once you fail condition means result < float_value. stop and
       then return the result.'''
    if float_value >= 0:
        result = 0
        while result + 1 <= float_value: 
            result += 1
        return result
    else:
        result = 0
        while result - 1 >= float_value:
            result -= 1
        return result

def bool_to_int(bool_value):
    '''if bool_value is True return 1 else return 0'''
    if bool_value:
        return 1
    else:
        return 0