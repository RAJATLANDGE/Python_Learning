# nested loop


i = 1
while i < 11:
    j = 1
    while j < 11:
        print(f"{i} * {j}   = {i*j}")
        j+=1
    print(" ")
    i+=1

games = ["cricket", "vollyball", "basketball"]
persons = ["rahul", "saurabh", "manoj"]

for game in games:
    for person in persons:
        print(f" {game} for {person}")



for i in range(1,11):
    for j in range(1,11):
        print(f"{i}   *   {j} = {i*j}")
    print(" ")


print("------------------------------")
# pass, break, continue
# break = break inner most loop

for i in range(1,11):
    for j in range(1,11):
        print(f"{i}   *   {j} = {i * j}")
        if j%5==0:
            break
    print(" ")
    if i%3==0:
        break


# continue

for i in range(1,11):
    for j in range(1,11):
        if j%5==0:
            continue
        print(f"{i}  *  {j} = {i*j}")
    print(" ")


# pass
# uses for pass to skip blog
if 5<9:
    print("------")
    pass
    print("------")
    print("------")