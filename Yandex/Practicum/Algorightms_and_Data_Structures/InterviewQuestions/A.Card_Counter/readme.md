A. Card Counter

Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод

Все языки	0.25 секунд	256Mb	стандартный ввод или input.txt	стандартный вывод или output.txt

Node.js 14.15.5	1 секунда	256Mb

Python 3.7.3	1 секунда	256Mb

OpenJDK Java 11	0.5 секунд	256Mb

C# (MS .NET 6.0 + ASP)	1 секунда	256Mb

OpenJDK Java 15	0.5 секунд	256Mb

Kotlin 1.9.21 (JRE 21)	0.5 секунд	256Mb

C# (MS .NET 5.0 + ASP)	1 секунда	256Mb

На стол в ряд выложены карточки, на каждой карточке написано натуральное число.

За один ход разрешается взять карточку либо с левого, либо с правого конца ряда. 

Всего можно сделать 
k
 ходов. Итоговый счет равен сумме чисел на выбранных карточках.

Определите, какой максимальный счет можно получить по итогам игры.

Вы можете воспользоваться заготовками кода для данной задачи из репозитория курса

Формат ввода

В первой строке записано число карточек 

n
 (
1
≤
n
≤
1
0
5
).


Во второй строке записано число ходов 
k
 (
1
≤
k
≤
n
).

В третьей строке через пробел даны числа, записанные на карточках. 
i -е по счету число записано на 
i
-й слева карточке. Все числа натуральные и не превосходят 
1
0
4
.

Формат вывода

Выведите единственное число —- максимальную сумму очков, которую можно набрать, сделав 
k
 ходов.

Пример 1

Ввод	Вывод

7

3

5 8 2 1 3 4 11

24

Пример 2

Ввод	Вывод

5

5

1 2 3 4 5

15

Пример 3

Ввод	Вывод

7

4

1 1 9 2 2 2 6

17
