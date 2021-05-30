def Function() :
    with open("ex_test.txt",'r') as a :
        data_a = a.read()
    with open("ex_test2.txt",'r') as b :
        data_b = b.read()
    with open("ex_test.txt",'w') as a :
        a.write(data_b)
    with open("ex_test2.txt",'w') as b :
        b.write(data_a)
Function()

 