#DATAMARK - Market Intelligence Brazil(http://ppv.datamark.com.br/analise-de-mercado/higiene-bucal/cremes-dentais-394/):
toneladas_ano = [48924, 53917, 57902, 63555, 62685.5, 67192.5, 70290.4, 73387.2, 76484.1] #2007-2015

crescimento = []
for i in range(0, 8, 1):
  crescimento.append((toneladas_ano[i+1] - toneladas_ano[i]) * 100 / toneladas_ano[i]) 

soma = 0
for i in range(len(crescimento)):
  soma = soma + crescimento[i]
media_crescimento = soma / 8 #Resultado em %
media_crescimento = media_crescimento / 100

#M = C * (1 + i) ** n
toneladas_2021 = toneladas_ano[8] * (1 + media_crescimento) ** 6

gramas_2021 = toneladas_2021 * 1000000
quantidade_tubo = 70 #g
pastas_ano = gramas_2021 / quantidade_tubo
pastas_mes = pastas_ano / 12

print('São vendidas aproximadamente {:.0f} pastas dentais no Brasil por mês.'.format(pastas_mes))
