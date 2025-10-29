from django import forms
from .models import Triagem

class TriagemForm(forms.ModelForm):
    class Meta:
        model = Triagem
        fields = '__all__'
        labels = {
            'tr1': 'Eu realmente não presto atenção aos detalhes:',
            'tr2': 'Já fui acusado de imprecisões no meu trabalho:',
            'tr3': 'Frequentemente cometo erros por descuido em minhas atividades:',
            'tr4': 'Tenho dificuldade em manter minha atenção no trabalho:',
            'tr5': 'Tenho dificuldade em manter o foco ao ler textos longos:',
            'tr6': 'Tenho dificuldade em manter o foco durante conversas:',
            'tr7': 'Meus familiares me culpam por não ouvir quando eles falam:',
            'tr8': 'Minha mente frequentemente está em outro lugar, mesmo quando não há distração aparente:',
            'tr9': 'Tenho dificuldade em seguir instruções:',
            'tr10': 'Tenho dificuldade em completar minhas tarefas (no trabalho, em casa):',
            'tr11': 'Tenho dificuldade em manter o foco durante minhas atividades (domésticas, profissionais):',
            'tr12': 'Tenho dificuldade em organizar meu tempo:',
            'tr13': 'Meu trabalho geralmente é confuso ou desorganizado:',
            'tr14': 'É difícil para mim organizar tarefas que exigem várias etapas:',
            'tr15': 'Tenho tendência a evitar tarefas que exigem esforço mental contínuo (lição de casa, redação de um relatório, etc.):',
            'tr16': 'Frequentemente acho difícil realizar trabalhos que exigem esforço mental contínuo (trabalhos escolares, escrever um relatório):',
            'tr17': 'Tenho tendência a agir no último minuto:',
            'tr18': 'Frequentemente perco coisas de que preciso para minha vida diária:',
            'tr19': 'Frequentemente perco coisas de que preciso para o meu trabalho:',
            'tr20': 'Frequentemente perco coisas de que preciso para minhas atividades/lazer:',
            'tr21': 'Sou facilmente distraído pelo meu ambiente:',
            'tr22': 'Frequentemente sou distraído por pensamentos não relacionados à atividade que estou fazendo:',
            'tr23': 'Sou facilmente distraído pelo que está acontecendo ao meu redor:',
            'tr24': 'Frequentemente sou esquecido em minha vida diária (fazendo tarefas domésticas, fazendo compras...):',
            'tr25': 'Frequentemente tenho dificuldade em cumprir minhas obrigações (compromissos, retornar ligações, pagar contas...):',
            'tr26': 'Frequentemente balanço minhas mãos ou pés enquanto estou sentado:',
            'tr27': 'Tenho dificuldade em ficar quieto:',
            'tr28': 'Frequentemente saio do meu assento desnecessariamente durante uma reunião:',
            'tr29': 'Frequentemente saio do meu assento desnecessariamente no trabalho:',
            'tr30': 'Frequentemente me levanto do assento quando não é apropriado fazê-lo:',
            'tr31': 'As pessoas ao meu redor acham que sou uma pessoa inquieta:',
            'tr32': 'Frequentemente demonstro impaciência em circunstâncias inapropriadas:',
            'tr33': 'Tenho dificuldade em ficar parado quando a situação exige:',
            'tr34': 'As pessoas próximas a mim me acham difícil de acompanhar:',
            'tr35': 'As pessoas ao meu redor me consideram uma pessoa impaciente:',
            'tr36': 'É difícil para mim ficar sentado por muito tempo:',
            'tr37': 'Tenho tendência a monopolizar conversas:',
            'tr38': 'Frequentemente dou a resposta a uma pergunta antes que ela seja concluída:',
            'tr39': 'Frequentemente termino as frases das outras pessoas:',
            'tr40': 'Tenho dificuldade em esperar minha vez de falar em uma conversa:',
            'tr41': 'É difícil para mim esperar minha vez em uma fila:',
            'tr42': 'Frequentemente interrompo os outros quando estão ocupados:',
            'tr43': 'Frequentemente me imponho em conversas:'
        }
        exclude = ['usuario', 'teste', 'age', 'gender', 'resultado_ml', 'probabilidades_ml',
                   'data_envio', 'psicologo_revisor', 'revisado', 'comentario_revisor', 'data_revisao']