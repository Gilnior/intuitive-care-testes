-- Queries de load: criar as queries para carregar o conteúdo dos arquivos obtidos nas tarefas de preparação num banco MySQL ou Postgres (Atenção ao encoding dos arquivos!)
-- Montar uma query analítica que traga a resposta para as seguintes perguntas:
-- Quais as 10 operadoras que mais tiveram despesas com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último ano?
-- Quais as 10 operadoras que mais tiveram despesas com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?


CREATE USER IF NOT EXISTS'gil'@'localhost' IDENTIFIED BY 'Easyteste3pa$$word';
GRANT CREATE,DELETE,DROP,INSERT,UPDATE,SELECT ON * . * TO 'gil'@'localhost';
FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS teste3
DEFAULT CHARACTER SET utf8
DEFAULT COLLATE utf8_general_ci;

SET GLOBAL local_infile = 'ON';
