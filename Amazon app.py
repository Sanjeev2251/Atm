import os
from operator  import itemgetter
m=[{'name':'sanjeev','password':'1245','status':'Approval'},
   {'name':'sasi','password':'4645','status':'Approval'},
   {'name':'dfgr#','password':'7894','status':'pending'}]
c=[{'name':'sursh','password':'4564'},
   {'name':'#42s4','password':'1543'}]
l=[{'product name':'laptop','price':25000,'stock':10},
   {'product name':'mobile','price':2500,'stock':11},
   {'product name':'charger','price':500,'stock':15}]
b=[]
def addmerchant():
    os.system('cls')
    print("***add merchant***")
    c=str(input("Enter the merchant name:"))
    d=str(input("Enter the password:"))
    z=None
    for i in m:
        z=i
        if c==z['name'] and d==z['password']:
            print("merchant is already exsits")
        else:
            m.append({"name":c,"password":d,'status':'Approval'})
            print("Merchant is added successfully")
            break

            
def removemerchant():
    os.system('cls')
    print('***remove merchant***')
    e=str(input("Enter the name:"))
    print(m)
    for i in range(len(m)):
        if m[i]['name'] == e:
            del m [i]
            print("Merchant is removed successfully")
            print(m)
            break
    else:
        print("Merchant is not found")
        os.system('cls')
        
def approvalmerchant():
    print("****Welcome to Approval Merchant page****")
    z1=None
    for i in range(len(m)):
        z1 = m[i]
        if z1['status']=='pending':
            print(z1["name"],"is waiting for approval")
            s1=int(input("1.Approval\n2.Not Approval"))
            if s1==1:
                print("Merchant is approval successfully")
                m[i]['status'] = 'Approval'
            elif s1==2:
                print("Merchant is rejected")
            else:
                print("invalid")
            break
def admin():
    os.system('cls')
    print("***Welcome to Admin page***")
    name=str(input("Enter the admin name:"))
    password=str(input("Enter the password:"))
    if name=="sanjeev" and password=="2222":
        os.system('cls')
        while True:
            print("---Login successfully---")
            b=int(input("1.add merchant\n2.remove merchant\n3.approval merchant\n4.Exit\nEnter the option"))
            if b==1:
                os.system('cls')
                addmerchant()
            elif b==2:
                os.system('cls')
                removemerchant()
            elif b==3:
                os.system('cls')
                approvalmerchant()
            elif b==4:
                break
            else:
                print("Invalid option")
                os.system('cls')
    else:
        print("Invalid admin")
        os.system('cls')
def newm():
    os.system('cls')
    print("*****Welcome to New merchant page*****")
    mn=str(input("Enter the new merchant name:"))
    mp=str(input("Enter the new merchant password:"))
    for i in m:
        if mn==i['name'] and mp==i['password']:
            print("Merchant is already exist")
    else:
        m.append({'name':mn,'password':mp,'status':'pending'})
        print("Wait..approval from admin")
        input("<<<..press ENTER TO CONTINUE..>>>")
        os.system('cls')
                   
        
def addproduct():
    s=str(input("Enter the product name:"))
    p=input("Enter the price:")
    st=input("Enter the stock:")
    t=None
    for i in l:
        t=i
        if s==t['product name'] and p==t['price'] and st==t['stock']:
            print("Product is already added in list")
    else:
        l.append({'product name':s,'price':p,'stock':st})
        print("Product is added successfully")
        print(l)
        input("...press ENTER TO CONTINUE...")
        os.system('cls')
def removeproduct():
    os.system('cls')
    j=str(input("Enter the product name:"))
    print(l)
    for i in range(len(l)):
        if l[i]['product name'] == j:
            del l[i]
            print("Product is remove successfully")
            print(l)
            break
    else:
        print("Product is not found")
def available():
    print("*****product Available page*****")
    d=None
    for i in l:
        d=i
        print("1.Available product name:",d['product name'])
        print("2.Product price:",d['price'])
        print("3.Available Stock:",d['stock'])
        input("<<<...Please Enter to CONTIUNE...>>>")
def login():
    os.system('cls')
    print("----Login successfully----")
    print("1.Add product\n2.Remove product\n3.Available product\n3.exit")
    i=int(input("Enter the choose:"))
    if i==1:
        os.system('cls')
        addproduct()
    elif i==2:
        os.system('cls')
        removeproduct()
    elif i==3:
        os.system('cls')
        available()
    elif i==4:
        return
    else:
        print('your request is pending')

    
