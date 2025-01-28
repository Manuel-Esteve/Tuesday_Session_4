s1 = "hello world!"
print(s1)
print(s1[0], s1[1], s1[2])
print(s1[4], s1[7]) # print both o-s
print(s1[11], s1[-1]) #print the last one
print(s1[-2])

print(s1[14//2]) # double slash to make integer
s1 = "hello"
s2 = "world"
print(s1+ " " + s2 + "!")

#if operations:
if "bob":
    print("bob is")
else:
    print("bob isn't")

if "" :
    print("empty String is true")
if "" :
    print("empty String is false")

s = "abcdefghijklmnop"
print(len(s))
# we can iterate over a string and get each character!!
for character in s:
    print(character, end=" ")
print()
i = 0
while i < len(s):
    print(s[len(s) - i - 1], end= " ")
    i += 1

# slide is fancy index
s = "0123456789"
print(s)
print(s[2:3]) #2
print(s[4:6]) #45
print(s[:3]) # 012
print(s[3:]) # 3456789
print(s[1:7:2]) # 135
print(s[::-1])
print(s[::-2])

