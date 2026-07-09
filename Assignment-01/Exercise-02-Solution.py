def average_tuple(two_dimentional_tuple):
    '''
    Getting n*m tuples and returning the avarage of ith index
    '''
    return tuple(map(lambda List: sum(List)/len(List) ,zip(*two_dimentional_tuple)) )

if __name__ == '__main__':
    expression_to_evaluate = input()
    print(eval(expression_to_evaluate))
