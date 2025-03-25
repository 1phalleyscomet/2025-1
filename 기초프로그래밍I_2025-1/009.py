k=int(input("숫자를 입력하시오>"))
sum=1
for i in range(1,k+1,1):
    sum=sum*i #sum*=i
print(k,"!=",sum)