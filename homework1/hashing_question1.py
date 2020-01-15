import random
import numpy as np
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# random.seed(2)

def getNumberOfTrials(domain):
    uniques = {}
    i = 0
    collision = False
    while not collision:
        randvalue = random.randint(1, domain)
        i += 1
        if str(randvalue) in uniques.keys():
            collision = True
            # print(uniques[str(randvalue)])
        uniques.update({str(randvalue): randvalue})
    return i


def getTimeElasped(m, n):
    data = pd.DataFrame([], columns=['m', 'n', 'time'])
    for each_m in m:
        for each_n in n:
            startTimer = time.time()
            x_lab = experiment(each_m, each_n)
            endTimer = time.time()
            timeSpent = endTimer - startTimer
            output = pd.DataFrame([[ each_m, each_n, timeSpent]], columns=['m', 'n', 'time'])
            data = data.append(output)
            # print(output)
    return data


def experiment(m, n):
    x_labels = []
    for each in range(m):
        x = getNumberOfTrials(n)
        x_labels.append(x)
    return x_labels


startTime = time.time()
n = 5000
m = 300
x_labels = []
y_labels = []
for each in range(m):
    x = getNumberOfTrials(n)
    x_labels.append(x)
    y = each / m
    y_labels.append(y)

endTime = time.time()


# Question 1
print("##### Number of trials for before a collision #### ")
k = getNumberOfTrials(n)
print("my k value is ", k, " \n")

print("B: (10 points) Repeat the experiment m = 300 times, and record for each time how many random trials this took.")
# print("my x_labels are ", x_labels , "\n" )
# print("my y_labels are ", y_labels,"\n")

plt.hist(x_labels,cumulative=True, histtype= "step" , density=True,bins=len(x_labels))
plt.xlabel("Number of trials")
plt.show()
print("C: (10 points) Empirically estimate the expected number of k random trials in order to have a collision")

estimate = np.round(np.sum(x_labels) / m)
print("my estimate is about ", estimate, "\n")

print("D: how long it took for m = 300 trials ")
timeElapsed1 = endTime - startTime
print("For m =  300 trials, it took about ", timeElapsed1, "seconds", "\n")
print("Show a plot of the run time as you gradually increase the parameters n and m")

n = [5000, 50000 ,500000, 1000000]
m = [300,  6000, 10000]
x_runtime = getTimeElasped(m, n)

fig , ax = plt.subplots()

for m in [300,  6000, 10000]:
    ax.plot(x_runtime[x_runtime.m == m].n, x_runtime[x_runtime.m == m].time, label=m)

ax.set_xlabel("domain Size n")
ax.set_ylabel("Time (in Second)")
ax.legend(loc='best')
plt.show()
