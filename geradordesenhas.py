#maiusculas e minusculas
#simbolos e espaço

chave = input('Digite a base da sua senha:')

senha = ''

for letra in chave:
#regra de substituição
      if letra in 'Aa':   senha = senha + '10'
      elif letra in 'Bb': senha = senha +'1'
      elif letra in 'Cc': senha = senha +'&'
      elif letra in 'Dd':  senha = senha +'3'
      elif letra in 'Ee':senha = senha +'*'
      elif letra in 'Ff': senha = senha +'15'
      elif letra in 'Rr': senha = senha + '#'  
      elif letra in 'Ss': senha = senha + '%'
      elif letra in 'Mm': senha = senha + '@'
      else: senha = senha +letra

      print(senha)