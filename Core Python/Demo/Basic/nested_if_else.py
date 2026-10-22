gender=input('Enter gender(F/M):')
age=int(input('Enter age:'))

if(gender == 'M'):
    if(age >= 21):
        print('Boy elligible for marriage.')
    else:
        print('Boy is not elligible for marriage.')
else:
    if(age >= 18):
        print('Girl is elligible for marriage.')
    else:
        print('Girl is not elligible marriage.')



