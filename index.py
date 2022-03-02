print('Mohasebe Enegry Mechanici,yekaha bar hasb SI mibashad.')
M = float(input('Jerm(KG): '))
V = float(input('Tondi(M/S):'))
K = M * (V**2) / 2
H = float(input('Ertefa(H):'))
U = M*9.81*H
print(f'Energy jonbeshi(K) = {K}')
print(f'Energy potancielle(U) = {U}')
print(f'Energy mechanici(E) : {K+U}')