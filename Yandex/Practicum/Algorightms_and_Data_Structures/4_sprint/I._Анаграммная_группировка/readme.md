I. Анаграммная группировка

Ограничение времени	1 секунда

Ограничение памяти	64Mb

Ввод	стандартный ввод или input.txt

Вывод	стандартный вывод или output.txt

Вася решил избавиться от проблем с произношением и стать певцом.

Он обратился за помощью к логопеду. Тот посоветовал Васе выполнять упражнение, 

которое называется анаграммная группировка. В качестве подготовительного этапа нужно выбрать из множества строк анаграммы.

Анаграммы –— это строки, которые получаются друг из друга перестановкой символов. 

Например, строки «SILENT» и «LISTEN» являются анаграммами.

Помогите Васе найти анаграммы.

Формат ввода

В первой строке записано число n —– количество строк.

Далее в строку через пробел записаны n строк.

n не превосходит 6000. Длина каждой строки не более 100 символов.

Формат вывода

Нужно вывести в отсортированном порядке индексы строк, которые являются анаграммами.

Каждая группа индексов должна быть выведена в отдельной строке. 

Индексы внутри одной группы должны быть отсортированы по возрастанию. 

Группы между собой должны быть отсортированы по возрастанию первого индекса.

Обратите внимание, что группа анаграмм может состоять и из одной строки. 

Например, если в исходном наборе нет анаграмм, то надо вывести n групп, каждая из которых состоит из одного индекса.

Пример

Ввод	Вывод

6

tan eat tea ate nat bat

0 4

1 2 3

5
