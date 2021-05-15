import mysql.connector
import csv


from mysql.connector import cursor


def tableRelacao_Operadoras_Ativas_ANS():
    try:
        db = mysql.connector.connect(host='localhost', user='gilmar', passwd='Teste3pswd!', auth_plugin='mysql_native_password',database='teste3')  # o ideal seria por a senha em outro arquivo, mas tudo bem
        cursor = db.cursor()
     
        with db:
            createquery = """
            CREATE TABLE IF NOT EXISTS Relação_Operadoras_Ativas_ANS(
            id int AUTO_INCREMENT PRIMARY KEY,
            registro_ans int(10),
            cnpj int(16),
            razao_social varchar(100),
            nome_fantasia varchar(70),
            modalidade varchar(30),
            logradouro varchar(60),
            número int(7),
            complemento varchar(50),
            bairro varchar(50),
            cidade	varchar(30),
            uf char(2),
            cep int(10),
            ddd smallint,
            telefone int(9),
            fax	int(8),
            endereço_eletrônico	varchar(40),
            representante varchar(50),
            cargo_representante varchar(40),
            data_registro_ans date)
            """
            datequery = '''SELECT DATE_FORMAT(data_registro_ans, "%d/%m/%Y") FROM Relação_Operadoras_Ativas_ANS'''
            cursor.execute(createquery)
            cursor.execute(datequery)

    except mysql.connector.Error as e:
        print(e)


def relatorio_to_sql():
    file = 'csvs_teste3/Relatorio_cadop.csv'   
    try:
        db = mysql.connector.connect(host='localhost', user='gilmar', passwd='Teste3pswd!', auth_plugin='mysql_native_password',database='teste3')
        cursor = db.cursor()
        with db:
            with open(file, newline='') as file:
                csv_data = csv.reader(file, delimiter=';', strict=True)
                skip = True
                for row in csv_data:
                    if skip:
                        skip = False
                        continue
                    query = f"INSERT INTO teste3.Relação_Operadoras_Ativas_ANS(registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, número, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereço_eletrônico, representante, cargo_representante, data_registro_ans) VALUES({row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}, {row[7]}, {row[8]}, {row[9]}, {row[10]}, {row[11]}, {row[12]}, {row[13]}, {row[14]}, {row[15]}, {row[16]}, {row[17]}, {row[18]})",
                    cursor.execute(query)

    except mysql.connector.Error as e:
        print(e)


def tableDemonstracoesContaveis():
    try:
        db = mysql.connector.connect(host='localhost', user='gilmar', passwd='Teste3pswd!', auth_plugin='mysql_native_password',database='teste3')  # o ideal seria por a senha em outro arquivo, mas tudo bem
        cursor = db.cursor()
     
        with db:
            createquery = """
            CREATE TABLE IF NOT EXISTS Demonstracoes_Contaveis(
            id int AUTO_INCREMENT PRIMARY KEY,
            DATA date,
            REG_ANS int(10),
            CD_CONTA_CONTABIL int,
            DESCRICAO varchar(60),
            VL_SALDO_FINAL float(9,2))
            """
            datequery = '''SELECT DATE_FORMAT(DATA, "%d/%m/%Y") FROM Demonstracoes_Contaveis'''
            cursor.execute(createquery)
            cursor.execute(datequery)

    except mysql.connector.Error as e:
        print(e)


def demonstracoes_to_sql():
    try:
        db = mysql.connector.connect(host='localhost', user='gilmar', passwd='Teste3pswd!', auth_plugin='mysql_native_password',database='teste3')  # o ideal seria por a senha em outro arquivo, mas tudo bem
        cursor = db.cursor()
        for nn in range(19,21):
            nn = str(nn)
            for i in range(1,5):
                i = str(i)
                file = f'csvs_teste3/{i}T20{nn}.csv'
                with db:
                    with open(file, newline='') as file:
                        csv_data = csv.reader(file, delimiter=';', strict=True)
                        skip = True
                        try:
                            for row in csv_data:
                                if skip:
                                    skip = False
                                    continue
                                query = f"INSERT INTO teste3.Demonstracoes_Contaveis(DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_FINAL) VALUES({row[0]},{row[1]},{row[2]},{row[3]},{row[4]})",
                                cursor.execute(query)
                        except Exception:
                            print('demonstracoes_to_sql() Error')

    except mysql.connector.Error as e:
        print(e)


def main():
    tableRelacao_Operadoras_Ativas_ANS()  # works
    relatorio_to_sql()
    tableDemonstracoesContaveis()  # works
    demonstracoes_to_sql()


if __name__=='__main__':
    main()
