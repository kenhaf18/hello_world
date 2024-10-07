#4-1
pizza = ['pepperoni', 'cheese', 'meat lovers']
for pizza in pizza:
    print(f"I think {pizza.title()} pizza is the best pizza.")
    print(f"I love my {pizza.title()} pizza.\n")
print("Pizza is great!")

#4-2
animal = ['cheeta', 'leopard', 'panther']
for animal in animal:
    print(f"I think a {animal.title()} would make a great pet.\n")
print("All of these animals are super exciting and would make a great pet!")

#4-3
for x in range(1, 21):
    print(x)

#8-1 
def display_message(message):
    print(f"I am learning so much in the chapter about calling messages.")
display_message('message')

#8-2
def favorite_book(book):
    print(f"One of my favorite books is {book.title()}")
favorite_book('the oxygen theif')

#8-3

def make_shirt(size, message):
    print("\nI'm going to make a " + size + " t-shirt.")
    print('My shirt will say, "' + message + '"')

make_shirt('large', 'Coding is cool')
make_shirt(message="I LOVE COLLEGE", size='small')

#8-4
def make_shirt(size='large', message='I love Python!'):
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Coding takes a while\n')

#8-5
def describe_city(city, country='The United States'):
    location = city.title() + " is in " + country.title() + ".\n"
    print(location)

describe_city('New York City')
describe_city('Los Angeles')
describe_city('Rome','Italy')

#8-6
def city_country(city, country):
    return(city.title() + ", " + country.title())

city = city_country('New Orleans' , 'United States')
print(city)

city = city_country('Rome' , 'Italy')
print(city)

city = city_country('Toronto' , 'Canada')
print(city)

#8-7
def make_album(artist, title):
    album_dict = {'artist': artist.title(),'title': title.title(),}
    return album_dict
album = make_album('Radiohead' , 'The Bends')
print(album)

album = make_album('Fiona Apple' , 'When the Pawn...')
print(album)

album = make_album('Elliot Smith' , 'Either/Or')
print(album)