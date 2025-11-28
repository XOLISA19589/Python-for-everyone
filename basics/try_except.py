#if code inside try worsk, the except is skipped
#if code inside try fails, the except statement is executed

x = 67    #try block will be excecuted
try:
    print(x)
except NameError:
    print('Varibale x is not defined')
except:
    print('Something else went wrong')

try:
    print(y)
except NameError:            #The try block will generate a NameError,because x is not defined
    print('Variable y is not defined')
except:
    print('Something else went wrong')
  
#The try block does not raise any errors,so the else block is executed
try:
    print('Hello')
except:
    print('Something went wrong')
else:
    print('Nothing went wrong')
    
#The finally block gets executed no matter if the try block raises any errors or not 
try:
    print(v)
except:
    print('Something went wrong')
finally:
    print("The 'try except' is finished")
  
 #TypeError, the last except will be executed   
z = 'string' + 5  
try:
    print(z)
except NameError:
    print('Variable z is not defined')
except:
    print('Something else went wrong')
    
