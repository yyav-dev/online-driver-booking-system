-- phpMyAdmin SQL Dump
-- version 4.4.12
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: May 02, 2023 at 01:43 PM
-- Server version: 5.6.25
-- PHP Version: 5.6.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `driverhire`
--

-- --------------------------------------------------------

--
-- Table structure for table `actingdriver`
--

CREATE TABLE IF NOT EXISTS `actingdriver` (
  `Driverid` varchar(10) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Gender` varchar(1) NOT NULL,
  `DOB` varchar(10) NOT NULL,
  `Licenseno` varchar(20) NOT NULL,
  `Validity` varchar(15) NOT NULL,
  `Renewal` varchar(15) NOT NULL,
  `Street` varchar(50) NOT NULL,
  `Location` varchar(50) NOT NULL,
  `City` varchar(50) NOT NULL,
  `Phoneno` varchar(10) NOT NULL,
  `Aadharno` varchar(16) NOT NULL,
  `Driversince` varchar(10) NOT NULL,
  `Driverstatus` varchar(20) NOT NULL,
  `Vehicleinfo` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `actingdriver`
--

INSERT INTO `actingdriver` (`Driverid`, `Name`, `Gender`, `DOB`, `Licenseno`, `Validity`, `Renewal`, `Street`, `Location`, `City`, `Phoneno`, `Aadharno`, `Driversince`, `Driverstatus`, `Vehicleinfo`) VALUES
('DR101', 'Nataraj', 'M', '10-04-1990', 'TN43A393978', '10-04-2025', '04-2025', 'BG Street', 'V Colony', 'Pollachi', '9159990890', '459435347347', '2002', 'Live', 'All Vehicles'),
('DR102', 'Balan.K', 'M', '22-04-1980', 'TN32A59559', '10-03-2024', '04-2024', '34, VKV Layout', 'Venkatesa Colony', 'Pollachi', '8906756789', '54874578877', '2000', 'Live', 'All Vehicles'),
('DR103', 'Karthick.N', 'M', '10-08-1995', 'TN43A3967', '18-05-2024', '06-2024', '45,Ganapathy Street', 'Parvathy Apartments', 'Pollachi', '9698786534', '980273548908', '10-01-2020', 'Live', 'All Vehicles'),
('DR104', 'Shanthi.A', 'F', '16-09-1998', 'TN45A6789', '06-01-2025', '02-2025', '89,Sai Ram Street', 'Chinnamplayam', 'Pollachi', '9876436829', '897645670923', '19-03-2020', 'Live', 'All vehicles'),
('DR105', 'Arun.B', 'M', '16-10-1990', 'TN45A789', '06-09-2024', '10-2024', '16,Kaliamman Kovil Street', 'Devanurpudhur', 'Udumalpet', '979806873', '99097867665', '06-06-2022', 'Live', 'All vehicles'),
('DR106', 'Arun.B', 'M', '19-06-1989', 'TN45A36789', '-30-09-2026', '10-2026', '89,Karunanudhi Street', 'Kinathukaduvu', 'Coimbatore', '8976895645', '986543789012', '28-09-2015', 'Live', 'SUV vehicles'),
('DR107', 'Udhay.M', 'M', '19-09-1995', 'TN567A567', '18-08-2023', '09-2023', '101,Ayyapan Kovil Street', 'Sellapampalayam', 'Udumalpet', '9876563787', '908764578912', '21-09-2020', 'Live', 'All Vehicles');

-- --------------------------------------------------------

--
-- Table structure for table `adminlogin`
--

CREATE TABLE IF NOT EXISTS `adminlogin` (
  `adminid` varchar(10) NOT NULL,
  `adminpass` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminlogin`
--

INSERT INTO `adminlogin` (`adminid`, `adminpass`) VALUES
('admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE IF NOT EXISTS `customers` (
  `Custcode` varchar(10) NOT NULL,
  `Custname` varchar(50) NOT NULL,
  `Gender` varchar(1) NOT NULL,
  `Street` varchar(50) NOT NULL,
  `Location` varchar(50) NOT NULL,
  `City` varchar(50) NOT NULL,
  `Customersince` varchar(10) NOT NULL,
  `Landmark` varchar(50) NOT NULL,
  `Phoneno` varchar(10) NOT NULL,
  `Alternateno` varchar(10) NOT NULL,
  `Status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`Custcode`, `Custname`, `Gender`, `Street`, `Location`, `City`, `Customersince`, `Landmark`, `Phoneno`, `Alternateno`, `Status`) VALUES
('CUS001', 'Kavitha Hari', 'F', '34, Sai Nagar', 'Thillai Nagar', 'Udumalpet', '2015', 'Near Roundana', '9842256756', '9159923456', 'Live'),
('CUS002', 'Saritha Muthu', 'F', '123, Cheran Nagar', 'CBE Road', 'Pollachi', '2015', 'Near PKD', '9842212345', '8089067567', 'Live'),
('CUS003', 'Venmathi.K', 'F', '34, Sakarabani Street', 'Venkatesa Colony', 'Pollachi', '2012', 'Scanpoint', '8764531234', '8764534455', 'Live'),
('CUS004', 'Divya Ganesh', 'F', '89,Ambedkar Street', 'Vadukapalayam', 'Pollachi', '2020', 'Naer Government School', '7010524562', '9698751523', 'Live'),
('CUS005', 'Hari Prasath', 'M', '78,Kumaran Nagar', 'Mahalingapuram', 'Pollachi', '2021', 'Naer AVM Hospital', '8798567890', '8906545679', 'Live'),
('CUS006', 'Ram Kumar', 'M', '89,Venkatraman Street', 'Chinnampalayam', 'Pollachi', '2019', 'Near KKR Jewellers', '7898765435', '9098734564', 'Live');

-- --------------------------------------------------------

--
-- Table structure for table `driverallotment`
--

CREATE TABLE IF NOT EXISTS `driverallotment` (
  `Bookno` varchar(10) NOT NULL,
  `Bookdate` varchar(10) NOT NULL,
  `Custcode` varchar(10) NOT NULL,
  `Custname` varchar(50) NOT NULL,
  `Driverid` varchar(10) NOT NULL,
  `Drivername` varchar(50) NOT NULL,
  `Reqdate` varchar(10) NOT NULL,
  `Noofdays` varchar(5) NOT NULL,
  `Salaryperday` varchar(10) NOT NULL,
  `Allowance` varchar(10) NOT NULL,
  `Totalcharge` varchar(10) NOT NULL,
  `Sourceplace` varchar(50) NOT NULL,
  `Destinationplace` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `driverallotment`
--

INSERT INTO `driverallotment` (`Bookno`, `Bookdate`, `Custcode`, `Custname`, `Driverid`, `Drivername`, `Reqdate`, `Noofdays`, `Salaryperday`, `Allowance`, `Totalcharge`, `Sourceplace`, `Destinationplace`) VALUES
('1', '22/04/2023', 'CUS001', 'Kavitha', 'DRV01', 'Nataraj', '24/4/2023', '1', '1000', '300', '1300', 'Udumalpet', 'Madurai'),
('2', '23/4/2023', 'CUS003', 'Saritha Muthu', 'DRV102', 'Balan.K', '24/4/2023', '2', '1200', '300', '3000', 'Pollachi', 'Chennai'),
('5', '30/4/2023', 'CUS004', 'Divya Ganesh', 'DRV106', 'Arun.B', '10-05-2023', '1', '1200', '200', '1400', 'Pollachi', 'Madurai'),
('7', '1/5/2023', 'CUS010', 'Lakshmi', 'DRV201', 'Sundarraj.K', '5/5/2023', '1', '1200', '100', '1300', 'Pollachi', 'Erode');

-- --------------------------------------------------------

--
-- Table structure for table `driverbooking`
--

CREATE TABLE IF NOT EXISTS `driverbooking` (
  `Bookno` varchar(10) NOT NULL,
  `Bookdate` varchar(10) NOT NULL,
  `Custcode` varchar(10) NOT NULL,
  `Custname` varchar(50) NOT NULL,
  `Reqdate` varchar(10) NOT NULL,
  `Source` varchar(50) NOT NULL,
  `Destination` varchar(30) NOT NULL,
  `Noofdays` varchar(3) NOT NULL,
  `Specification` varchar(50) NOT NULL,
  `Bookstatus` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `driverbooking`
--

INSERT INTO `driverbooking` (`Bookno`, `Bookdate`, `Custcode`, `Custname`, `Reqdate`, `Source`, `Destination`, `Noofdays`, `Specification`, `Bookstatus`) VALUES
('1', '22/04/2023', 'CUS001', 'Kavitha', '24/04/2023', 'Pollachi', 'Madurai', '1', 'Temple Visit', 'Cancelled'),
('2', '23/4/2023', 'CUS003', 'Saritha Muthu', '24/4/2023', 'Pollachi', 'Chennai', '2', 'Experienced Driver', 'Booked'),
('3', '23/4/2023', 'CUS003', 'Venmathi.K', '24/04/2023', 'Pollachi', 'Tiruppur', '1', 'NIL', 'Booked'),
('4', '23/4/2023', 'CUS004', 'Divya Ganesh', '24/04/2023', 'Pollachi', 'Kodaikanal', '2', 'Experienced Driver', 'Booked'),
('5', '30/4/2023', 'CUS004', 'Divya Ganesh', '10-05-2023', 'Pollachi', 'Madurai', '1', 'Senior Driver', 'Booked');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `actingdriver`
--
ALTER TABLE `actingdriver`
  ADD PRIMARY KEY (`Driverid`);

--
-- Indexes for table `adminlogin`
--
ALTER TABLE `adminlogin`
  ADD PRIMARY KEY (`adminid`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`Custcode`);

--
-- Indexes for table `driverallotment`
--
ALTER TABLE `driverallotment`
  ADD PRIMARY KEY (`Bookno`);

--
-- Indexes for table `driverbooking`
--
ALTER TABLE `driverbooking`
  ADD PRIMARY KEY (`Bookno`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
