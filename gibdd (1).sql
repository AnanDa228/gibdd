-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 09, 2021 at 12:50 AM
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

--
-- Dumping data for table `автомобили`
--

INSERT INTO `автомобили` (`Код автомобиля`, `Код водителя`, `Код марки`, `Регистрационный номер`, `Номер кузова`, `Номер двигателя`, `Номер техпаспорта`, `Дата выпуска`, `Дата регистрации`, `Цвет`, `Технический осмотр`, `Дата технического осмотра`, `Описание`, `Код сотрудника`) VALUES
(1234, 1, 1, '123', '456', '123GG', '5667PP', '2021-11-03', '2021-11-10', 'Белый', 'да', '2021-12-01', 'Белая машина', 1);

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

--
-- Dumping data for table `автомобили в угоне`
--

INSERT INTO `автомобили в угоне` (`Дата угона`, `Дата обращения`, `Код автомобиля`, `Код водителя`, `Обстоятельства угона`, `Отметка об нахождении`, `Дата нахождения`, `Код сотрудника`) VALUES
('2021-12-25', '2021-12-15', 1234, 1, 'wdcewc', 'wdcwcw', '2021-12-31', 1);

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

--
-- Dumping data for table `водители`
--

INSERT INTO `водители` (`Код водителя`, `ФИО`, `Дата рождения`, `Адрес`, `Паспортные данные`, `Номер водительского удостоверения`, `Дата выдачи удостоверения`, `Дата окончания удостоверения`, `Категория удостоверения`, `Описание`, `Код сотрудника`) VALUES
(1, 'Мержинский Виталий Германович', '2016-02-18', 'ул.Гаврилова', '322341', 123, '2021-12-17', '2021-12-30', '2b', 'Высокий мужчина', 1);

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

--
-- Dumping data for table `должности`
--

INSERT INTO `должности` (`Код должности`, `Наименование должности`, `Оклад`, `Обязанности`, `Требования`) VALUES
(1, 'Смотрящий', 30000, 'Наблюдать за пойманными нарушителями закона', 'Хорошая физ форма'),
(2, 'Патрульный', 40000, 'Вести патруль местности', 'Хорошая физ форма'),
(3, 'Командующий операциями захвата', 90000, 'Командовать операциями захвата ', 'Высшее или средне-специально образование и опыт работы 10 лет'),
(4, 'Глава крыла отделения', 120000, 'Командование всеми сотрудниками вверенного ему крыла и несение ответственности за них', 'Высшее образование и опыт работы 15 лет'),
(5, 'Глава отделения ГИБДД', 150000, 'Командование всеми сотрудниками в отделение ГИБДД и несение ответственности ', 'Высшее образование и опыт работы работы 20 лет ');

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

--
-- Dumping data for table `звания`
--

INSERT INTO `звания` (`Код звания`, `Наименование`, `Надбавка`, `Обязанности`, `Требования`) VALUES
(1, 'Рядовой полиции', 5000, 'Быть рядовым и слушаться старших по званию', 'Особых требований не имеется'),
(2, 'Мл. сержант полиции', 15000, 'Вести патруль с другими младшими и средними сержантами', 'Иметь хорошую физ форму'),
(3, 'Мл. лейтенант полиции ', 19000, 'Является офицером, должен командовать вверенными ему людьми и нести ответственность за них', 'Иметь высшее или средне-специальное образование '),
(4, 'Майор полиции', 50000, 'Является старшим офицером, должен ввести карательные операции и командовать вверенной ему дивизией', 'Высшее образование и опыт работы 15 лет'),
(5, 'Полковник полиции', 60000, 'Командует всеми сотрудниками полиции на вверенной ему территории', 'Высшее образование и опыт работы 20 лет');

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

--
-- Dumping data for table `марки автомобилей`
--

INSERT INTO `марки автомобилей` (`Код марки`, `Наименование`, `Фирма производитель`, `Страна производитель`, `Дата начала производства`, `Дата окончания производства`, `Характеристики`, `Категория`, `Описание`) VALUES
(1, 'LadaVesta', 'LADA', 'Россия', '2019-09-06', '2021-06-03', 'Старая машина', 'Легковая', 'Белая машина'),
(2, 'Buggati Veiron', 'Buggati', 'Италия', '2021-08-25', '2021-12-31', 'Спорт кар', 'Спорт машина', 'Быстрая машина');

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
-- Dumping data for table `сотрудники`
--

INSERT INTO `сотрудники` (`Код сотрудника`, `ФИО`, `Возраст`, `Пол`, `Адрес`, `Телефон`, `Паспортные данные`, `Код должности`, `Код звания`) VALUES
(1, 'Фролов Илья Денисович', 19, 'мужской', 'ул. Арийская 52', 89993456, '322341', 2, 1),
(2, 'Збаровский Антон Александрович', 19, 'Мужской', 'ул. Арийская 80', 891645688, '452454', 2, 2),
(3, 'Смирнов Глеб Александрович', 24, 'Мужской', 'ул. Пролетарская 52', 899965767, '3263876', 3, 3),
(4, 'Пак Владимир Германович', 24, 'Мужской', 'ул. Вовская 89', 8997890, '45245476', 2, 2),
(5, 'Булочков Максим Владиславович', 67, 'Мужской', 'ул. Разбитых фонарей 28', 899789078, '224545678', 1, 2);

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
  ADD KEY `Код водителя` (`Код водителя`),
  ADD KEY `Код сотрудника` (`Код сотрудника`);

--
-- Indexes for table `водители`
--
ALTER TABLE `водители`
  ADD PRIMARY KEY (`Код водителя`),
  ADD KEY `Код сотрудника` (`Код сотрудника`);

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
  ADD KEY `Код должности` (`Код должности`),
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
  ADD CONSTRAINT `автомобили в угоне_ibfk_2` FOREIGN KEY (`Код водителя`) REFERENCES `водители` (`Код водителя`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `автомобили в угоне_ibfk_3` FOREIGN KEY (`Код сотрудника`) REFERENCES `сотрудники` (`Код сотрудника`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `водители`
--
ALTER TABLE `водители`
  ADD CONSTRAINT `водители_ibfk_1` FOREIGN KEY (`Код сотрудника`) REFERENCES `сотрудники` (`Код сотрудника`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `сотрудники`
--
ALTER TABLE `сотрудники`
  ADD CONSTRAINT `сотрудники_ibfk_1` FOREIGN KEY (`Код должности`) REFERENCES `должности` (`Код должности`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `сотрудники_ibfk_2` FOREIGN KEY (`Код звания`) REFERENCES `звания` (`Код звания`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
