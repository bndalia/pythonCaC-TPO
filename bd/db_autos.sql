-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.32-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para crud_flask_python
CREATE DATABASE IF NOT EXISTS `crud_flask_python` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `crud_flask_python`;

-- Volcando estructura para tabla crud_flask_python.autos
CREATE TABLE IF NOT EXISTS `autos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `marca` varchar(45) NOT NULL,
  `modelo` varchar(45) NOT NULL,
  `year` varchar(45) NOT NULL,
  `color` varchar(45) NOT NULL,
  `puertas` varchar(45) NOT NULL,
  `combustible` varchar(45) NOT NULL,
  `foto` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla crud_flask_python.autos: ~10 rows (aproximadamente)
/*!40000 ALTER TABLE `autos` DISABLE KEYS */;
INSERT INTO `autos` (`id`, `marca`, `modelo`, `year`, `color`, `puertas`, `combustible`, `foto`) VALUES
	(2, 'Ford', 'Focus', '2022', 'Blanco', '4', 'Nafta', 'focus.jpg'),
	(3, 'Chevrolet', 'Cruze LTZ', '2019', 'Blanco', '4', 'Nafta', 'cruze.jpg'),
	(7, 'Toyota', 'Corolla', '2018', 'Gris', '4', 'Nafta', 'toyota_corolla.webp'),
	(8, 'Chevrolet', 'Onix', '2015', 'Rojo', '4', 'Diesel', 'onix.webp'),
	(10, 'Peugeot', '208', '2022', 'Azul', '2', 'Nafta', '208.jpeg'),
	(15, 'Fiat', 'Cronos', '2023', 'Rojo', '4', 'Diesel', 'cronos.jpg'),
	(16, 'Volskwagen', 'Vento', '2020', 'Gris', '4', 'Nafta', 'vento.jpg'),
	(17, 'Honda', 'Civic', '2018', 'Negro', '4', 'Diesel', 'civic.jpg'),
	(18, 'Renault', 'Sandero', '2022', 'Rojo', '4', 'Diesel', 'sandero.jpg'),
	(19, 'Toyota', 'Hilux', '2021', 'Blanco', '4', 'Nafta', 'hilux.webp');
/*!40000 ALTER TABLE `autos` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
