john = 0 
sasha = 0 
chris = 0 

ans = input("has the voting finished: ")


while ans == "no":
    print("enter you vote: you can vote for john, sasha or chris ")
    vote = input("vote here: ")
    if vote == 'john':
        john=+1
    elif vote =='sasha':
        sasha =+1
    elif vote == 'chris':
        chris=+1
    ans = input("Has the voting finished: ")

    if ans == ' yes':
        print("john:"+str(john))
        print('sasha:'+ str(sasha))
        print('chris: '+str(chris))
    
    if ans or vote =='END':
        print('john:'+str(john))
        print('sasha:'+str(sasha))
        print('chris:'+str(chris))
        print('total:'+str(john+chris+sasha))
    
