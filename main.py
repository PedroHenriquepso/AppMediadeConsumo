distancia_percorrida = float(input('Digite a distancia percorrida (em quilometros):'))
combustivel_consumido = float(input('Digite o total de combustível consumido (em litros): ')) 

media_consumo = distancia_percorrida / combustivel_consumido
print('A média de consumo do carro e de {} km/l'.format(media_consumo))
  