import os
l={2000:0,500:0,100:0,50:0}
t=0
bal=10000
userpin="1111"
min=[]
ob={}
def admin():
    global t
    os.system('cls')
    print("______Welcome Admin_____")
    user=input("Enter the username:")
    pasw=input("Enter the password:")
    if(user=="sanjeev" and pasw=="1114"):
        os.system('cls')
        print("Login successfully")
        while True:
            print("1.Load\n2.show balance\n3.Exit")
            c=int(input("Choose the option"))
            if(c==1):
                os.system('cls')
                print("load the amount")
                for i in l:
                    print("no of ",i," notes:")
                    e=int(input())
                    l[i]=l[i]+e
                    s=i*l[i]
                    t=t+s
                print("Loaded successfully",t)
            elif c==2:
                os.system('cls')
                for i in l:
                    print(i,"->",l[i])
                print("Total amount is loaded:",t)
            elif c==3:
                os.system('cls')
                input("Thank you admin")
                break
            else:
                print("correct option")
    else:
        print("Invalid password")
        os.system('cls')
def Deposite():
    global t,bal,l,min
    print("Welcome to depoiste page:)")
    amo=int(input("Enter the number of 2000:"))
    m=int(input("Enter the number of 500:"))
    n=int(input("Enter the number of 100:"))
    n1=int(input("Enter the number of 50:"))
    updt_am_2000=l.get(2000)+amo
    l.update({2000:updt_am_2000})
    updt_am_500=l.get(500)+m
    l.update({500:updt_am_500})
    updt_am_100=l.get(100)+n
    l.update({100:updt_am_100})
    updt_am_50=l.get(50)+n1
    l.update({50:updt_am_50})
    add=2000*amo+500*m+100*n+50*n1
    bal+=add
    t+=add
    print("Successfully deposited and your current balance:",bal)
    sta="deposite amount:",add,"\ncurrent bal:",bal
    min.append(sta)
def withdrawl():
    global bal,min
    s=int(input("Enter the withdrawl amount:"))
    if (s<bal and s%100==0):
        print("Take cash")
        bal-=s
        print("Your available balance amount is:",bal)
        sta1="withdrawal amount:",s,"current bal:",bal
        min.append(sta1)
    else:
        print("Invalid cash")
def checkbalance():
    global min
    print("Your balance is:",bal)
    sak="current balance after transcation:",bal
    min.append(sak)
def changepassword():
    global userpin
    c=str(input("Enter the old pin:"))
    d=str(input("Enter the new pin:"))
    e=str(input("confirm the new pin:"))
    if d!=e:print("Mismatch pin")
    else:
        userpin=d
        print("Your pin changed successfully")
def mini():
    print("Your last 5 statement is\n",min)

   
    
    
def otherbank():
    global ob,bal
    print("Welcome to other bank transfer page:)")
    while True:
        print("1.transfer amount\n2.Exit")
        d=int(input("Enter the option"))
        if d==1:
            os.system('cls')
            print("Welcome to amount transfer page:)")
            temp={"code":'',"wallet":0}
            name=str(input("Enter the bank account's name:"))
            code=str(input("Enter the ifsc code:"))
            code1=str(input("conform the ifsc code:"))
            if code==code1:
                if name not in ob.keys():
                    temp['code']=code
                    ob[name]=temp
                    amu=int(input("Enter the amount to transfer:"))
                    tra=int(input("Do you want to transfer 1.yes 2.no "))
                    if tra==1:
                        ob[name]['wallet']+=amu
                        balance=ob[name]['wallet']
                        print("other bank account balance:",balance)
                        bal-=amu
                        print("your current balance is",bal)
                    elif tra==2:
                        input("<...cancel the transcation...>")
                    sta1="transfer amount:",amu,"other bank acoount balance:",ob[name]['wallet'],"your account balance:",bal
                    min.append(sta1)
            else:
                print("your ifsc code is mismatch") 
        elif d==2:
            os.system('cls')
            return            
    
def user():
    global bal,userpin
    print("---Welcome to Indian Bank---")
    trial=3
    while 1<=trial<=3:
        pin=input("Enter the pin number:")
        if pin==userpin:
            os.system("cls")
            while True:
                print("Login successfully")
                print("1.Deposite\n2.withdrawal\n3.check balance\n4.change password\n5.Mini statement\n6.other bank transcation\n7.Exit")
                s=int(input("Enter the option:"))
                if s==1:
                    os.system('cls')
                    Deposite()
                elif s==2:
                    os.system('cls')
                    withdrawl()
                elif s==3:
                    os.system('cls')
                    checkbalance()
                elif s==4:
                    os.system('cls')
                    changepassword()
                elif s==5:
                    os.system('cls')
                    mini()
                elif s==6:
                    os.system('cls')
                    otherbank()
                elif s==7:
                    os.system
                    input("Thank you")
                    break
                else:
                    print("Invalid option")
            
        else:
            trial-=1
            print("Wrong pin number,you have",trial,"Trial left")
        if trial==0:
            print("Your card id blocked for 24 yrs")
os.system('cls')
while True:
    print("----ATM----")
    print("1.Admin\n2.User\n3.Exit")
    a=int(input())
    if a==1:
        os.system('cls')
        admin()
    elif a==2:
        os.system('cls')
        user()
    elif a==3:
        os.system('cls')
        input("Thank you for choosing our bank")
        break




