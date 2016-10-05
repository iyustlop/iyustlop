function[comprobacion]=es_tangente_derecha(A,L)
    %Tangencia entre elipse y pared izquierda (x2=0) ¡CREO QUE ESTO ESTA MAL!!!!!)
    AdjA=adjuntos(A);
    comprobacion=AdjA(2,2)-2*AdjA(2,3)*L+AdjA(3,3)*L^2;   %SI ESTO VALE CERO, la elipse Aa es tangente a la dirección del lado derecho
end