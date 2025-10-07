import pandas as pd
import numpy as np

df = pd.read_csv("C:\Users\USER\Desktop\dataser_PI-IV\893 participants.csv")


colunas_escala_10 = ['Q7, Q8,	Q9,	Q10,	Q11,	Q12,	Q13,	Q14,	Q15,	Q16,	Q17,	Q18,	Q19,	Q20,	Q21,	Q22,	Q23,	Q24,	Q25,	Q26,	Q27,	Q28,	Q29,	Q30,	Q31,	Q32,	Q33,	Q34,	Q35,	Q36,	Q37,	Q38,	Q39,	Q40,	Q41,	Q42,	Q43,	Q44,	Q45,	Q46,	Q47,	Q48,	Q49,	Q50,	Q51,	Q52,	Q53,	Q54,	Q55,	Q56,	Q57,	Q58,	Q59,	Q60,	Q61,	Q62,	Q63,	Q64,	Q65,	Q66,	Q67,	Q68,	Q69,	Q70,	Q71,	Q72,	Q73,	Q74,	Q75,	Q76,	Q77,	Q78,	Q79,	Q80,	Q81,	Q82,	Q83,	Q84,	Q85,	Q86,	Q87,	Q88,	Q89,	Q112,	Q113,	Q114,	Q115,	Q116,	Q117,	Q118,	Q119,	Q120,	Q121,	Q122,	Q123,	Q124,	Q125,	Q126,	Q127,	Q128,	Q129,	Q130,	Q131,	Q132,	Q133,	Q134,	Q135,	Q136,	Q137,	Q138,	Q139,	Q140,	Q141,	Q142,	Q143,	Q144,	Q145,	Q146,	Q147,	Q148,	Q149,	Q150,	Q151,	Q152,	Q153,	Q154,	Q155,	Q156,	Q157,	Q158,	Q159,	Q160,	Q161,	Q162,	Q163,	Q164,	Q165,	Q166,	Q167,	Q168,	Q169,	Q170,	Q171,	Q172,	Q173,	Q174,	Q175,	Q176,	Q177,	Q178,	Q179,	Q180,	Q181,	Q182,	Q183,	Q184,	Q185,	Q186,	Q187,	Q188,	Q189,	Q190,	Q191,	Q192,	Q193,	Q194,	Q195,	Q196,	Q197']

# Detectar colunas com escala de 1 a 10 (valores entre 1 e 10)
for col in df.columns:
    try:
        valores_unicos = df[col].dropna().unique()
        if all((val >= 1 and val <= 10) for val in valores_unicos) and len(valores_unicos) > 5:
            colunas_escala_10.append(col)
    except:
        continue

# Função de rebalanceamento
def rebalancear_1a10_para_1a5(valor):
    return round(((valor - 1) / 9) * 4 + 1)

df[colunas_escala_10] = df[colunas_escala_10].applymap(rebalancear_1a10_para_1a5)


df.to_csv("dataset_rebalanceado.csv", index=False)
