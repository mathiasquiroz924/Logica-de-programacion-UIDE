import random 
def jugador ():
    opciones = ['piedra' , 'papel', 'tijera']
    
    print ('Bienvenido al juego de Piedra, Papel o Tijera ')
    
    jugador= input ( 'Elige piedra, papel o tijera: ') . lower()

    if jugador not in opciones: 
        print ('Opcion no valida ') 
        return

    computadora= random.choice(opciones)
    print(f'La computadora eligio: {computadora}')





    