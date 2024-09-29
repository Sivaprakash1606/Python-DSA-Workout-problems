string="Wake me early at 5 a.m"
n=3
result=""
for char in string:
    if char.isalpha():
        asciii=65 if char.isupper() else 97
        ch=(ord(char)-asciii+n)%26+asciii
        result=result+chr(ch)
    elif char.isdigit():
        ch=(int(char)+n)%10
        result=result+str(ch)
    else:
        result=result+char
print(result)


