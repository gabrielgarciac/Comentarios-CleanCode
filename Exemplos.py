# Exemplo de comentário bom:


# Comentários que citam direiros autorais:

# Direitos autorais (C) 2003, 2004, 2005, por Object Mentor, Inc. Todos os direitos reservados.
# Distribuido sob os termos da versão 2 ou posterior da Licenca Publica Geral da GNU.


# Comentários em que você encontra um modo para não ter que escreve-lo.

# Em vez disto:

    escolha = 0
    desempenho = 0
    DAMPlayer = 0

    # Atribuição de dano extra pela escolha da arma.

    if escolha == 1 and desempenho == 1:
        DAMPlayer += 8
    elif escolha == 2 and desempenho == 1:
        DAMPlayer += 12
    elif escolha == 3 and desempenho == 1:
       DAMPlayer += 19

    elif escolha == 1 and desempenho == 2:
       DAMPlayer += 12
    elif escolha == 2 and desempenho == 2:
       DAMPlayer += 17
    elif escolha == 3 and desempenho == 2:
       DAMPlayer += 20

    elif escolha == 1 and desempenho == 2:
       DAMPlayer += 19
    elif escolha == 2 and desempenho == 3:
       DAMPlayer += 23
    elif escolha == 3 and desempenho == 3:
       DAMPlayer += 35

# Isto:

    def adicionarDanoExtra(escolha, desempenho):
        DAMPlayer = 0

        if escolha == 1 and desempenho == 1:
            DAMPlayer += 8
        # ...

    adicionarDanoExtra(escolha, desempenho):




# Exemplo de comentário ruim:

# Comentários de créditos de autoria:

# INÍCIO PARTE GLADEMIR
# if livro == 5:
# ...
# ...
# FIM PARTE GLADEMIR



# Comentários redundântes:

# PlayerDodgeChance = 0  # Chance de desvio do player.
# BossDodgeChance = 0  # Chance de desvio do Boss.

