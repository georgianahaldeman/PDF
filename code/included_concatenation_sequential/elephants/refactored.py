# "One Little Elephant" nursery rhyme

def verse_one():
    print("One little elephant went out to play,")
    print("Upon a spider's web one day.")
    print("He had such enormous fun,")
    print("That he called for another elephant to come!\n")

def verse_multiple(count_str):
    print(f"{count_str.capitalize()} little elephants went out to play,")
    print("Upon a spider's web one day.")
    print("They had such enormous fun,")
    print("That they called for another elephant to come!\n")


# Call all verses
verse_one()
verse_multiple("two")
verse_multiple("three")
verse_multiple("four")
verse_multiple("five")