# - So!, shouted boss, heading to Tim's office, We have new contract!
# - What is it? - ask Tim.
# - Do not know, frankly, it's secret! It's from army! - boss was obviously excited.
# - So how are we supposed to write anything, if it is so big secret?
# - And that's the point! We won't know it, but we will write it. We have to prepare mechanism to create dynamic classes with properties and methods given as a parameters. - explained boss.
# - I don't think that's, umm... But would we at least know names of these properties and methods, right?
# - No. Remember that it's secret, so we'll not know anything!
# - Nah, it's impossible! - cried Tim.
#
# Then Tims went to find you - his almighty guru - and ask to help him. You reminded him:
# - It's Python, here everything is possible! Ok, let's see....
#
# So, in that Kata, your task is to finish function create_class that will get some class name and secret dictionary and make class of it. That dictionary will be delivered by function army_get_secret_from_file() which is already completed.
# Tim also asked you to make sure that if class name is empty, it should be None as result, and to make possible to call function without second parameter.
#
# Do not worry, these test properties and methods are dummy, so you won't know the army's mysteries, so you (probably) won't be executed.
#
#
#
# Check also previous: Python's Dynamic Classes #1 Kata and Python's Dynamic Classes #2 Kata.
#
# FundamentalsObject-oriented Programming
# Solution
from typing import Type

def create_class(class_name: str, secrets: dict = None) -> Type:
    if not class_name or not isinstance(class_name, str): return None
    if secrets is None: secrets = dict()
    return type(class_name, (), secrets)