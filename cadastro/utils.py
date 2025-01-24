def validador(cpf):
    cpf = cpf.replace('.', '').replace('-', '')
    if len(cpf) == 11:
        if cpf == '00000000000' or cpf == '11111111111' or cpf == '22222222222' or cpf == '33333333333' or cpf == '44444444444' or cpf == '55555555555' or cpf == '66666666666' or cpf == '77777777777' or cpf == '88888888888' or cpf == '99999999999':
            return False
        else:
            soma = 0
            for ncpf in range(9):
                soma += int(cpf[ncpf]) * (10 - ncpf)
            soma = soma * 10 % 11
            if soma == int(cpf[9]):
                soma = 0
                for ncpf in range(10):
                    soma += int(cpf[ncpf]) * (11 - ncpf)
                soma = soma * 10 % 11
                if soma == int(cpf[10]):
                    return True
                else:
                    return False
            else:
                return False
    else:
        return False