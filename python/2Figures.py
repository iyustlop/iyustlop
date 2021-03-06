import numpy as np
import matplotlib.pyplot as plt

TIME,AESA_DEMAND,BULK_DEMAND,AESA_Current_Position_PRM,Bulk_Current_Position_PRM,AESA_Current_Position_EST,Bulk_Current_Position_EST,AESA_Current_Velocity_EST,Bulk_Current_Velocity_EST,AESA_Integral_Control,Bulk_Integral_Control,AESA_Disturbance_EST,Bulk_Disturbance_EST,AESA_Torque,Bulk_Torque,AESA_Control_Mode,Bulk_Control_Mode,MSG_Counter,MDU_Status,FIN = np.genfromtxt('/home/portatil/Documentos/Desarrollo/python/APRM_PolRamp20toNeg20OrientNeg90.csv',delimiter=';',skiprows=1,autostrip=True,unpack=True)

TIEMPO = []
ERROR_AESA = []
VELOCIDAD = []

for i in range(len(TIME)):
	CTIEMPO=[0.004*i]
	TIEMPO.append(CTIEMPO)
ERROR_AESA = np.subtract(AESA_DEMAND, AESA_Current_Position_PRM)

for i in range(len(TIEMPO)):
	if i == 0:
		CVELOCIDAD=AESA_Current_Position_PRM[i]/0.004
		VELOCIDAD.append(CVELOCIDAD)
	else:
		CVELOCIDAD=(AESA_Current_Position_PRM[i]-AESA_Current_Position_PRM[i-1])/0.004
		VELOCIDAD.append(CVELOCIDAD)

f = plt.figure(1)
AESA_Demand_plot = plt.subplot2grid((1,1),(0,0))

AESA_Demand_plot.plot(TIEMPO, AESA_Current_Position_PRM,'-', label='AESA_Current_Position_PRM')
AESA_Demand_plot.grid(True)
# set_%ticks, fija lso valores.
AESA_Demand_plot.set_yticks([-30,-20,-10,0,10,20,30])
AESA_Demand_plot.legend()



g = plt.figure(2)
plt.plot(TIEMPO, VELOCIDAD, '-', label='AESA_Speed',color='k')
plt.grid(True)

plt.subplots_adjust(left=0.09, bottom=0.16, right=0.94, top=0.95, wspace=0.2, hspace=0)
plt.legend()
plt.show()


