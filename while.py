n=1
a = [ ]
while n:
    print("enter a number")
    n=int(input () )
    if n%2==0:
        a.append(n)

print("your list is",list (set(a)))
    
