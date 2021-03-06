import matplotlib.pyplot as plt
import numpy as np

TIME,AESA_DEMAND,BULK_DEMAND,AESA_Current_Position_PRM,Bulk_Current_Position_PRM,AESA_Current_Position_EST,Bulk_Current_Position_EST,AESA_Current_Velocity_EST,Bulk_Current_Velocity_EST,AESA_Integral_Control,Bulk_Integral_Control,AESA_Disturbance_EST,Bulk_Disturbance_EST,AESA_Torque,Bulk_Torque,AESA_Control_Mode,Bulk_Control_Mode,MSG_Counter,MDU_Status,FIN = np.genfromtxt('APRM_PolRamp20toNeg20.csv',delimiter=';',skiprows=1,autostrip=True,unpack=True)

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

print(len(TIEMPO))
print(len(ERROR_AESA))
print(len(VELOCIDAD))

plt.figure('AESA Demand') # Crea una ventana titulada 'AESA Speed'
fig, ax1 = plt.subplots()
ax1.plot(TIEMPO, AESA_Current_Position_PRM, label='AESA_Current_Position_PRM',color='b')
ax1.set_xlabel('time (s)')
ax1.set_ylabel('AESA_Current_Position_PRM', color='k')
ax1.legend()
for tl in ax1.get_yticklabels():
    tl.set_color('k')

#instruccion que hace que se duplique el eje Y, Comparte el eje X
ax2 = ax1.twinx()

ax2.plot(TIEMPO, ERROR_AESA, label='ERROR_AESA', color='r')
ax2.set_ylabel('ERROR_AESA', color='k')
ax2.legend()
for tl in ax2.get_yticklabels():
    tl.set_color('k')

plt.grid(color='k', linestyle='-', linewidth=0.5)

#plt.figure('Error AESA') # Crea una ventana titulada 'scatter'	
#plt.show()

plt.figure('AESA Speed') # Crea una ventana titulada 'AESA Speed'
#speed.plot(TIEMPO, VELOCIDAD, label='AESA_Speed',color='k')
plt.grid(color='k', linestyle='-', linewidth=0.5)
plt.show()


