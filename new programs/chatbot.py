#Creating first chatbot

bot_name: str = 'Maya'
print(f'Hi I am {bot_name}. How may I assist you today?')

while True:
    user_input: str = input('You :').lower()

if  user_input in ['hi', 'hello']:
    print(f{bot_name}':Hello there, let me know may I help you')
elif  user_input in ['bye', 'goodbye']:
    print(f'Goodbye, Have a nice day')
elif  user_input in ('hi', 'hello'):
    print(f'Hello there, let me know may I help you')






