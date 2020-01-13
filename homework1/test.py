import random


domain = 5

uniques = {}
i = 0
isFull = False
while not isFull:
    randvalue = random.randint(1, domain)
    i += 1
    # print(len(uniques.keys()))
    if len(uniques.keys()) == domain:
        isFull = True
        # print(uniques[str(randvalue)])
    uniques.update({str(randvalue): randvalue})
