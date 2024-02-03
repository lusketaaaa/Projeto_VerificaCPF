#Exercicio -  Gerar primeiro digito de CPF
print("Bem-vindo ao Gerador de primeiro digito de CPF!")
cpf_usuario = input("Digite seu CPF: ") 
cpf_usuario_sem_pontos = cpf_usuario.replace(".", "")
cpf_usuario_sem_ponto_e_traco = cpf_usuario_sem_pontos.replace("-", "")

#preciso multiplicar os numeros 1 por 1, minha ideia e usar o indice [ ]

m1 = int(cpf_usuario_sem_ponto_e_traco[0]) * 10
m2 = int(cpf_usuario_sem_ponto_e_traco[1]) * 9
m3 = int(cpf_usuario_sem_ponto_e_traco[2]) * 8
m4 = int(cpf_usuario_sem_ponto_e_traco[3]) * 7
m5 = int(cpf_usuario_sem_ponto_e_traco[4]) * 6
m6 = int(cpf_usuario_sem_ponto_e_traco[5]) * 5
m7 = int(cpf_usuario_sem_ponto_e_traco[6]) * 4
m8 = int(cpf_usuario_sem_ponto_e_traco[7]) * 3
m9 = int(cpf_usuario_sem_ponto_e_traco[8]) * 2

soma_das_multiplicacoes = m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8 + m9

#multiplicar o resultado das multiplicacoes por 10

multiplicacoes_vezes_10 = soma_das_multiplicacoes * 10

#obter o resto da divisao da conta anterior por 11

divisao_da_multiplicacao10 = multiplicacoes_vezes_10 % 11

#se resultado anterior > 9, resultado e zero //  se for < 9, resultado e o proprio resto(resultado anterior)

resultado_primeirodigitocpf = divisao_da_multiplicacao10 if divisao_da_multiplicacao10 < 9 else 0 

#verificacao do segundo digito

m11 = int(cpf_usuario_sem_ponto_e_traco[0]) * 11
m12 = int(cpf_usuario_sem_ponto_e_traco[1]) * 10
m13 = int(cpf_usuario_sem_ponto_e_traco[2]) * 9
m14 = int(cpf_usuario_sem_ponto_e_traco[3]) * 8
m15 = int(cpf_usuario_sem_ponto_e_traco[4]) * 7
m16 = int(cpf_usuario_sem_ponto_e_traco[5]) * 6
m17 = int(cpf_usuario_sem_ponto_e_traco[6]) * 5
m18 = int(cpf_usuario_sem_ponto_e_traco[7]) * 4
m19 = int(cpf_usuario_sem_ponto_e_traco[8]) * 3
m20 = int(cpf_usuario_sem_ponto_e_traco[9]) * 2  

soma_das_multiplicacoes_2 = m11 + m12 + m13 + m14 + m15 + m16 + m17 + m18 + m19 + m20

multiplicacoes_vezes_10_2 = soma_das_multiplicacoes_2 * 10

divisao_multiplicacao10_2 = multiplicacoes_vezes_10_2 % 11

resultado_segundodigitocpf = divisao_multiplicacao10_2 if divisao_multiplicacao10_2 < 9 else 0 
 
print(f"O primeiro digito e {resultado_primeirodigitocpf}")
print(f"O segundo digito e {resultado_segundodigitocpf}")

if int(cpf_usuario_sem_ponto_e_traco[9]) == resultado_primeirodigitocpf and int(cpf_usuario_sem_ponto_e_traco[10]) == resultado_segundodigitocpf:
    print("O CPF informado é válido.")
else:
    print("O CPF informado não é válido.")

 



