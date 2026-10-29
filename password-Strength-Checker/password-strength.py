# This Is The First ever Project I've Done On My Own, So Far im 10 Days into 30 Days Of Python Wish me luck 
print('--PASSWORD STRENGTH CHECKER--')

score = 0 
usr_pass = input('Password: ')
if len(usr_pass) >= 8:
    score += 5
    print('✅Password Is Atleast 8 Characters Long✅')
else:
    print('❗Password Needs To Be Atleast 8 Characters Long❗')

if any(char.isdigit() for char in usr_pass):
    score += 5
    print('✅Password Has Numbers✅')
else:
    print('❗password Has No Numbers❗')

special = ['!', '@','#','$','%','^','&','*','(',')','-','_','~','`',':',';','/','?']
if any(char in special for char in usr_pass):
    score += 5
    print('✅Password Has Special Characters✅')
else:
    print('❗Password Has No Special Characters❗')

if any(char.isupper() for char in usr_pass):
    score += 5
    print('✅ Password has upper Case letters✅')
else: 
    print('❗Password Has No Upper Case Letters❗')

if any(char.islower() for char in usr_pass):
    score += 5
    print('✅Password Has Lower Case Letters✅')
else: 
    print('❗Password Has No Lower Case Letters❗')

if score == 5:
    print(f'🚨BAD PASSWORD')
elif score == 10:
    print(f'⚠️WEAK PASSWORD')
elif score == 15:
    print(f'⚖️MEDIUM PASSWORD')
elif score == 20:
    print(f'👍GOOD PASSWORD')
else:
    print(f'💪STRONG PASSWORD')

print(f'🏆YOUR FINAL SCORE IS {score}/25')

# First Project successful, or atleast i think so