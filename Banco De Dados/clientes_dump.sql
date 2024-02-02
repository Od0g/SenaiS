BEGIN TRANSACTION;
CREATE TABLE clientes (
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               idade INTEGER,
               cpf     VARCHAR(11) NOT NULL,
               email TEXT NOT NULL,
               fone TEXT,
               cidade TEXT,
               uf VARCHAR(2) NOT NULL,
               criado_em DATE NOT NULL 
, bloqueado BOOLEAN);
INSERT INTO "clientes" VALUES(1,'Fabio',23,'44444444444','fabio@email.com','11-1000-2014','Belo Horizonte','MG','2014-06-11',NULL);
INSERT INTO "clientes" VALUES(2,'Joao',21,'55555555555','joao@email.com','11-1234-5600','Sao Paulo','SP','2014-06-09',NULL);
INSERT INTO "clientes" VALUES(3,'Xavier',24,'66666666666','xavier@email.com','12-1234-5601','Campinas','SP','2014-06-10',NULL);
INSERT INTO "clientes" VALUES(4,'Augusto',20,'48588443821','inacioaugusto197@icloud.com','16997594202','ibate','sp','2024-02-01',NULL);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('clientes',4);
COMMIT;
