
import random
import logging
logging.basicConfig( filename='app.log', filemode='a',level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s') #создание лог-файла

while True: #проверка, что вводится число
    n=input("Введите количество бочонков ")
    try:
        val=int(n)
        if int(n)>0:
            logging.info("Введено количество бочонков: %s ", n)
            break    
        else:
            raise ValueError
    except ValueError:
        logging.error("Введено неверное значение %s", n)
        print("Введено некорректное значение. Попробуйте еще раз!")
n=int(n)
list=[] #создание пустого списка
for i in range(0,n): # заполнение списка числами от 1 до n
    list.append(i+1)
random.shuffle(list) # перемешивает рандомно числа в списке
for i in range (0,n):
    input("Нажмите на клавишу Enter, чтобы узнать номер следующего бочонка...")
    print("Бочонок под номером :")
    print(list[i])
    logging.info("Номер бочонка: %s ", list[i])
input("Нажмите на клавишу Enter, чтобы выйти...")
