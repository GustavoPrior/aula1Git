# Inicialização das listas para armazenar as leituras dos sensores
leituras_ldr = []
leituras_ultrassonico = []

# Coletar 10 leituras simuladas de cada sensor
print("Insira as leituras do LDR e do Sensor Ultrassônico:")

for i in range(10):
    valor_ldr = float(input("Leitura {} do LDR: ".format(i+1)))
    valor_ultrassonico = float(input("Leitura {} do Sensor Ultrassônico (em cm): ".format(i+1)))
    leituras_ldr.append(valor_ldr)
    leituras_ultrassonico.append(valor_ultrassonico)

# Calcular a média dos valores medidos
media_ldr = sum(leituras_ldr) / len(leituras_ldr)
media_ultrassonico = sum(leituras_ultrassonico) / len(leituras_ultrassonico)

# Exibir os resultados
print("\nResultados:")
print("Média das leituras do LDR: {:.2f}".format(media_ldr))
print("Média das leituras do Sensor Ultrassônico: {:.2f} cm".format(media_ultrassonico))

# Exibir os dados coletados
print("\nLeituras do LDR:", leituras_ldr)
print("Leituras do Sensor Ultrassônico:", leituras_ultrassonico)