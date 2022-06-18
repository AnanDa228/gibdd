-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Июн 18 2022 г., 11:29
-- Версия сервера: 8.0.19
-- Версия PHP: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `diplom`
--

-- --------------------------------------------------------

--
-- Структура таблицы `клиенты`
--

CREATE TABLE `клиенты` (
  `Код клиента` int NOT NULL,
  `Фамилия клиента` varchar(75) NOT NULL,
  `Имя клиента` varchar(75) NOT NULL,
  `Отчество клиента` varchar(75) NOT NULL,
  `Адрес клиента` varchar(75) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Телефон клиента` varchar(75) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `персонал`
--

CREATE TABLE `персонал` (
  `Оклад` varchar(75) NOT NULL,
  `Фамилия работника` varchar(75) NOT NULL,
  `Имя работника` varchar(75) NOT NULL,
  `Отчество работника` varchar(75) NOT NULL,
  `Должность` varchar(75) NOT NULL,
  `Код работника` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `поставщики`
--

CREATE TABLE `поставщики` (
  `РНН поставщика` int NOT NULL,
  `Наименование фирмы` varchar(75) NOT NULL,
  `Адрес фирмы` varchar(75) NOT NULL,
  `Телефоны фирмы` varchar(75) NOT NULL,
  `Код товара` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `авторизация`
--

CREATE TABLE `авторизация` (
  `Логин` varchar(50) NOT NULL,
  `Пароль` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `операция купли`
--

CREATE TABLE `операция купли` (
  `Номер накладной` int NOT NULL,
  `Дата покупки` date NOT NULL,
  `Стоимость покупки` varchar(75) NOT NULL,
  `Количество закупленного товара` varchar(75) NOT NULL,
  `Код товара` int NOT NULL,
  `РНН поставщика` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `операция продажи`
--

CREATE TABLE `операция продажи` (
  `Номер кассового чека` int NOT NULL,
  `Дата реализации` date NOT NULL,
  `Количество проданного товара` varchar(75) NOT NULL,
  `Цена товара` varchar(75) NOT NULL,
  `Код товара` int NOT NULL,
  `Код клиента` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `склад`
--

CREATE TABLE `склад` (
  `Номер склада` int NOT NULL,
  `Адрес склада` varchar(75) NOT NULL,
  `Телефон склада` varchar(75) NOT NULL,
  `Код товара` int NOT NULL,
  `Код работника` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `товар`
--

CREATE TABLE `товар` (
  `Код товара` int NOT NULL,
  `Наименование товара` varchar(75) NOT NULL,
  `Производитель` varchar(75) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `товар`
--

INSERT INTO `товар` (`Код товара`, `Наименование товара`, `Производитель`) VALUES
(1, 'Картошка', 'Беларусь'),
(2, 'Молоко', 'Россия'),
(3, 'Курица', 'Казахстан');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `клиенты`
--
ALTER TABLE `клиенты`
  ADD PRIMARY KEY (`Код клиента`);

--
-- Индексы таблицы `персонал`
--
ALTER TABLE `персонал`
  ADD PRIMARY KEY (`Код работника`);

--
-- Индексы таблицы `поставщики`
--
ALTER TABLE `поставщики`
  ADD PRIMARY KEY (`РНН поставщика`),
  ADD KEY `Код товара` (`Код товара`);

--
-- Индексы таблицы `операция купли`
--
ALTER TABLE `операция купли`
  ADD PRIMARY KEY (`Номер накладной`),
  ADD KEY `Код товара` (`Код товара`,`РНН поставщика`),
  ADD KEY `РНН поставщика` (`РНН поставщика`);

--
-- Индексы таблицы `операция продажи`
--
ALTER TABLE `операция продажи`
  ADD PRIMARY KEY (`Номер кассового чека`),
  ADD KEY `Код товара` (`Код товара`,`Код клиента`),
  ADD KEY `Код клиента` (`Код клиента`);

--
-- Индексы таблицы `склад`
--
ALTER TABLE `склад`
  ADD PRIMARY KEY (`Номер склада`),
  ADD KEY `Код товара` (`Код товара`,`Код работника`),
  ADD KEY `Код работника` (`Код работника`);

--
-- Индексы таблицы `товар`
--
ALTER TABLE `товар`
  ADD PRIMARY KEY (`Код товара`);

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `поставщики`
--
ALTER TABLE `поставщики`
  ADD CONSTRAINT `поставщики_ibfk_1` FOREIGN KEY (`Код товара`) REFERENCES `товар` (`Код товара`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `операция купли`
--
ALTER TABLE `операция купли`
  ADD CONSTRAINT `операция купли_ibfk_1` FOREIGN KEY (`Код товара`) REFERENCES `товар` (`Код товара`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `операция купли_ibfk_2` FOREIGN KEY (`РНН поставщика`) REFERENCES `поставщики` (`РНН поставщика`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `операция продажи`
--
ALTER TABLE `операция продажи`
  ADD CONSTRAINT `операция продажи_ibfk_1` FOREIGN KEY (`Код товара`) REFERENCES `товар` (`Код товара`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `операция продажи_ibfk_2` FOREIGN KEY (`Код клиента`) REFERENCES `клиенты` (`Код клиента`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `склад`
--
ALTER TABLE `склад`
  ADD CONSTRAINT `склад_ibfk_1` FOREIGN KEY (`Код товара`) REFERENCES `товар` (`Код товара`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `склад_ibfk_2` FOREIGN KEY (`Код работника`) REFERENCES `персонал` (`Код работника`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
