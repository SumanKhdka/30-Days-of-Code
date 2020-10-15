# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(input())
d={}
for i in range(N):
    entry=input().split()
    d[entry[0]]=entry[1]

ans=[]

try:
    while(1):
        new=str(input())
        if(new in d.keys()):
            ans.append(new+"="+str(d[new]))
        else:
            ans.append('Not found')
except(EOFError):
    pass

for a in ans:
    print(a)