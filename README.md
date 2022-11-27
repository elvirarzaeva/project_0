# Проект 0. Угадай число

## Оглавление  
[1. Описание проекта](.README.md#Описание-проекта)  
[2. Какой кейс решаем?](.README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](.README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](.README.md#Этапы-работы-над-проектом)  
[5. Результат](.README.md#Результат)    
[6. Выводы](.README.md#Выводы) 

### Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up:[к оглавлению](_)


### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**     
Учимся писать хороший код на python


### Краткая информация о данных
Числа в диапазоне от 1 до 100
Применение цикла while
применение метода бинарного поиска
  
:arrow_up:[к оглавлению](.README.md#Оглавление)


### Этапы работы над проектом  
Используем метод бинарного (двоичного) поиска для того, чтобы алгоритм выполнял поиск числа меньше чем за 20 попыток. В цикле while находим среднее значение и сравниваем его с искомым числом. Число найдено, когда среднее значение равно загаданному числу. Прерываем цикл

:arrow_up:[к оглавлению](.README.md#Оглавление)


### Результаты:  
Алгоритм угадывает число в среднем за 101 попытку. При использовании метода бинарного поиска, число попыток не превышает 20.   

:arrow_up:[к оглавлению](.README.md#Оглавление)


### Выводы:  
Оба алгорита успешно выполняют работу

:arrow_up:[к оглавлению](.README.md#Оглавление)
