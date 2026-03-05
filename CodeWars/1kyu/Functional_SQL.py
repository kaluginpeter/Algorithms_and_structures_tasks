# In this Kata we are going to mimic the SQL syntax.
#
# To do this, you must implement the query() function. This function returns an object with the following methods:
#
# def select ...
# def from_ ...
# def where ...
# def order_by ...
# def group_by ...
# def having ...
# def execute ...
# The methods are chainable and the query is executed by calling the execute method.
#
# ⚠️ Note: The order of appearance of a clause in a query doesn't matter. However, when it comes time for you to run the query, you MUST execute the clauses in this logical order: from first, then where, then groupBy, then having, then select and finally orderBy.
#
# Of course, you can make queries over object collections:
#
# persons = [
#     {"name": "Peter", "profession": "teacher", "age": 20, "marital_status": "married"},
#     {"name": "Michael", "profession": "teacher", "age": 50, "marital_status": "single"},
#     {"name": "Peter", "profession": "teacher", "age": 20, "marital_status": "married"},
#     {"name": "Anna", "profession": "scientific", "age": 20, "marital_status": "married"},
#     {"name": "Rose", "profession": "scientific", "age": 50, "marital_status": "married"},
#     {"name": "Anna", "profession": "scientific", "age": 20, "marital_status": "single"},
#     {"name": "Anna", "profession": "politician", "age": 50, "marital_status": "married"}
# ]
#
# # SELECT * FROM persons
# query().select().from_(persons).execute()
# # [{"name": "Peter", ...}, {"name": "Michael", ...}]
# You can select some fields:
#
# def profession(person):
#     return person["profession"]
#
# # SELECT profession FROM persons
# query().select(profession).from_(persons).execute() # select receives a function that will be called with the values of the array
# # ["teacher", "teacher", "teacher", "scientific", "scientific", "scientific", "politician"]
# If you repeat a SQL clause (except where() or having()), an exception will be thrown:
#
# query().select().select().execute() # DuplicateSelectError()
# query().select().from_([]).select().execute() # DuplicateSelectError()
# query().select().from_([]).from_([]).execute() # DuplicateFromError()
# query().select().from_([]).where().where() # This is an AND filter (see below)
# You can omit any SQL clause:
#
# numbers = [1, 2, 3]
#
# query().select().execute() # []
# query().from_(numbers).execute() # [1, 2, 3]
# query().execute() # []
# You can apply filters:
#
# def is_teacher(person):
#     return person["profession"] == "teacher"
#
# # SELECT profession FROM persons WHERE profession="teacher"
# query().select(profession).from_(persons).where(is_teacher).execute()
# # ["teacher", "teacher", "teacher"]
#
# # SELECT * FROM persons WHERE profession="teacher"
# query().select().from_(persons).where(is_teacher).execute()
# # [{"person": "Peter", "profession": "teacher", ...}, ...]
#
# def name(person):
#     return person["name"]
#
# # SELECT name FROM persons WHERE profession="teacher"
# query().select(name).from_(persons).where(is_teacher).execute()
# # ["Peter", "Michael", "Peter"]
# Aggregations are also possible:
#
# # SELECT * FROM persons GROUP BY profession <- Bad in SQL but possible in this kata
# query().select().from_(persons).group_by(profession).execute()
# # [
# #     ["teacher", [
# #         {"name": "Peter", "profession": "teacher", ...},
# #         {"name": "Michael", "profession": "teacher", ...}
# #     ]],
# #     ["scientific", [
# #         {"name": "Anna", "profession": "scientific"},
# #         ...
# #     ]],
# #     ...
# # ]
# You can mix where() with groupBy():
#
# # SELECT * FROM persons WHERE profession='teacher' GROUP BY profession
# query().select().from_(persons).where(is_teacher).group_by(profession).execute()
# Or with select():
#
# def profession_group(group):
#     return group[0]
#
# # SELECT profession FROM persons GROUP BY profession
# query().select(profession_group).from_(persons).group_by(profession).execute()
# # ["teacher", "scientific", "politician"]
# Another example:
#
# def is_even(number):
#     return number % 2 == 0
#
# def parity(number):
#     return "even" if is_even(number) else "odd"
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # SELECT * FROM numbers
# query().select().from_(numbers).execute()
# # [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # SELECT * FROM numbers GROUP BY parity
# query().select().from_(numbers).group_by(parity).execute()
# # [["odd", [1, 3, 5, 7, 9]], ["even", [2, 4, 6, 8]]]
# Multilevel grouping:
#
# def is_prime(number):
#     if number < 2:
#         return False
#
#     divisor = 2
#
#     while number % divisor != 0:
#         divisor += 1
#
#     return divisor == number
#
# def prime(number):
#     return "prime" if is_prime(number) else "divisible"
#
# # SELECT * FROM numbers GROUP BY parity, is_prime
# query().select().from_(numbers).group_by(parity, prime).execute()
# # [["odd", [["divisible", [1, 9]], ["prime", [3, 5, 7]]]], ["even", [["prime", [2]], ["divisible", [4, 6, 8]]]]]
# orderBy should be called after groupBy, so the values passed to orderBy function are the grouped results by the groupBy function.
#
# Filter groups with having():
#
# def odd(group):
#     return group[0] == "odd"
#
# # SELECT * FROM numbers GROUP BY parity HAVING odd(number) = true <- I know, this is not a valid SQL statement, but you can understand what I am doing
# query().select().from_(numbers).group_by(parity).having(odd).execute()
# # [["odd", [1, 3, 5, 7, 9]]]
# You can order the results:
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# def descendent_compare(number1, number2):
#     return number2 - number1
#
# # SELECT * FROM numbers ORDER BY value DESC
# query().select().from_(numbers).order_by(descendent_compare).execute()
# # [9, 8, 7, 6, 5, 4, 3, 2, 1]
# from() supports multiple collections:
#
# teachers = [
#   {
#     "teacher_id": "1",
#     "teacher_name": "Peter"
#   },
#   {
#     "teacher_id": "2",
#     "teacher_name": "Anna"
#   }
# ]
#
#
# students = [
#   {
#     "student_name": "Michael",
#     "tutor": "1"
#   },
#   {
#     "student_name": "Rose",
#     "tutor": "2"
#   }
# ]
#
# def teacher_join(join):
#     return join[0]["teacher_id"] == join[1]["tutor"]
#
# def student(join):
#     return {"student_name": join[1]["student_name"], "teacher_name": join[0]["teacher_name"]}
#
# # SELECT student_name, teacher_name FROM teachers, students WHERE teachers.teacher_id = students.tutor
# query().select(student).from_(teachers, students).where(teacher_join).execute()
# # [{"student_name": "Michael", "teacher_name": "Peter"}, {"student_name": "Rose", "teacher_name": "Anna"}]
# Finally, where() and having() admit multiple AND and OR filters:
#
# def tutor1(join):
#     return join[1]["tutor"] == "1"
#
# # SELECT student_name, teacher_name FROM teachers, students WHERE teachers.teacher_id = students.tutor AND tutor = 1
# query().select(student).from_(teachers, students).where(teacher_join).where(tutor1).execute()
# # [{"student_name": "Michael", "teacher_name": "Peter"}] <- AND filter
#
# numbers = [1, 2, 3, 4, 5, 7]
#
# def less_than_3(number):
#     return number < 3
#
# def greater_than_4(number):
#     return number > 4
#
# # SELECT * FROM number WHERE number < 3 OR number > 4
# query().select().from_(numbers).where(less_than_3, greater_than_4).execute()
# # [1, 2, 5, 7] <- OR filter
#
# numbers = [1, 2, 1, 3, 5, 6, 1, 2, 5, 6]
#
# def greater_than_1(group):
#     return len(group[1]) > 1
#
# def is_pair(group):
#     return group[0] % 2 == 0
#
# def val(value):
#     return value
#
# def frequency(group):
#     return {"value": group[0], "frequency": len(group[1])}
#
# # SELECT number, count(number) FROM numbers GROUP BY number HAVING count(number) > 1 AND is_pair(number)
# query().select(frequency).from_(numbers).group_by(val).having(greater_than_1).having(is_pair).execute()
# # [{"value": 2, "frequency": 2}, {"value": 6, "frequency": 2}])
# Requirements Recap
# Clause	⚠️ Must be executed...	Arg(s) Count	Arg Type	Repeatable?
# from	First	1 or More (=> cartesian product of specified tables)	Table(s) (i.e., arrays)	No
# where	Second	1 or More (=> to be logically OR'd)	Functions	Yes (each repetition is a logical AND)
# groupBy	Third	1 or More (=> groups by the 1st fn, then, within each subgroup, groups by the 2nd fn, ...)	Functions	No
# having	Fourth	1 or More (=> to be logically OR'd)	Functions	Yes (each repetition is a logical AND)
# select	Fifth	0 (selects everything) or 1	Function	No
# orderBy	Last	1	Function	No
# execute	-	None (just executes the entire query)	-	-
# If any of the unrepeatable clauses are repeated in the query, your solution MUST raise an Error object with the error message "duplicate " followed by the name of the duplicated clause. If the clause is multi-word, merge it into one (ex: groupby).
#
# For example, if the groupBy clause is duplicated, you should throw an Error with the exact string message "duplicate groupby" (capitalization doesn't matter).
# For Python, there are Exception classes preloaded to use for this purpose; DuplicateFromError, DuplicateSelectError, DuplicateGroupByError, and DuplicateOrderByError. You do not need to provide a message to these classes.
#
# Functional ProgrammingAlgorithms
# Solution
from preloaded import DuplicateFromError, DuplicateSelectError, DuplicateGroupByError, DuplicateOrderByError
from functools import cmp_to_key


