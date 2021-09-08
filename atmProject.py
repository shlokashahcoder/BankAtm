balance= [["id","name","balance"],
          ["abc1002","shloka",15000],
          ["abc1003","driti",10000],
          ["abc1004","kavya",12000]]

def checkBalance():
    for x in balance:
        if x[0]==id:
            print("Your Current Balance Is: "+str(x[2]))

def cashWithdrawal():
    amount = int(input("enter the amount"))
    for y in balance:
        if y[0]==id:
            cb = y[2]-amount
            print(cb)

def cashDeposit():
    amount = int(input("enter the amount"))
    for y in balance:
        if y[0]==id:
            cb = y[2]+amount
            print(cb)

id= input("Enter Your Id")
print("click 1 for balace enquiry")
print("click 2 for deposit")
print("click 3 for cash withdrawal")

choice = int (input("enter your choice"))

if choice==1:
    checkBalance()
elif choice==2:
    cashDeposit()
elif choice==3:
    cashWithdrawal()
else:
    print("no such option")