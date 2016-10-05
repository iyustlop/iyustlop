function[A]=simetriza(A)
    
    for i=1:size(A,1)
        for j=1:i;
            A(j,i)=A(i,j);
        end
    end
end