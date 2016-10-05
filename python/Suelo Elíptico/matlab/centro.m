function[centro]=centro(A)
 %devuelve un vector con las coordenadas [x0,y0] del centro de la cónica
    T=ones(2);   
    F=[1,1];
    for i=1:2;  
        for j=1:2;
            T(i,j)=A(i,j);
        end
        F(i)=-A(3,i);
    end
    %De esta forma hemos creado la matriz de términos cuadráticos T, y los términos independintes necesarios para el sistema.
    Tinv=T^-1;
    sol=F*Tinv;
    centro=[sol(1,1),sol(1,2)];
end