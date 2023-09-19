import string
import random
import tqdm

Alphabets = [x for x in string.ascii_uppercase]
alphabets = [x for x in string.ascii_lowercase]
Numbers = [x for x in string.digits]
Special = [x for x in string.punctuation]

list = [Alphabets, alphabets, Numbers, Special]

def generate():
    pas = [Alphabets, Numbers, Special]
    for a0 in range(9):
        pas.append(random.choice(list))
    random.shuffle(pas)
    password = ""
    for v in pas:
        #print(v, 4)
        password += random.choice(v)
    #print(password)
    return password
    
#generate()
#print(Alphabets, Numbers, Special)
#print(Special, alphabets)
passwords = [generate() for i in tqdm.tqdm(range(100000000))]
#print(passwords)
if len(set(passwords)) != 100000000:
    print("lorduu")

