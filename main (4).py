class bankaccount:
  def __init__(self,account_number,account_holder_name,inital_balance=0.0):
    self.__account_number=account_number
    self.__account_holder_name=account_holder_name
    self.__account_balance=inital_balance
    def deposit(self,amount):
      if amount > 0:
        self.__account_balance+=amount
        print("deposited₹{}.new balance:₹{}".format(amount,self.__account_balance))
      else:
        print("invalid deposit amount.please deposit a positive amount")
    def withdrew(self,amount):
       if amount > 0and amount<=self.__account_balance:
         self.__account_balance-=amount
         print("withdrew₹{}new balance:₹{}".format(amount,self.__account_balance))
       else:
         print("invalid withdrew amount or in sufficient balance")
         def display_balance(self):
           print("account number for {}(account #{}):₹{}".format(self.__account_holder_name,self.__account_number,self.__account_balance))
           account=bankaccount(account_number="00875791255",account_holder_name="ramu",inital_balance=5000.00)
           
           
account.display_balance() 
account.deposit(500.00)
account.withdrew(200.00)
account.display_balance()


           
         
         
       
         
        
      
      
      
      