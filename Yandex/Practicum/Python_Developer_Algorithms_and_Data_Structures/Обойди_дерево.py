# Задача «Обойди дерево»
# Прошло несколько поколений после того, как первый человек ступил на Марс.
# При отборе претендентов для марсианских миссий введено правило:
# по генеалогическому древу кандидата подсчитывается,
# сколько времени его предки в совокупности провели на Марсе:
# большой «марсианский семейный стаж» считается преимуществом при отборе.
# Ваша задача — написать метод, который принимает на вход бинарное дерево (генеалогическое древо)
# и возвращает сумму значений space_experience всех узлов этого дерева.
# В прекоде к заданию описано дерево. Каждый узел дерева — это объект класса Spaceman. У этого класса:
# два обязательных атрибута — name и space_experience;
# два опциональных атрибута — father и mother, эти атрибуты заполняются,
# если родители космонавта тоже были космонавтами.
# В коде описан класс DynastyExperienceCounter,
# при его инициализации в конструктор передаётся объект класса Spaceman — космонавт.
# Допишите метод count_dynasty_experience класса DynastyExperienceCounter,
# который посчитает необходимый стаж космонавта и всех его предков.
# Решением должен быть рекурсивный обход дерева:
# в каждом следующем уровне рекурсии должны обрабатываться узлы,
# хранящиеся в атрибутах father и mother текущего узла.
# Solution Breadth First Search Time O(N) Memory O(N)
from __future__ import annotations
from typing import Optional


class Spaceman:

    def __init__(
            self,
            name: str,
            space_experience: int,
            father: Optional[Spaceman] = None,
            mother: Optional[Spaceman] = None,
    ):
        self.name = name
        self.space_experience = space_experience
        self.father = father
        self.mother = mother


class DynastyExperienceCounter:

    def __init__(self, spaceman: Spaceman):
        self.root = spaceman
        self.total_experience: int = 0

    def count_dynasty_experience(self, root=None):
        if not root:
            return 0
        # Доработайте метод, чтобы он считал
        # суммарный опыт династии космонавтов.
        self.total_experience += root.space_experience
        self.count_dynasty_experience(root.father)
        self.count_dynasty_experience(root.mother)
        return self.total_experience

yu_a_makarin = Spaceman(
    name='Юрий Алексеевич Макарин',
    space_experience=10,
    father=Spaceman(
        name='Алексей Михайлович Макарин',
        space_experience=25,
        mother=Spaceman(
            name='Евгения Владимировна Беляева',
            space_experience=1
        )
    ),
    mother=Spaceman('Ангелина Васильевна Черенкова', 5)
)
counter = DynastyExperienceCounter(yu_a_makarin)
result = counter.count_dynasty_experience(counter.root)
print(result)