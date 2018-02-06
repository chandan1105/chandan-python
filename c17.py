#using numeric operator
e=int(input("enter real part ="))
f=int(input("enter imaginary part ="))
g=complex(e,f)
print(g)

#using list
l=[0,3,4,"python",6,8,3,9]
print(l[2])
print(l[3][0])
l[2]=200
print(l)

#using string
a="python"
print(a)
print(a[2])
print(a[0:3])

#using tuples
t=(1,2,3,4,5,6,7,8)
print(t)

#using dictionary
d={1:200,2:400,"pi":314}
print(d[2])
print(d["pi"])

#using set
s1={2,2,3,4,4,5,7,}
s2={6,4,8,9,10,40}
print(s1)
print(s2)
print(s1&s2)
print(s1|s2)
print(s1^s2)
print(s1-s2)

#using boolean operator
print(2==2)
print(2!=2)
#using bitwise
a=12345
b=23457
print(a&b)
print(a|b)
print(a^b)
print(2<<1)
