function[a,b,x0,y0,alfa]=genera_elipse_locales(maxa,maxb, mina, minb,L)
    
    dimax=max(maxa,maxb);    
    
    y0min=dimax;
    y0max=L-dimax;
    x0=dimax;  %Posición inicial del centro de la elipse.
    
    while 1==1;
        a=rand*(maxa-mina)+mina;
        b=rand*(maxb-minb)+minb;
     
        y0=rand*(y0max-y0min)+y0min;
    
        alfa=rand*2*pi;
    
        A=cambio_locales_fijos(a,b,x0,y0,alfa); %Cambio a fijos
        if es_elipse(A)==1;  %Comprobación elipse
            break
        end
    end
        
end