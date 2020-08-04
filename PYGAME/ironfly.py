import pygame
from pygame.locals import*
import random
import math
import sys

def win():
	pygame.init()
	pygame.mixer.init()
	pygame.display.set_caption("IRON FLY")
	pantalla = pygame.display.set_mode((500,512))

	img_fel= pygame.image.load('img/fel.png').convert_alpha()

	pygame.mixer.music.load('sond/fel.mp3')
	pygame.mixer.music.play()

	fuente = pygame.font.SysFont("monospace",30)

	run = True

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			pantalla.blit(img_fel,(0,0))
			label = fuente.render("MUCHAS GRACIAS POR JUGAR",1,negro)
			pantalla.blit(label,(30,477))

		pygame.display.update()
		pygame.display.flip()


def game_over():
	pygame.init()
	pygame.mixer.init()
	pygame.display.set_caption("IRON FLY")
	pantalla = pygame.display.set_mode((500,512))

	#imagen de fondo
	img_gover = pygame.image.load('img/gover.png').convert_alpha()

	#musica
	pygame.mixer.music.load('sond/IWKTG Soundtrack - 05 - Death.mp3')
	pygame.mixer.music.play()

	#TEXTO DE FONDO
	fuente = pygame.font.SysFont("monospace",23)

	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
            
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:
					#si presionas r, vuelves al nivel 1
					nivel1()
					run = False
					sys.exit()

			pantalla.blit(img_gover,(0,0))

			#texto dentro del game over
			label = fuente.render("PRESIONA R PARA VOLVER A JUGAR",1,rojo)
			pantalla.blit(label,(50,457))

		pygame.display.update()
		pygame.display.flip()
###################################################################################3        
def nivel1():
	pygame.init()
	pygame.mixer.init()
	ancho = 500
	alto = 512
	pygame.display.set_caption("IRON FLY")
	pantalla = pygame.display.set_mode((ancho,alto))

	rojo = (255,0,0)
	negro = (0,0,0)

    #imagen de fondo 
	img_1 = pygame.image.load('img/lvl1.png').convert_alpha()
    
    #imagen de la mosca
	mosca1 = pygame.image.load('img/mosca1.png').convert_alpha()
	#mosca enemiga
	mosca2 = pygame.image.load('img/dead.png').convert_alpha()
	mosca3 = pygame.image.load('img/dead2.png').convert_alpha()

	cora = pygame.image.load('img/life.png').convert_alpha()

	pygame.mixer.music.load('sond/africa.mp3')
	pygame.mixer.music.play(-1)

	#coordenadas y velocidades
	x = 250
	y = 450
	x2 = 260
	y2 = 460
	x3 = 270
	y3 = 430

	mosca1_vely = 0.7
	mosca2_velx = 0.7
	mosca3_velx = 0.7

	puntaje = 0
	vidas = 3

	#FUENTA PARA TEXTO EN PANTALLA
	fuente = pygame.font.Font(None,30)
	p1 = fuente.render(str(puntaje),0, negro)
	p2 = fuente.render(str(vidas),0, negro)

	run = True
	fps = pygame.time.Clock()
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			#detecar click del mouse
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				#si mouse toca la mosca
				if mosca1.get_rect(top=y,left=x).collidepoint(mouse_pos):
					#sumas +1 punto   
					puntaje += 1
					#se imprime en la pantalla
					p1 = fuente.render(str(puntaje),0, negro)
					#mosca reaparece en un punto random
					y = (x+100)
					x = random.randint(0, (y+1))

					#sonido al hacer click en la mosca
					hit = pygame.mixer.Sound('sond/hit2.wav')
					hit.play()
					
					#si puntaje es igual a 25, pasa al nivel 2
					if puntaje == 25:
						nivel2()
						run = False
						sys.exit()

                #si tocas las moscas rojas pierdes una vida
				if mosca2.get_rect(top=y2,left=x2).collidepoint(mouse_pos) or mosca3.get_rect(top=y3,left=x3).collidepoint(mouse_pos):
					vidas -= 1
					p2 = fuente.render(str(vidas),0, negro)
                    
                    #sonido al hacer click mosca roja
					hit_mr = pygame.mixer.Sound('sond/hit3.wav')
					hit_mr.play()

					#punto random mosca2
					x2 = (y2+100)
					y2 = random.randint(0, (x2+1))

					#punto random mosca3
					x3 = (y3+100)
					y3 = random.randint(0, (x3-1))

					#si vidas llega a 0, GAME OVER!!!
					if vidas == 0:
						game_over()
						run = False
						sys.exit()

        #si la mosca toca arriba, reaparece en un punto random
		if y<0:
			y = (x+200)
			x = random.randint(0, (y))

        #si mosca2 toca izquierda retorna punto random hacia izquierda
		if x2<0:
			x2 = (y2+100)
			y2 = random.randint(0, (x2+1))

        #si mosca3 toca derecha vuelve punto random hacia derecha
		if x3>ancho:
			x3 = (y3+100)
			y3 = random.randint(0, (x3-1))

        #control de velocidades
		y -= mosca1_vely
		x2 -= mosca2_velx
		x3 += mosca3_velx

		pantalla.blit(img_1,(0,0))
		label = fuente.render("PUNTOS:",1,rojo)
		label2 = fuente.render(" / 25",1,negro)
		pantalla.blit(p1,(110,5))
		pantalla.blit(label,(10,5))
		pantalla.blit(label2,(130,5))
		pantalla.blit(p2,(50,35))
		pantalla.blit(cora,(10,30))
		pantalla.blit(mosca1,(x,y))
		pantalla.blit(mosca2,(x2,y2))
		pantalla.blit(mosca3,(x3,y3))

		pygame.display.update()
		fps.tick(500)
		pygame.display.flip()
