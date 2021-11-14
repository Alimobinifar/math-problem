list1=[] 
list2=[]
def fill_list():
    x=input('please enter an charachter or number  : ')
    list1.append(x)
    while True:
        print('Thank you '+'if you wanna continue filling first list please enter {}'+'\n'+
        'if you wanna fill next list please type {}'.format('continue','next')
        )
        varibale_decision=input()
        if varibale_decision =='continue':
            new_variable=input('ok enter your value:')
            list1.append(new_variable)
        elif varibale_decision=='next':
            break
    print(list1)

fill_list()

    