def group_by(data, fns):
    if not fns:
        return data

    fn = fns[0]
    groups = {}

    for item in data:
        key = fn(item)
        groups.setdefault(key, []).append(item)

    rest = fns[1:]

    result = []
    for key, values in groups.items():
        result.append([key, group_by(values, rest)])

    return result


class Query:

    def __init__(self):
        self.data = []
        self.select_fn = None
        self.where_groups = []
        self.group_fns = None
        self.having_groups = []
        self.order_fn = None
        self.called = {}

    def select(self, fn=None):
        if self.called.get("select"):
            raise DuplicateSelectError()

        self.called["select"] = True
        self.select_fn = fn
        return self

    def from_(self, data=None, join_data=None):
        if self.called.get("from"):
            raise DuplicateFromError()

        self.called["from"] = True

        if data is None:
            self.data = []
            return self

        if join_data is None:
            self.data = list(data)
            return self

        joined = []
        for a in data:
            for b in join_data:
                joined.append([a, b])

        self.data = joined
        return self

    def where(self, *fns):
        self.where_groups.append(fns)
        return self

    def group_by(self, *fns):
        if self.called.get("group_by"):
            raise DuplicateGroupByError()

        self.called["group_by"] = True
        self.group_fns = fns
        return self

    def having(self, *fns):
        self.having_groups.append(fns)
        return self

    def order_by(self, fn):
        if self.called.get("order_by"):
            raise DuplicateOrderByError()

        self.called["order_by"] = True
        self.order_fn = fn
        return self

    def apply_where(self, data):
        if not self.where_groups:
            return data

        result = []

        for row in data:
            valid = True
            for group in self.where_groups:
                if not any(fn(row) for fn in group):
                    valid = False
                    break
            if valid:
                result.append(row)

        return result

    def apply_having(self, data):
        if not self.having_groups:
            return data

        result = []

        for row in data:
            valid = True
            for group in self.having_groups:
                if not any(fn(row) for fn in group):
                    valid = False
                    break
            if valid:
                result.append(row)

        return result

    def execute(self):

        result = list(self.data)

        if not result and "from" not in self.called:
            return []

        result = self.apply_where(result)

        if self.group_fns:
            result = group_by(result, self.group_fns)
            result = self.apply_having(result)

        if self.select_fn:
            result = list(map(self.select_fn, result))

        if self.order_fn:
            result = sorted(result, key=cmp_to_key(self.order_fn))

        return result


def query():
    return Query()