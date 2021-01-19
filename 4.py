import random
punctuations="""!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~0123456789""";
with open("sample3.txt", "r") as f:
    r=f.read();
    text=str(r);
    text2="";
    for char in text:
        if char not in punctuations:
            text2=text2 + char;
    text2=text2.lower();
    text2=text2.split();
    c=0;
    text3=[];
    templist=[];
    for i in text2:
        if c<3:
            c=c+1;
            templist.append(i);
        else:
            c=0;
            text3.append(templist);
            templist=[];
    
    x=random.randint(0,len(text3));

    words=[text3[x][0],text3[x][1],text3[x][2]];
    flag=True;
    while (len(words)<200) and (flag==True):
        flag=False;
        for i in range(len(text3)):
            if (text3[x][2]==text3[i][1]) and (text3[x][1]==text3[i][0]):
                words.append(text3[i][2]);
                x=i;
                flag=True;
                if len(words)==200:
                    flag=False;
                    break;
    print(words);
    print(len(words));

    

