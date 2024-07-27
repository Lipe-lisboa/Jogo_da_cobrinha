import pygame
from pygame.locals import *
from sys import exit
from random import randint # sorteia um valor em um determinado intervalo

pygame.init()

# o valor da musica tem que variar de  0 a 1
pygame.mixer.music.set_volume(0.3)

musica_de_fundo = pygame.mixer.music.load('Super Mario Bros. Theme Song.mp3')
pygame.mixer.music.play(-1)
musica_colisao= pygame.mixer.Sound('smw_coin.wav')

largura = 640
altura = 480 
#eixo X tem 640px
#eixo y tem 280px (no pygame p eixo y é na verticar pra baixo)

x_vermelho = largura / 2
y_vermelho = altura / 2

x_verde = randint(40, 600)
y_verde = randint(50, 430)

tela = pygame.display.set_mode(size = (largura, altura))
fonte = pygame.font.SysFont(
    name= 'arial',
    size=40,
    bold=True,
    italic=False
    )

relogio = pygame.time.Clock()

pontos = 0

pygame.display.set_caption('Jogo')

while True:
    # velocidade do jogo (quantidade de frames/segundo)
    # Quanto maior o numero de frames mais rapido o jogo roda
    relogio.tick(80)
    
    
    # preenche a tela com preto (limpa a tela)
    tela.fill((0,0,0))
    
    menssagem = f'Pontos {pontos}'
    
    texto_formatado = fonte.render(menssagem, True, (255,255,255))
    
    #pra cada interação do usuario:
    for event in pygame.event.get():
        
        #Caso o usuario queira sair so jogo:
        if event.type == QUIT:
            pygame.quit()
            exit()
        
       
        '''
        # se eu apertei qualquer tecla:
        if event.type == KEYDOWN:
            if event.key == K_a:
                if (x  != 0):
                    x -= 20
                
            if event.key == K_d:
                if (x != 640):
                    x += 20

            if event.key == K_w:
                if (y != 0):
                    y -= 20
                     

            if event.key == K_s:
                if (y != 480):
                    y += 20 '''
    
    if pygame.key.get_pressed()[K_a]:
        x_vermelho -= 5
        if (x_vermelho  < 0):
            x_vermelho = 680    
            
    if pygame.key.get_pressed()[K_d]:
        x_vermelho += 5
        
        if (x_vermelho  > 680):
            x_vermelho = 0
            
    if pygame.key.get_pressed()[K_w]:
        y_vermelho -= 5
        
        if (y_vermelho  < 0):
            y_vermelho = 480
            
    if pygame.key.get_pressed()[K_s]:
        y_vermelho += 5
        
        if (y_vermelho  > 480):
            y_vermelho = 0
            
    rt_vermelho = pygame.draw.rect(tela, (255,0,0), (x_vermelho, y_vermelho, 40, 50))
    rt_verde = pygame.draw.rect(tela, (0,255,0), (x_verde,y_verde, 40, 50))
    
    # verifica se um objeto colide com outro:
    if rt_vermelho.colliderect(rt_verde):
        pontos += 1
        musica_colisao.play(1)
        x_verde = randint(40, 600)
        y_verde = randint(50, 430)
    
    tela.blit(texto_formatado, (450, 40))
    #Pra cada interação o jogo tem que atualisar. Caso contrario ele trava
    pygame.display.update()