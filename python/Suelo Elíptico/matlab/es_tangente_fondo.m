function[comprobacion]=es_tangente_fondo(A,H)
    %Tangencia entre elipse y fondo:
    AdjA=adjuntos(A);
    comprobacion=AdjA(1,1)-2*AdjA(1,3)*H+AdjA(3,3)*H^2;   %SI ESTO VALE CERO, la elipse Aa es tangente a la dirección del fondo
end