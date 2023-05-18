import logging


class Coffee:
    has_milk = False
    has_sugar = False
    is_hot = False
    has_whole_beans = True


class Beans:
    ground = False


class Water:
    is_boiling = False


# Starting here
def main():
    print("Starting coffee machine...")
    beans = Beans()
    water = Water()

    coffee = brew_coffee(beans, water, add_sugar=True, add_milk=True)

    print("*Pretend this took a while...*")

    print("Your coffee is ready!")
    print("It is " + ("hot" if coffee.is_hot else "cold") + ",")
    print("it has " + ("milk" if coffee.has_milk else "no milk") + ",")
    print("It has " + ("sugar" if coffee.has_sugar else "no sugar") + ",")
    print("and " + ("there are whole beans floating in it... That is not really a coffee..." if coffee.has_whole_beans else "it smells delicious."))


def brew_coffee(beans, water, add_sugar=False, add_milk=False):
    coffee = Coffee

    beans = grind_beans(beans)
    logging.warning("Beans ground: " + str(beans.ground))

    water = boil_water(water)
    logging.warning("Water boiling: " + str(water.is_boiling))

    if add_milk:
        coffee = pour_milk(coffee)
    logging.warning("Coffee has milk: " + str(coffee.has_milk))

    if add_sugar:
        coffee = pour_sugar(coffee)
    logging.warning("Coffee has sugar: " + str(coffee.has_sugar))

    coffee.is_hot = water.is_boiling  # coffee is hot if water is boiling
    coffee.has_whole_beans = not beans.ground   # coffee has whole beans if beans are not ground

    return coffee


# While these methods do basically nothing here,
# in a real-world scenario they could represent thousands of lines of code.
# Try replacing some of the following "True"s with "False"s to see what happens.
# (aka, simulate a bug)


def grind_beans(beans):
    beans.ground = True
    return beans


def boil_water(water):
    water.is_boiling = True
    return water


def pour_milk(coffee):
    coffee.has_milk = True
    return coffee


def pour_sugar(coffee):
    coffee.has_sugar = True
    return coffee


# This is here just to start the whole thing
if __name__ == "__main__":
    main()
