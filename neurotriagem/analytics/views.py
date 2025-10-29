from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from django.utils import timezone
from django.db.models import Count, Avg
from user.models import NormalUser
from triagem.models import Triagem
import pandas as pd
import plotly.express as px
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count, Avg
from user.models import NormalUser
from triagem.models import Triagem
from triagem.forms import TriagemForm
import plotly.express as px
import pandas as pd

def dashboard_view(request):
    now = timezone.now()
    semana_inicio = now - timedelta(days=7)
    mes_inicio = now - timedelta(days=30)
    trimestre_inicio = now - timedelta(days=90)

    # Contagem total de pacientes
    total_pacientes = NormalUser.objects.count()

    # Total de testes realizados
    total_testes = Triagem.objects.count()

    # Testes realizados em períodos
    testes_ultima_semana = Triagem.objects.filter(data_envio__gte=semana_inicio).count()
    testes_mes = Triagem.objects.filter(data_envio__gte=mes_inicio).count()
    testes_trimestre = Triagem.objects.filter(data_envio__gte=trimestre_inicio).count()

    # --- Itens comentados por ausência de relacionamento no modelo atual ---

    # pacientes_com_um_teste = NormalUser.objects.annotate(num_testes=Count('triagem')).filter(num_testes=1).count()

    # pacientes_multiplos_testes_mesmo = Triagem.objects.values('paciente', 'teste').annotate(num=Count('id')).filter(num__gt=1).count()

    # testes_populares = Triagem.objects.values('teste__nome').annotate(qtd=Count('id')).order_by('-qtd')[:5]

    # media_testes_por_paciente = Triagem.objects.values('paciente').annotate(qtd=Count('id')).aggregate(media=Avg('qtd'))['media']

    # ultimos_resultados = Triagem.objects.select_related('paciente', 'teste').order_by('-data_realizacao')[:10]

    # --- FIM dos itens comentados ---

    # Gráfico de testes por semana
    df = pd.DataFrame({
        "Período": ["Última semana", "Último mês", "Último trimestre"],
        "Testes realizados": [testes_ultima_semana, testes_mes, testes_trimestre],
    })
    fig = px.bar(df, x="Período", y="Testes realizados", title="Testes Realizados por Período")
    chart_html = fig.to_html(full_html=False)

    context = {
        'total_pacientes': total_pacientes,
        'total_testes': total_testes,
        'testes_ultima_semana': testes_ultima_semana,
        'testes_mes': testes_mes,
        'testes_trimestre': testes_trimestre,
        'chart': chart_html,

        # Comentados por enquanto:
        # 'pacientes_com_um_teste': pacientes_com_um_teste,
        # 'pacientes_multiplos_testes_mesmo': pacientes_multiplos_testes_mesmo,
        # 'testes_populares': testes_populares,
        # 'media_testes_por_paciente': round(media_testes_por_paciente or 0, 2),
        # 'ultimos_resultados': ultimos_resultados,
    }

    return render(request, "analytics/visao_geral.html", context)

def pacients_list(request):
    pacients = NormalUser.objects.all().order_by('id')
    context = {'pacients': pacients}
    return render(request, 'analytics/pacient_list.html', context)


def paciente_detail_view(request, id):
    user = get_object_or_404(NormalUser, id=id)
    tests = Triagem.objects.filter(usuario=user).select_related('teste').order_by('-data_envio')

    context = {
        'user': user,
        'tests': tests
    }
    return render(request, 'analytics/pacient_detail.html', context)

@login_required
def triagem_detail_view(request, id):
    triagem = get_object_or_404(Triagem, id=id)
    form = TriagemForm(instance=triagem)

    respostas = [(field.label, getattr(triagem, name))
                 for name, field in form.fields.items() if name.startswith('tr')]

    if request.method == "POST":
        revisado = request.POST.get("revisado") == "on"
        comentario = request.POST.get("comentario", "")

        # pega a instância real do psicólogo logado
        psicologo = request.user.get_real_instance()

        triagem.revisado = revisado
        triagem.comentario_revisor = comentario
        triagem.psicologo_revisor = psicologo
        triagem.data_revisao = timezone.now()
        triagem.save()

        return redirect('analytics:pacient_detail', triagem.usuario.id)

    context = {
        "triagem": triagem,
        "respostas": respostas
    }
    return render(request, "analytics/triagem_detail.html", context)

