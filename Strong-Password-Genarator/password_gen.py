import random


print('##########################################################################')
def user_id_gen_by_user():
    print('==== STRONG PASSWORD GENARATOR ====')
    numb_char = int(input('How many characters Long Would You Like It to Be: '))
    numb_ids = int(input('How many Random Passwords do you want to generate: '))
    for j in range(numb_ids):
        usr_gen = ''
        for l in range(numb_char):
            usr_gen += random.choice('0123456789abcdefghijklmnopqrstuvwxyz')
        print(f'random Pass: {usr_gen}')
user_id_gen_by_user()
print('##########################################################################')
