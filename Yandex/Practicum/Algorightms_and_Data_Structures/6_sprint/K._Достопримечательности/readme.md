K. Достопримечательности

Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод

Все языки	0.1 секунда	64Mb	стандартный ввод или input.txt	стандартный вывод или output.txt

Node.js 14.15.5	0.3 секунды	64Mb

OpenJDK Java 11	0.5 секунд	64Mb

C# (MS .NET 6.0 + ASP)	0.3 секунды	64Mb

Python 3.12.1	1.5 секунд	64Mb

Java 21 (Temurin JDK)	0.5 секунд	64Mb

Kotlin 1.8.0 (JRE 11)	0.5 секунд	64Mb

C# (MS .NET 5.0 + ASP)	0.3 секунды	64Mb

Вы приехали на архипелаг Алгосы (наконец-то!). Здесь есть n достопримечательностей. 

Ваша лодка может высадить вас у одной из них, забрать у какой-то другой, 

возможно, той же самой достопримечательности и увезти на материк.

Чтобы более тщательно спланировать свой маршрут,

вы хотите узнать расстояния между каждой парой достопримечательностей Алгосов. 

Некоторые из них соединены мостами, по которым вы можете передвигаться в любую сторону.

Всего мостов m.

Есть вероятность, что карта архипелага устроена так, что нельзя добраться 

от какой-то одной достопримечательности до другой без использования лодки.

Найдите кратчайшие расстояния между всеми парами достопримечательностей.

Формат ввода

В первой строке даны числа n (1 ≤ n ≤ 100) и m (0 ≤ m ≤ n (n-1)/2).

В следующих m строках описаны мосты. 

Каждый мост задаётся номерами двух достопримечательностей 1 ≤ u, v ≤ n 

и длиной дороги 1 ≤ L ≤ 103.

Формат вывода

Выведите матрицу n × n кратчайших расстояний. 

На пересечении i-й строки и j-го столбца должно стоять расстояние 

от i-й до j-й достопримечательности. Если между какой-то парой нет пути,

то в соответствующей клетке поставьте -1.

Пример 1

Ввод	Вывод

4 4

1 2 1

2 3 3

3 4 5

1 4 2

0 1 4 2 

1 0 3 3 

4 3 0 5 

2 3 5 0 

Пример 2

Ввод	Вывод

3 2

1 2 1

1 2 2

0 1 -1 

1 0 -1 

-1 -1 0 

Пример 3

Ввод	Вывод

2 0

0 -1 

-1 0 

