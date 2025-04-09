-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema tutoriza
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `tutoriza` ;

-- -----------------------------------------------------
-- Schema tutoriza
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `tutoriza` DEFAULT CHARACTER SET utf8mb4 ;
USE `tutoriza` ;

-- -----------------------------------------------------
-- Table `tutoriza`.`alumnos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tutoriza`.`alumnos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `correo` VARCHAR(100) NOT NULL,
  `password` VARCHAR(150) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tutoriza`.`asesorias`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tutoriza`.`asesorias` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tema` VARCHAR(50) NOT NULL,
  `fecha` DATETIME NOT NULL,
  `tiempo` DECIMAL NOT NULL,
  `nota` VARCHAR(50) NOT NULL,
  `alumno_id` INT NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_asesorias_alumnos_idx` (`alumno_id` ASC) VISIBLE,
  CONSTRAINT `fk_asesorias_alumnos`
    FOREIGN KEY (`alumno_id`)
    REFERENCES `tutoriza`.`alumnos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
