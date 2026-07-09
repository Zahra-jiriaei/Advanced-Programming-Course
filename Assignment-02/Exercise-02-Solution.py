def memorize_1():
    word504={}
    def inner(**kwargs):
        nonlocal word504
        
        if len(word504)==0:
            print('None')
            print('\n')
            word504=kwargs
        else:
            # words which have been memorised yesterday
            ## sorting values
            for keywords in list(word504.keys()):
                value_word504=word504[keywords]
                if "," in value_word504:
                    value_word504_2=value_word504.split(', ')
                    value_word504_3=sorted(value_word504_2, key=lambda s: (len(s),s))
                    value_word504_4=', '.join(value_word504_3) 
                    word504[keywords]=value_word504_4
                    
            ## sorting keys
            sort_word504 = dict(sorted(word504.items()))
        
            ## print value
            word504_items=list(sort_word504.items()) 
            text='{}: {}'
            for i in range(len(word504_items)):
                print (text.format(word504_items[i][0],word504_items[i][1]))
            print('\n')
                
            # deleteing day before yesteday info
            word504.clear()
            # words which have been memoris today
            word504=kwargs
            
    return inner

memorize=memorize_1()

if __name__ == '__main__':
    exec(input().replace('\\n', '\n'))
