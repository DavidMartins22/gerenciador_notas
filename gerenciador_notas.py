# ==========================================
# --- gerenciador_notas.py ---
# ==========================================

# Lista de dicionários utilizada para armazenar os dados dos estudantes.
# Cada estudante possui um nome (string) e uma lista de notas (float).

estudantes = [
    {
        'nome': 'Ana',
        'notas': [8.5, 7.0, 9.0]
    },

    {
        'nome': 'Carlos',
        'notas': [6.5, 7.5, 8.0]
    },

    {
        'nome': 'Mariana',
        'notas': [9.5, 8.0, 10.0]
    },

    {
        'nome': 'Lucas',
        'notas': [9.5, 6.5, 8.5]
    }
]

def calcular_media(notas):
    """
    Calcula a média das notas do estudante.

    Args:
        notas (list): Lista contendo notas do tipo float.

    Returns:
        float: Média calculada das notas.
    """

    if len(notas) == 0:
        return 0
    
    media = sum(notas) / len(notas)
    return media

def verificar_aprovacao(media, media_minima=7.0):
    """
    Verifica se o estudante foi aprovado ou reprovado.

    Args:
        media (float): Média final do estudante.
        media_minima (float): Média mínima para aprovação.

    Returns:
        str: 'Aprovado' ou 'Reprovado'.
    """

    if media >= media_minima:
        return 'Aprovado'
    else:
        return 'Reprovado'
    
def gerar_relatorio(alunos):
    """
    Gera um relatório com nome, média e situação dos estudantes.

    Args:
        alunos (list): Lista de dicionários contendo os dados dos estudantes.
    """

    print('\n=== RELATÓRIO DE DESEMPENHO ===')

    for aluno in alunos:
        media = calcular_media(aluno['notas'])
        situacao = verificar_aprovacao(media)

        print(f'Nome: {aluno['nome']}')
        print(f'Média: {media:.2f}')
        print(f'Situação: {situacao}')
        print('--------------------------------')

# Execução do relatório
gerar_relatorio()