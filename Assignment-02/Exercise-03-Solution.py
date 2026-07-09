import time

def log(original_function):
    '''decorator for developing calculate function'''
    def inner(*args,**kwargs):
        #Time calculating
        start = time.time()
        returned_value=original_function(*args,**kwargs)
        finish = time.time()
        time_consume=finish-start
        if time_consume<1:
            time_return='less than a second'
        else:
            time_return='more than a second'
        #function name   
        Function_Name=original_function.__name__
        
        #errors
        if type(returned_value) == str :
            print('Function Name:',"'{}'".format(Function_Name))
            print('Value Error:',returned_value)
            print("return value: None")
            print('Time Consumption:',time_return)
                  
        else:
            Number_of_Positional_Arguments=len(args)
            print('Function Name:',"'{}'".format(Function_Name))
            print('Number of Positional Arguments:',int(Number_of_Positional_Arguments))
            print('Keyword Arguments:',kwargs)
            print('return value:',returned_value)
            print('Time Consumption:',time_return)
    return inner

# Function
@log
def calculator(*args, operation='ADD', output_format='float'):
    '''Calculate number with this function, + - * / are available'''
    if len(args)>=2:
            
        if operation=='ADD':
            Add=sum (args)
            if output_format=='float':
                return float(Add)
            elif output_format=='int':
                return int(Add)
            else:
                 return 'Format must be float or int.'
                    
                    
        elif operation=='SUB':
            Sub=-1*sum(args)
            
            if output_format=='float':
                 return float(Sub)
            elif output_format=='int':
                return int(Sub)
            else:
                return 'Format must be float or int.'
                
        elif operation=='MUL':
            from operator import mul
            import functools
            Mul=functools.reduce(mul, args)
            if output_format=='float':
                return float(Mul)
            elif output_format=='int':
                return int(Mul)
            else:
                return 'Format must be float or int.'
                
        elif operation=='DIV':
            div=0
            for number in args:
                div /= number
            if output_format=='float':
                return float(div)
            elif output_format=='int':
                return int(div)
            else:
                return 'Format must be float or int.'
                
        else:
            return 'Operation must be ADD, SUB, MUL or DIV.'
        
    elif len(args)==1:
        pass
        
    elif len(args)==0:
        return 'At least one number must be entered.'
    
#Getting input
if __name__ == '__main__':
    code_to_execute = input()
    exec(code_to_execute)
