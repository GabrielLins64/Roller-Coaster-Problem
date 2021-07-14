import os
from numpy import mean

REPORT_PATH = "logs/"


def gerar_relatorio(parametros, tempos_espera_passageiros, tempos_carros):
    try:
        os.mkdir(REPORT_PATH)
        print(f"Diretório de logs foi criado em \"./{REPORT_PATH}\"")
    except FileExistsError:
        pass

    existing_logs_numbers = [int(f.split("_")[-1])
                             for f in os.listdir(REPORT_PATH) if f.startswith("log_")]
    log_number = max(existing_logs_numbers) + \
        1 if len(existing_logs_numbers) > 0 else 1

    report_time = lambda \
        str1, \
        callback: \
        f"Tempo {str1} de espera na fila: {round(callback(tempos_espera_passageiros), 3)}"

    with open(REPORT_PATH + "log_" + str(log_number), 'w') as file:
        file.write(f"Relatório do experimento {log_number}\n")
        file.write(f'Data de execução: {parametros["horario_inicio"]}\n')
        file.write(f'Duração do experimento: {round(parametros["tempo_execucao"], 2)} s\n')
        file.write(f'Parâmetros:\n')
        file.write(f'\tn: {parametros["n"]}\n')
        file.write(f'\tm: {parametros["m"]}\n')
        file.write(f'\tC: {parametros["C"]}\n')
        file.write(f'\tTe: {parametros["Te"]}\n')
        file.write(f'\tTm: {parametros["Tm"]}\n')
        file.write(f'\tTp: {parametros["Tp"]}\n')
        file.write("\n~~~~~~~~~ X ~~~~~~~~~ X ~~~~~~~~~\n")

        for carro in tempos_carros:
            file.write(f'\nCarro {carro["id"]}:\n')
            file.write(f'\tTempo parado: {round(carro["tempo_parado"], 3)}\n')
            file.write(f'\tTempo em movimento: {round(carro["tempo_de_movimento"], 3)}\n')
            file.write(f'\tTempo total: {round(carro["tempo_total"], 3)}\n')
            file.write(f'\tPercentual de utilização: {round(carro["tempo_de_movimento"] / carro["tempo_total"], 3)}\n')

        file.write("\nPassageiros:\n")
        file.write(report_time("mínimo", min) + '\n')
        file.write(report_time("máximo", max) + '\n')
        file.write(report_time("médio", mean) + '\n')

    print(report_time("mínimo", min))
    print(report_time("máximo", max))
    print(report_time("médio", mean))

    print(f"Relatório de execução salvo em \"{REPORT_PATH}\"")
