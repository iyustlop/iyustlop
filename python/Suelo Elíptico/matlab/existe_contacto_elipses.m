function[comprobacion]=existe_contacto_elipses(x,y,A1,A2)
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
                    sol=sol+xx(i)*A1(i,j)*xx(j) ; 
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
                end
            end
            %HASTA AQUI       
            Z2(m,n)=sol;
        end
    end
            
    comprobacion=any(any((Z1<0&Z2<0)));
    
end