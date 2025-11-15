from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseForbidden
from .models import Triagem, Teste
from user.models import NormalUser
from .forms import TriagemForm
from .loading_ml.tdah_prediction import prever_triagem
from .utils import (
    calcular_idade,
    gerar_pdf_bytes,
    gerar_relatorio_ia,
    calcular_subescalas,
    calcular_percentis,
)


def gerar_pdf_relatorio(triagem, respostas):
    """Gera PDF a partir das respostas de uma triagem."""
    subescalas = calcular_subescalas(respostas)
    percentis = calcular_percentis(subescalas)
    texto_relatorio = gerar_relatorio_ia(percentis)

    # Constrói o nome completo manualmente
    paciente_nome = f"{triagem.usuario.first_name} {triagem.usuario.last_name}"

    pdf_bytes = gerar_pdf_bytes(
        texto=texto_relatorio,
        paciente=paciente_nome,
        psicologo="SEU NOME - CRP",
        cidade="Cidade"
    )

    response = HttpResponse(pdf_bytes, content_type="application/pdf")
    response['Content-Disposition'] = f'inline; filename="relatorio_{triagem.id}.pdf"'
    return response


def triagem_view(request, teste_nome):
    teste = get_object_or_404(Teste, nome=teste_nome)

    if not request.user.is_authenticated:
        return redirect('login')

    resultado = None
    instancia = None

    if request.method == 'POST':
        form = TriagemForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)

            usuario_real = request.user.get_real_instance()
            if not isinstance(usuario_real, NormalUser):
                return HttpResponseForbidden("Apenas usuários normais podem realizar triagens.")

            # Preenche informações do usuário
            instancia.usuario = usuario_real
            instancia.teste = teste
            instancia.age = calcular_idade(usuario_real.born)
            instancia.gender = usuario_real.gender

            # Prepara dados para IA
            dados_ml = form.cleaned_data.copy()
            dados_ml['gender'] = usuario_real.gender
            dados_ml['age'] = instancia.age

            # Faz previsão
            resultado_ml = prever_triagem(dados_ml)

            # Salva resultados na instância
            instancia.resultado_ml = resultado_ml['classe']
            instancia.probabilidades_ml = resultado_ml.get('probabilidades')
            instancia.save()

            resultado = resultado_ml

            # Se o usuário clicou em "Gerar PDF"
            if 'baixar_pdf' in request.POST:
                respostas = [dados_ml.get(f"tr{i}") for i in range(1, 44)]
                return gerar_pdf_relatorio(instancia, respostas)

    else:
        form = TriagemForm()

    return render(request, 'triagem/formulario.html', {
        'form': form,
        'resultado': resultado,
        'teste': teste,
        'triagem': instancia
    })


def visualizar_relatorio(request, triagem_id):
    triagem = get_object_or_404(Triagem, id=triagem_id)

    # Recupera respostas da triagem
    respostas = [getattr(triagem, f"tr{i}") for i in range(1, 44)]
    return gerar_pdf_relatorio(triagem, respostas)
