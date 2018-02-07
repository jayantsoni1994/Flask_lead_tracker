-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 14, 2017 at 01:18 PM
-- Server version: 10.1.21-MariaDB
-- PHP Version: 7.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flaskappdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `course_names`
--

CREATE TABLE `course_names` (
  `id` varchar(32) NOT NULL,
  `courses` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `course_names`
--

INSERT INTO `course_names` (`id`, `courses`) VALUES
('Data_science', 'Data_science'),
('Python', 'Python'),
('None', 'None'),
('Devops', 'Devops')
('IoT', 'IoT')
('Design', 'Design')
('FullStack', 'FullStack');

-- --------------------------------------------------------

--
-- Table structure for table `joinings`
--

CREATE TABLE `joinings` (
  `id` int(16) NOT NULL,
  `course` varchar(32) NOT NULL,
  `name` varchar(32) NOT NULL,
  `comlection_date` varchar(32) NOT NULL,
  `data_joining` varchar(32) NOT NULL,
  `course_fee` varchar(32) NOT NULL,
  `instructor` varchar(32) NOT NULL,
  `aadhar_number` varchar(64) NOT NULL,
  `mobile` varchar(16) NOT NULL,
  `email` varchar(32) NOT NULL,
  `remarks` varchar(64) NOT NULL,
  `status` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `joinings`
--

INSERT INTO `joinings` (`id`, `course`, `name`, `comlection_date`, `data_joining`, `course_fee`, `instructor`, `aadhar_number`, `mobile`, `email`, `remarks`, `status`) VALUES
(1, 'python', 'ravi34', '1/1/18', '9/9/17', '100', 'khan', '1111222215656', '9676008292', 'ravi.kiran@gmail.com', 'nice', 'complect'),
(2, 'digital', 'anand', '2017-11-15', '2017-09-11', '10000', 'ravi', '1111222215656', '9696969696', 'ravi.kiran@gmail.com', 'learn more', 'dead'),
(3, 'ui', 'nani', '10/10/2017', '6/6/2017', '10000', 'khan', '122156589652', '8888999912', 'abc@gmail.com', 'nice', 'delay'),
(4, 'datascience', 'ram', '10/10/2017', '7/7/2017', '10000', 'abc', '121225565896\r\n', '12256996', 'abc@gmail.com', '-------', 'inprocess');

-- --------------------------------------------------------

--
-- Table structure for table `registers`
--

CREATE TABLE `registers` (
  `id` int(11) NOT NULL,
  `st_name` varchar(32) NOT NULL,
  `st_mobile` varchar(32) NOT NULL,
  `st_email` varchar(32) NOT NULL,
  `st_course` varchar(32) NOT NULL,
  `st_source` varchar(32) NOT NULL,
  `st_lead_status` varchar(32) NOT NULL,
  `st_demo_date` varchar(32) NOT NULL,
  `st_counsler` varchar(32) NOT NULL,
  `st_remarks` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `registers`
--

INSERT INTO `registers` (`id`, `st_name`, `st_mobile`, `st_email`, `st_course`, `st_source`, `st_lead_status`, `st_demo_date`, `st_counsler`, `st_remarks`) VALUES
(1, 'ravikiran', '9676008292', 'ravi.kiran@gmail.com', 'Python', 'web', 'Demo', '9/11/2017', 'khan', 'good'),
(2, 'ravi', '5689865211234', 'ravi@gmail.com', 'Python', 'web', 'Demo', '1/1/17', 'khan', 'good'),
(3, 'ravi34', '8639139453', 'rrrr@gmail.com', 'python', 'web', 'Demo', '1/1/17', 'ravi', 'nice'),
(4, 'abc', '9676008292', 'raju@gmail.com', 'datascience', 'datascience', 'Demo', '1/1/17', 'ravi', 'none'),
(5, 'ghtjyiu7yt', '9696969696', 'rkmudrageda@digital-lync.com', 'Python', 'none', 'demo', '2017-09-23', 'ravi', 'nice'),
(7, 'nani11', '9676008292', 'vas@gmail.com', 'Python', 'web', 'Demo', '2017-09-16', 'khan', 'nice'),
(8, 'khan', '9696969696', 'abc@gmail.com', 'python', 'Website', 'Counselling', '2017-09-15', 'khan', 'nice');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `joinings`
--
ALTER TABLE `joinings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `registers`
--
ALTER TABLE `registers`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `joinings`
--
ALTER TABLE `joinings`
  MODIFY `id` int(16) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `registers`
--
ALTER TABLE `registers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
