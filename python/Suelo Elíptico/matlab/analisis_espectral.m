function[autovalores,autovectores]=analisis_espectral(A) 
[autovectores,autovalores]=eig(A);
autovalores=diag(autovalores())
end