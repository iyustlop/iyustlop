function[comprobacion]=es_tangente_izquierda(A)
    %Tangencia entre elipse y pared izquierda (x2=0) ¡CREO QUE ESTO ESTA MAL!!!!!)
    AdjA=adjuntos(A);
    comprobacion=AdjA(2,2);  %SI ESTO VALE CERO, la elipse Aa es tangente a la dirección del lado izquierdo
end