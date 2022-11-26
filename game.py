<<<<<<< HEAD
import numpy as np
number = np.random.randint(1, 101)
count = 0
=======
#***Игра "Угадай число"*** 

import game as np
number = np.random.randint(1, 101) #загадываем число 
count = 0 #количество попыток
>>>>>>> master

while True:
    count+=1
    predict_number = int(input('Угадай число от 1 до 100: '))
    
    if predict_number > number:
        print('Число должно быть меньше!')
    
    elif predict_number < number:
        print('Число должно быть больше!')
        
    else:
        print(f'Вы угадали число!Это число - {number}, за {count} попыток')
<<<<<<< HEAD
        break #конец игры, завершение цикла
    
    
=======
        break #конец игры, завершение цикла
>>>>>>> master
