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


#meio da tela
x_cobra= largura / 2
y_cobra = altura / 2

x_maca = randint(40, 600)
y_maca = randint(50, 430)


velocidade = 10
x_controle = velocidade
y_controle = 0

tela = pygame.display.set_mode(size = (largura, altura))

relogio = pygame.time.Clock()


fonte_1 = pygame.font.SysFont(
    name= 'arial',
    size= 20,
    bold=True,
    italic=False
)

fonte_2 = pygame.font.SysFont(
    name= 'arial',
    size= 40,
    bold=True,
    italic=False
)
pontos = 0

pygame.display.set_caption('Jogo')

comprimento_max_cobra = 5
lista_corpo_cobra = []
cabeca = []
morreu = False

#essa função serve pra 'DESENHAR' a cobra, ela cria um quadradinho pra cada posição da cobra
def aumenta_cobra(lista_corpo_cobra):
    for xey in lista_corpo_cobra:
        pygame.draw.rect(tela, (0,255,0), (xey[0], xey[1], 20,20))
        
        
while True:
    # velocidade do jogo (quantidade de frames/segundo)
    # Quanto maior o numero de frames mais rapido o jogo roda
    relogio.tick(25)
    
    # preenche a tela com preto (limpa a tela)
    tela.fill((255,255,255))
    
    if morreu == False:       
        menssagem = f'Pontos: {pontos}'
        texto_formatado = fonte_2.render(menssagem, True, (0,0,0))
        
        #pra cada interação do usuario:
        for event in pygame.event.get():
            
            #Caso o usuario queira sair so jogo:
            if event.type == QUIT:
                pygame.quit()
                exit()
            
        
            
            # se eu apertei qualquer tecla:
            # faz com que a cobra continue se movimentando com apenas um click
            if event.type == KEYDOWN:
                if event.key == K_a:
                    
                    
                    if x_controle == velocidade:
                        pass
                    
                    else:
                        x_controle = -velocidade
                        y_controle = 0 
                    
                if event.key == K_d:
                    if x_controle == -velocidade:
                        pass
                    
                    else:
                        x_controle = velocidade
                        y_controle = 0 

                if event.key == K_w:
                    if y_controle == velocidade:
                        pass
                    
                    else:
                        x_controle = 0
                        y_controle = -velocidade 

                if event.key == K_s:
                    if y_controle == -velocidade:
                        pass
                    
                    else:
                        x_controle = 0
                        y_controle = velocidade
                    
        x_cobra = x_cobra + x_controle
        y_cobra = y_cobra + y_controle
        
        if x_cobra > 640:
            x_cobra = 0
        if x_cobra < 0:
            x_cobra = 640
            
        if y_cobra < 0:
            y_cobra = 480
            
        if y_cobra > 480:
            y_cobra = 0

        
        cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra,y_cobra, 20, 20))
        maca = pygame.draw.rect(tela, (255,0,0), (x_maca, y_maca, 20, 20))
        
        # verifica se um objeto colide com outro:
        if cobra.colliderect(maca):
            pontos += 1
            musica_colisao.play(1)
            x_maca = randint(40, 600)
            y_maca = randint(50, 430)
            comprimento_max_cobra += 1

            
        #pra cada deslocamento da cobra eu adiciono a posição        
        lista_corpo_cobra.append([x_cobra, y_cobra])
        
        
        # se a ultima posição da cobra (cabeça) estiver na lista quer diser que a cobra
        # encostou em uma parte do corpo ja existente
        
        if lista_corpo_cobra.count([x_cobra, y_cobra]) > 1:
            print('morreu')
            morreu = True
        
        #esse if serve pra controlar o tamanho da cobra
        if len(lista_corpo_cobra) > comprimento_max_cobra:
            
            #deleta a ultima posição da cobra
            del lista_corpo_cobra[0]
        aumenta_cobra(lista_corpo_cobra)
    
        #coloca o texto na tela
        tela.blit(texto_formatado, (450, 40))
    
    else:
        pygame.mixer.music.play(0)
    
        menssagem = f'Game Over. Aperte R para reiniciar'
        texto_formatado = fonte_1.render(menssagem, True, (0,0,0)) 
        
        #coloca o texto na tela
        tela.blit(texto_formatado, (150, 100))
                
        lista_corpo_cobra.clear()
            
        x_cobra= largura / 2
        y_cobra = altura / 2
            
        pontos = 0
        
        for event in pygame.event.get():
        
            #Caso o usuario queira sair so jogo:
            if event.type == QUIT:
                pygame.quit()
                exit()
                
            if event.type == KEYDOWN:
                if event.key == K_r:
                        morreu = False
    
    #Pra cada interação o jogo tem que atualisar. Caso contrario ele trava
    pygame.display.update()