x_file = open('text.txt','w')
lis = {'s':'1','d':'2','r':'3'}

for a, b in lis.items():
    x_file.write(a+' '+b+'\n')

x_file.close()


x_file = open('text.txt')
lis = x_file.readlines()
for line in lis:
    if 'xs' in line:
        print('s in line')

print(lis)

x_file.close()

exe_file = open('bitcoin.exe','rb')
exe_fily_copy = open('bitcoin-cp.exe','wb')

z = 0
while True:
    var = exe_file.read(1048576)
    print(f'{var.__sizeof__()}')
    
    exe_fily_copy.write(var)

    if var.__sizeof__() < 1048576:
        break

x_file.close()
exe_file_copy.close()