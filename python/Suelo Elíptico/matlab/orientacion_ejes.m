function[alfa]=orientacion_ejes(A)
    T=ones(2,2);
    for i=1:2;  
        for j=1:2;
            T(i,j)=A(i,j);
        end
    end
    %De esta forma hemos creado la matriz de términos cuadráticos T
    [v,w]=analisis_espectral(T);

    alfa=atan(w(1,2)/w(1,1));

end