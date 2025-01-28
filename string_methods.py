methods = dir("hi")
useful_methods = []
for method in methods:
    if "__" in method:
        continue
    useful_methods.append(method)
print(useful_methods)

print(help("hi".capitalize)) # get help for whatever method you want
print("cat".capitalize())
s = "i go to school everyday."
print(s.capitalize())

print("HELLO".casefold())
print()
print("hello". center(20, "*"))
print("banananananananana".count("ana"))

print("ana ana banana".find("ana",5)) # 0 because ana is in position 0, or put number do start from there

print("abc".index("b",2))

words = ["i", "like", "to, ""sing"]
print(" ".join(words))

s = "I like to go hiking!"
print(s.replace(" ","! !"))
s = "I like to go hiking!"
# print(s.split())
print(s.replace("!", "").split())
print(s.upper())

print("i like to go skiing".title())