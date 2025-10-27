'''
1.
1.You are building a billing system where you need a function `calculate_total(price, quantity)` that returns the total price. How would you design the function to accept only positional arguments?

'''
def calculate_total(price, quantity, /):
    return price * quantity
print(calculate_total(10,2))
# print(calculate_total(price=10, quantity=2))


'''
2.2. In a video game, players can choose their character's weapon. If no weapon is selected, the default should be "Sword". 
- Write a function `choose_weapon(player_name, weapon="Sword")`.  
- What happens if a player does not specify the weapon?
'''

def choose_weapon(player_name, weapon='sword'):
    print(f'Name: {player_name} chosen weapon: {weapon}')
choose_weapon('sam','gun')
choose_weapon('sam')

'''
3.
3. You are creating a report generator. A function `generate_report(title, author, date)` must allow passing arguments out of order for flexibility. How would you call the function using keyword arguments so that `date` is passed first, then `title`, then `author`?
'''
def generate_report(title, author, date):
    print(f'Title:{title}\nAuthor:{author}\nDate:{date}')
print(generate_report(date='2025-10-21', title='Python Assignment', author='Sameera'))

'''
4.
4. You're building a restaurant app where customers can order multiple dishes. You need a function `order_food(*dishes)` that can accept any number of dish names. How would you design the function so it prints all the dishes ordered, regardless of how many are passed?
'''

def order_food(*dishes):
    print('Dishes Ordered')
    i = 1
    for dish in dishes:
        print(f'{i}.{dish}')
        i = i + 1

order_food('Burger', 'Pizza')
order_food('Pizza', 'Burger', 'rice', 'dal')

'''
5. 
5. In a movie booking system, you want a function `book_ticket(details)` that accepts various information like `name`, `movie`, `seats`, `show_time`, etc. How can you design the function to accept different types of details and display them?
'''
def book_ticket(**details):
    for key, value in details.items():
        print(f'{key}:{value}')
print(book_ticket(name='Sameera', movie='xyz', seats=2, show_time='11:15'))
