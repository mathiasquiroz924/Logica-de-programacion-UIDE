import random 
def jugar():
    opciones = ['piedra' , 'papel', 'tijera']
    
    print ('Bienvenido al juego de Piedra, Papel o Tijera ')
    
    jugador= input ( 'Elige piedra, papel o tijera: ') . lower()

    if jugador not in opciones: 
        print ('Opcion no valida ') 
        return

    computadora= random.choice(opciones)
    print(f'La computadora eligio: {computadora}')

    if jugador == computadora:
        print('Empate, sigue intentando!')
    elif (jugador == 'piedra'and computadora == 'tijera') or (jugador == 'papel'and computadora == 'piedra') or (jugador == 'tijera'and computadora == 'papel'):
        print ('Felicidades ganaste!')
    else:
        print ('Perdiste, vuelve a intentar!') 
jugar()







    