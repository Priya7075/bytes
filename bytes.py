# y=b"python"
# print(y,type(y))# b 'pyhon' bytes
# print(list(y))#[112,121,116,104,111,110]
# print(tuple(y))#(112,121,116,104,111,110)
# print(set(y))#{104,111,121,116,110, 112}
# y=b"python"
# for i in y:
    # # print(i)
# print(ord('p'))#112
# print(chr(80))    #p
# y=b"python"
# y[0]=80 #TypeError:'bytes' object does not support item assignment
# v=b'[1,2,3]'
# print(list(v))#[91, 49, 44, 50, 44, 51, 93]
# print(ord('['))#91
# print(ord(','))#44
# print(chr(91))#[
m=bytearray(b"python")
print(m)
print(m[0]) 
m[0]=80
print(m)   
         