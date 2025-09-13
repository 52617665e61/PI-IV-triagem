from django.shortcuts import render
import pandas as pd
import plotly.express as px

def dashboard_view(request):
    df = pd.DataFrame({
        "Categoria": ["TDAH", "Autismo", "Ansiedade"],
        "Pacientes": [30, 20, 50]
    })

    fig = px.bar(df, x="Categoria", y="Pacientes", title="Distribuição de Diagnósticos")

    chart_html = fig.to_html(full_html=False)

    return render(request, "analytics/visao_geral.html", {"chart": chart_html})

def paciente_detail_view(request, paciente_id):
    return render(request, 'analytics/pacient_detail.html', {'paciente_id': paciente_id})
