list1=[] 
list2=[]
result_list=[]
def merge_lists(n,x):
    for i in range (len(x)):
        result_list.append(n[i])
        result_list.append(x[i])
    print(result_list)

def fill_list2():
    x=input('please enter an charachter or number  for list 2 : ')
    list2.append(x)
    while True:
        print('Thank you '+'if you wanna continue filling first list please enter {}'+'\n'+
        'if you wanna finish the operation {}'.format('continue','finish')
        )
        varibale_decision=input()
        if varibale_decision =='continue':
            new_variable=input('ok enter your value:')
            list1.append(new_variable)
        elif varibale_decision=='finish':
            merge_lists(list1, list2)
            break
    # print(list2)
def fill_list1():
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
            fill_list2()
            break

    # print(list1)
fill_list1()
