import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt


def dibuja_conica(x,y,A,color):
    
    N=len(x)
    assert(len(x)==len(y)),"¡La longitud de los vectores x e y debe coincidir!"
    xx=np.array([1,1,1],dtype=float)
    X,Y=np.meshgrid(x,y)
    Z=np.ones((N,N),dtype=float)
        
    for m in range (0,N):
        for n in range (0,N):
            xx[0]=X[m][n]
            xx[1]=Y[m][n]   
            #ESTO YA ES EL ALGORITMO DE MULTIPLICACION DE MATRICES
            sol=float(0)
            for i in range (0,3):
                for j in range (0,3):
                    sol=sol+xx[i]*A[i][j]*xx[j]             
            #HASTA AQUI       
            Z[m][n]=sol
            

             
    plt.contour(X,Y,Z,levels=[0],colors=color)
         
    return X,Y,Z
    
def analisis_espectral(A):  
    autovalores,autovectores=np.linalg.eig(np.asmatrix(A))
    return autovalores, autovectores
    
def es_elipse(A):
    #Comprueba que la cónica dada por A sea una elipse real y devuelve True si lo es.
    if (A[1][1]+A[2][2])*determinante(A)<0:
        comprobacion=True
    else:
        comprobacion=False
    return comprobacion

    
def haz_de_elipses(x,y,A1,A2):
    #Dibuja el haz de elipses que pasan por los puntos de intersección de las elipses Aa y Ab
    N=len(x)
    assert(len(x)==len(y)),"¡La longitud de los vectores x e y debe coincidir!"
    xx=np.array([1,1,1],dtype=float)
    X,Y=np.meshgrid(x,y)
    
    Z1=np.ones((N,N),dtype=float) 
    for m in range (0,N):
        for n in range (0,N):
            xx[0]=X[m][n]
            xx[1]=Y[m][n]   
            #ESTO YA ES EL ALGORITMO DE MULTIPLICACION DE MATRICES
            sol=float(0)
            for i in range (0,3):
                for j in range (0,3):
                    sol=sol+xx[i]*A1[i][j]*xx[j]             
            #HASTA AQUI       
            Z1[m][n]=sol
            
    Z2=np.ones((N,N),dtype=float) 
    for m in range (0,N):
        for n in range (0,N):
            xx[0]=X[m][n]
            xx[1]=Y[m][n]   
            #ESTO YA ES EL ALGORITMO DE MULTIPLICACION DE MATRICES
            sol=float(0)
            for i in range (0,3):
                for j in range (0,3):
                    sol=sol+xx[i]*A2[i][j]*xx[j]             
            #HASTA AQUI       
            Z2[m][n]=sol    
            
    for i in range (-5,6):
        lambd=i/5+0.1
        plt.contour(X,Y,Z1+lambd*Z2,0,linestyles="dashed")
  
def determinante(A):
    detA=A[0][0]*A[1][1]*A[2][2]+A[0][1]*A[1][2]*A[2][0]+A[1][0]*A[2][1]*A[0][2]-A[0][2]*A[1][1]*A[2][0]-A[0][0]*A[1][2]*A[2][1]-A[0][1]*A[1][0]*A[2][2]
    return(detA)
def adjuntos(A):
    Adj=np.ones((3,3))
    Adj[0][0]=A[1][1]*A[2][2]-A[1][2]*A[2][1]
    Adj[0][1]=A[0][2]*A[1][1]-A[0][1]*A[1][2]
    Adj[0][2]=A[0][1]*A[1][2]-A[0][2]*A[1][1]
    Adj[1][1]=A[0][0]*A[2][2]-A[0][2]*A[2][0]
    Adj[1][2]=A[0][1]*A[0][2]-A[0][0]*A[1][2]
    Adj[2][2]=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    Adj[1][0]=Adj[0][1]
    Adj[2][0]=Adj[0][2]
    Adj[2][1]=Adj[1][2]
      
    return(Adj)

def es_tangente_fondo(A,H):
    #Tangencia entre elipse y fondo:
    AdjA=adjuntos(A)
    comprobacion=AdjA[0][0]-2*AdjA[0][2]*H+AdjA[2][2]*H**2   #SI ESTO VALE CERO, la elipse Aa es tangente a la dirección del fondo
    return comprobacion

def es_tangente_izquierda(A):
    #Tangencia entre elipse y pared izquierda (x2=0) ¡CREO QUE ESTO ESTA MAL!!!!!)
    AdjA=adjuntos(A)
    comprobacion=AdjA[1][1]  #SI ESTO VALE CERO, la elipse Aa es tangente a la dirección del lado izquierdo
    return comprobacion

def es_tangente_derecha(A,L):
    #Tangencia entre elipse y pared derecha (x2=L)
    AdjA=adjuntos(A)
    comprobacion=AdjA[1][1]-2*AdjA[1][2]*L+AdjA[2][2]*L**2   #SI ESTO VALE CERO, la elipse Aa es tangente a la dirección del lado derecho
    return comprobacion

