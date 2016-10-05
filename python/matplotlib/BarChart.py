import matplotlib.pyplot as plt

x=[0,2,4,6]
y=[6,5,7,4]

x2=[1,3,5,7]
y2=[10,15,17,14]

plt.bar(x,y, label='Position Demand', color='blue')
plt.bar(x2,y2, label='Servo Error',color='red')
plt.xlabel('Time')
plt.ylabel('Position Demand')

plt.title('Repositioner Demand\n Position')
plt.legend()
plt.show()

