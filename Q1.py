d={"zo":"zoho","a":"and","in":"invoice","bk":"books","bg":"billing","exp":"expense","io":"inventory","chek":"checkout","pa":"payroll","com":"commerce","py":"payments"}
words="zobgachek"
word=""
result=""
for i in words:
    word=word+i
    if word in d:
        result=result+d[word]+" "
        word=""
print(result)
