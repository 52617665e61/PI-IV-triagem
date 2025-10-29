from django.db import models

class Teste(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Triagem(models.Model):
    usuario = models.ForeignKey('user.NormalUser', on_delete=models.CASCADE, related_name='triagens')
    teste = models.ForeignKey('Teste', on_delete=models.CASCADE, related_name='respostas')
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=[('1', 'Masculino'), ('0', 'Feminino')])
    tr1 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr2 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr3 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr4 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr5 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr6 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr7 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr8 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr9 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr10 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr11 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr12 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr13 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr14 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr15 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr16 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr17 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr18 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr19 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr20 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr21 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr22 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr23 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr24 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr25 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr26 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr27 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr28 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr29 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr30 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr31 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr32 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr33 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr34 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr35 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr36 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr37 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr38 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr39 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr40 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr41 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr42 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    tr43 = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    
    resultado_ml = models.TextField(blank=True, null=True)
    probabilidades_ml = models.JSONField(blank=True, null=True)
    data_envio = models.DateTimeField(auto_now_add=True)
    psicologo_revisor = models.ForeignKey(
        'user.PsicologoUser', on_delete=models.SET_NULL, null=True, blank=True, related_name='triagens_corrigidas'
    )
    revisado = models.BooleanField(default=False)
    comentario_revisor = models.TextField(blank=True, null=True)
    data_revisao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.usuario} - {self.age} anos"
