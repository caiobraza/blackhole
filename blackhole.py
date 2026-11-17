# --- 1. IMPORTAÇÃO DAS BIBLIOTECAS ---
import turtle    # Biblioteca nativa para abrir uma janela e desenhar formas/pontos na tela
import colorsys  # Biblioteca para converter cores de um padrão (HSV) para outro (RGB)
import math      # Biblioteca de matemática (traz seno, cosseno, pi, etc.)
import random    # Biblioteca para sortear números aleatórios

# --- 2. CONFIGURAÇÕES GERAIS ---
random.seed(42)  # Trava o sorteio aleatório: toda vez que rodar, o desenho sai igual
TILT = -0.22     # Define a inclinação do disco do buraco negro na tela

# --- 3. PREPARANDO A JANELA ---
screen = turtle.Screen()     # Cria a janela onde o desenho vai aparecer
screen.setup(800, 500)       # Define o tamanho da janela: 800 de largura por 500 de altura
screen.bgcolor("#020208")    # Pinta o fundo da janela de azul bem escuro (quase preto)
screen.colormode(1.0)        # Avisa o Python que as cores vão variar de 0.0 a 1.0
screen.tracer(40)            # Só atualiza a imagem na tela a cada 40 pontos (deixa bem mais rápido)

# --- 4. PREPARANDO O PINCEL ---
t = turtle.Turtle()          # Cria o "pincel" que vai desenhar os pontos
t.hideturtle()               # Esconde a setinha do pincel para não atrapalhar o visual
t.speed(0)                   # Coloca a velocidade do pincel no máximo possível
t.penup()                    # Levanta o pincel do papel (ele anda sem riscar linhas entre os pontos)

# --- 5. FUNÇÕES DE APOIO (COR E POSIÇÃO) ---
def plasma_color(heat, v=1.0):
    # Calcula a cor do gás quente conforme o nível de calor (heat vai de 0 a 1)
    hue = 0.02 + heat * 0.11       # Muda a cor do vermelho (0.02) até o amarelo (0.13)
    sat = 1.0 - (heat ** 2) * 0.7  # Tira um pouco da cor forte no centro para parecer branco brilhante
    return colorsys.hsv_to_rgb(hue, sat, v)  # Converte essa cor para o formato RGB que a tela entende

def place_tilted(x, y):
    # Posiciona o pincel dando um efeito 3D inclinado
    y *= 0.32                              # Achata a altura (Y) para o círculo parecer visto de lado
    c, s = math.cos(TILT), math.sin(TILT)  # Calcula o seno e cosseno do ângulo de inclinação
    t.goto(x * c - y * s, x * s + y * c)   # Move o pincel para a nova posição já inclinada

# --- 6. DESENHANDO AS CAMADAS ---
def background_stars():
    # Desenha 180 estrelas no fundo
    for _ in range(180):                        # Repete o bloco abaixo 180 vezes
        x = random.randint(-395, 395)           # Sorteia uma posição na horizontal
        y = random.randint(-245, 245)           # Sorteia uma posição na vertical
        t.goto(x, y)                            # Move o pincel até lá
        t.dot(random.randint(1, 3), "white")    # Desenha uma bolinha branca pequena (1 a 3 pixels)

def gravitational_lens(count):
    # Desenha o halo de luz que contorna o buraco negro por cima e por baixo
    for _ in range(count):                      # Repete o desenho conforme a quantidade pedida
        is_top = random.choice([True, False])   # Sorteia se o ponto vai para o arco de cima ou de baixo
        if is_top:
            angle = random.uniform(0.15, math.pi - 0.15)              # Ângulo na metade de cima
        else:
            angle = random.uniform(math.pi + 0.15, 2 * math.pi - 0.15) # Ângulo na metade de baixo
        
        dist = random.gauss(0, 1)               # Gera um número concentrado perto de zero
        r = 74 + abs(dist) * 16                 # Define a distância do centro (logo fora da esfera negra)
        heat = max(0, min(1, 1 - (r - 74) / 34)) # Quanto mais perto da borda preta, mais quente/claro
        
        x = r * math.cos(angle)                 # Transforma o ângulo e distância em posição X
        y = r * math.sin(angle) * 0.92          # Transforma em posição Y (levemente oval)
        c, s = math.cos(TILT), math.sin(TILT)   # Prepara a rotação
        t.goto(x * c - y * s, x * s + y * c)    # Move o pincel para a posição final do halo
        
        # Desenha o ponto luminoso do halo
        t.dot(random.randint(2, 4), plasma_color(heat, random.uniform(0.5, 0.95)))

def accretion_disk(count, front_half=False):
    # Desenha o anel de gás girando ao redor (metade de trás ou metade da frente)
    for _ in range(count):
        if front_half:
            angle = random.uniform(math.pi, 2 * math.pi)  # Sorteia ângulos da parte da frente
        else:
            angle = random.uniform(0, math.pi)            # Sorteia ângulos da parte de trás
            
        progress = random.random() ** 1.4      # Concentra mais partículas perto do centro
        r = 78 + progress * 212                # Define o raio: vai de 78 (perto) até 290 (longe)
        
        # Cria ondas suaves na cor para parecer gás em movimento
        turbulence = math.sin(r * 0.18 + angle * 3) * 0.15
        heat = max(0, min(1, (1 - progress) + turbulence)) # Calcula a temperatura do ponto
        
        x = r * math.cos(angle)                            # Calcula posição X no círculo
        y = r * math.sin(angle) + random.gauss(0, 3)       # Calcula posição Y com leve tremor
        place_tilted(x, y)                                 # Move o pincel aplicando a inclinação 3D
        
        # Define tamanho (maior perto do centro) e brilho (apaga nas bordas)
        size = random.randint(2, 4) if progress < 0.6 else random.randint(1, 3)
        brightness = random.uniform(0.6, 1.0) * (1 - progress * 0.45)
        t.dot(size, plasma_color(heat, brightness))        # Desenha o ponto de gás

def event_horizon():
    # Desenha o centro escuro do buraco negro
    t.goto(0, 0)           # Vai exatamente para o meio da tela
    t.dot(146, "#ffeaad")  # Desenha um círculo claro (borda de luz presa pela gravidade)
    t.dot(140, "#000000")  # Desenha um círculo preto um pouco menor por cima (a sombra)

# --- 7. ORDEM DE EXECUÇÃO ---
background_stars()                      # 1º: Pinta o céu estrelado no fundo
gravitational_lens(1400)                # 2º: Desenha o arco de luz dobrada
accretion_disk(2200, front_half=False)  # 3º: Desenha a metade de trás do anel de gás
event_horizon()                         # 4º: Desenha a bola preta (cobrindo o anel de trás)
accretion_disk(2200, front_half=True)   # 5º: Desenha a metade da frente por cima da bola preta

screen.update()  # Mostra os últimos pontos que faltavam na tela
turtle.done()    # Mantém a janela aberta até você clicar no X para fechar