######################################################################
def nivel2():
	pygame.init()
	pygame.mixer.init()
 
    #titulo ventana
	pygame.display.set_caption("IRON FLY")
	#tamaño ventana
	pantalla = pygame.display.set_mode((500,512))

	rojo = (255,0,0)
	negro = (0,0,0)

	#imagen de fondo
	img_2 = pygame.image.load('img/fondo2.png').convert_alpha()

	#imagen vidas
	cora = pygame.image.load('img/life.png').convert_alpha()

	mosca = pygame.image.load('img/mosca1.png').convert_alpha()
	mosca1 = pygame.image.load('img/mosca2.png').convert_alpha()

	mosca2 = pygame.image.load('img/dead.png').convert_alpha()
	mosca3 = pygame.image.load('img/dead2.png').convert_alpha()

	pygame.mixer.music.load('sond/egipto.mp3')
	pygame.mixer.music.play(-1)
    
	x = 250
	y = 450
	x_1 = 260
	y_1 = 460
	x2 = 260
	y2 = 460
	x3 = 270
	y3 = 430

	mosca_vely = 0.7
	mosca1_vely = 0.7
	mosca2_velx = 0.8
	mosca3_velx = 0.8

	puntaje = 0
	vidas = 3

	fuente = pygame.font.Font(None,30)
	p1 = fuente.render(str(puntaje),0, negro)
	p2 = fuente.render(str(vidas),0, negro)

	run = True
	fps = pygame.time.Clock()
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				if mosca1.get_rect(top=y,left=x).collidepoint(mouse_pos) or mosca.get_rect(top=y_1,left=x_1).collidepoint(mouse_pos):
					puntaje += 1
					p1 = fuente.render(str(puntaje),0, negro)

					y = (x+100)
					x = random.randint(0, (y+1))
					y_1 = (x_1+100)
					x_1 = random.randint(0, (y_1+1))

					hit = pygame.mixer.Sound('sond/hit2.wav')
					hit.play()

					#si puntaje es igual a 20, pasas al nivel 3
					if puntaje == 20:
						nivel3()
						run = False
						sys.exit()

				if mosca2.get_rect(top=y2,left=x2).collidepoint(mouse_pos) or mosca3.get_rect(top=y3,left=x3).collidepoint(mouse_pos):
					vidas -= 1
					p2 = fuente.render(str(vidas),0, negro)

					hit_mr = pygame.mixer.Sound('sond/hit3.wav')
					hit_mr.play()

					x2 = (y2+100)
					y2 = random.randint(0, (x2+1))

					x3 = (y3+100)
					y3 = random.randint(0, (x3-1))

					if vidas == 0:
						game_over()
						run = False
						sys.exit()

		if y<0:
			y = (x+200)
			x = random.randint(0, (y))
        
        #si mosca toca abajo, retorna punto random
		if y_1>512:
			y_1 = (x_1+100)
			x_1 = random.randint(0, (y_1))

		if x2<0:
			x2 = (y2+100)
			y2 = random.randint(0, (x2+1))

		if x3>500:
			x3 = (y3+100)
			y3 = random.randint(0, (x3-1))

		y -= mosca1_vely
		y_1 += mosca_vely
		x2 -= mosca2_velx
		x3 += mosca3_velx

		pantalla.blit(img_2,(0,0))
		label = fuente.render("PUNTOS:",1,rojo)
		pantalla.blit(p1,(110,5))
		pantalla.blit(label,(10,5))
		label2 = fuente.render(" / 20",1,negro)
		pantalla.blit(label2,(130,5))
		pantalla.blit(p2,(50,35))
		pantalla.blit(cora,(10,30))
		pantalla.blit(mosca,(x_1,y_1))
		pantalla.blit(mosca1,(x,y))
		pantalla.blit(mosca2,(x2,y2))
		pantalla.blit(mosca3,(x3,y3))

		pygame.display.update()
		fps.tick(500)
		pygame.display.flip()
