function[]=haz_de_elipses(x,y,A1,A2)
    %Dibuja el haz de elipses que pasan por los puntos de intersección de las elipses Aa y Ab
    N=length(x);
    xx=[1,1,1];
    [X,Y]=meshgrid(x,y);
    
    Z1=ones(N);
    for m=1:N;
        for n=1:N;
            xx(1)=X(m,n);
            xx(2)=Y(m,n);   
            %ESTO YA ES EL ALGORITMO DE MULTIPLICACION DE MATRICES
            sol=0;
            for i=1:3;
                for j=1:3;
                    sol=sol+xx(i)*A1(i,j)*xx(j); 
                end
            end
            %HASTA AQUI       
            Z1(m,n)=sol;
        end
    end
            
    Z2=ones(N);
    for m=1:N;
        for n=1:N;
            xx(1)=X(m,n);
            xx(2)=Y(m,n);  
            %ESTO YA ES EL ALGORITMO DE MULTIPLICACION DE MATRICES
            sol=0;
            for i=1:3;
                for j=1:3;
                    sol=sol+xx(i)*A2(i,j)*xx(j);             
            %HASTA AQUI       
                end
            end
            Z2(m,n)=sol;    
        end
    end
    
    hold on
    for i=-5:6;
        lambd=i/5+0.1;
   
        contour(X,Y,Z1+lambd*Z2,[0,0],'.-');
    end
    hold off