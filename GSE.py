print("                                                    ☢ Silent Professor  ☣️")
print()

from googlesearch import search


data=input("Enter Your Search  :   ")
print()

for i in search(data,12,advanced=True):
    print(i.url)
    print(i.title)
    print(i.description)
    print()
    print()

stop=input(print("                                               ⚙️     Created By Rr Satyamev-Jayate       ⚙️      " ))