#######################################################################################
def nivel3():
	pygame.init()
	pygame.mixer.init()

	pygame.display.set_caption("IRON FLY")
	pantalla = pygame.display.set_mode((500,512))

	#imagen de fondo
	img_3 = pygame.image.load('img/fondo3.png').convert_alpha()
	cora = pygame.image.load('img/life.png').convert_alpha()

	mosca = pygame.image.load('img/mosca1.png').convert_alpha()
	mosca1 = pygame.image.load('img/mosca2.png').convert_alpha()

	mosca2 = pygame.image.load('img/dead.png').convert_alpha()
	mosca3 = pygame.image.load('img/dead2.png').convert_alpha()

	pygame.mixer.music.load('sond/medieval.mp3')
	pygame.mixer.music.play(-1)
    
	x = 250
	y = 450
	x_1 = 260
	y_1 = 460
	x2 = 260
	y2 = 460
	x3 = 270
	y3 = 430

	mosca_velx = 1.1
	mosca1_velx = 1.1
	mosca2_vely = 1.5
	mosca3_vely = 1.5

	puntaje = 0
	vidas = 3

	fuente = pygame.font.Font(None,30)
	p1 = fuente.render(str(puntaje),0, negro)
	p2 = fuente.render(str(vidas),0, negro)
	
	run = True
	fps = pygame.time.Clock()
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				if mosca1.get_rect(top=y,left=x).collidepoint(mouse_pos) or mosca.get_rect(top=y_1,left=x_1).collidepoint(mouse_pos):
					puntaje += 1
					p1 = fuente.render(str(puntaje),0, negro)

					x = (y+100)
					y = random.randint(0, (y+100))
					x_1 = (y_1+100)
					y_1 = random.randint(0, (y_1+100))

					hit = pygame.mixer.Sound('sond/hit2.wav')
					hit.play()

					if puntaje == 15:
						win()
						run = False
						sys.exit()

				if mosca2.get_rect(top=y2,left=x2).collidepoint(mouse_pos) or mosca3.get_rect(top=y3,left=x3).collidepoint(mouse_pos):
					vidas -= 1
					p2 = fuente.render(str(vidas),0, negro)

					hit_mr = pygame.mixer.Sound('sond/hit3.wav')
					hit_mr.play()

					y2 = (x2+100)
					x2 = random.randint(0, (y2+1))

					y3 = (x3+100)
					x3 = random.randint(0, (y3-1))

					if vidas == 0:
						game_over()
						run = False
						sys.exit()
		
		if x>500:
			x = (y+100)
			y = random.randint(0, (x-1))

		if x_1<0:
			x_1 = (y_1+100)
			y_1 = random.randint(0, (x_1+1))

		if y2<0:
			y2 = (x2+200)
			x2 = random.randint(0, (y2))

		if y3>512:
			y3 = (x3+100)
			x3 = random.randint(0, (y3))

		x += mosca1_velx
		x_1 -= mosca_velx
		y2 -= mosca2_vely
		y3 += mosca3_vely

		pantalla.blit(img_3,(0,0))
		label = fuente.render("PUNTOS:",1,rojo)
		label2 = fuente.render(" / 15",1,negro)
		pantalla.blit(p1,(110,5))
		pantalla.blit(label,(10,5))
		pantalla.blit(label2,(130,5))
		pantalla.blit(p2,(50,35))
		pantalla.blit(cora,(10,30))
		pantalla.blit(mosca,(x_1,y_1))
		pantalla.blit(mosca1,(x,y))
		pantalla.blit(mosca2,(x2,y2))
		pantalla.blit(mosca3,(x3,y3))
		pygame.display.update()
		fps.tick(500)
		pygame.display.flip()
##########################################################################
pygame.init()

#COLORES
rojo = (255,0,0)
negro = (0,0,0)

#DIMENSION DE LA VENTANA
pantalla = pygame.display.set_mode((500,512))

#titulo de la ventana
pygame.display.set_caption("IRON FLY")

titulo = pygame.image.load('img/ironfly.png').convert_alpha()

#imagen de fondo INTRO
img_intro = pygame.image.load('img/intro.png').convert_alpha()

#TEXTO DE FONDO
fuente = pygame.font.SysFont("monospace",20)

#MUSICA DE FONDO
pygame.mixer.music.load('sond/intro.mp3')
pygame.mixer.music.play()

run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
        
        #imprimir fondo
		pantalla.blit(img_intro,(0,0))

		#imprimir titulo de fondo
		pantalla.blit(titulo,(90,0))

		#dibujar boton
		b1 = pygame.draw.rect(pantalla, (negro),(140,450,85,40))

		#texto dentro del boton
		label = fuente.render("JUGAR",1,rojo)
		pantalla.blit(label,(149,457))

		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			#si hace click en jugar se cierra la intro
			#da comienzo al nivel 1
			if b1.collidepoint(pos):
				pygame.quit()
				nivel1()
				run = False

	pygame.display.flip()

pygame.quit()