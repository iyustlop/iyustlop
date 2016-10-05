import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = 	[7,8,6,6,11]
eating   = 	[1,2,2,3,1]
working  =	[8,8,8,8,7.25]
playing  =	[3,1,3,2,1]



plt.stackplot(days,sleeping,eating,working,playing, colors=['m','c','r','k'])

plt.xlabel('Time')
plt.ylabel('Position Demand')

plt.title('Repositioner Demand\n Position')

plt.show()

