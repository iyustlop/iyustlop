function[inferior]=punto_inferior(A)
    
    AdjA=adjuntos(A);
    cc=AdjA(1,1);
    cb=-2*AdjA(1,3); 
    ca=AdjA(3,3);    
    
    inferior=(-cb+sqrt(cb^2-4*ca*cc))/2/ca;
        
    
end