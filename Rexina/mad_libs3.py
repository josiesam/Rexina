name = input('Enter a name: ')
theme = input('Enter party theme: ')
place = input('Enter location: ')
days_of_the_week = ('Enter a day of the week: ')
time = input('Enter the time: ')
verb = input('Enter a verb: ')
animal = input('Enter an animal: ')
body_part = input('Enter a body part: ')
contact_info = input('Enter contact info: ')

sentence = f"{name} is having a {theme} party! it's going to be at {place} on {days_of_the_week} please make sure to show up at {time}, or else you will be required to {verb} a/an {animal} with your {body_part} RSVP at {contact_info}"
print(sentence)