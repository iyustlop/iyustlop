import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8]
y=[5,1,8,3,6,4,2,7]

plt.scatter (x,y, label='Repositioner Demand', color='k', marker='*', s=1000)

plt.xlabel('Time')
plt.ylabel('Position Demand')

plt.title('Repositioner Demand\n Position')

plt.show()

