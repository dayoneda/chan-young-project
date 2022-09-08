#a, b = map(int, input().split())
#print(a+b)

#a,b = map(int, input().split())
#print(round(a/b,2))


#a=[1,1,2,2,2,8]
#b=map(int,input().split())

#print(list(ai-bi for ai,bi in zip(a,b)))

a = [1, 1, 2, 2, 2, 8]
b = list(map(int, input().split()))
for i in range(6):
    print(a[i]-b[i],end=" ")
    