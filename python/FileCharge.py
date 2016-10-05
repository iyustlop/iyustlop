import matplotlib.pyplot as plt
import numpy as np

TIME,AESA_DEMAND,BULK_DEMAND,AESA_Current_Position_PRM,Bulk_Current_Position_PRM,AESA_Current_Position_EST,Bulk_Current_Position_EST,AESA_Current_Velocity_EST,Bulk_Current_Velocity_EST,AESA_Integral_Control,Bulk_Integral_Control,AESA_Disturbance_EST,Bulk_Disturbance_EST,AESA_Torque,Bulk_Torque,AESA_Control_Mode,Bulk_Control_Mode,MSG_Counter,MDU_Status,FIN = np.genfromtxt('APRM_PolRamp20toNeg20.csv',delimiter=';',skip_header=1,autostrip=True,unpack=True)

TIEMPO = []
ERROR_AESA = []
ERROR_BULKHEAD = []

for i in range(len(TIME)):
	CTIEMPO=[0.004*i]
	TIEMPO.append(CTIEMPO)

ERROR_AESA = np.subtract(AESA_DEMAND, AESA_Current_Position_PRM)
ERROR_BULKHEAD = np.subtract(BULK_DEMAND,Bulk_Current_Position_PRM)
#print(len(ERROR_AESA))

plt.plot(TIEMPO,AESA_Current_Position_PRM, label = 'AESA Current Position')
plt.plot(TIEMPO,ERROR_AESA, label = 'AESA Error')

plt.xlabel('TIME (s)')
plt.ylabel('Position Demand')
plt.title('Repositioner Demand\n Position')
plt.legend()

plt.savefig('AESA position',dpi='figure', facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None)

plt.show()

plt.plot(TIEMPO,Bulk_Current_Position_PRM, label = 'Bulkhead Current Position' )
plt.plot(TIEMPO,ERROR_BULKHEAD, label = 'Bulkhead Error')
plt.xlabel('TIME (s)')
plt.ylabel('Position Demand')
plt.title('Repositioner Demand\n Position')
plt.legend()
plt.show()

plt.savefig