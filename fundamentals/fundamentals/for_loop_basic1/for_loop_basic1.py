print("BASICS: ")
for i in range(0, 151):
    print(i)


print("MULTIPLES OF 5: ")
for i in range(5, 1001, 5):
    print(i)


print("COUNTING THE DOJO WAY: ")
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
        continue
    elif i % 5 == 0:
        print("Coding")
        continue
    print(i)
    

print("WHOA, THAT SUCKER'S HUGE: ")
sum = 0
for x in range(500000):
    if x % 2 != 0:
        sum += x

print(sum)

print("COUNTDOWN BY FOURS: ")
for i in range(2018, 0, -4):
    print(i)

print("FLEXIBLE COUNTER: ")
lowNum = 0
highNum = 40
mult = 6
for i in range(lowNum, highNum):
    if i % mult == 0:
        print(i)