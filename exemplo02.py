previsoes = ['Ensolarado','Nublado','Chuvoso','Tempestade','Ensolarado']
print(previsoes)

previsao_feliz = 'Ensolarado'

for p in previsoes:
    print(p)
    if p == previsao_feliz:
        print('Aproveite para passear')
    else:
        print('Não esqueça o guarda chuva')   
    