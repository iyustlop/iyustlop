import matplotlib.pyplot as plt

population_ages = [22,55,66,77,88,12,34,45,67,78,89,10,92,93,84,75]

#ids = [x for x in range(len(population_ages))]

bins = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(population_ages, bins, histtype='bar',rwidth=0.8)

plt.xlabel('Time')
plt.ylabel('Position Demand')

plt.title('Repositioner Demand\n Position')

plt.show()

