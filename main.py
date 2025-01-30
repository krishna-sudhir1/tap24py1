h = "hello"
w = "world"

print(h,w)
n1 = 5

#typecast
print(h+str(n1))

n2 = 3
res = n1 + n2
out = f"{n1} + {n2} = {n1 + n2}"
print(out)


if n1 < n2:
    print("Lesser")
    print("<"*6)
elif n1 == n2:
    print("Equal")
    print('=====')
else:
    print("Greater")
    print(">"*len("Greater"))

f = 17.3
print(type(f))