def son_tangentes(A,B):
    #Comprueba si dos elipses A y B dadas son tangentes.
    DetA=determinante(A)
    DetB=determinante(B)
    AdjA=adjuntos(A)
    AdjB=adjuntos(B)
    TaB=A[0][0]*AdjB[0][0]+A[1][1]*AdjB[1][1]+A[2][2]*AdjB[2][2]+2*A[0][1]*AdjB[0][1]+2*A[0][2]*AdjB[0][2]+2*A[1][2]*AdjB[1][2]
    TAb=AdjA[0][0]*B[0][0]+AdjA[1][1]*B[1][1]+AdjA[2][2]*B[2][2]+2*AdjA[0][1]*B[0][1]+2*AdjA[0][2]*B[0][2]+2*AdjA[1][2]*B[1][2]
    
    P=TAb/DetB-TaB**2/3/DetB**2
    Q=2*TaB**3/27/DetB**3-TaB*TAb/3/DetB**2-DetA/DetB

    comprobacion=(P/3)**3+(Q/2)**2  #SI ESTO VALE CERO, Aa y Ab son tangentes
    return comprobacion    
    
def centro(A):
    #devuelve un vector con las coordenadas [x0,y0] del centro de la cónica
    T=np.ones((2,2))
    F=[1,1]
    for i in range(0,2):  
        for j in range(0,2):
            T[i][j]=A[i][j]
        F[i]=-A[2][i]
    #De esta forma hemos creado la matriz de términos cuadráticos T, y los términos independintes necesarios para el sistema.
    Tinv=np.matrix(T).I
    sol=np.matrix(F)*np.matrix(Tinv)
    sol=sol.tolist()
    centro=sol[0][0],sol[0][1]
    return centro
    
def orientacion_ejes(A):
    T=np.ones((2,2))
    for i in range(0,2):  
        for j in range(0,2):
            T[i][j]=A[i][j]
    #De esta forma hemos creado la matriz de términos cuadráticos T
    v,w=analisis_espectral(T)
    #Esto es simplemente el arco tangente de los elementos del vector del eje x' de la elipse (complicado por tema de tipos)
    alfa=np.arctan(w[0].tolist()[0][1]/w[0].tolist()[0][0])
#OJO!: POR ALGUNA RAZON ESTO ME LO DA NEGATIVO (parece que esta bien asi)
    return -alfa

def cambio_locales_fijos(a,b,x0,y0,alfa):
    A=np.ones((3,3))
    A[0][0]=np.cos(alfa)**2/a**2+np.sin(alfa)**2/b**2
    A[0][1]=(1/a**2-1/b**2)*np.cos(alfa)*np.sin(alfa)
    A[1][1]=np.sin(alfa)**2/a**2+np.cos(alfa)**2/b**2
    A[0][2]=-x0*(np.cos(alfa)**2/a**2+np.sin(alfa)**2/b**2)-y0*(1/a**2-1/b**2)*np.cos(alfa)*np.sin(alfa)
    A[1][2]=-x0*(1/a**2-1/b**2)*np.cos(alfa)*np.sin(alfa)-y0*(np.sin(alfa)**2/a**2+np.cos(alfa)**2/b**2)
    A[2][2]=x0**2*(np.cos(alfa)**2/a**2+np.sin(alfa)**2/b**2)+y0**2*(np.sin(alfa)**2/a**2+np.cos(alfa)**2/b**2)+2*x0*y0*(1/a**2-1/b**2)*np.cos(alfa)*np.sin(alfa)-1
    A[1][0]=A[0][1] 
    A[2][0]=A[0][2]    
    A[2][1]=A[1][2]    

    return A  
    
def genera_elipse_locales(maxa,maxb, mina, minb,L):
    
    dimax=max(maxa,maxb)    
    
    y0min=dimax;    y0max=L-dimax;    x0=dimax  #Posición inicial del centro de la elipse.
    
    while True==True:
        a=np.random.sample()*(maxa-mina)+mina
        b=np.random.sample()*(maxb-minb)+minb
     
        y0=np.random.sample()*(y0max-y0min)+y0min 
    
        alfa=np.random.sample()*2*np.pi
    
        A=cambio_locales_fijos(a,b,x0,y0,alfa) #Cambio a fijos
        if es_elipse(A)==True:  #Comprobación elipse
            break
        
    return a,b,x0,y0,alfa
    
def genera_elipse_fijos(maxa,maxb, mina, minb,L):
    
    dimax=max(maxa,maxb)    
    
    y0min=dimax;    y0max=L-dimax;    x0=dimax  #Posición inicial del centro de la elipse.
    
    while True==True:
        a=np.random.sample()*(maxa-mina)+mina
        b=np.random.sample()*(maxb-minb)+minb
     
        y0=np.random.sample()*(y0max-y0min)+y0min 
    
        alfa=np.random.sample()*2*np.pi
    
        A=cambio_locales_fijos(a,b,x0,y0,alfa) #Cambio a fijos
        if es_elipse(A)==True:  #Comprobación elipse
            break
        
    return A
    
