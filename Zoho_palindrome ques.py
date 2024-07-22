string="Bob sees a racecar ahead fast"
print(string)
arr_words=[]
word=""
for i in string:
    if i ==" ":
        arr_words.append(word)
        word=""
        continue
    word=word+i
arr_words.append(word)
Not_palindrome=[]
for word in arr_words:
    left=0
    right=len(word)-1
    is_palindrome=True
    while left<right:
        if word[left].lower() != word[right].lower():
            is_palindrome=False
            break
        left=left+1
        right=right-1
    if is_palindrome == False:
        Not_palindrome.append(word)
without_pali=(" ".join(Not_palindrome))
print("Output : " +without_pali)



