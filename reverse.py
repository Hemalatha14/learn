n=int(input("enter num"))
m=int(n)
rev =0
while(n>0):
  reminder = n%10
  rev = (rev*10) + reminder
  n = n //10
def add(a,b):
  return a+b
print(m,"+",rev,"=",add(m,rev))