def punto_inferior(A):
    
    cc=adjuntos(A)[0][0]
    cb=-2*adjuntos(A)[0][2]  
    ca=adjuntos(A)[2][2]     
    
    inferior=(-cb+np.sqrt(cb**2-4*ca*cc))/2/ca
        
    
    return inferior
    
def existe_contacto_elipses(x,y,A1,A2):
    N=len(x)
    assert(len(x)==len(y)),"¡La longitud de los vectores x e y debe coincidir!"
    xx=np.array([1,1,1],dtype=float)
    X,Y=np.meshgrid(x,y)
    
    Z1=np.ones((N,N),dtype=float) 
    for m in range (0,N):
        for n in range (0,N):
            xx[0]=X[m][n]
            xx[1]=Y[m][n]   
            #ESTO YA ES EL ALGORITMO DE MULTIPLICACION DE MATRICES
            sol=float(0)
            for i in range (0,3):
                for j in range (0,3):
                    sol=sol+xx[i]*A1[i][j]*xx[j]             
            #HASTA AQUI       
            Z1[m][n]=sol
            
    Z2=np.ones((N,N),dtype=float) 
    for m in range (0,N):
        for n in range (0,N):
            xx[0]=X[m][n]
            xx[1]=Y[m][n]   
            #ESTO YA ES EL ALGORITMO DE MULTIPLICACION DE MATRICES
            sol=float(0)
            for i in range (0,3):
                for j in range (0,3):
                    sol=sol+xx[i]*A2[i][j]*xx[j]             
            #HASTA AQUI       
            Z2[m][n]=sol    
            
          
    
    return np.any(np.all([Z1<0,Z2<0],axis=0))


def simetriza(A):
    assert(np.size(A,axis=0)==np.size(A,axis=1)),"¡La matriz debe ser cuadrada!"
    
    for i in range (0,np.size(A,axis=0)):
        for j in range (0,i+1):
            A[j][i]=A[i][j]
    return A
    
#INICIO DEL PROGRAMA EN SÍ    
    
H=15 #Profundidad del fondo (positivo hacia abajo)
L=10  #Longitud de la franja de terreno estudiada (encajada en paredes verticales)    
    
N=50                   #Resolución 
x=np.linspace(0,H,N)   #Espacio x de trabajo
y=np.linspace(0,L,N)   #Espacio y de trabajo
    
maxa=1; maxb=.75; mina=0.75; minb=0.5     #Valores máximos y mínimos de la longitud de los ejes
maxelipses=10 #Numero máximo de elipses introducidas.

colores=["purple","blue","green","yellow","orange","red"]*np.round((maxelipses/6)+2)


elipses=np.ones((maxelipses,3,3))


a,b,x0,y0,alfa=genera_elipse_locales(maxa,maxb, mina, minb,L)

print("Moviendo elipse ",1," de ",maxelipses) 
    
while True==True:
      
      A=cambio_locales_fijos(a,b,x0,y0,alfa)
      
      if punto_inferior(A)<(H-min(mina,minb)):
          x0=x0+min(mina,minb)
                     
      elif punto_inferior(A)<H:
          x0=x0+(H-punto_inferior(A))       
        
      else:
          elipses[0][:][:]=A[:][:]
          break
        
    
dibuja_conica(x,y,A,colores[0]) 
plt.axes()

matriz_contactos=np.zeros((maxelipses,maxelipses),dtype=bool)

for numeroelipse in range(1,maxelipses):
       
    a,b,x0,y0,alfa=genera_elipse_locales(maxa,maxb, mina, minb,L)
   
    
    print("Moviendo elipse ",numeroelipse+1," de ",maxelipses)    
    
    for i in range(0,100):
        
               
        A=cambio_locales_fijos(a,b,x0,y0,alfa)
        
        comprobacion_contacto_elipses=np.zeros([maxelipses],dtype=bool)
        for j in range(0,numeroelipse):  
            comprobacion_contacto_elipses[j]=existe_contacto_elipses(x,y,A,elipses[j][:][:])          
        
        if np.any(comprobacion_contacto_elipses):
            matriz_contactos[numeroelipse][:]=comprobacion_contacto_elipses
            break
                
        elif punto_inferior(A)<(H-min(mina,minb)): 
            x0=x0+min(mina,minb)
                     
        elif punto_inferior(A)<H:
            x0=x0+(H-punto_inferior(A)) 
        
        elif i==99:
            print("ERROR: Número de Iteraciones Insuficiente")
            break
        else: 
            break
            
    
    
    X,Y,Z=dibuja_conica(x,y,A,colores[numeroelipse])
    elipses[numeroelipse][:][:]=A[:][:]

matriz_contactos=simetriza(matriz_contactos)

