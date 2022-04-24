def percentual_arredondado(valor, total):
 return round(valor/total, 4)
def percentual_status(resultados):
   # Recebe uma lista do tipo [('Nome', nota, reprovou_falta, fez_quarta_prova), (), ()]
   # Retorna (aprovados, aprovados_quarta_prova, reprovados_nota, reprovados_falta)
   aprovados = 0
   aprovados_quarta_prova = 0
   reprovados_nota = 0
   reprovados_falta = 0
   for elemento in resultados:
      if (elemento[2] == True):
         reprovados_falta = reprovados_falta + 1
      elif (elemento[3] == True and elemento[1] >= 5):
         aprovados_quarta_prova = aprovados_quarta_prova + 1
      elif (elemento[3] == False and elemento[1] >= 7):
         aprovados = aprovados + 1
      else:
         reprovados_nota = reprovados_nota + 1
   return percentual_arredondado(aprovados, len(resultados)), percentual_arredondado(aprovados_quarta_prova, len(resultados)), percentual_arredondado(reprovados_nota, len(resultados)), percentual_arredondado(reprovados_falta, len(resultados))