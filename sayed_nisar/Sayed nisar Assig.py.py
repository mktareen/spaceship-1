

def pyramid():
  for i in range(1,5):
   print(' ',end = '')
   if i==4:
    print('*')
    

  for i in range(1,4):
   print(' ',end ='')
   if i==3:
    print('*' * 3)


  for i in range(1,3):
   print(' ',end ='')
   if i==2:
    print('*' * 5) 
    

  for i in range(1,2):
   print(' ',end ='')
   if i==1:
    print('*' * 7)
    

    
    
pyramid()    
pyramid()  






def add(x):
    def ad(y):
        return x + y
 
    return ad
 
add_15 = add(15)
 
print("The result is", add_15(10))
 
# Returning different function
def outer(x):
    return x * 10
 
def myfunc():
     
    # returning different function
    return outer
 

res = myfunc()
 
print("\nThe result is:", res(10))


