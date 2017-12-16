
print ("Madlib Maker\n--------------------")

def repeatRequest():
    repeatLib = input("Do it again (y/n)?: ")
    if repeatRequest != "n":
        main()
        
    else:
        print("Thanks for playing!")
    
def userInputs():
    username = input("Enter a name: ")
    
    #Adjectives for story
    adjective1 = input("Enter an adjective: ")
    adjective2 = input("Enter a second adjective: ")
    adjective3 = input("Enter one more adjective: ")

    #Verbs for the story
    verb1 = input("Enter a verb: ")
    verb2 = input("Enter another verb: ")
    verb3 = input("Enter one more verb: ")

    #nouns for the story
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    noun3 = input("Enter one more noun: ")
    noun4 = input("We really like nouns give us another: ")

    AnimalInput = input("Name an animal as a plural noun: ")
    FoodInput = input("Name your most hated food: ")
    FruitInput = input("A fruit that reminds you of a body part as plural noun:  ")
    NumberInput = input("Enter your favorite number as text: ")
    SuperheroInput = input("What is the nerdiest superhero: ")
    CountryInput = input("Name a country you would never want to visit: ")
    DessertInput = input("Name a dessert that makes you happy: ")
    YearInput = input("What was the best year of your life: ")

    #The template for the story
    print ("Your Madlibs Story")
    print (" ")
    print ("This morning I woke up and felt {1} because {0} was going to finally {4} over the big {2} {7}.\nOn the other side of the {8} were many {11}s protesting to keep {12} in stores.\nThe crowd began to {5} to the rhythm of the {9}, which made all of the {13} very {3}.\n{0} tried to {6} into the sewers and found {14} rats.\nNeeding help, {0} quickly called {15}. {15} appeared and saved {0} by flying to {16} and dropping {0} into a puddle of {17}.\n{0} then fell asleep and woke up in the year {18}, in a world where {10} ruled the world.".format(username,adjective1,adjective2,adjective3,verb1, verb2, verb3, noun1,noun2,noun3,noun4,AnimalInput,FoodInput,FruitInput, NumberInput,SuperheroInput, CountryInput,DessertInput,YearInput))

def main():
    userInputs()
    repeatRequest()
    
main()