def existingm():
    os.system('cls')
    print("***welcome to exsiting merchant page***")
    g=str(input("Enter the name:"))
    h=str(input("Enter the password:"))
    for i in m:
        if g==i['name'] and h==i['password']and i['status']=='Approval':
            login()
        elif g==i['name'] and h==i['password'] and i['status']=='pending':
            print("request is sent to admin for approval")

                            
def merchant():
    while True:
        print("*****Welcome to Merchant page*****")
        print("1.New merchant\n2.Existing merchant\n3.exit")
        f=int(input("Enter the choose:"))
        if f==1:
            os.system('cls')
            newm()
        elif f==2:
            os.system('cls')
            existingm()
        elif f==3:
            break
        else:
            print("Invalid")
        os.system('cls')
def new():
    os.system('cls')
    print("***Welcome to New Buyer page***")
    name=str(input("Enter the new buyers:"))
    password=str(input("Enter the password:"))
    if (name,password) not in b:
        b.append({"Name":name,"Password":password})
        print("Buyer is added successfully.....")
    else:
        print("buyers is already exisiting")
def showproduct():
    global l
    os.system('cls')
    print("*****Welcome to show product page*****")
    p=str(input("Enter the product name:"))
    for o in l:
        if o['product name'] == p:
            print("Product name:",o['product name'])
            print("price:",o['price'])
            print("Stock:",o['stock'])
    input("<<<...Please ENTER TO CONTINUE...>>>")
            
def fliter():
    os.system('cls')
    global l
    print("*****Welcome to Fliter page*****")
    fll=int(input("1.Price 2.Stock"))
    if fll==1:
        fl=sorted(l,key=itemgetter('price'))
        print("Flitered using by price:",*fl)
    elif fll==2:
        fl1=sorted(l,key=itemgetter('stock'))
        print("Flitered using by stock:",*fl1)
def placeorder():
    global l
    os.system('cls')
    print("***Welcome to order place page***")
    po=str(input("Enter the product name to order:"))
    qo=int(input("Enter the quantity to order:"))
    for i in l:
        if po == i['product name']:
            print("*******************")
            print("Available product list")
            print("*******************")
            print("1.product name:",i['product name'])
            print("2.Cost of product:",i['price'])
            print("3.Avaliable stock:",i['stock'])
            pa=int(input("Do you want to buy 1.yes 2.No"))
            if pa == 1:
                ko=i['price']*qo
                i['stock']=i['stock']-qo
                print("*****Ordered list*****")
                print("1.product name:",i['product name'])
                print("2.Cost of product:",ko)
                bo=int(input("1.Buy Now 2.Cancel order"))
                if bo == 1:
                    print("product name:",i['product name'])
                    print("Total Price:",ko)
                    print("Ordered is placed")
                elif bo ==2:
                    return
            elif pa==2:
                return

def existing():
    os.system('cls')
    print("*****Welcome to Buyer page*****")
    name=str(input("Enter the buyer:"))
    password=str(input("Enter the password:"))
    for i in b:
        if name==i["Name"] and password==i["Password"]:
            os.system('cls')
            print("---Login successfully---")
            print("1.show the product\n2.fliter\n3.place order\n4.Exist")
            s1=int(input("Enter the option:"))
            if s1==1:
                showproduct()
            elif s1==2:
                fliter()
            elif s1==3:
                placeorder()
            elif s1==4:
                break
            else:
                print("Buyer details is not added")
                input("<...press ENTER TO CONTINUE...>")
                        
    
def buyers():
    while True:
        print("***welcome to buyer***")
        print("1.New buyer\n2.Existing buyer\n3.Exit")
        q=int(input("Enter the choice:"))
        if q==1:
            os.system('cls')
            new()
        elif q==2:
            os.system('cls')
            existing()
        elif q==3:
            input("Thank you buyers")
            break
        else:
            print("Invalid")
            os.system('cls') 
os.system('cls')   
while True: 
    print("*****Amazon******")
    print("1.Admin\n2.Merchant\n3.Buyers\n4.exit")
    a=int(input("choose the option"))
    if a==1:
        os.system('cls')
        admin()
    elif a==2:
        os.system('cls')
        merchant()
    elif a==3:
        os.system('cls')
        buyers()
    elif a==4:
        input("Thank you")
        break
    else:
        print("Invalid operation")
