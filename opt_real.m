function opt_real=opt_real(gama,M,sita)
K=1480;
A2=(M*sind(gama-sita))/(K-M*cosd(gama-sita));
A1=atand(A2);
B2=(M+2*K*cosd(gama)/(2*sqrt(K^2+M^2-2*K*M*cosd(gama-sita))));
B1=atand(B2);
opt_real=A1+B1-gama;
