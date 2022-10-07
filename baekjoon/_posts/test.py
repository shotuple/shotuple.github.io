num = N = int(input())
cnt = 0

while True:
    a = num//10 # 10의 자리
    b = num%10 # 1의 자리
    c = (a+b)%10 
    num = (b*10)+c

    cnt+=1
    if(num==N):
        break
print(cnt)

input_num = temp = int(input())
cnt = 0

while True:
    num1 = temp // 10
    num2 = temp % 10
    sum_num = num1 + num2
    
    temp = int(str(num2) + str(sum_num % 10))
    
    cnt += 1
    
    if input_num == temp:
        break
    
print(cnt)


        
    