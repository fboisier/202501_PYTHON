-- MySQL Workbench Synchronization
-- Generated: 2025-04-04 21:11
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: Roberto Alvarez

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

ALTER SCHEMA `db_tutoriza`  DEFAULT CHARACTER SET utf8  DEFAULT COLLATE utf8_general_ci ;

ALTER TABLE `db_tutoriza`.`assessorias` 
DROP FOREIGN KEY `fk_assessorias_usuarios`;

ALTER TABLE `db_tutoriza`.`usuarios` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ;

ALTER TABLE `db_tutoriza`.`assessorias` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ,
CHANGE COLUMN `data` `data` DATE NOT NULL ;

ALTER TABLE `db_tutoriza`.`assessorias` 
ADD CONSTRAINT `fk_assessorias_usuarios`
  FOREIGN KEY (`usuario_id`)
  REFERENCES `db_tutoriza`.`usuarios` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
