E. Вставка строк

Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод

Все языки	1 секунда	64Mb	стандартный ввод или input.txt	стандартный вывод или output.txt

Swift 5.8.1	0.2 секунды	64Mb

GNU c++17 7.3	0.2 секунды	64Mb

GNU GCC 12.2 C++20	0.2 секунды	64Mb

У Риты была строка s, Гоша подарил ей на 8 марта ещё n других строк ti, 1≤ i≤ n. 

Теперь Рита думает, куда их лучше поставить.

Один из вариантов —– расположить подаренные строки внутри имеющейся строки s, 

поставив строку ti сразу после символа строки s с номером ki

(в частности, если ki=0, то строка вставляется в самое начало s).

Помогите Рите и определите, какая строка получится после вставки в s всех подаренных Гошей строк.

Формат ввода

В первой строке дана строка s. Строка состоит из строчных букв английского алфавита,

не бывает пустой и её длина не превышает 105 символов.

Во второй строке записано количество подаренных строк — натуральное число n, 1 ≤ n ≤ 105.

В каждой из следующих n строк через пробел записаны пары ti и ki.

Строка ti состоит из маленьких латинских букв и не бывает пустой.

ki — целое число, лежащее в диапазоне от 0 до |s|. 

Все числа ki уникальны. Гарантируется, что суммарная длина всех строк ti не превосходит 105.

Формат вывода

Выведите получившуюся в результате вставок строку.

Пример 1

Ввод	Вывод

abacaba

3

queue 2

deque 0

stack 7

dequeabqueueacabastack

Пример 2

Ввод	Вывод

kukareku

2


p 1

q 2

kpuqkareku
