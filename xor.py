def x_o_r(byte1, byte2, byte3): 
    return hex(byte1 ^ byte2 ^byte3)
f1 = open("p1.txt", "r")
str1 = f1.read()#get p1
f2 = open("c1.txt", "r")
str2 = f2.read()#get c1
f3 = open("c2.txt", "r")
str3 = f3.read()#get c2
num1 = int(str1, 16)
num2 = int(str2, 16)
num3 = int(str3, 16)
print(x_o_r(num1, num2, num3)[2:])#xor