class pattern:
    def pattern(self,n,count):
        num=n
        c=1
        for i in range(count):
            space=count-i
            print(" " * space,end="")
            for j in range(c):
                print(num,end=" ")
            print()
            c=c+1
            num=num+3
n=3
count=3
Pattern=pattern()
Pattern.pattern(3,count)
