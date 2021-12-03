-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 02, 2021 at 05:26 PM
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
-- Database: `gibdd`
--

-- --------------------------------------------------------

--
-- Table structure for table `автомобили`
--

CREATE TABLE `автомобили` (
  `Код автомобиля` int NOT NULL,
  `Код водителя` int NOT NULL,
  `Код марки` int NOT NULL,
  `Регистрационный номер` varchar(50) NOT NULL,
  `Номер кузова` varchar(50) NOT NULL,
  `Номер двигателя` varchar(50) NOT NULL,
  `Номер техпаспорта` varchar(50) NOT NULL,
  `Дата выпуска` date NOT NULL,
  `Дата регистрации` date NOT NULL,
  `Цвет` text NOT NULL,
  `Технический осмотр` text NOT NULL,
  `Дата технического осмотра` date NOT NULL,
  `Описание` text NOT NULL,
  `Код сотрудника` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `автомобили в угоне`
--

CREATE TABLE `автомобили в угоне` (
  `Дата угона` date NOT NULL,
  `Дата обращения` date NOT NULL,
  `Код автомобиля` int NOT NULL,
  `Код водителя` int NOT NULL,
  `Обстоятельства угона` text NOT NULL,
  `Отметка об нахождении` text NOT NULL,
  `Дата нахождения` date NOT NULL,
  `Код сотрудника` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `водители`
--

CREATE TABLE `водители` (
  `Код водителя` int NOT NULL,
  `ФИО` text NOT NULL,
  `Дата рождения` date NOT NULL,
  `Адрес` text NOT NULL,
  `Паспортные данные` varchar(50) NOT NULL,
  `Номер водительского удостоверения` int NOT NULL,
  `Дата выдачи удостоверения` date NOT NULL,
  `Дата окончания удостоверения` date NOT NULL,
  `Категория удостоверения` varchar(50) NOT NULL,
  `Описание` text NOT NULL,
  `Код сотрудника` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `должности`
--

CREATE TABLE `должности` (
  `Код должности` int NOT NULL,
  `Наименование должности` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Оклад` int NOT NULL,
  `Обязанности` text NOT NULL,
  `Требования` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `звания`
--

CREATE TABLE `звания` (
  `Код звания` int NOT NULL,
  `Наименование` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Надбавка` int NOT NULL,
  `Обязанности` text NOT NULL,
  `Требования` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `марки автомобилей`
--

CREATE TABLE `марки автомобилей` (
  `Код марки` int NOT NULL,
  `Наименование` text NOT NULL,
  `Фирма производитель` text NOT NULL,
  `Страна производитель` text NOT NULL,
  `Дата начала производства` date NOT NULL,
  `Дата окончания производства` date NOT NULL,
  `Характеристики` text NOT NULL,
  `Категория` text NOT NULL,
  `Описание` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `сотрудники`
--

CREATE TABLE `сотрудники` (
  `Код сотрудника` int NOT NULL,
  `ФИО` text NOT NULL,
  `Возраст` int NOT NULL,
  `Пол` text NOT NULL,
  `Адрес` varchar(50) NOT NULL,
  `Телефон` int NOT NULL,
  `Паспортные данные` varchar(50) NOT NULL,
  `Код должности` int NOT NULL,
  `Код звания` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `автомобили`
--
ALTER TABLE `автомобили`
  ADD PRIMARY KEY (`Код автомобиля`),
  ADD KEY `Код марки` (`Код марки`),
  ADD KEY `Код водителя` (`Код водителя`),
  ADD KEY `Код сотрудника` (`Код сотрудника`);

--
-- Indexes for table `автомобили в угоне`
--
ALTER TABLE `автомобили в угоне`
  ADD KEY `Код автомобиля` (`Код автомобиля`),
  ADD KEY `Код водителя` (`Код водителя`);

--
-- Indexes for table `водители`
--
ALTER TABLE `водители`
  ADD PRIMARY KEY (`Код водителя`);

--
-- Indexes for table `должности`
--
ALTER TABLE `должности`
  ADD PRIMARY KEY (`Код должности`);

--
-- Indexes for table `звания`
--
ALTER TABLE `звания`
  ADD PRIMARY KEY (`Код звания`);

--
-- Indexes for table `марки автомобилей`
--
ALTER TABLE `марки автомобилей`
  ADD PRIMARY KEY (`Код марки`);

--
-- Indexes for table `сотрудники`
--
ALTER TABLE `сотрудники`
  ADD PRIMARY KEY (`Код сотрудника`),
  ADD UNIQUE KEY `Код должности` (`Код должности`),
  ADD KEY `Код звания` (`Код звания`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `автомобили`
--
ALTER TABLE `автомобили`
  ADD CONSTRAINT `автомобили_ibfk_1` FOREIGN KEY (`Код марки`) REFERENCES `марки автомобилей` (`Код марки`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `автомобили_ibfk_2` FOREIGN KEY (`Код водителя`) REFERENCES `водители` (`Код водителя`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `автомобили_ibfk_3` FOREIGN KEY (`Код сотрудника`) REFERENCES `сотрудники` (`Код сотрудника`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Constraints for table `автомобили в угоне`
--
ALTER TABLE `автомобили в угоне`
  ADD CONSTRAINT `автомобили в угоне_ibfk_1` FOREIGN KEY (`Код автомобиля`) REFERENCES `автомобили` (`Код автомобиля`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `автомобили в угоне_ibfk_2` FOREIGN KEY (`Код водителя`) REFERENCES `водители` (`Код водителя`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Constraints for table `должности`
--
ALTER TABLE `должности`
  ADD CONSTRAINT `должности_ibfk_1` FOREIGN KEY (`Код должности`) REFERENCES `сотрудники` (`Код должности`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Constraints for table `сотрудники`
--
ALTER TABLE `сотрудники`
  ADD CONSTRAINT `сотрудники_ibfk_1` FOREIGN KEY (`Код должности`) REFERENCES `должности` (`Код должности`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `сотрудники_ibfk_5` FOREIGN KEY (`Код должности`) REFERENCES `должности` (`Код должности`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
