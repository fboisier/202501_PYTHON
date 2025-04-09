-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema esquema_tutoriza
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema esquema_tutoriza
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_tutoriza` DEFAULT CHARACTER SET utf8 ;
USE `esquema_tutoriza` ;

-- -----------------------------------------------------
-- Table `esquema_tutoriza`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_tutoriza`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(50) NOT NULL,
  `apellido` VARCHAR(50) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `password` VARCHAR(200) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_tutoriza`.`asesorias`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_tutoriza`.`asesorias` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tema` VARCHAR(50) NOT NULL,
  `fecha` DATE NOT NULL,
  `duracion` INT NOT NULL,
  `notas` VARCHAR(50) NOT NULL,
  `tutor` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  `usuarios_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_asesorias_usuarios_idx` (`usuarios_id` ASC) VISIBLE,
  CONSTRAINT `fk_asesorias_usuarios`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `esquema_tutoriza`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
