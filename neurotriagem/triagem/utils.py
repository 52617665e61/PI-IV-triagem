from datetime import date

def calcular_idade(data_nascimento):
    hoje = date.today()
    return hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

def calcular_subescalas(respostas):
    D = sum([respostas[i] for i in [0,1,2,3,4,5,6,7,8,34,35,39]])
    I = sum([respostas[i] for i in [16,17,18,19,20,31,32,36,42]])
    AE = sum([respostas[i] for i in [21,22,23,24,25,37,40]])
    H = sum([respostas[i] for i in [12,13,14,15,29,30,41]])

    AAMA_items = [respostas[i] for i in [9,10,11,26,27,28,33,38]]
    AAMA = sum([5 - v for v in AAMA_items])  # inversão automática

    return {"D": D, "I": I, "AE": AE, "AAMA": AAMA, "H": H}

def calcular_percentis(subescalas):
    r = subescalas
    p = {}

    p["D"] = (
        "Inferior" if r["D"] <= 21 else
        "Média Inferior" if r["D"] <= 29 else
        "Média" if r["D"] <= 38 else
        "Média Superior" if r["D"] <= 46 else
        "Superior"
    )

    p["I"] = (
        "Inferior" if r["I"] <= 24 else
        "Média Inferior" if r["I"] <= 31 else
        "Média" if r["I"] <= 39 else
        "Média Superior" if r["I"] <= 48 else
        "Superior"
    )

    p["AE"] = (
        "Inferior" if r["AE"] <= 2 else
        "Média Inferior" if r["AE"] <= 4 else
        "Média" if r["AE"] <= 6 else
        "Média Superior" if r["AE"] <= 8 else
        "Superior"
    )

    p["AAMA"] = (
        "Inferior" if r["AAMA"] <= 14 else
        "Média Inferior" if r["AAMA"] <= 16 else
        "Média" if r["AAMA"] <= 20 else
        "Média Superior" if r["AAMA"] <= 24 else
        "Superior"
    )

    p["H"] = (
        "Inferior" if r["H"] <= 9 else
        "Média Inferior" if r["H"] <= 12 else
        "Média" if r["H"] <= 14 else
        "Média Superior" if r["H"] <= 18 else
        "Superior"
    )

    return p

import google.generativeai as genai

genai.configure(api_key="chave")

model = genai.GenerativeModel("gemini-2.5-pro")

def gerar_relatorio_ia(percentis):
    prompt = f"""
Você é um psicólogo profissional treinado. Analise os seguintes resultados do teste TDAH-AD:

Desatenção (D): {percentis['D']};
Impulsividade (I): {percentis['I']};
Aspectos Emocionais (AE): {percentis['AE']};
Autorregulação (AAMA): {percentis['AAMA']};
Hiperatividade (H): {percentis['H']}.

Forneça um parecer técnico, sucinto.
Não use frases como: 
"dependeria de comparação com normas", 
"assumindo que escores altos indicam sintomas", 
"o teste isolado não indica diagnóstico", 
ou variações disso.
"""
    resp = model.generate_content(prompt)
    return resp.text.strip()

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from textwrap import wrap
from datetime import datetime
from io import BytesIO


def gerar_pdf_bytes(texto, paciente, psicologo, cidade):
    buffer = BytesIO()

    c = canvas.Canvas(buffer, pagesize=A4)
    largura, altura = A4
    y = altura - 2 * cm

    # Cabeçalho
    c.setFont("Helvetica-Bold", 12)
    c.drawString(2 * cm, y, f"Paciente: {paciente}")
    y -= 15
    c.drawString(2 * cm, y, f"Psicólogo Responsável: {psicologo}")
    y -= 40

    # Título
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(largura / 2, y, "Relatório TDAH-AD")
    y -= 30

    # Corpo
    c.setFont("Helvetica", 11)
    for linha in texto.split("\n"):
        for parte in wrap(linha, width=100):
            c.drawString(2 * cm, y, parte)
            y -= 15
            if y < 80:
                c.showPage()
                y = altura - 2 * cm
                c.setFont("Helvetica", 11)

    # Rodapé
    c.setFont("Helvetica-Oblique", 9)
    c.drawString(2 * cm, 1.8 * cm, f"Local: {cidade}")
    c.drawRightString(largura - 2 * cm, 1.8 * cm,
                      f"Data do relatório: {datetime.today().strftime('%d/%m/%Y')}")

    c.save()

    buffer.seek(0)
    return buffer
