-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 22, 2021 at 11:55 PM
-- Server version: 8.0.19
-- PHP Version: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `transport`
--

-- --------------------------------------------------------

--
-- Table structure for table `автомобили`
--

CREATE TABLE `автомобили` (
  `Код автомобиля` int NOT NULL,
  `Код марки` int NOT NULL,
  `Код вида автомобиля` int NOT NULL,
  `Регистрационный номер` varchar(50) NOT NULL,
  `Номер кузова` varchar(50) NOT NULL,
  `Номер двигателя` varchar(50) NOT NULL,
  `Год выпуска` date NOT NULL,
  `Код сотрудника-водителя` int NOT NULL,
  `Дата последнего ТО` date NOT NULL,
  `Код сотрудника-механика` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `виды автомобилей`
--

CREATE TABLE `виды автомобилей` (
  `Код вида автомобиля` int NOT NULL,
  `Наименование` text NOT NULL,
  `Описание` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `виды грузов`
--

CREATE TABLE `виды грузов` (
  `Код вида груза` int NOT NULL,
  `Наименование` text NOT NULL,
  `Код вида автомобиля для транспортировки` int NOT NULL,
  `Описание` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `грузы`
--

CREATE TABLE `грузы` (
  `Код груза` int NOT NULL,
  `Наименование` text NOT NULL,
  `Код вида груза` int NOT NULL,
  `Срок годности` varchar(50) NOT NULL,
  `Особенности` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `должности`
--

CREATE TABLE `должности` (
  `Код должности` int NOT NULL,
  `Наименование должности` text NOT NULL,
  `Оклад` int NOT NULL,
  `Обязанности` text NOT NULL,
  `Требования` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `марки автомобилей`
--

CREATE TABLE `марки автомобилей` (
  `Код марки` int NOT NULL,
  `Наименование` text NOT NULL,
  `Технические характеристики` text NOT NULL,
  `Описание` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `рейсы`
--

CREATE TABLE `рейсы` (
  `Код автомобиля` int NOT NULL,
  `Заказчик` varchar(100) NOT NULL,
  `Откуда` varchar(100) NOT NULL,
  `Куда` varchar(100) NOT NULL,
  `Дата отправления` date NOT NULL,
  `Дата прибытия` date NOT NULL,
  `Код груза` int NOT NULL,
  `Цена` int NOT NULL,
  `Отметка об оплате` varchar(50) NOT NULL,
  `Отметка об возвращении` varchar(50) NOT NULL,
  `Код сотрудника` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `сотрудники`
--

CREATE TABLE `сотрудники` (
  `Код сотрудника` int NOT NULL,
  `ФИО` text NOT NULL,
  `Пол` text NOT NULL,
  `Адрес` varchar(50) NOT NULL,
  `Телефон` int NOT NULL,
  `Паспортные данные` varchar(50) NOT NULL,
  `Код должности` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `автомобили`
--
ALTER TABLE `автомобили`
  ADD PRIMARY KEY (`Код автомобиля`),
  ADD KEY `Код марки` (`Код марки`,`Код вида автомобиля`,`Код сотрудника-водителя`,`Код сотрудника-механика`),
  ADD KEY `Код сотрудника-водителя` (`Код сотрудника-водителя`),
  ADD KEY `Код сотрудника-механика` (`Код сотрудника-механика`),
  ADD KEY `Код вида автомобиля` (`Код вида автомобиля`);

--
-- Indexes for table `виды автомобилей`
--
ALTER TABLE `виды автомобилей`
  ADD PRIMARY KEY (`Код вида автомобиля`);

--
-- Indexes for table `виды грузов`
--
ALTER TABLE `виды грузов`
  ADD PRIMARY KEY (`Код вида груза`),
  ADD KEY `Код вида автомобиля для транспортировки` (`Код вида автомобиля для транспортировки`);

--
-- Indexes for table `грузы`
--
ALTER TABLE `грузы`
  ADD PRIMARY KEY (`Код груза`),
  ADD KEY `Код вида груза` (`Код вида груза`);

--
-- Indexes for table `должности`
--
ALTER TABLE `должности`
  ADD PRIMARY KEY (`Код должности`);

--
-- Indexes for table `марки автомобилей`
--
ALTER TABLE `марки автомобилей`
  ADD PRIMARY KEY (`Код марки`);

--
-- Indexes for table `рейсы`
--
ALTER TABLE `рейсы`
  ADD KEY `Код груза` (`Код груза`,`Код сотрудника`),
  ADD KEY `Код сотрудника` (`Код сотрудника`),
  ADD KEY `Код автомобиля` (`Код автомобиля`);

--
-- Indexes for table `сотрудники`
--
ALTER TABLE `сотрудники`
  ADD PRIMARY KEY (`Код сотрудника`),
  ADD KEY `Код должности` (`Код должности`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `автомобили`
--
ALTER TABLE `автомобили`
  ADD CONSTRAINT `автомобили_ibfk_1` FOREIGN KEY (`Код сотрудника-водителя`) REFERENCES `сотрудники` (`Код сотрудника`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `автомобили_ibfk_2` FOREIGN KEY (`Код сотрудника-механика`) REFERENCES `сотрудники` (`Код сотрудника`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `автомобили_ibfk_3` FOREIGN KEY (`Код вида автомобиля`) REFERENCES `виды автомобилей` (`Код вида автомобиля`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `автомобили_ibfk_4` FOREIGN KEY (`Код марки`) REFERENCES `марки автомобилей` (`Код марки`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `виды грузов`
--
ALTER TABLE `виды грузов`
  ADD CONSTRAINT `виды грузов_ibfk_1` FOREIGN KEY (`Код вида автомобиля для транспортировки`) REFERENCES `виды автомобилей` (`Код вида автомобиля`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `грузы`
--
ALTER TABLE `грузы`
  ADD CONSTRAINT `грузы_ibfk_1` FOREIGN KEY (`Код вида груза`) REFERENCES `виды грузов` (`Код вида груза`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `рейсы`
--
ALTER TABLE `рейсы`
  ADD CONSTRAINT `рейсы_ibfk_1` FOREIGN KEY (`Код сотрудника`) REFERENCES `сотрудники` (`Код сотрудника`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `рейсы_ibfk_2` FOREIGN KEY (`Код груза`) REFERENCES `грузы` (`Код груза`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `рейсы_ibfk_3` FOREIGN KEY (`Код автомобиля`) REFERENCES `автомобили` (`Код автомобиля`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `сотрудники`
--
ALTER TABLE `сотрудники`
  ADD CONSTRAINT `сотрудники_ibfk_1` FOREIGN KEY (`Код должности`) REFERENCES `должности` (`Код должности`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
