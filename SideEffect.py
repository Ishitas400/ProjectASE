def func_no_side_effects(animals):
    print(f"Animals before change - {animals} id - {id(animals)}")
    animals = animals + ["tiger", "lion"]
    print(f"Animals after change - {animals} id - {id(animals)}")


animal_list = ["tiger", "lion"]
print(f"Animals List before function call - {animal_list} id - {id(animal_list)}")

func_no_side_effects(animal_list)
print(f"Animals List after function call - {animal_list} id - {id(animal_list)}")

str = "tiger", "lion"
result = sorted(str)
print(result)


# snippet to prove function act as an argument and return values
def herbivorous(animal):
    return animal.upper()


def carnivorous(animal):
    return animal.lower()


def omnivorous(func):
    # storing the function in a variable
    omnivorous = func("This is a function passed as an argument.")
    print(omnivorous)


# Passing function as an argument
omnivorous(herbivorous)
omnivorous(carnivorous)


# Closures in python

def extinct( ):
    # variable defined outside the inner function
    name = "Turtles"

    # return a nested anonymous function
    return lambda: "Green " + name


# call the outer function
message = extinct()

# call the inner function
print(message())
