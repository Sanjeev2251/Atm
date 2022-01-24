import os
import datetime
userd={}
flag=True
total=10
route = {"1":"Coimbatore","2":"Tiruppur","3":"Erode","4":"Salem"}
booking = {
    "Coimbatore":[],
    "Tiruppur":[],
    "Erode":[],
    "Salem":[]
}
history_list=[]
def newuser():
    print("Welcome to new user page:)")
    temp = {"password": "","wallet":3000}
    name=str(input("Enter the name:"))
    password=str(input("Enter the password:"))
    if name not in userd.keys():
        temp['password'] = password
        userd[name] = temp
        print("Registered successfully")
    else:
        print("User is already exsiting")
        
def ticketbooking(name,c,seat):
    global total
    for i in range(0,seat):
        temp={"name":"","status":"","timestamp":"","seat booked":""}
        temp['name']=name
        if total>=1:
            temp['status']='booked'
            total-=1
        else:
            temp['status']='Waiting'
        temp['timestamp']=str(datetime.datetime.now())
        temp["seat booked"]=int(seat)
        if c != 5:
            booking[route[str(c)]].append(temp)
        else:
            pass
    print(booking)
    print("Available seats:",total)


def booking2(name):
    global total,booking
    print("welcome to ticket booking page:)")
    print("1.Coimbatore->Chennai(Rs250)\n2.Trippur->Chennai(Rs200)\n3.Erode->Chennai(Rs150)\n4.Salem-Chennai(Rs100)\n5.exit")
    c=int(input("Enter the travelling route:"))
    s=int(input("Enter the seats:"))
    if c==1: 
        if userd[name]['wallet'] >= s*250:
            ticketbooking(name,c,s)
            userd[name]['wallet']=userd[name]['wallet']-s*250
            print("ticket is  booked successfully")
        else:
            print("your crossing the wallet limit")
    if c==2: 
        if userd[name]['wallet'] >= s*200:
            ticketbooking(name,c,s)
            userd[name]['wallet']=userd[name]['wallet']-s*200
            print("ticket is booked successfully")
        else:
            print("your crossing the wallet limit")
    if c==3: 
        if userd[name]['wallet'] >= s*150:
            ticketbooking(name,c,s)
            userd[name]['wallet']=userd[name]['wallet']-s*150
            print("ticket is booked successfully")
        else:
            print("your crossing the wallet limit")
    if c==4:
        if userd[name]['wallet'] >= s*100:
            ticketbooking(name,c,s)
            userd[name]['wallet']=userd[name]['wallet']-s*100
            print("ticket is booked successfully")
        else:
            print("your crossing the wallet limit")
    if c==5:
        return
    his="Name of passanger:",name,"Seat booked:",s,"wallet:",userd[name]['wallet']
    history_list.append(his)
    print(userd) 
def ticketcancel(name,e,f):
    global total
    count = 1
    for element in booking[route[str(e)]]:
            if element['status']=='booked' and count <= f:
                booking[route[str(e)]][count-1]['status']='cancelled'
                total+=1
                count+=1
    his="Name of passanger:",name,"Seat booked:",f,"wallet:",userd[name]['wallet']
    history_list.clear()
    count1=1
    for key, values in booking.items():
        if key == route[str(e)]:
            for i in range(0,len(values)):
                if values[i]['status'] == "Waiting" and count1 <= f:
                    booking[key][i]['status'] = "booked"
                    count1 = count1 + 1
                    total = total - 1
            #if values[i]['status']=="booked":
                #print(booking[key][i]['name']+" has be booked")
    print(booking)
  
def history():
    print("welcome to booking history page:)")
    print(history_list)
    input("...press ENTER TO CONTINUE...")
    os.system('cls')

def booking1(name):
    os.system('cls')
    print("welcome to booking page:)")
    print("1.Booking Ticket\n2.History of ticket")
    g=int(input())
    if g==1:
        os.system('cls')
        booking2(name)
    elif g==2:
        os.system('cls')
        history()

def cancel(name):
    os.system('cls')
    print("Welcome to ticket cancel page:)")
    print("1.Coimbatore->Chennai(Rs250)\n2.Trippur->Chennai(Rs200)\n3.Erode->Chennai(Rs150)\n4.Salem-Chennai(Rs100)\n5.exit")
    e=int(input("Enter the travelling route to cancelling:"))
    f=int(input("Enter the seats:"))
    if e==1: 
        ticketcancel(name,e,f)
        userd[name]['wallet']=userd[name]['wallet']+f*250
        print("ticket cancelled")
       
    elif e==2: 
        ticketcancel(name,e,f)
        userd[name]['wallet']=userd[name]['wallet']+f*200
        print("ticket cancelled")
    elif e==3: 
        ticketcancel(name,e,f)
        userd[name]['wallet']=userd[name]['wallet']+f*150
        print("ticket cancelled")
    elif e==4:
        ticketcancel(name,e,f)
        userd[name]['wallet']=userd[name]['wallet']+f*100
        print("ticket cancelled")
    print("Avaliable seat:",total)
    print(userd)
def existing():
    os.system('cls')
    print("Welcome to existing page")
    name=str(input("Enter the name:"))
    password=str(input("Enter the password:"))
    if userd[name]['password']==password:
        os.system('cls')
        print("login successfully..")
        print("1.Booking Ticket\n2.Cancel ticket\n3.Exist")
        b=int(input())
        if b==1:
            os.system('cls')
            booking1(name)
        elif b==2:
            os.system('cls')
            cancel(name)
        elif b==3:
            return
    else:
        print("user name and password not in existing user")  
os.system('cls')
while flag:
    print("--Railway Ticket--")
    print("1.New User\n2.Existing user\n3.Exist")
    a=int(input())
    if a==1:
        os.system('cls')
        newuser()
    elif a==2:
        os.system('cls')
        existing()
    elif a==3:
        flag=False
