try:
    text = input('Enter your text: ')
    count = text.split()
    res = len(count)
    print(f'There are {res} words in text.')
except TypeError:
    print('Please enter a valid text.(str)')