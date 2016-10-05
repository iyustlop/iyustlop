import matplotlib.pyplot as plt

x=[0,1,2,3]
y=[6,5,7,4]

x2=[0,1,2,3]
y2=[10,15,17,14]

plt.plot(x,y, label='Position Demand')
plt.plot(x2,y2, label='Servo Error')
plt.xlabel('Time')
plt.ylabel('Position Demand')

plt.title('Repositioner Demand\n Position')
plt.legend()
plt.show()

