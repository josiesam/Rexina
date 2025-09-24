loop = int(input("How many times to you want to play: "))

for i in range(loop):

    name = input("Enter a name: ")
    theme = input("Enter a theme: ")
    place = input("Enter a place: ")
    day_of_the_week = input("Enter a day of the week: ")
    time = input("Enter a time: ")
    verb = input("Enter a verb: ")
    animal = input("Enter a animal: ")
    body_part = input("Enter a body part: ")
    contact_info = input("Enter a contact info: ")


    line1 = f"{name} is having a/an"
    line2 = f"{theme} party!"
    line3 = f"It's going to be at {place}"
    line4 = f"on {day_of_the_week}."
    line5 = f"Please make sure to show up at"
    line6 = f"{time}, or else"
    line7 = f"you will be required to"
    line8 = f"{verb} a/an {animal}"
    line9 = f"with your {body_part}."
    line10 = f"RSVP at {contact_info}."

    print()
    print()
    print(f"{line1:^50}")
    print(f"{line2:^50}")
    print(f"{line3:^50}")
    print(f"{line4:^50}")
    print(f"{line5:^50}")
    print(f"{line6:^50}")
    print(f"{line7:^50}")
    print(f"{line8:^50}")
    print(f"{line9:^50}")
    print(f"{line10:^50}")
    print()
    print()