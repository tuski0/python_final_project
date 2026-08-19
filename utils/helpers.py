def get_string(prom_message):

    value = input(prom_message).strip()
    if value :
        if isinstance(value, str): 
            return value
        else :
            print('문자열만 입력해주세요')
    else :
        print('문자열을 입력해주세요')

def get_integer(prom_message):
    try:
        value = int(input(prom_message))
        return value
    except ValueError:
        print('정수만 입력해주세요')
    

def get_float(prom_message):
    try:
        value = float(input(prom_message))
        return value
    except ValueError:
        print('실수(숫자)만 입력해주세요')

def get_select(prom_message):
    while True:
        try:
            value = int(input(prom_message))
            if value >= 1 and value <= 6 :
                return value
            else :
                print('1 ~ 6 사이의정수만 입력해주세요')
                continue
        except ValueError:
            print('정수만 입력해주세요')



