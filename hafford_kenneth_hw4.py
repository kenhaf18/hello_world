#6-1 
print("\n")
friend = {
    'first_name' : 'fae',
    'last_name' : 'baguyo',
    'age' : '18',
    'city' : 'manhattan'
}
print(friend['first_name'])
print(friend['last_name'])
print(friend['age'])
print(friend['city'])

print("\n")
#6-2
favorite_numbers = {
    'fae' : '4',
    'tyler' : '19', 
    'elijah' : '23',
    'nick' : '12',
}
for friend, number in favorite_numbers.items():
    print(f"{friend.title()}'s favorite number is {number}\n")
#6-3
programming_vocabulary = {
    'mutable' : 'has the ability to change',
    'float' : 'a number that has a decimal',
    'elif' : 'stands for "else-if" ',
    'dictionary' : 'a set of data where you store words and their meanings',
}
key = 'mutable'
print("\n" + key.title() + ": " + programming_vocabulary[key])

key = 'float'
print("\n" + key.title() + ": " + programming_vocabulary[key])

key = 'elif'
print("\n" + key.title() + ": " + programming_vocabulary[key])

key = 'dictionary'
print("\n" + key.title() + ": " + programming_vocabulary[key])
        
#6-4
programming_vocabulary = {
    'mutable' : 'has the ability to change',
    'float' : 'a number that has a decimal',
    'elif' : 'stands for "else-if" ',
    'dictionary' : 'a set of data where you store words and their meanings',
}
for word, meaning in programming_vocabulary.items():
    print(f"\n{word.title()} = {meaning}")

#6-5
rivers = {
    'mississippi': 'united states',
    'amazon' : 'brazil',
    'yellow' : 'china'
}
for river, country in rivers.items():
    print("The " + river.title() + " river runs through " + country.title() + ".")

print("\nThese are the rivers within my dictionary:")
for river in rivers.keys():
    print(river.title())

print("\nThese are the countrys within my dictionary:")
for country in rivers.keys():
    print(country.title())
print("\n")

#6-7
favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }
coders = ['ken', 'james', 'adrianna', 'jen', 'sarah', 'edward', 'phil']
for coder in coders:
    if coder in favorite_languages.keys():
        print(coder.title() + ", thank you for taking the poll")
    else:
        print(coder.title() + ", please tell us what your favorite language is.")

#6-8
pets = []

pet = {
    'animal type': 'linx',
    'name': 'alex',
    'owner': 'ken',
    'weight': 240,
    'eats': 'rabbits',}
pets.append(pet)

pet = {
    'animal type': 'cat',
    'name': 'craig',
    'owner': 'emily',
    'weight': 12,
    'eats': 'fish',}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'lexi',
    'owner': 'lucas',
    'weight': 15,
    'eats': 'homework',}
pets.append(pet)

for pet in pets:
    print("\nThis is everything I know about" + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))

#6-9
favorite_places = {
    'tom' : ['arcade' , 'thirft' , 'carnival'],
    'kat' : ['campus center' , 'dining hall' , 'kitchen'],
    'matt' : ['library' , 'gym' , 'skate park']
}
for name, places in favorite_places.items():
    print("\n" + name.title() + "enjoys to go to these places:")
    for place in places:
        print(place.title())

#6-10
favorite_numbers = {
    'fae' : ['4', '8', '12'],
    'tyler' : ['19', '38', '57'],
    'elijah' : ['23', '46', '69'],
    'nick' : ['12', '24', '48']
}
for friend, number in favorite_numbers.items():
    print(f"{friend.title()}'s favorite number is {number}\n")

#6-11
cities = {
    'new york' : {
        'country' : 'united states',
        'population' : '8.3 million',
        'fact' : 'There are more than 800 languages spoken within new york city'
},
    'los angeles' : {
        'country' : 'united states',
        'population' : '3.8 million',
        'fact' : 'LA is known for the production of many famous movies', 
},
    'dallas' : {
        'country' : 'united states',
        'population' : '1.3 million',
        'fact' : 'Dallas is best known for their large portions of food', 
}
}

for city, city_value in cities.items():
    country = city_value['country'].title()
    population = city_value['population']
    fact = city_value['fact']

    print("\n" + city.title() + " is in " + country + ".")
    print("This city has a population of " + (population) + ".")
    print(fact)