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
    i=0;
    while i<len(text2):
        j=0;
        k=len(text2);
        while j<len(text2):
            if len(text2[i])+len(text2[j])==20:
                print(text2[i],text2[j]);
                text2.pop(i);
                text2.pop(j);
                break;
            else:     
                j=j+1;
        if k==len(text2):
            i=i+1;
