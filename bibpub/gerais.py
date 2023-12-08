def num_cpf_valido(num_cpf):
   """ Valida o número do CPF.
      Argumento:
            cpf: O número do CPF a ser validado.
      Returna:
            Retorna `True` se o número do CPF for válido, `False` caso contrário.
   """
   cpf = num_cpf.replace('.', '').replace('-', '')
   cpf_list = list(cpf)
   mult = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
   soma = 0
   for index, digito in enumerate(cpf_list):
      soma += int(digito) * mult[index]
   resto = soma % 11
   return cpf_list[9] == str(resto)