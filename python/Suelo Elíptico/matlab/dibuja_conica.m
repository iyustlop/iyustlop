function[X,Y,Z]=dibuja_conica(x,y,A,color)
    
    N=length(x);
    xx=[1,1,1];
    [X,Y]=meshgrid(x,y);
    Z=ones(N);
        
    for m=1:N;
        for n=1:N;
            xx(1)=X(m,n);
            xx(2)=Y(m,n);   
            %ESTO YA ES EL ALGORITMO DE MULTIPLICACION DE MATRICES
            sol=0;
            for i=1:3;
                for j=1:3;
                    sol=sol+xx(i)*A(i,j)*xx(j);
                end
            end
        
            %HASTA AQUI       
            Z(m,n)=sol;
            end
    end
 
    contour(X,Y,Z,[0,0],color);
end
