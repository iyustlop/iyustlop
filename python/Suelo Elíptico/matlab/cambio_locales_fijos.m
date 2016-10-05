function[A]=cambio_locales_fijos(a,b,x0,y0,alfa)
    A=ones(3);
    A(1,1)=cos(alfa)^2/a^2+sin(alfa)^2/b^2;
    A(1,2)=(1/a^2-1/b^2)*cos(alfa)*sin(alfa);
    A(2,2)=sin(alfa)^2/a^2+cos(alfa)^2/b^2;
    A(1,3)=-x0*(cos(alfa)^2/a^2+sin(alfa)^2/b^2)-y0*(1/a^2-1/b^2)*cos(alfa)*sin(alfa);
    A(2,3)=-x0*(1/a^2-1/b^2)*cos(alfa)*sin(alfa)-y0*(sin(alfa)^2/a^2+cos(alfa)^2/b^2);
    A(3,3)=x0^2*(cos(alfa)^2/a^2+sin(alfa)^2/b^2)+y0^2*(sin(alfa)^2/a^2+cos(alfa)^2/b^2)+2*x0*y0*(1/a^2-1/b^2)*cos(alfa)*sin(alfa)-1;
    A(2,1)=A(1,2); 
    A(3,1)=A(1,3);    
    A(3,2)=A(2,3);  

end