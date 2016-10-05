function[comprobacion_contacto_elipses,elipses,matriz_contactos]=medio_eliptico()

clc
clear all
hold on

H=10; %Profundidad del fondo (positivo hacia abajo)
L=10;  %Longitud de la franja de terreno estudiada (encajada en paredes verticales)    
    
N=50;                   %Resolución 
x=linspace(0,H,N);   %Espacio x de trabajo
y=linspace(0,L,N);   %Espacio y de trabajo
    
maxa=1; maxb=.75; mina=0.75; minb=0.5;     %Valores máximos y mínimos de la longitud de los ejes
maxelipses=15; %Numero máximo de elipses introducidas.

elipses=ones(3,3,maxelipses);


[a,b,x0,y0,alfa]=genera_elipse_locales(maxa,maxb, mina, minb,L);

fprintf('Moviendo elipse 1 de %d',maxelipses)
    
while true==true;
      
      A=cambio_locales_fijos(a,b,x0,y0,alfa);
      
      if punto_inferior(A)<(H-min(mina,minb));
          x0=x0+min(mina,minb);
      
                     
      elseif punto_inferior(A)<H;
          x0=x0+(H-punto_inferior(A));
              
      else
          elipses(:,:,1)=A(:,:);
          break
          
      end
end

dibuja_conica(x,y,A,'green'); 

matriz_contactos=zeros(maxelipses,maxelipses);


for numeroelipse=2:maxelipses;
       
    [a,b,x0,y0,alfa]=genera_elipse_locales(maxa,maxb, mina, minb,L);
   
    
    fprintf('Moviendo elipse %d de %d',numeroelipse,maxelipses)    
    
    for i=1:1000;
                       
        A=cambio_locales_fijos(a,b,x0,y0,alfa);
        
        comprobacion_contacto_elipses=zeros(maxelipses,1);
        
        for j=1:numeroelipse;  
            comprobacion_contacto_elipses(j)=existe_contacto_elipses(x,y,A,elipses(:,:,j));          
        end 
        
        
        if any(comprobacion_contacto_elipses)
            matriz_contactos(numeroelipse,:)=true;
            break
                
        elseif punto_inferior(A)<(H-min(mina,minb)) 
            x0=x0+min(mina,minb)/10;  %Aquí se indica cúanto avanza en cada iteracion
                     
        elseif punto_inferior(A)<H
            x0=x0+(H-punto_inferior(A)); 
                     
        elseif i==999
            %'ERROR: Número de Iteraciones Insuficiente'
            break
        else 
            break
        end
        
    end
    
    dibuja_conica(x,y,A,'blue');
    elipses(:,:,numeroelipse)=A(:,:);
    
end    

matriz_contactos=simetriza(matriz_contactos);



hold off
end