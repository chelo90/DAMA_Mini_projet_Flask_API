CREATE DATABASE bd_test_api;

CREATE TABLE `client` (
  `id_client` int NOT NULL AUTO_INCREMENT,
  `code_client` varchar(100) NOT NULL,
  `nom_client` varchar(100) NOT NULL,
  `solde_client` float NOT NULL DEFAULT '0',
  `etat` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_client`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
