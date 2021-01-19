import random

x = int(input("Δώσε τις διαστάσεις του τετραγώνου:"));
lst = list(range(x*x));
s = 0;
for m in range(100):
    # ελέγχω για την στρογγυλοποίηση προς τα πάνω
    if x*x%2==0:
        hand = random.sample(lst, k = (x*x//2));
        k = x*x//2;
    else:
        hand = random.sample(lst, k = (x*x//2+1));
        k = x*x//2+1;

    b =list(range(x*x));
    # βάζω τους άσους σε μονοδιάστατο και μετά κανω την μεταφορά στον δυσδιάστατο 
    for i in range(x*x):
        b[i] = 0;

    i = 0;
    j = 0;
    
    for h in range(k):
        b[hand[h]]=1;

    a = [];
    h = 0;

    for i in range(x):
        row = [];
        for j in range(x):
            row.append(b[h]);
            h = h+1;
        a.append(row);
    # βρίσκω τις τετράδες
    d1=0;
    d2=0;
    v=0;
    h=0;
    for i in range(x-3):
        for j in range(x-3):
            if a[i][j]==a[i+1][j+1]==a[i+2][j+2]==a[i+3][j+3]==1:
                d1=d1+1;
            if a[i][j]==a[i][j+1]==a[i][j+2]==a[i][j+3]==1:
                h=h+1;
            if a[i][j]==a[i+1][j]==a[i+2][j]==a[i+3][j]==1:
                v=v+1;
    # μου βγάζει πρόβλημα για την άλλη διαγώνιο            
    #    for i in range(x-3):
    #        for j in range(x,3,-1):
    #            if a[i][j]==a[i+1][j-1]==a[i+2][j-2]==a[i+3][j-3]==1:
    #                d2=d2+1;
    
    
    s = s+v+h+d1+d2;

print("Ο μέσος όρος των τετράδων είναι: ", s/100);



