import random
print('###################################################################################################################')
print("\n---------------------ROCK PAPER SCISSORS---------------------")
a = ('Rock','rock')
b = ('scissors', 'scissor', 'Scissor', 'Scissors')
c = ('paper', 'Paper')

r = '🗿'
s =  '✂️'
pp = '📄'
while True:
    i =input('\n(Type "quit" To Exit) \nRock Paper Scissor: ')
    if i == 'quit':
        print('Succesfully Quit')
        break
    if i in a:
        p = print(f'You Picked: {r} {i} {r}')
    elif i in b:
        p = print(f'You Picked: {s} {i} {s}')
    elif i in c:
        p = print(f'You Picked: {pp} {i} {pp}')
    else:
        print('Invaild Choice')
        print('Retry')
        continue
    k = ['🗿Rock🗿', '📄Paper📄', '✂️Scissor✂️']
    u = random.choice(k)
    print(f'I Picked: {u}')
    if u == '🗿Rock🗿' and i in b:
        print('❌I Won Easy❌')
    elif u == '🗿Rock🗿' and i in c:
        print('🎉You Won🎉')
    elif u == '🗿Rock🗿' and i in a:
        print('🟰  Draw, Fair Game  🟰')
    elif u == '✂️Scissor✂️' and i in c:
        print('❌I Won Easy❌')
    elif u =='✂️Scissor✂️' and i in b:
        print('🟰  Draw, Fair Game  🟰')
    elif u == '✂️Scissor✂️' and i in a:
        print('🎉You Won🎉')
    elif u == '📄Paper📄' and i in a:
        print('❌I Won Easy❌')
    elif u == '📄Paper📄' and i in b:
        print('🎉You Won🎉')
    elif u == '📄Paper📄'and i in c:
        print('🟰  Draw, Fair Game 🟰')
    break

print('###################################################################################################################')
