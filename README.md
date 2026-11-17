# 🕳️ Simulação Visual de um Buraco Negro em Python

Arte generativa que simula visualmente um **Buraco Negro** (inspirado no Gargantua, de *Interestelar*) com disco de acreção e efeito de lente gravitacional, desenvolvido utilizando apenas bibliotecas nativas do Python.

## 📸 Resultado

<img width="1920" height="1080" alt="black_hole" src="https://github.com/user-attachments/assets/f51d9d97-95fa-4dbc-a1ae-68631cf9000b" />


> *Nota: Para que a imagem acima apareça no GitHub, salve o print da tela com o nome `black_hole.png` na mesma pasta do arquivo ou cole a imagem diretamente no editor do README.*

---

## ✨ O que o código faz

A cena é construída em **5 camadas** sobrepostas para criar a ilusão de profundidade 3D:

1. **Fundo Estrelado:** Espalha estrelas de tamanhos variados pelo espaço.
2. **Lente Gravitacional:** Simula a luz do disco traseiro sendo curvada por cima e por baixo do buraco negro devido à gravidade extrema.
3. **Disco de Acreção (Parte Traseira):** Desenha a metade de trás do anel de gás superaquecido.
4. **Horizonte de Eventos:** Desenha o anel de fótons e a esfera negra central que bloqueia a luz que passa atrás dela.
5. **Disco de Acreção (Parte Frontal):** Sobrepõe a metade da frente do disco sobre a esfera negra, criando o efeito 3D.

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

Nenhuma instalação externa é necessária. O projeto usa apenas módulos padrão do **Python 3**:

* **`turtle`**: Criação da janela gráfica e renderização dos pontos na tela.
* **`math`**: Trigonometria (`sin`, `cos`, `pi`) para órbitas circulares e matriz de rotação 2D/3D.
* **`colorsys`**: Conversão de cores **HSV para RGB** para gerar o degradê de temperatura do plasma (do vermelho frio nas bordas ao branco incandescente no centro).
* **`random`**: Distribuição gaussiana e variações naturais nas partículas de gás.

---

## 🚀 Como Executar

1. Certifique-se de ter o **Python 3** instalado na sua máquina.
2. Clone este repositório:
   ```bash
3. git clone [(https://github.com/caiobraza/blackhole.git)
