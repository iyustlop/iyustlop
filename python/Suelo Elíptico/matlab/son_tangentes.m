function[comprobacion]=son_tangentes(A,B)
    %Comprueba si dos elipses A y B dadas son tangentes.
    DetA=det(A);
    DetB=det(B);
    AdjA=adjuntos(A);
    AdjB=adjuntos(B);
    TaB=A(1,1)*AdjB(1,1)+A(2,2)*AdjB(2,2)+A(3,3)*AdjB(3,3)+2*A(1,2)*AdjB(1,2)+2*A(1,3)*AdjB(1,3)+2*A(2,3)*AdjB(2,3);
    TAb=AdjA(1,1)*B(1,1)+AdjA(2,2)*B(2,2)+AdjA(3,3)*B(3,3)+2*AdjA(1,2)*B(1,2)+2*AdjA(1,3)*B(1,3)+2*AdjA(2,3)*B(2,3);
    
    P=TAb/DetB-TaB^2/3/DetB^2;
    Q=2*TaB^3/27/DetB^3-TaB*TAb/3/DetB^2-DetA/DetB;

    comprobacion=(P/3)^3+(Q/2)^2;  %SI ESTO VALE CERO, Aa y Ab son tangentes
end