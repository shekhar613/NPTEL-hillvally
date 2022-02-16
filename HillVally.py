'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
# hill = True and Vally = False

def hillValey(l):
    hill = None
    vally = None
    
    a = l[0]
    for i in l:
        if i>a:
            a = i
            hill = True
      
    a = l[0]
    for i in l:
        if i<a:
            a = i
            vally = True
           
    
    if hill==True and vally==True:
        return True
    else:
        return False
    
   
        

print(hillValey([5,4,1,2,3]))
        



