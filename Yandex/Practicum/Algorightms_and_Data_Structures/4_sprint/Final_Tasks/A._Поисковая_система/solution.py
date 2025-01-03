# -- ПРИНЦИП РАБОТЫ --
# Алгоритм выполняет поиск по следующему принципу:
#    Создается main_database, которое хранит <слово, <индекс_документа, количество вхождений>>.
#    main_database наполняется каждым словом из гистограммы документа.
#    Далее принимается m запросов:
#        Для запроса создается гистограмма и собирается пул(dict<index_database, freq>) подходящих индексов документов,
#        путем подсчета релевантности по вхождению в документ, слов из запроса.
#        Далее пул сортируется и выводится 5(или меньше) найденных документов.
# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
# Алгоритм корректно обрабатывает документы и запросы, следуя нескольким ключевым шагам:
# 1. Построение базы данных:
#     Для каждого документа создается гистограмма слов и заполняется main_database
# 2. Обработка запросов:
#     Для каждого запроса формируется гистограмма, после чего собираются уникальные индексы документов,
#     содержащие слова из запроса. Релевантность вычисляется с помощью суммирования частоты слов запроса в документах.
# 3. Извлечение результатов:
#     Извлечение до 5 наиболее релевантных документов происходит с использованием сортировки пула.
# Таким образом, алгоритм корректен. ■
# Временная сложность
# 1. Построение базы данных(database и main_database):
#     Суммарное время O(nL), где n — количество документов, а L — средняя длина документа.
# 2. Обработка запросов: O(m(Q + n)), где m — количество запросов, Q — средняя длина запроса, n — количество документов.
# 3. Сортировка пула: O(KlogK), где K размер пула.
# Итоговая временная сложность: O(n * L + m * (Q + n) * KlogK)
# Пространственная сложность
# 1. Хранение базы данных: O(nW), где W — максимальное количество уникальных слов в документе.
# 2. Основная база данных: O(nW) для хранения уникальных слов и индексов документов.
# 3. Хранение пула документов: O(K), где K количество подходящих документов
# Итоговая пространственная сложность: O(nW + K), где W — максимальное количество уникальных слов.

import sys
from collections import Counter


def print_answer(pool: list[tuple[int, int]]) -> None:
    for idx in range(min(5, len(pool))):
        if idx:
            sys.stdout.write(' ')
        sys.stdout.write(str(pool[idx][0] + 1))
    sys.stdout.write('\n')


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    main_database: dict[str, dict[int, int]] = dict()
    for database_idx in range(n):
        sentence: str = sys.stdin.readline().rstrip()
        histogram: dict[str, int] = Counter(sentence.split())
        for word in histogram:
            if word not in main_database:
                main_database[word] = dict()
            main_database[word][database_idx] = histogram[word]

    m: int = int(sys.stdin.readline().rstrip())
    for _ in range(m):
        query: str = sys.stdin.readline().rstrip()
        query_histogram: dict[str, int] = Counter(query.split())
        correct_databases: dict[int, int] = dict()
        for word in query_histogram:
            if word not in main_database:
                continue
            for database_idx, freq in main_database[word].items():
                correct_databases[database_idx] = correct_databases.get(database_idx, 0) + freq
        pool: list[tuple(int, int)] = sorted(correct_databases.items(), key=lambda pair: (-pair[1], pair[0]))
        print_answer(pool)


if __name__ == '__main__':
    solution()