x = int(input("Введите число "))
if x==4:
    print("x>0 and y<0")
elif x==1:
    print("x>0 and y>0")
elif x==3:
    print("x<0 and y<0")
elif x==2:
    print("x<0 and y>0")
else:
    if x>4 or x<0:
        print("Такого диапозона нет")  

    