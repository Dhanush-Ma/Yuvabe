import json

def formatMessage(name: str, age: int):
    return f"Hello {name}, you are {age} years old"


formatedMessage = formatMessage("Jane Doe", 44)

print(formatedMessage)

# scopes
# global
num = 20

def loaclscopeFn():
    # loacl
    num = 10
    print(num)

def globalScope():
    # loacl
    global num
    num = 60
    print(num)

globalScope()
loaclscopeFn()
print(num)


# exception handling
try: 
    num = 9/8
    print(num)
except Exception as e: 
    print(e)



