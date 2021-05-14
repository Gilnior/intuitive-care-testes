import mysql.connector
import os

def relatorio_to_sql():
    db = mysql.connector.connect(host='localhost', user='gil',passwd='Easyteste3pa$$word',auth_plugin='mysql_native_password')  # o ideal seria por a senha em outro arquivo, mas tudo bem

    cursor = db.cursor()

    cursor.execute('''
    LOAD DATA LOCAL INFILE "csvs_teste3/Relatorio_cadop.csv" INTO TABLE teste3.Relação_Operadoras_Ativas_ANS
    FIELDS TERMINATED BY ';'
    LINES TERMINATED BY '\\n'
    IGNORE 3 LINES
    (registro_ans,cnpj, razao_social, nome_fantasia, modalidade, logradouro, número, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereço_eletrônico, representante, cargo_representante, data_registro_ans)
    SET data_registro_ans=STR_TO_DATE(@datevar, '%d/%m/%Y')
    ''')

    db.close()

    
relatorio_to_sql()
