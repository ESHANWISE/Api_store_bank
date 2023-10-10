-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 10, 2023 at 01:58 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `storebankdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `store`
--

CREATE TABLE `store` (
  `store_id` int(11) NOT NULL,
  `store_name` varchar(120) NOT NULL,
  `store_phone` varchar(50) NOT NULL,
  `store_address` varchar(200) NOT NULL,
  `store_pic` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `store`
--

INSERT INTO `store` (`store_id`, `store_name`, `store_phone`, `store_address`, `store_pic`) VALUES
(1, 'Laterna Bookstores', '07048283853', 'Ojodu berger', 'http://127.0.0.1:5000/static/store/store1.jpg'),
(2, 'The Book ', '08022222222', 'Ikorodu, Lagos', 'http://127.0.0.1:5000/static/stores/store2.jpg'),
(3, 'SodBooks', '08033333333', 'FUTA Gate, Akure', 'http://127.0.0.1:5000/static/stores/store3.jpg'),
(4, 'CSS Bookstores', '08044444444', 'CSS, Obalende, Lagos', 'http://127.0.0.1:5000/static/stores/store4.jpg'),
(5, 'Bookcraft Africa', '08055555555', 'Adebayo street, Ikeja', 'http://127.0.0.1:5000/static/stores/store5.jpg'),
(6, 'Lantern Books', '08066666666', 'Kudirat Abiola Way, Ikeja', 'http://127.0.0.1:5000/static/stores/store6.jpg'),
(8, 'amazon store name', '08060466102', 'allen ave', 'https://amazon.com/logo.png'),
(9, 'amazon store name', '08060466102', 'allen ave', 'https://amazon.com/logo.png'),
(10, 'amazon store name', '08060466102', 'allen ave', 'https://amazon.com/logo.png'),
(11, 'amazon store name', '08060466102', 'allen ave', 'https://amazon.com/logo.png');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `store`
--
ALTER TABLE `store`
  ADD PRIMARY KEY (`store_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `store`
--
ALTER TABLE `store`
  MODIFY `store_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
