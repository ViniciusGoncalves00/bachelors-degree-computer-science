CREATE TABLE IF NOT EXISTS `funcionario` (
	`cpf` char(11) NOT NULL UNIQUE,
	`hotel` char(1) NOT NULL,
	`nome` varchar(128) NOT NULL,
	`telefone` char(11) NOT NULL,
	`email` varchar(64) NOT NULL,
	`login` varchar(64) NOT NULL UNIQUE,
	`senha` varchar(64) NOT NULL,
	`reserva` char(64) NOT NULL,
	PRIMARY KEY (`cpf`)
);

CREATE TABLE IF NOT EXISTS `hotel` (
	`id` char(64) NOT NULL UNIQUE,
	`nome` varchar(128) NOT NULL,
	`categoria` int NOT NULL,
	`telefone` char(11) NOT NULL,
	`email` varchar(64) NOT NULL UNIQUE,
	`endereco` varchar(128) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `quarto` (
	`id` char(64) NOT NULL UNIQUE,
	`hotel` char(1) NOT NULL,
	`quantidade_de_leitos` int NOT NULL,
	`tipo` enum NOT NULL,
	`valor_diaria` decimal(64) NOT NULL,
	`status` enum NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `hospede` (
	`cpf` int AUTO_INCREMENT NOT NULL UNIQUE,
	`nome` varchar(128) NOT NULL,
	`telefone` int NOT NULL,
	`email` varchar(64) NOT NULL,
	`endereco` varchar(128) NOT NULL,
	`reserva` char(64) NOT NULL,
	PRIMARY KEY (`cpf`)
);

CREATE TABLE IF NOT EXISTS `reserva` (
	`id` char(64) NOT NULL UNIQUE,
	`data_de_entrada` date NOT NULL,
	`data_de_saida` date NOT NULL,
	`status` enum NOT NULL,
	`pagamento` char(1) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `pagamento` (
	`id` varchar(64) NOT NULL UNIQUE,
	`forma_de_pagamento` enum NOT NULL,
	`data_de_pagamento` date NOT NULL,
	`valor_total` decimal(64) NOT NULL,
	`status` enum NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `quarto_reserva` (
	`quarto` char(1) NOT NULL UNIQUE,
	`reserva` char(1) NOT NULL UNIQUE,
	PRIMARY KEY (`quarto`, `reserva`)
);

ALTER TABLE `funcionario` ADD CONSTRAINT `funcionario_fk1` FOREIGN KEY (`hotel`) REFERENCES `hotel`(`id`);

ALTER TABLE `funcionario` ADD CONSTRAINT `funcionario_fk7` FOREIGN KEY (`reserva`) REFERENCES `reserva`(`id`);

ALTER TABLE `quarto` ADD CONSTRAINT `quarto_fk1` FOREIGN KEY (`hotel`) REFERENCES `hotel`(`id`);
ALTER TABLE `hospede` ADD CONSTRAINT `hospede_fk5` FOREIGN KEY (`reserva`) REFERENCES `reserva`(`id`);
ALTER TABLE `reserva` ADD CONSTRAINT `reserva_fk4` FOREIGN KEY (`pagamento`) REFERENCES `pagamento`(`id`);

ALTER TABLE `quarto_reserva` ADD CONSTRAINT `quarto_reserva_fk0` FOREIGN KEY (`quarto`) REFERENCES `quarto`(`id`);

ALTER TABLE `quarto_reserva` ADD CONSTRAINT `quarto_reserva_fk1` FOREIGN KEY (`reserva`) REFERENCES `reserva`(`id`);