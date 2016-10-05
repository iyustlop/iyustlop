function[comprobacion]=es_elipse(A)
    %Comprueba que la cónica dada por A sea una elipse real y devuelve True si lo es.
    if (A(2,2)+A(3,3))*det(A)<0
        comprobacion=true
    else
        comprobacion=false
end