# This program demonstrates polymorphism.

import f_animals as animals

def main():
    # Create a Mammal object, a Dog object, and
    # a Cat object.
    mammal = animals.Mammal('regular animal')
    dog = animals.Dog()
    cat = animals.Cat()


    # Display information about each one.
    print('Here are some animals and')
    print('the sounds they make.')
    print('--------------------------')
    show_mammal_info(mammal)
    print()
    show_dog_info(dog)
    print()
    show_cat_info(cat)
    print()

def show_mammal_info(obj):
    if isinstance(obj, animals.Mammal):

        obj.show_species()
        obj.make_sound()
    else:
        print(f"{obj} does not belong ot the Mammal class object.")

def show_dog_info(obj):
    obj.show_species()
    obj.make_sound()

def show_cat_info(obj):
    obj.show_species()
    obj.make_sound()

# Call the main function.
main()


