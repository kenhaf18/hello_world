#10-1
from pathlib import Path

print("10-1")
print("This is the text file:")
path = Path('learning_python.txt')
learning_python = path.read_text()
print(learning_python)

#10-2
from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
changes = contents.splitlines
for change in changes:
    change = change.replace('python' , 'HTML')
    print(change)

#10-3
from pathlib import Path

path = Path('guest.txt')

name = input("What's your name? ")
path.write_text(name)

#10-4
from pathlib import Path

path = Path('guest_book.txt')

prompt = "\nHi, what's your name? "

guest_names = []
while True:
    name = input(prompt)

    if name == 'stop':
        break

    print(f"Thank you {name}, you are now added to the guest book")
    guest_names.append(name)

#10-6

try:
    x = input("Give me a number: ")
    x = int(x)

    y = input("Give me another number: ")
    y = int(y)
except ValueError:
    print("Please, enter a number")
else:
    sum = x + y
    print(f"{x} + {y} = {sum}.")