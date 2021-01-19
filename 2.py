import random

def power(a,b):
    if b==1:
        return a;
    elif b==0:
        return 1;
    elif b%2==0:
        return (power(a,b/2)**2);
    else:
        return (a*power(a,b//2)**2);

n=int(input("Δώσε τον όρο της ακολουθίας Fibonacci: "));

if n<=0:
    print("Σφάλμα! Ο αριθμός που έδωσες είναι μικρότερος του 0");
elif n==1:
    p=0;
    print("Ο αριθμός είναι πρώτος!");

else:
    a=0;
    b=1;
    c=0;
    p=0;
    while c<n:
        p=a+b;
        a=b;
        b=p;
        c=c+1;
    print(p);
    
    flag=False;
    for i in range(20):
        x=random.choice(range(2,n));
        if (power(x,n))%n==x:
            flag=True;
            

    if flag==False:
        print("Ο αριθμός είναι πρώτος!");
    else:
        print("Ο αριθμός δεν είναι πρώτος");

        