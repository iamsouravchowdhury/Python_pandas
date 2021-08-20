import numpy as np
import pandas as pd

dic1= {
    'name' : ['potter','rohan','sourav','priyanka'] ,
    'marks' :[12,34,56,78],
    'city' : ['Siliguri','Nainital','Kolkata','Darjeeling']
}

hf=pd.DataFrame(dic1)
print(hf)

hf.to_csv('friends.csv')  #Convert to excel
hf.to_csv('friend.csv', index=False)  #To cut out index
print(hf.tail(2))

print(hf.head(2))

print(hf.describe())

payroll= pd.read_csv('payroll.csv')
print(payroll)

# payroll['Employee']
