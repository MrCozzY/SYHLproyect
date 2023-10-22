import pygame

ancho = 1280
alto = 720

H_FA2F2F = (250, 47, 47)
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Personajes/JhonDoe.png").convert()
        #obtiene el rectangulo (sprite)
        self.rect=self.image.get_rect()
        #centra la imagen
        self.rect=(ancho // 2, alto // 2)
        #velocidad personaje(inicial)
        self.velocidad_x = 0 
    


#enemigos
class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("Personajes/enemigo1.png").convert()



def main():
    pygame.init()
    pantalla=pygame.display.set_mode([ancho, alto])
    pygame.display.set_caption("Helldie")
    icono=pygame.image.load("Personajes/logo.png")
    pygame.display.set_icon(icono)
    salir = False
    reloj1 = pygame.time.Clock()
    #sprites
    sprites=pygame.sprite.Group()
    jugador=Jugador()
    sprites.add(jugador)
    #colores 
    BG_color=(25,29,42)
    black_color=(0,0,0,0)
    blue_color=(93,132,255)
    white_color=(255,255,255,255)
    red_color=(200,20,50)
    #musica de fondo 
    pygame.mixer.music.load('sonidos_y_musica/music1.wav')
    pygame.mixer.music.play(-1)
    # Sonido
    sonido_arriba = pygame.image.load('pygame-audio/volume_up.png')
    sonido_abajo = pygame.image.load('pygame-audio/volume_down.png')
    sonido_mute = pygame.image.load('pygame-audio/volume_muted.png')
    sonido_max = pygame.image.load('pygame-audio/volume_max.png')
    #superficie
    surface1=pygame.Surface((1000,alto))
    surface1.fill(black_color)
    surface2=pygame.Surface([500,360])
    surface2.fill(white_color)
    #rectangulos
    
    r2= pygame.Rect(200,200,100,50)
    r1 =pygame.Rect(140,0,500,360)
   
   
    #Loop principal

    while salir !=True:
        #pantalla.blit(Jugador,())
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 salir=True   
             if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_a:
                     jugador.rect.move(-10,0)
                 if event.key == pygame.K_d:
                     jugador.move_ip(10,0)
                 if event.key == pygame.K_w:
                     jugador.move_ip(0,-10)
                 if event.key == pygame.K_s:
                     jugador.move_ip(0,10)
                # if jugador:
                     #d
                 
        sprites.update()
        sprites.draw(surface1)
            
        reloj1.tick(40)
        pantalla.fill(BG_color)
        pantalla.blit(surface1,[140,0])
        #pantalla.blit(surface2,[140,0])
        pygame.draw.rect(pantalla,blue_color,r1) 

	    # Control del audio
	    # Baja volumen

        pygame.display.update()
    
    pygame.quit()


main()