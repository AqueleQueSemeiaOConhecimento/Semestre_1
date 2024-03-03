import pygame 
import time
pygame.init()

print("Pygame version:", pygame.version.ver)

# Verifique se o Pygame foi inicializado corretamente
if not pygame.mixer.get_init():
    print("Erro: Pygame não foi inicializado corretamente.")
else:
    print("Pygame foi inicializado corretamente.")

# Tente carregar e reproduzir a música
try:
    pygame.mixer.music.load('python/teste_2/msc/msc.mp3')
    pygame.mixer.music.play()
    print("Música tocando...")
except pygame.error as e:
    print("Erro ao carregar ou reproduzir música:", e)

time.sleep(20)
pygame.quit()