import random

x = random.random()               # give the random number in between o to 1.
print(x)

int_random = random.randint(1,50)            # give the radom number in between given range 50 is also include
print(int_random)
# e.g
discount = 5000 * int_random/100
print(discount)

y = random.randrange(0,100,5)
print("y",y)

names = ["rajat", "santosh", "mahesh", "gopal", "pramod"]
last_name = ["singh", "reddy", "pawar", "raut"]
domains = ["@gmail.com", "@rediffmail.com", "@yahoo.com"]

random_name = random.choice(names)
print(random_name)

for _ in range(1,101):
    print(f"{random.choice(names)}.{random.choice(last_name)}{random.choice(domains)}")

cards = [1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13]

random.shuffle(cards)
print(cards)

# e.g
captch_codes = ["A", "8", "l", "h", "2", "R"]
for i in range(1,11):
    random.shuffle(captch_codes)
    print("".join(captch_codes))

card_set1 = random.choices(cards, k=5)
print(card_set1)
card_set2 = random.choices(cards, k=10)
print(card_set2)
card_set3 = random.choices(cards, k=13)
print(card_set3)



