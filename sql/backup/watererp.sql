-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Sep 22, 2017 at 07:57 AM
-- Server version: 5.7.19-0ubuntu0.16.04.1
-- PHP Version: 7.0.22-0ubuntu0.16.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `watererp`
--

-- --------------------------------------------------------

--
-- Table structure for table `access_list`
--

CREATE TABLE `access_list` (
  `id` bigint(20) NOT NULL,
  `user_id` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `access_list`
--

INSERT INTO `access_list` (`id`, `user_id`) VALUES
(1, 'admin1'),
(2, 'admin2'),
(3, 'admin3'),
(4, 'admin4'),
(5, 'admin5'),
(6, 'admin6'),
(7, 'admin7'),
(8, 'admin8'),
(9, 'admin9'),
(10, 'admin10'),
(11, 'admin11'),
(12, 'admin12'),
(13, 'admin13'),
(14, 'dddd');

-- --------------------------------------------------------

--
-- Table structure for table `adjustments`
--

CREATE TABLE `adjustments` (
  `id` bigint(20) NOT NULL,
  `can` varchar(255) DEFAULT NULL,
  `amount` decimal(20,3) DEFAULT NULL,
  `remarks` varchar(255) DEFAULT NULL,
  `txn_time` timestamp NULL DEFAULT NULL,
  `status` varchar(255) NOT NULL,
  `cust_details_id` bigint(20) DEFAULT NULL,
  `bill_full_details_id` bigint(20) DEFAULT NULL,
  `transaction_type_master_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `customer_complaints_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `adjustments`
--

INSERT INTO `adjustments` (`id`, `can`, `amount`, `remarks`, `txn_time`, `status`, `cust_details_id`, `bill_full_details_id`, `transaction_type_master_id`, `user_id`, `customer_complaints_id`) VALUES
(16892, '39B06411', '115000.000', '1//hakuwa na maji miezi ya kiangazi apunguziwe bili zake alipe nusu//barua ya 15/8/2015', '2015-02-11 10:30:00', 'INITIATED', NULL, NULL, 1, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `application_txn`
--

CREATE TABLE `application_txn` (
  `id` bigint(20) NOT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `middle_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `organization` bit(1) DEFAULT NULL,
  `organization_name` varchar(255) DEFAULT NULL,
  `designation` varchar(255) DEFAULT NULL,
  `mobile_no` bigint(20) DEFAULT NULL,
  `office_no` bigint(20) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `street` varchar(255) DEFAULT NULL,
  `plot_no` varchar(255) DEFAULT NULL,
  `block_no` varchar(255) DEFAULT NULL,
  `tanesco_meter` varchar(255) DEFAULT NULL,
  `water_connection_use` varchar(255) DEFAULT NULL,
  `b_street` varchar(255) DEFAULT NULL,
  `ward` varchar(255) DEFAULT NULL,
  `dma` varchar(255) DEFAULT NULL,
  `b_plot_no` varchar(255) DEFAULT NULL,
  `registered_mobile` bigint(20) DEFAULT NULL,
  `id_number` varchar(255) DEFAULT NULL,
  `property_doc` varchar(255) DEFAULT NULL,
  `can` varchar(255) DEFAULT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `meter_reading` decimal(20,3) DEFAULT NULL,
  `requested_date` date DEFAULT NULL,
  `connection_date` date DEFAULT NULL,
  `remarks` varchar(255) DEFAULT NULL,
  `meter_no` varchar(255) DEFAULT NULL,
  `approved_date` date DEFAULT NULL,
  `deed_doc` varchar(255) DEFAULT NULL,
  `agreement_doc` varchar(255) DEFAULT NULL,
  `tariff_category_master_id` bigint(20) DEFAULT NULL,
  `meter_details_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `request_at_id` bigint(20) DEFAULT NULL,
  `division_master_id` bigint(20) DEFAULT NULL,
  `street_master_id` bigint(20) DEFAULT NULL,
  `id_proof_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `application_type_master`
--

CREATE TABLE `application_type_master` (
  `id` bigint(20) NOT NULL,
  `application_type` varchar(255) DEFAULT NULL,
  `created_date` timestamp NULL DEFAULT NULL,
  `updated_date` timestamp NULL DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `created_by` varchar(255) DEFAULT NULL,
  `updated_by` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `application_type_master`
--

INSERT INTO `application_type_master` (`id`, `application_type`, `created_date`, `updated_date`, `status`, `created_by`, `updated_by`) VALUES
(1, 'Charity Institute', '2016-03-03 16:00:00', '2016-03-03 16:00:00', '1', 'abc', 'abc'),
(2, 'Feasibility Reciept', '2016-03-03 16:00:00', '2016-03-03 16:00:00', '1', 'abc', 'abc'),
(3, 'Filling Station', '2016-03-03 16:00:00', '2016-03-03 16:00:00', '1', 'abc', 'abc'),
(4, 'General', '2016-03-03 16:00:00', '2016-03-03 16:00:00', '1', 'abc', 'abc');

-- --------------------------------------------------------

--
-- Table structure for table `bank_master`
--

CREATE TABLE `bank_master` (
  `id` bigint(20) NOT NULL,
  `bank_code` varchar(255) NOT NULL,
  `bank_name` varchar(255) NOT NULL,
  `bank_branch` varchar(255) DEFAULT NULL,
  `bank_account` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `bank_master`
--

INSERT INTO `bank_master` (`id`, `bank_code`, `bank_name`, `bank_branch`, `bank_account`) VALUES
(85, 'BOT', 'BANK OF TANZANIA              ', 'DAR ES SALAAM       ', NULL),
(86, 'CRDB', 'CRDB KIGOMA BRANCH            ', 'KIGOMA              ', NULL),
(87, 'NBC', 'NBC KIGOMA BRANCH             ', 'KIGOMA              ', NULL),
(88, 'NMB', 'NMB KIGOMA BRANCH             ', 'KIGOMA              ', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `bill_details`
--

CREATE TABLE `bill_details` (
  `id` bigint(20) NOT NULL,
  `can` varchar(255) DEFAULT NULL,
  `bill_number` varchar(255) DEFAULT NULL,
  `bill_date` date NOT NULL,
  `bill_time` varchar(255) DEFAULT NULL,
  `meter_make` varchar(255) DEFAULT NULL,
  `current_bill_type` varchar(255) DEFAULT NULL,
  `from_month` varchar(255) DEFAULT NULL,
  `to_month` varchar(255) DEFAULT NULL,
  `meter_fix_date` date DEFAULT NULL,
  `initial_reading` decimal(20,3) DEFAULT NULL,
  `present_reading` decimal(20,3) DEFAULT NULL,
  `units` decimal(20,3) DEFAULT NULL,
  `water_cess` decimal(20,3) DEFAULT NULL,
  `sewerage_cess` decimal(20,3) DEFAULT NULL,
  `service_charge` decimal(20,3) DEFAULT NULL,
  `meter_service_charge` decimal(20,3) DEFAULT NULL,
  `total_amount` decimal(20,3) DEFAULT NULL,
  `net_payable_amount` decimal(20,3) DEFAULT NULL,
  `telephone_no` varchar(255) DEFAULT NULL,
  `meter_status` varchar(255) DEFAULT NULL,
  `met_reader_code` varchar(255) DEFAULT NULL,
  `bill_flag` varchar(255) DEFAULT NULL,
  `svr_status` varchar(255) DEFAULT NULL,
  `terminal_id` varchar(255) DEFAULT NULL,
  `meter_reader_id` varchar(255) DEFAULT NULL,
  `user_id` varchar(255) DEFAULT NULL,
  `mobile_no` varchar(255) DEFAULT NULL,
  `notice_no` varchar(255) DEFAULT NULL,
  `lat` varchar(255) DEFAULT NULL,
  `longi` varchar(255) DEFAULT NULL,
  `no_meter_amt` decimal(20,3) DEFAULT NULL,
  `met_reading_dt` date DEFAULT NULL,
  `is_rounding` bit(1) DEFAULT NULL,
  `insert_dt` timestamp NULL DEFAULT NULL,
  `status` varchar(255) NOT NULL,
  `mtr_reader_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `bill_details`
--

INSERT INTO `bill_details` (`id`, `can`, `bill_number`, `bill_date`, `bill_time`, `meter_make`, `current_bill_type`, `from_month`, `to_month`, `meter_fix_date`, `initial_reading`, `present_reading`, `units`, `water_cess`, `sewerage_cess`, `service_charge`, `meter_service_charge`, `total_amount`, `net_payable_amount`, `telephone_no`, `meter_status`, `met_reader_code`, `bill_flag`, `svr_status`, `terminal_id`, `meter_reader_id`, `user_id`, `mobile_no`, `notice_no`, `lat`, `longi`, `no_meter_amt`, `met_reading_dt`, `is_rounding`, `insert_dt`, `status`, `mtr_reader_id`) VALUES
(1, '10100111', '', '2016-02-01', '', '', 'L', '201602', '201602', NULL, '0.000', NULL, '0.000', '0.000', '0.000', '0.000', '0.000', '0.000', '0.000', '', '', '', '', '', '', '', '', '', '', '0', '0', '0.000', '2016-02-27', b'0', '2016-09-05 07:47:34', 'INITIATED', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `bill_full_details`
--

CREATE TABLE `bill_full_details` (
  `id` bigint(20) NOT NULL,
  `can` varchar(255) NOT NULL,
  `div_code` varchar(255) NOT NULL,
  `sec_code` varchar(255) DEFAULT NULL,
  `sec_name` varchar(255) DEFAULT NULL,
  `met_reader_code` varchar(255) DEFAULT NULL,
  `conn_date` date DEFAULT NULL,
  `cons_name` varchar(255) NOT NULL,
  `house_no` varchar(255) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `city` varchar(255) NOT NULL,
  `pin_code` varchar(255) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `pipe_size` decimal(20,3) DEFAULT NULL,
  `board_meter` varchar(255) DEFAULT NULL,
  `sewerage` varchar(255) DEFAULT NULL,
  `prev_bill_type` varchar(255) DEFAULT NULL,
  `prev_bill_month` date DEFAULT NULL,
  `prev_avg_kl` decimal(20,3) DEFAULT NULL,
  `met_reading_dt` date NOT NULL,
  `prev_reading` decimal(20,3) DEFAULT NULL,
  `met_reading_mo` date DEFAULT NULL,
  `met_avg_kl` decimal(20,3) DEFAULT NULL,
  `arrears` decimal(20,3) DEFAULT NULL,
  `reversal_amt` decimal(20,3) DEFAULT NULL,
  `installment` decimal(20,3) DEFAULT NULL,
  `other_charges` decimal(20,3) DEFAULT NULL,
  `surcharge` decimal(20,3) DEFAULT NULL,
  `hrs_surcharge` varchar(255) DEFAULT NULL,
  `res_units` bigint(20) DEFAULT NULL,
  `met_cost_installment` decimal(20,3) DEFAULT NULL,
  `int_on_arrears` decimal(20,3) DEFAULT NULL,
  `last_pymt_dt` date DEFAULT NULL,
  `last_pymt_amt` decimal(20,3) DEFAULT NULL,
  `bill_number` varchar(255) DEFAULT NULL,
  `bill_date` date NOT NULL,
  `bill_time` varchar(255) DEFAULT NULL,
  `meter_make` varchar(255) DEFAULT NULL,
  `current_bill_type` varchar(255) DEFAULT NULL,
  `from_month` varchar(255) DEFAULT NULL,
  `to_month` varchar(255) DEFAULT NULL,
  `meter_fix_date` date DEFAULT NULL,
  `initial_reading` decimal(20,3) DEFAULT NULL,
  `present_reading` decimal(20,3) DEFAULT NULL,
  `units` decimal(20,3) DEFAULT NULL,
  `water_cess` decimal(20,3) DEFAULT NULL,
  `sewerage_cess` decimal(20,3) DEFAULT NULL,
  `service_charge` decimal(20,3) DEFAULT NULL,
  `meter_service_charge` decimal(20,3) DEFAULT NULL,
  `total_amount` decimal(20,3) DEFAULT NULL,
  `net_payable_amount` decimal(20,3) DEFAULT NULL,
  `telephone_no` varchar(255) DEFAULT NULL,
  `meter_status` varchar(255) DEFAULT NULL,
  `bill_flag` varchar(255) DEFAULT NULL,
  `svr_status` varchar(255) DEFAULT NULL,
  `terminal_id` varchar(255) DEFAULT NULL,
  `meter_reader_id` varchar(255) DEFAULT NULL,
  `user_id` varchar(255) DEFAULT NULL,
  `mobile_no` varchar(255) DEFAULT NULL,
  `notice_no` varchar(255) DEFAULT NULL,
  `lat` varchar(255) DEFAULT NULL,
  `longi` varchar(255) DEFAULT NULL,
  `no_meter_amt` decimal(20,3) DEFAULT NULL,
  `lock_charges` decimal(20,3) DEFAULT NULL,
  `due_amount` decimal(20,3) DEFAULT NULL,
  `meter_details_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `bill_full_details`
--

INSERT INTO `bill_full_details` (`id`, `can`, `div_code`, `sec_code`, `sec_name`, `met_reader_code`, `conn_date`, `cons_name`, `house_no`, `address`, `city`, `pin_code`, `category`, `pipe_size`, `board_meter`, `sewerage`, `prev_bill_type`, `prev_bill_month`, `prev_avg_kl`, `met_reading_dt`, `prev_reading`, `met_reading_mo`, `met_avg_kl`, `arrears`, `reversal_amt`, `installment`, `other_charges`, `surcharge`, `hrs_surcharge`, `res_units`, `met_cost_installment`, `int_on_arrears`, `last_pymt_dt`, `last_pymt_amt`, `bill_number`, `bill_date`, `bill_time`, `meter_make`, `current_bill_type`, `from_month`, `to_month`, `meter_fix_date`, `initial_reading`, `present_reading`, `units`, `water_cess`, `sewerage_cess`, `service_charge`, `meter_service_charge`, `total_amount`, `net_payable_amount`, `telephone_no`, `meter_status`, `bill_flag`, `svr_status`, `terminal_id`, `meter_reader_id`, `user_id`, `mobile_no`, `notice_no`, `lat`, `longi`, `no_meter_amt`, `lock_charges`, `due_amount`, `meter_details_id`) VALUES
(293, '30518511', '01', '01', NULL, NULL, '2016-09-16', 'Harry', '9-56/b', 'Street4', 'Newyork', '500039', 'Domestic', '0.750', NULL, NULL, NULL, NULL, NULL, '0000-00-00', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '100.000', '100', NULL, NULL, NULL, NULL, NULL, '7382', '2016-09-16', NULL, NULL, NULL, NULL, '201609', NULL, NULL, NULL, NULL, '100.000', '100.000', '100.000', NULL, '300.000', '315.000', NULL, '1', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '15.000', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `bill_run_details`
--

CREATE TABLE `bill_run_details` (
  `id` bigint(20) NOT NULL,
  `can` varchar(255) DEFAULT NULL,
  `from_dt` timestamp NULL DEFAULT NULL,
  `to_dt` timestamp NULL DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `remarks` varchar(255) DEFAULT NULL,
  `bill_full_details_id` bigint(20) DEFAULT NULL,
  `bill_run_master_id` bigint(20) DEFAULT NULL,
  `bill_details_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `bill_run_details`
--

INSERT INTO `bill_run_details` (`id`, `can`, `from_dt`, `to_dt`, `status`, `remarks`, `bill_full_details_id`, `bill_run_master_id`, `bill_details_id`) VALUES
(1, '30518511', NULL, NULL, 4, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `bill_run_master`
--

CREATE TABLE `bill_run_master` (
  `id` bigint(20) NOT NULL,
  `date` timestamp NULL DEFAULT NULL,
  `area` varchar(255) DEFAULT NULL,
  `success` int(11) DEFAULT NULL,
  `failed` int(11) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bill_run_master`
--

INSERT INTO `bill_run_master` (`id`, `date`, `area`, `success`, `failed`, `status`) VALUES
(1, '2016-06-25 22:05:47', '0', 0, 0, 'In Process');

-- --------------------------------------------------------

--
-- Table structure for table `burst_complaint`
--

CREATE TABLE `burst_complaint` (
  `id` bigint(20) NOT NULL,
  `meter_location` varchar(255) DEFAULT NULL,
  `burst_pipe` varchar(255) DEFAULT NULL,
  `from_left` varchar(255) DEFAULT NULL,
  `from_sb` varchar(255) DEFAULT NULL,
  `burst_area` varchar(255) DEFAULT NULL,
  `pipe_type` varchar(255) DEFAULT NULL,
  `pipe_size` int(11) DEFAULT NULL,
  `hole_size` int(11) DEFAULT NULL,
  `repair_code` varchar(255) DEFAULT NULL,
  `water_leakage_complaint_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `cash_book_master`
--

CREATE TABLE `cash_book_master` (
  `id` bigint(20) NOT NULL,
  `cash_book_entry_type` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `category_master`
--

CREATE TABLE `category_master` (
  `id` bigint(20) NOT NULL,
  `category_name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `category_master`
--

INSERT INTO `category_master` (`id`, `category_name`) VALUES
(1, 'Domestic'),
(2, 'Institutional'),
(3, 'Commercial'),
(4, 'Industrial'),
(5, 'Kiosks');

-- --------------------------------------------------------

--
-- Table structure for table `category_pipe_size_mapping`
--

CREATE TABLE `category_pipe_size_mapping` (
  `id` bigint(20) NOT NULL,
  `category_master_id` bigint(20) DEFAULT NULL,
  `pipe_size_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `charge_base`
--

CREATE TABLE `charge_base` (
  `id` bigint(20) NOT NULL,
  `code` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `collection_type_master`
--

CREATE TABLE `collection_type_master` (
  `id` bigint(20) NOT NULL,
  `coll_name` varchar(255) DEFAULT NULL,
  `txn_type` varchar(255) NOT NULL,
  `has_account_no` bit(1) DEFAULT NULL,
  `account_code` varchar(255) DEFAULT NULL,
  `receipt_code` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `collection_type_master`
--

INSERT INTO `collection_type_master` (`id`, `coll_name`, `txn_type`, `has_account_no`, `account_code`, `receipt_code`) VALUES
(55, 'Bowser/Other Customers', 'PAYMENT', b'0', '1011', '101'),
(56, 'New Water Connection', 'PAYMENT', b'0', '1022', '103'),
(57, 'Reconnection  Fee', 'PAYMENT', b'1', '1023', '108'),
(58, 'Line Maintenance', 'PAYMENT', b'1', NULL, '113'),
(59, 'Meter Test Fee', 'PAYMENT', b'1', '1030', '114'),
(60, 'Arrears ad', 'PAYMENT', b'0', NULL, '115'),
(61, 'Water Meter Rent', 'PAYMENT', b'1', '1013', '116'),
(62, 'Deposit', 'PAYMENT', b'0', NULL, '117'),
(63, 'Cesspit', 'PAYMENT', b'0', NULL, '118'),
(64, 'Extension/Alteration', 'PAYMENT', b'1', '1030', '119'),
(65, 'Compensation from customer', 'PAYMENT', b'1', '1013', '224'),
(66, 'Water Sales Adjustment', 'ADJUSTMENT', b'1', NULL, '301'),
(67, 'Water Service Charges Adjustment', 'ADJUSTMENT', b'1', NULL, '302'),
(68, 'Water Meter Rent Adjustment', 'ADJUSTMENT', b'1', NULL, '303'),
(69, 'Water Rentals Adjustment', 'ADJUSTMENT', b'1', NULL, '304'),
(70, 'Sewer Removal Adjustment', 'ADJUSTMENT', b'1', NULL, '401'),
(71, 'Sewer Service Charges Adjustment', 'ADJUSTMENT', b'1', NULL, '402'),
(72, 'Sewer Meter Rent Adjustment', 'ADJUSTMENT', b'1', NULL, '403'),
(73, 'Sewer Rentals Adjustment', 'ADJUSTMENT', b'1', NULL, '404'),
(74, 'New Sewer Connection Charges', 'PAYMENT', b'0', NULL, '405'),
(75, 'Advance Payment', 'PAYMENT', b'1', '1011', '501'),
(76, 'Advance Adjustment', 'ADJUSTMENT', b'1', NULL, '502'),
(77, 'Water Sales', 'C', b'1', '1011', '601'),
(78, 'Water Service Charges', 'PAYMENT', b'1', '1030', '602'),
(79, 'Water Other Charges', 'PAYMENT', b'1', '1014', '604'),
(80, 'Address Change', 'PAYMENT', b'1', NULL, '654'),
(81, 'Sewer Use', 'PAYMENT', b'1', NULL, '701'),
(82, 'Sewer Service Charges', 'PAYMENT', b'1', NULL, '702'),
(83, 'Sewer Rentals', 'PAYMENT', b'1', NULL, '703'),
(84, 'Sewer Other Charges', 'PAYMENT', b'1', NULL, '704'),
(85, 'Other Deposits', 'PAYMENT', b'0', '1030', '705'),
(86, 'Transfer of funds', 'PAYMENT', b'0', NULL, '706'),
(87, 'Meter Test Fee(not in use)', 'PAYMENT', b'0', NULL, '801'),
(88, 'VAT Refund', 'PAYMENT', b'0', NULL, '802'),
(89, 'Bank Interest', 'PAYMENT', b'0', NULL, '803'),
(90, 'Gain/Loss on forex', 'PAYMENT', b'0', NULL, '804'),
(91, 'Disposal Income (Sale of Assets)', 'PAYMENT', b'0', NULL, '805'),
(92, 'Tender Document Fees', 'PAYMENT', b'0', NULL, '806'),
(93, 'Investment Income', 'PAYMENT', b'0', NULL, '807'),
(94, 'Salary Notice', 'PAYMENT', b'0', NULL, '808'),
(95, 'Broken/stolen Meters', 'PAYMENT', b'1', NULL, '809'),
(96, 'Doubtful Debts Written Back', 'PAYMENT', b'0', NULL, '900'),
(97, 'Advances Recovery', 'PAYMENT', b'0', NULL, '901'),
(98, 'Staff Imprest', 'PAYMENT', b'0', NULL, '902'),
(99, 'Debtors(water meter rent)', 'PAYMENT', b'0', NULL, '903'),
(100, 'Other Debtors', 'PAYMENT', b'0', NULL, '904'),
(101, 'Prepayments', 'PAYMENT', b'0', NULL, '905'),
(102, 'Billing for other services', 'PAYMENT', b'0', '1030', '906'),
(103, 'Governmant Grant', 'PAYMENT', b'0', '8100', '908'),
(104, 'Donor Grant', 'PAYMENT', b'0', NULL, '909'),
(105, 'Workshop', 'PAYMENT', b'0', NULL, '910'),
(106, 'Canteen', 'PAYMENT', b'0', NULL, '911'),
(107, 'Carpentry', 'PAYMENT', b'0', NULL, '912'),
(108, 'Conference Hall (room)', 'PAYMENT', b'0', NULL, '913');

-- --------------------------------------------------------

--
-- Table structure for table `coll_details`
--

CREATE TABLE `coll_details` (
  `id` bigint(20) NOT NULL,
  `reversal_ref` varchar(255) DEFAULT NULL,
  `receipt_no` varchar(255) DEFAULT NULL,
  `receipt_amt` decimal(20,3) DEFAULT NULL,
  `receipt_dt` timestamp NULL DEFAULT NULL,
  `receipt_mode` varchar(255) DEFAULT NULL,
  `instr_no` varchar(255) DEFAULT NULL,
  `instr_dt` date DEFAULT NULL,
  `instr_issuer` varchar(255) DEFAULT NULL,
  `svr_status` varchar(255) DEFAULT NULL,
  `can` varchar(255) DEFAULT NULL,
  `cons_name` varchar(255) DEFAULT NULL,
  `terminal_id` varchar(255) DEFAULT NULL,
  `coll_time` timestamp NULL DEFAULT NULL,
  `txn_status` varchar(255) DEFAULT NULL,
  `meter_reader_id` varchar(255) DEFAULT NULL,
  `user_id` varchar(255) DEFAULT NULL,
  `remarks` varchar(255) DEFAULT NULL,
  `settlement_id` varchar(255) DEFAULT NULL,
  `ext_settlement_id` varchar(255) DEFAULT NULL,
  `lat` varchar(255) DEFAULT NULL,
  `long_i` varchar(255) DEFAULT NULL,
  `payment_types_id` bigint(20) DEFAULT NULL,
  `bank_master_id` bigint(20) DEFAULT NULL,
  `collection_type_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `coll_details`
--

INSERT INTO `coll_details` (`id`, `reversal_ref`, `receipt_no`, `receipt_amt`, `receipt_dt`, `receipt_mode`, `instr_no`, `instr_dt`, `instr_issuer`, `svr_status`, `can`, `cons_name`, `terminal_id`, `coll_time`, `txn_status`, `meter_reader_id`, `user_id`, `remarks`, `settlement_id`, `ext_settlement_id`, `lat`, `long_i`, `payment_types_id`, `bank_master_id`, `collection_type_master_id`) VALUES
(1, '', '1', '15900.000', '2011-03-25 09:30:00', 'Cash', NULL, NULL, '', '0', '30518511', '', '', '2011-03-26 00:00:14', '', '', '', '168698.0', 'Feb-2011', '', '0', '0', 1, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `complaint_type_master`
--

CREATE TABLE `complaint_type_master` (
  `id` bigint(20) NOT NULL,
  `complaint_type` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `complaint_type_master`
--

INSERT INTO `complaint_type_master` (`id`, `complaint_type`) VALUES
(1, 'INCORRECT BILL'),
(2, 'WATER LEAKAGE'),
(3, 'SERVICE UNAVAILABILITY');

-- --------------------------------------------------------

--
-- Table structure for table `configuration_details`
--

CREATE TABLE `configuration_details` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `value` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `configuration_details`
--

INSERT INTO `configuration_details` (`id`, `name`, `value`, `description`) VALUES
(1, 'ADMIN', '97', NULL),
(2, 'EWURA', '1', 'EWURA - % of Water Usage Charges'),
(3, 'SEWERAGE', '10', 'Sewerage as % of Water Usage Charges'),
(4, 'SUPERVISION', '10', 'Used in proceedings'),
(5, 'LABOUR CHARGES', '20', 'Used in proceedings'),
(6, 'SITE SURVEY', '5', 'Used in proceedings'),
(7, 'CONNECTION FEE OF A & B', '20', 'Used in proceedings'),
(8, 'APPLICATION FORM FEE', '1000', 'Used in proceedings'),
(9, 'ONLINE_PAYMENT_SERVER_URL', 'http://', 'This server will be invoked for making online payments'),
(10, 'ONLINE_PAYMENT_SERVICE_CODE', 'TESTS001', 'WaterERP Service Code for Online Payment'),
(11, 'ONLINE_PAYMENT_MERCHANT_CODE', 'Test001', 'WaterERP Merchant Code for Online Payment'),
(12, 'BOARD_METER', 'T', 'true'),
(13, 'CITY', 'KIGOMA', ''),
(14, 'PIN', '812', ''),
(15, 'SEWERAGE_CONN', 'F', 'false'),
(16, 'MIN_AVG_KL', '2.5', 'Min. Avg KL in case customer\'s Avg KL is not available'),
(17, 'NAME_CHANGE_FEE', '1000', NULL),
(18, 'MIGRATION_BILL_MONTH', '201303', 'Bill Month to migrate. Only used during one time migration');

-- --------------------------------------------------------

--
-- Table structure for table `connection_terminate`
--

CREATE TABLE `connection_terminate` (
  `id` bigint(20) NOT NULL,
  `can` varchar(255) DEFAULT NULL,
  `request_date` date DEFAULT NULL,
  `meter_recovered` bit(1) DEFAULT NULL,
  `last_meter_reading` decimal(20,3) DEFAULT NULL,
  `meter_recovered_date` date DEFAULT NULL,
  `meter_details_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `connection_type_master`
--

CREATE TABLE `connection_type_master` (
  `id` bigint(20) NOT NULL,
  `connection_type` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `connection_type_master`
--

INSERT INTO `connection_type_master` (`id`, `connection_type`) VALUES
(1, 'Sewerage Connection'),
(2, 'Water And Sewerage');

-- --------------------------------------------------------

--
-- Table structure for table `current_users`
--

CREATE TABLE `current_users` (
  `id` bigint(20) NOT NULL,
  `terminal_id` varchar(255) DEFAULT NULL,
  `meter_reader_id` varchar(255) DEFAULT NULL,
  `user_id` varchar(255) DEFAULT NULL,
  `request_type` varchar(255) DEFAULT NULL,
  `login_time` timestamp NULL DEFAULT NULL,
  `ip` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `current_users`
--

INSERT INTO `current_users` (`id`, `terminal_id`, `meter_reader_id`, `user_id`, `request_type`, `login_time`, `ip`) VALUES
(1, 'TerminalId1', 'MeterReaderId1', 'UserId1', 'RequestType1', '2016-03-18 15:00:00', 'Ip1'),
(2, 'sss', 'sss', 'sss', 'ssss', '2016-04-12 15:00:00', 'ssss');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `id` bigint(20) NOT NULL,
  `prev_meter_reading` decimal(20,3) DEFAULT NULL,
  `new_meter_reading` decimal(20,3) DEFAULT NULL,
  `organization` bit(1) DEFAULT NULL,
  `organization_name` varchar(255) DEFAULT NULL,
  `designation` varchar(255) DEFAULT NULL,
  `deed_doc` varchar(255) DEFAULT NULL,
  `agreement_doc` varchar(255) DEFAULT NULL,
  `remarks` varchar(255) DEFAULT NULL,
  `requested_date` date DEFAULT NULL,
  `can` varchar(255) DEFAULT NULL,
  `previous_name` varchar(255) DEFAULT NULL,
  `previous_mobile` bigint(20) DEFAULT NULL,
  `previous_email` varchar(255) DEFAULT NULL,
  `new_email` varchar(255) DEFAULT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `middle_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `mobile_no` bigint(20) DEFAULT NULL,
  `id_number` varchar(255) DEFAULT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `status` varchar(255) NOT NULL,
  `changed_date` date DEFAULT NULL,
  `change_type` varchar(255) NOT NULL,
  `old_tariff_category_id` bigint(20) DEFAULT NULL,
  `new_tariff_category_id` bigint(20) DEFAULT NULL,
  `new_proof_master_id` bigint(20) DEFAULT NULL,
  `old_pipe_size_master_id` bigint(20) DEFAULT NULL,
  `requested_pipe_size_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `customer_complaints`
--

CREATE TABLE `customer_complaints` (
  `id` bigint(20) NOT NULL,
  `remarks` varchar(255) DEFAULT NULL,
  `relevant_doc` varchar(255) DEFAULT NULL,
  `complaint_by` varchar(255) DEFAULT NULL,
  `complaint_date` date DEFAULT NULL,
  `can` varchar(255) DEFAULT NULL,
  `adjustment_amt` decimal(20,3) DEFAULT NULL,
  `adjustment_bill_id` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `complaint_type_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer_complaints`
--

INSERT INTO `customer_complaints` (`id`, `remarks`, `relevant_doc`, `complaint_by`, `complaint_date`, `can`, `adjustment_amt`, `adjustment_bill_id`, `status`, `complaint_type_master_id`) VALUES
(7, 'incorrect bill', '/api/download/7_82eaa75fc125f8ee80c26ab30280d188_WaterLeakage Complaint.JPG', 'A0100111', '2016-09-09', 'A0100111', NULL, NULL, 1, 1),
(8, 'Incorrect Bill', '', 'A0100111', '2016-09-09', 'A0100111', '380.340', '297', 5, 1),
(9, 'incorrect bill', '', 'javed', '2016-09-14', '04060001', NULL, NULL, 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `cust_details`
--

CREATE TABLE `cust_details` (
  `id` bigint(20) NOT NULL,
  `can` varchar(255) NOT NULL,
  `div_code` varchar(255) DEFAULT NULL,
  `sec_code` varchar(255) DEFAULT NULL,
  `sec_name` varchar(255) DEFAULT NULL,
  `met_reader_code` varchar(255) DEFAULT NULL,
  `conn_date` date DEFAULT NULL,
  `cons_name` varchar(255) NOT NULL,
  `house_no` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `pin_code` varchar(255) DEFAULT NULL,
  `category_unused` varchar(255) DEFAULT NULL,
  `pipe_size` decimal(20,3) DEFAULT NULL,
  `board_meter` varchar(255) DEFAULT NULL,
  `sewerage` varchar(255) DEFAULT NULL,
  `prev_bill_type` varchar(255) DEFAULT NULL,
  `prev_bill_month` date DEFAULT NULL,
  `prev_avg_kl` decimal(20,3) DEFAULT NULL,
  `met_reading_dt` date DEFAULT NULL,
  `prev_reading` decimal(20,3) DEFAULT NULL,
  `met_reading_mo` date DEFAULT NULL,
  `met_avg_kl` decimal(20,3) DEFAULT NULL,
  `arrears` decimal(20,3) DEFAULT NULL,
  `reversal_amt` decimal(20,3) DEFAULT NULL,
  `installment` decimal(20,3) DEFAULT NULL,
  `other_charges` decimal(20,3) DEFAULT NULL,
  `surcharge` decimal(20,3) DEFAULT NULL,
  `hrs_surcharge` varchar(255) DEFAULT NULL,
  `res_units` bigint(20) DEFAULT NULL,
  `met_cost_installment` decimal(20,3) DEFAULT NULL,
  `int_on_arrears` decimal(20,3) DEFAULT NULL,
  `last_pymt_dt` date DEFAULT NULL,
  `last_pymt_amt` decimal(20,3) DEFAULT NULL,
  `mobile_no` varchar(255) DEFAULT NULL,
  `cc_flag` varchar(255) DEFAULT NULL,
  `cp_flag` varchar(255) DEFAULT NULL,
  `notice_flag` varchar(255) DEFAULT NULL,
  `dr_flag` varchar(255) DEFAULT NULL,
  `lat` varchar(255) DEFAULT NULL,
  `longi` varchar(255) DEFAULT NULL,
  `meter_fix_date` date DEFAULT NULL,
  `lock_charges` decimal(20,3) DEFAULT NULL,
  `id_number` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `status` varchar(255) NOT NULL,
  `organisation_name` varchar(255) DEFAULT NULL,
  `designation` varchar(255) DEFAULT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `deed_doc` varchar(255) DEFAULT NULL,
  `agreement_doc` varchar(255) DEFAULT NULL,
  `tariff_category_master_id` bigint(20) DEFAULT NULL,
  `pipe_size_master_id` bigint(20) DEFAULT NULL,
  `division_master_id` bigint(20) DEFAULT NULL,
  `street_master_id` bigint(20) DEFAULT NULL,
  `meter_details_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `cust_details`
--

INSERT INTO `cust_details` (`id`, `can`, `div_code`, `sec_code`, `sec_name`, `met_reader_code`, `conn_date`, `cons_name`, `house_no`, `address`, `city`, `pin_code`, `category_unused`, `pipe_size`, `board_meter`, `sewerage`, `prev_bill_type`, `prev_bill_month`, `prev_avg_kl`, `met_reading_dt`, `prev_reading`, `met_reading_mo`, `met_avg_kl`, `arrears`, `reversal_amt`, `installment`, `other_charges`, `surcharge`, `hrs_surcharge`, `res_units`, `met_cost_installment`, `int_on_arrears`, `last_pymt_dt`, `last_pymt_amt`, `mobile_no`, `cc_flag`, `cp_flag`, `notice_flag`, `dr_flag`, `lat`, `longi`, `meter_fix_date`, `lock_charges`, `id_number`, `email`, `status`, `organisation_name`, `designation`, `photo`, `deed_doc`, `agreement_doc`, `tariff_category_master_id`, `pipe_size_master_id`, `division_master_id`, `street_master_id`, `meter_details_id`) VALUES
(4673, '10102611', 'TEST AREA', '10102611', '', '', NULL, 'TEST TEST', '026', 'BOMA AREA, , TEST', 'TEST', '303', NULL, '0.250', 'T', 'F', 'U', '2016-01-01', '0.000', NULL, NULL, NULL, '0.000', '49112.400', '0.000', '0.000', '0.000', '0.000', '0.00', 1, '0.000', '0.000', NULL, '0.000', '', '0', '0', '0', '0', '0', '0', NULL, '0.000', '', '', 'ACTIVE', NULL, NULL, NULL, NULL, NULL, 6, 1, 11, 14, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `cust_meter_mapping`
--

CREATE TABLE `cust_meter_mapping` (
  `id` bigint(20) NOT NULL,
  `from_date` date NOT NULL,
  `to_date` date DEFAULT NULL,
  `cust_details_id` bigint(20) DEFAULT NULL,
  `meter_details_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `cust_meter_mapping`
--

INSERT INTO `cust_meter_mapping` (`id`, `from_date`, `to_date`, `cust_details_id`, `meter_details_id`) VALUES
(1, '2016-09-12', NULL, 4673, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `databasechangelog`
--

CREATE TABLE `databasechangelog` (
  `ID` varchar(255) NOT NULL,
  `AUTHOR` varchar(255) NOT NULL,
  `FILENAME` varchar(255) NOT NULL,
  `DATEEXECUTED` datetime NOT NULL,
  `ORDEREXECUTED` int(11) NOT NULL,
  `EXECTYPE` varchar(10) NOT NULL,
  `MD5SUM` varchar(35) DEFAULT NULL,
  `DESCRIPTION` varchar(255) DEFAULT NULL,
  `COMMENTS` varchar(255) DEFAULT NULL,
  `TAG` varchar(255) DEFAULT NULL,
  `LIQUIBASE` varchar(20) DEFAULT NULL,
  `CONTEXTS` varchar(255) DEFAULT NULL,
  `LABELS` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `databasechangeloglock`
--

CREATE TABLE `databasechangeloglock` (
  `ID` int(11) NOT NULL,
  `LOCKED` bit(1) NOT NULL,
  `LOCKGRANTED` datetime DEFAULT NULL,
  `LOCKEDBY` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `databasechangeloglock`
--

INSERT INTO `databasechangeloglock` (`ID`, `LOCKED`, `LOCKGRANTED`, `LOCKEDBY`) VALUES
(1, b'1', '2016-09-16 19:03:00', 'LAPTOP-LVH2GO30 (192.168.56.1)');

-- --------------------------------------------------------

--
-- Table structure for table `departments_hierarchy`
--

CREATE TABLE `departments_hierarchy` (
  `id` bigint(20) NOT NULL,
  `dept_hierarchy_name` varchar(255) DEFAULT NULL,
  `parent_dept_hierarchy_id` int(11) DEFAULT NULL,
  `creation_date` timestamp NULL DEFAULT NULL,
  `last_modified_date` timestamp NULL DEFAULT NULL,
  `status_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `departments_master`
--

CREATE TABLE `departments_master` (
  `id` bigint(20) NOT NULL,
  `department_name` varchar(255) DEFAULT NULL,
  `parent_deparment` int(11) DEFAULT NULL,
  `creation_date` timestamp NULL DEFAULT NULL,
  `last_modified_date` timestamp NULL DEFAULT NULL,
  `departments_hierarchy_id` bigint(20) DEFAULT NULL,
  `department_type_master_id` bigint(20) DEFAULT NULL,
  `status_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `department_type_master`
--

CREATE TABLE `department_type_master` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `creation_date` timestamp NULL DEFAULT NULL,
  `last_modified_date` timestamp NULL DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `status_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `designation_mappings`
--

CREATE TABLE `designation_mappings` (
  `id` bigint(20) NOT NULL,
  `type` varchar(255) DEFAULT NULL,
  `desig_category_master_id` bigint(20) DEFAULT NULL,
  `sub_desig_category_master_id` bigint(20) DEFAULT NULL,
  `designation_master_id` bigint(20) DEFAULT NULL,
  `group_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `designation_master`
--

CREATE TABLE `designation_master` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `creation_date` timestamp NULL DEFAULT NULL,
  `last_modified_date` timestamp NULL DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `order_no` int(11) DEFAULT NULL,
  `service_type` varchar(255) DEFAULT NULL,
  `code` varchar(255) DEFAULT NULL,
  `desigalias` varchar(255) DEFAULT NULL,
  `status_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `designation_master`
--

INSERT INTO `designation_master` (`id`, `name`, `creation_date`, `last_modified_date`, `description`, `order_no`, `service_type`, `code`, `desigalias`, `status_master_id`) VALUES
(1, 'Board of Directors', '2016-08-18 20:41:51', '2016-08-18 20:42:39', NULL, NULL, NULL, NULL, NULL, 2),
(2, 'Managing Director', '2016-08-18 20:41:51', '2016-08-18 20:42:39', NULL, NULL, NULL, NULL, NULL, 2),
(3, 'Public Relations Officer', '2016-08-18 20:41:51', '2016-08-18 20:42:39', NULL, NULL, NULL, NULL, NULL, 2),
(4, 'Procurement management Unit', '2016-08-18 20:41:51', '2016-08-18 20:42:39', NULL, NULL, NULL, NULL, NULL, 2),
(5, 'Planning&Construction Eng.', '2016-08-18 20:41:51', '2016-08-18 20:42:39', NULL, NULL, NULL, NULL, NULL, 2),
(6, 'HR&AM', '2016-08-18 20:41:51', '2016-08-18 20:42:39', NULL, NULL, NULL, NULL, NULL, 2),
(7, 'Commercial Manager', '2016-08-18 20:41:51', '2016-08-18 20:42:39', NULL, NULL, NULL, NULL, NULL, 2),
(8, 'Finance Manager', '2016-08-18 20:41:51', '2016-08-18 20:42:39', NULL, NULL, NULL, NULL, NULL, 2),
(9, 'Internal Auditor', '2016-08-18 20:41:51', '2016-08-18 20:42:39', NULL, NULL, NULL, NULL, NULL, 2),
(10, 'Meter Reader', '2016-08-18 20:41:51', '2016-08-18 20:42:39', NULL, NULL, NULL, NULL, NULL, 2),
(11, 'Credit Control Oficer', '2016-08-18 20:41:51', '2016-08-18 20:42:39', NULL, NULL, NULL, NULL, NULL, 2),
(12, 'Billing Officer', '2016-08-18 20:41:51', '2016-08-18 20:42:39', NULL, NULL, NULL, NULL, NULL, 2),
(13, 'Customer Relation Officer', '2016-08-18 20:41:51', '2016-08-18 20:42:39', NULL, NULL, NULL, NULL, NULL, 2),
(14, 'Operation and Maintanance Tech.', '2016-08-18 20:41:51', '2016-08-18 20:42:39', NULL, NULL, NULL, NULL, NULL, 2),
(15, 'Distribution Network Technician', '2016-08-18 20:41:51', '2016-08-18 20:42:39', NULL, NULL, NULL, NULL, NULL, 2),
(16, 'Production Engineer', '2016-08-18 20:41:51', '2016-08-18 20:42:39', NULL, NULL, NULL, NULL, NULL, 2),
(17, 'Watchman', '2016-08-18 20:41:51', '2016-08-18 20:42:39', NULL, NULL, NULL, NULL, NULL, 2),
(18, 'HR &Admn.Officer', '2016-08-18 20:41:51', '2016-08-18 20:42:39', NULL, NULL, NULL, NULL, NULL, 2),
(19, 'Personal Secretary', '2016-08-18 20:41:51', '2016-08-18 20:42:39', NULL, NULL, NULL, NULL, NULL, 2),
(20, 'Driver', '2016-08-18 20:41:51', '2016-08-18 20:42:39', NULL, NULL, NULL, NULL, NULL, 2),
(21, 'Cashier', '2016-08-18 20:41:51', '2016-08-18 20:42:39', NULL, NULL, NULL, NULL, NULL, 2),
(22, 'Assistant Accountat', '2016-08-18 20:41:51', '2016-08-18 20:42:39', NULL, NULL, NULL, NULL, NULL, 2),
(23, 'Procurement and Suplies', '2016-08-18 20:41:51', '2016-08-18 20:42:39', NULL, NULL, NULL, NULL, NULL, 2),
(24, 'Electro mechanical Techns.', '2016-08-18 20:41:51', '2016-08-18 20:42:39', NULL, NULL, NULL, NULL, NULL, 2),
(25, 'Network Plumber', '2016-08-18 20:41:51', '2016-08-18 20:42:39', NULL, NULL, NULL, NULL, NULL, 2),
(26, 'O & M Plumber', '2016-08-18 20:41:51', '2016-08-18 20:42:39', NULL, NULL, NULL, NULL, NULL, 2),
(27, 'Technical Manager', '2016-08-18 20:41:51', '2016-08-18 20:42:39', NULL, NULL, NULL, NULL, NULL, 2),
(28, 'Head of Procurement', '2016-08-18 20:41:51', '2016-08-18 20:42:39', NULL, NULL, NULL, NULL, NULL, 2),
(29, 'O & M Engineer', '2016-08-18 20:41:51', '2016-08-18 20:42:39', NULL, NULL, NULL, NULL, NULL, 2);

-- --------------------------------------------------------

--
-- Table structure for table `desig_category_master`
--

CREATE TABLE `desig_category_master` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `creation_date` timestamp NULL DEFAULT NULL,
  `last_modified_date` timestamp NULL DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `alias` varchar(255) DEFAULT NULL,
  `order_by` int(11) DEFAULT NULL,
  `status_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `division_master`
--

CREATE TABLE `division_master` (
  `id` bigint(20) NOT NULL,
  `division_name` varchar(255) DEFAULT NULL,
  `division_code` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `division_master`
--

INSERT INTO `division_master` (`id`, `division_name`, `division_code`) VALUES
(1, 'DMA1', '01'),
(2, 'DMA2', '02'),
(3, 'DMA3', '03'),
(4, 'DMA4', '04'),
(5, 'DMA5', '05'),
(6, 'DMA6', '06'),
(7, 'DMA7', '07'),
(8, 'DMA8', '08'),
(9, 'DMA9', '09'),
(10, 'DMA10', '10'),
(11, 'General', '99');

-- --------------------------------------------------------

--
-- Table structure for table `docket_code`
--

CREATE TABLE `docket_code` (
  `id` bigint(20) NOT NULL,
  `code` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `docket_code`
--

INSERT INTO `docket_code` (`id`, `code`) VALUES
(1, 'Docket code 1'),
(2, 'Docket code 2');

-- --------------------------------------------------------

--
-- Table structure for table `emp_master`
--

CREATE TABLE `emp_master` (
  `id` bigint(20) NOT NULL,
  `date_of_birth` date DEFAULT NULL,
  `joining_date` date DEFAULT NULL,
  `marital_status` varchar(255) DEFAULT NULL,
  `employee_type` varchar(255) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `office_id_id` bigint(20) DEFAULT NULL,
  `designation_master_id` bigint(20) DEFAULT NULL,
  `directorate_id_id` bigint(20) DEFAULT NULL,
  `status_master_id` bigint(20) DEFAULT NULL,
  `reporting_to_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `emp_role_mapping`
--

CREATE TABLE `emp_role_mapping` (
  `id` bigint(20) NOT NULL,
  `internal_division` varchar(255) DEFAULT NULL,
  `internal_role` varchar(255) DEFAULT NULL,
  `creation_date` timestamp NULL DEFAULT NULL,
  `last_modified_date` timestamp NULL DEFAULT NULL,
  `parent_role_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `parent_user_id` bigint(20) DEFAULT NULL,
  `org_role_instance_id` bigint(20) DEFAULT NULL,
  `status_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `expense_details`
--

CREATE TABLE `expense_details` (
  `id` bigint(20) NOT NULL,
  `expense_no` varchar(255) DEFAULT NULL,
  `expense_amt` decimal(20,3) DEFAULT NULL,
  `expense_dt` timestamp NULL DEFAULT NULL,
  `instr_no` varchar(255) DEFAULT NULL,
  `instr_dt` date DEFAULT NULL,
  `payment_types_id` bigint(20) DEFAULT NULL,
  `bank_master_id` bigint(20) DEFAULT NULL,
  `collection_type_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `feasibility_status`
--

CREATE TABLE `feasibility_status` (
  `id` bigint(20) NOT NULL,
  `status` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `feasibility_status`
--

INSERT INTO `feasibility_status` (`id`, `status`) VALUES
(1, 'Application Accepted');

-- --------------------------------------------------------

--
-- Table structure for table `feasibility_study`
--

CREATE TABLE `feasibility_study` (
  `id` bigint(20) NOT NULL,
  `created_date` timestamp NULL DEFAULT NULL,
  `modified_date` timestamp NULL DEFAULT NULL,
  `prepared_date` timestamp NULL DEFAULT NULL,
  `zonal_head_approval_date` timestamp NULL DEFAULT NULL,
  `dept_head_inspected_date` timestamp NULL DEFAULT NULL,
  `operation_mangrapprove_date` timestamp NULL DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `division_master_id` bigint(20) DEFAULT NULL,
  `zone_master_id` bigint(20) DEFAULT NULL,
  `street_master_id` bigint(20) DEFAULT NULL,
  `application_txn_id` bigint(20) DEFAULT NULL,
  `prepared_by_id` bigint(20) DEFAULT NULL,
  `approved_by_zonal_head_id` bigint(20) DEFAULT NULL,
  `inspection_by_department_head_id` bigint(20) DEFAULT NULL,
  `approved_by_operation_manager_id` bigint(20) DEFAULT NULL,
  `category_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `file_number`
--

CREATE TABLE `file_number` (
  `id` bigint(20) NOT NULL,
  `file_no` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `file_number`
--

INSERT INTO `file_number` (`id`, `file_no`) VALUES
(1, 'F_101'),
(2, 'F_102'),
(3, 'F_103'),
(4, 'F_104'),
(5, 'F_105');

-- --------------------------------------------------------

--
-- Table structure for table `file_upload_master`
--

CREATE TABLE `file_upload_master` (
  `id` bigint(20) NOT NULL,
  `photo` blob,
  `photo_content_type` varchar(50) NOT NULL,
  `text_file` longtext,
  `binary_file` blob,
  `binary_file_content_type` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `group_master`
--

CREATE TABLE `group_master` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `creation_date` timestamp NULL DEFAULT NULL,
  `last_modified_date` timestamp NULL DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `status_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `hydrant_complaint`
--

CREATE TABLE `hydrant_complaint` (
  `id` bigint(20) NOT NULL,
  `from_left` varchar(255) DEFAULT NULL,
  `from_sb` varchar(255) DEFAULT NULL,
  `problem_at` varchar(255) DEFAULT NULL,
  `activity_type` varchar(255) DEFAULT NULL,
  `pressure` varchar(255) DEFAULT NULL,
  `pressure_time` int(11) DEFAULT NULL,
  `flow` varchar(255) DEFAULT NULL,
  `flow_time` int(11) DEFAULT NULL,
  `water_leakage_complaint_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `id_proof_master`
--

CREATE TABLE `id_proof_master` (
  `id` bigint(20) NOT NULL,
  `id_proof` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `id_proof_master`
--

INSERT INTO `id_proof_master` (`id`, `id_proof`) VALUES
(1, 'DRIVING LICENSE'),
(2, 'VOTER\'S ID'),
(3, 'PASSPORT'),
(4, 'OTHER ID');

-- --------------------------------------------------------

--
-- Table structure for table `instrument_issuer_master`
--

CREATE TABLE `instrument_issuer_master` (
  `id` bigint(20) NOT NULL,
  `instrument_issuer` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `instrument_issuer_master`
--

INSERT INTO `instrument_issuer_master` (`id`, `instrument_issuer`) VALUES
(1, 'issuer1'),
(2, 'issuer2'),
(3, 'issuer3');

-- --------------------------------------------------------

--
-- Table structure for table `invoice_payments`
--

CREATE TABLE `invoice_payments` (
  `id` bigint(20) NOT NULL,
  `amount` decimal(20,3) NOT NULL,
  `cust_details_id` bigint(20) NOT NULL,
  `bill_full_details_id` bigint(20) NOT NULL,
  `coll_details_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `item_category_master`
--

CREATE TABLE `item_category_master` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `creation_date` timestamp NULL DEFAULT NULL,
  `last_modified_date` timestamp NULL DEFAULT NULL,
  `category_code` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `item_code_master`
--

CREATE TABLE `item_code_master` (
  `id` bigint(20) NOT NULL,
  `item_code` varchar(255) DEFAULT NULL,
  `item_name` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `creation_date` timestamp NULL DEFAULT NULL,
  `last_modified_date` timestamp NULL DEFAULT NULL,
  `item_category_master_id` bigint(20) DEFAULT NULL,
  `item_sub_category_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `item_company_master`
--

CREATE TABLE `item_company_master` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `creation_date` timestamp NULL DEFAULT NULL,
  `last_modified_date` timestamp NULL DEFAULT NULL,
  `company_code` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `item_details`
--

CREATE TABLE `item_details` (
  `id` bigint(20) NOT NULL,
  `item_code` varchar(255) DEFAULT NULL,
  `item_name` varchar(255) DEFAULT NULL,
  `item_description` varchar(255) DEFAULT NULL,
  `size` varchar(255) DEFAULT NULL,
  `item_quantity` int(11) DEFAULT NULL,
  `unit_price` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `item_required`
--

CREATE TABLE `item_required` (
  `id` bigint(20) NOT NULL,
  `provided` int(11) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `rate_per_shs` decimal(20,3) DEFAULT NULL,
  `amount` decimal(20,3) DEFAULT NULL,
  `material_master_id` bigint(20) DEFAULT NULL,
  `application_txn_id` bigint(20) DEFAULT NULL,
  `feasibility_study_id` bigint(20) DEFAULT NULL,
  `proceedings_id` bigint(20) DEFAULT NULL,
  `uom_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `item_sub_category_master`
--

CREATE TABLE `item_sub_category_master` (
  `id` bigint(20) NOT NULL,
  `item_sub_category_code` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `creation_date` timestamp NULL DEFAULT NULL,
  `last_modified_date` timestamp NULL DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `category_code` varchar(255) DEFAULT NULL,
  `item_category_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `item_sub_code_master`
--

CREATE TABLE `item_sub_code_master` (
  `id` bigint(20) NOT NULL,
  `item_code_id` bigint(20) DEFAULT NULL,
  `item_sub_code` varchar(255) DEFAULT NULL,
  `item_name` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `creation_date` timestamp NULL DEFAULT NULL,
  `last_modified_date` timestamp NULL DEFAULT NULL,
  `item_ccode_id` bigint(20) DEFAULT NULL,
  `item_category_id` bigint(20) NOT NULL,
  `item_sub_category_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `jhi_authority`
--

CREATE TABLE `jhi_authority` (
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `jhi_authority`
--

INSERT INTO `jhi_authority` (`name`) VALUES
('ROLE_ACCOUNANT'),
('ROLE_ADMIN'),
('ROLE_BILLING'),
('ROLE_BILLRUN'),
('ROLE_BILLRUN_MANAGER'),
('ROLE_CUSTOMER'),
('ROLE_EMPLOYEE'),
('ROLE_GIS'),
('ROLE_OPERATION_MAINTENANCE'),
('ROLE_STORES_OFFICER'),
('ROLE_TECHNICAL_MANAGER'),
('ROLE_TECH_ZONAL_SUPERVISOR'),
('ROLE_USER');

-- --------------------------------------------------------

--
-- Table structure for table `jhi_persistent_audit_event`
--

CREATE TABLE `jhi_persistent_audit_event` (
  `event_id` bigint(20) NOT NULL,
  `principal` varchar(255) NOT NULL,
  `event_date` timestamp NULL DEFAULT NULL,
  `event_type` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `jhi_persistent_audit_event`
--

INSERT INTO `jhi_persistent_audit_event` (`event_id`, `principal`, `event_date`, `event_type`) VALUES
(1, 'admin', '2016-02-25 10:38:04', 'AUTHENTICATION_SUCCESS');

-- --------------------------------------------------------

--
-- Table structure for table `jhi_persistent_audit_evt_data`
--

CREATE TABLE `jhi_persistent_audit_evt_data` (
  `event_id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `value` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `jhi_persistent_audit_evt_data`
--

INSERT INTO `jhi_persistent_audit_evt_data` (`event_id`, `name`, `value`) VALUES
(1, 'remoteAddress', '0:0:0:0:0:0:0:1'),
(1, 'sessionId', '6F890CBF95F5F123CC8DF5E9B004A5F1');

-- --------------------------------------------------------

--
-- Table structure for table `jhi_persistent_token`
--

CREATE TABLE `jhi_persistent_token` (
  `series` varchar(255) NOT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `token_value` varchar(255) NOT NULL,
  `token_date` date DEFAULT NULL,
  `ip_address` varchar(39) DEFAULT NULL,
  `user_agent` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `jhi_user`
--

CREATE TABLE `jhi_user` (
  `id` bigint(20) NOT NULL,
  `login` varchar(50) NOT NULL,
  `password_hash` varchar(60) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `activated` bit(1) NOT NULL,
  `lang_key` varchar(5) DEFAULT NULL,
  `activation_key` varchar(20) DEFAULT NULL,
  `reset_key` varchar(20) DEFAULT NULL,
  `created_by` varchar(50) NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `reset_date` timestamp NULL DEFAULT NULL,
  `last_modified_by` varchar(50) DEFAULT NULL,
  `last_modified_date` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `jhi_user`
--

INSERT INTO `jhi_user` (`id`, `login`, `password_hash`, `first_name`, `last_name`, `email`, `activated`, `lang_key`, `activation_key`, `reset_key`, `created_by`, `created_date`, `reset_date`, `last_modified_by`, `last_modified_date`) VALUES
(1, 'system', ' ', 'System', 'System', 'system@localhost', b'1', 'en', NULL, NULL, 'system', '2016-02-25 10:37:37', NULL, 'admin', '2016-07-16 04:35:40'),
(2, 'anonymousUser', ' ', 'Anonymous', 'User', 'anonymous@localhost', b'1', 'en', NULL, NULL, 'system', '2016-02-25 10:37:37', NULL, NULL, NULL),
(3, 'admin', ' ', 'Administrator', 'Administrator', 'admin@localhost', b'1', 'en', NULL, NULL, 'system', '2016-02-25 10:37:37', NULL, NULL, NULL),
(4, 'user', ' ', 'User', 'User', 'user@localhost', b'1', 'en', NULL, NULL, 'system', '2016-02-25 10:37:37', NULL, NULL, NULL),
(5, 'customer', ' ', 'Customer', 'Support', 'customer@localhost', b'1', 'en', 'NULL', NULL, 'anonymousUser', '2016-09-15 23:01:40', NULL, 'admin', '2016-03-09 02:00:31'),
(6, 'water', ' ', 'Water', 'Ministry', 'water@localhost', b'1', 'en', '74075798038214678044', NULL, 'anonymousUser', '2016-08-18 01:25:10', NULL, 'water', '2016-09-14 04:33:40'),
(7, 'board', ' ', 'Board', 'Directors', 'board@localhost', b'1', 'en', '96267878389108527398', NULL, 'anonymousUser', '2016-08-18 01:25:10', NULL, 'board', '2016-09-14 04:35:32'),
(8, 'energy', ' ', 'Energy&Water', 'Authority', 'energy@localhost', b'1', 'en', '54288279092286381964', NULL, 'anonymousUser', '2016-08-18 01:25:10', NULL, 'energy', '2016-09-14 04:36:21');

-- --------------------------------------------------------

--
-- Table structure for table `jhi_user_authority`
--

CREATE TABLE `jhi_user_authority` (
  `user_id` bigint(20) NOT NULL,
  `authority_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `jhi_user_authority`
--

INSERT INTO `jhi_user_authority` (`user_id`, `authority_name`) VALUES
(1, 'ROLE_ADMIN'),
(3, 'ROLE_ADMIN'),
(9, 'ROLE_ADMIN'),
(30, 'ROLE_BILLRUN'),
(31, 'ROLE_BILLRUN_MANAGER'),
(5, 'ROLE_CUSTOMER'),
(19, 'ROLE_GIS');

-- --------------------------------------------------------

--
-- Table structure for table `job_card_item_requirement`
--

CREATE TABLE `job_card_item_requirement` (
  `id` bigint(20) NOT NULL,
  `quantity` int(11) DEFAULT NULL,
  `replace_length` varchar(255) DEFAULT NULL,
  `cascade_clamp` varchar(255) DEFAULT NULL,
  `no_of_section` int(11) DEFAULT NULL,
  `no_of_clamps` int(11) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `domain_object` bigint(20) DEFAULT NULL,
  `material_master_id` bigint(20) DEFAULT NULL,
  `uom_id` bigint(20) DEFAULT NULL,
  `water_leakage_complaint_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `job_card_site_status`
--

CREATE TABLE `job_card_site_status` (
  `id` bigint(20) NOT NULL,
  `tar_patching` varchar(255) DEFAULT NULL,
  `tar_patching_length` varchar(255) DEFAULT NULL,
  `tar_patching_breadth` varchar(255) DEFAULT NULL,
  `clean_site` varchar(255) DEFAULT NULL,
  `back_fill` varchar(255) DEFAULT NULL,
  `back_fill_length` varchar(255) DEFAULT NULL,
  `back_fill_breadth` varchar(255) DEFAULT NULL,
  `brick_layer` varchar(255) DEFAULT NULL,
  `paving` varchar(255) DEFAULT NULL,
  `paving_length` varchar(255) DEFAULT NULL,
  `paving_breadth` varchar(255) NOT NULL,
  `unable_to_locate` varchar(255) DEFAULT NULL,
  `water_leakage_complaint_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `main_sewerage_size`
--

CREATE TABLE `main_sewerage_size` (
  `id` bigint(20) NOT NULL,
  `size` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `main_sewerage_size`
--

INSERT INTO `main_sewerage_size` (`id`, `size`) VALUES
(1, 10),
(2, 11),
(3, 12);

-- --------------------------------------------------------

--
-- Table structure for table `main_water_size`
--

CREATE TABLE `main_water_size` (
  `id` bigint(20) NOT NULL,
  `size` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `main_water_size`
--

INSERT INTO `main_water_size` (`id`, `size`) VALUES
(1, 5),
(2, 6),
(3, 7);

-- --------------------------------------------------------

--
-- Table structure for table `make_of_pipe`
--

CREATE TABLE `make_of_pipe` (
  `id` bigint(20) NOT NULL,
  `make_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `make_of_pipe`
--

INSERT INTO `make_of_pipe` (`id`, `make_name`) VALUES
(1, 'Pipe make 1'),
(2, 'Pipe Make 2');

-- --------------------------------------------------------

--
-- Table structure for table `manage_cash_point`
--

CREATE TABLE `manage_cash_point` (
  `id` bigint(20) NOT NULL,
  `today_date` timestamp NULL DEFAULT NULL,
  `payee_name` varchar(255) DEFAULT NULL,
  `txn_amount` float DEFAULT NULL,
  `open_bal` float DEFAULT NULL,
  `avail_bal` float DEFAULT NULL,
  `total_receipts` int(11) DEFAULT NULL,
  `location_code` varchar(255) DEFAULT NULL,
  `transaction_type_master_id` bigint(20) DEFAULT NULL,
  `cash_book_master_id` bigint(20) DEFAULT NULL,
  `payment_types_id` bigint(20) DEFAULT NULL,
  `file_number_id` bigint(20) DEFAULT NULL,
  `customer_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `material_master`
--

CREATE TABLE `material_master` (
  `id` bigint(20) NOT NULL,
  `material_name` varchar(255) DEFAULT NULL,
  `consumable_flag` varchar(255) DEFAULT NULL,
  `uom_id` varchar(255) DEFAULT NULL,
  `category_id` bigint(20) DEFAULT NULL,
  `sub_category_id` bigint(20) DEFAULT NULL,
  `item_code_id` bigint(20) DEFAULT NULL,
  `item_sub_code_id` bigint(20) DEFAULT NULL,
  `rate_contract_flag` varchar(255) DEFAULT NULL,
  `unit_rate` decimal(20,3) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `creation_date` timestamp NULL DEFAULT NULL,
  `last_modified_date` timestamp NULL DEFAULT NULL,
  `company_code_id` decimal(20,3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `material_master`
--

INSERT INTO `material_master` (`id`, `material_name`, `consumable_flag`, `uom_id`, `category_id`, `sub_category_id`, `item_code_id`, `item_sub_code_id`, `rate_contract_flag`, `unit_rate`, `description`, `status`, `creation_date`, `last_modified_date`, `company_code_id`) VALUES
(2, 'Threading Tape', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '1000.000', NULL, NULL, '2016-03-30 15:00:00', '2016-03-30 15:00:00', NULL),
(3, 'G.S. Pipe', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '30000.000', NULL, NULL, '2016-03-30 15:00:00', '2016-03-30 15:00:00', NULL),
(4, 'Pipe Polly', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '1000.000', NULL, NULL, '2016-03-30 15:00:00', '2016-03-30 15:00:00', NULL),
(5, 'Coupling', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2000.000', NULL, NULL, '2016-03-30 15:00:00', '2016-03-30 15:00:00', NULL),
(6, 'Bib Tape', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '12000.000', NULL, NULL, '2016-03-30 15:00:00', '2016-03-30 15:00:00', NULL),
(7, 'Tee', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '3500.000', NULL, NULL, '2016-03-30 15:00:00', '2016-03-30 15:00:00', NULL),
(8, 'Union', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2000.000', NULL, NULL, '2016-03-30 15:00:00', '2016-03-30 15:00:00', NULL),
(9, 'Elbow', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '1000.000', NULL, NULL, '2016-03-23 15:00:00', '2016-03-30 15:00:00', NULL),
(10, 'Nipple', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '1000.000', NULL, NULL, '2016-03-30 15:00:00', '2016-03-30 15:00:00', NULL),
(11, 'Polly Connector', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2500.000', NULL, NULL, '2016-03-30 15:00:00', '2016-03-30 15:00:00', NULL),
(12, 'Plain Socket', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '1000.000', NULL, NULL, '2016-03-30 15:00:00', '2016-03-30 15:00:00', NULL),
(13, 'Reducing Socket/Bush', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2000.000', NULL, NULL, '2016-03-30 15:00:00', '2016-03-30 15:00:00', NULL),
(14, 'Stop Cock', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '12000.000', NULL, NULL, '2016-03-30 15:00:00', '2016-03-30 15:00:00', NULL),
(15, 'Clamp Saddle', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '3000.000', NULL, NULL, '2016-03-30 15:00:00', '2016-03-30 15:00:00', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `menu_item`
--

CREATE TABLE `menu_item` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `path` varchar(255) NOT NULL,
  `modified_date` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `menu_item`
--

INSERT INTO `menu_item` (`id`, `name`, `path`, `modified_date`) VALUES
(1, 'Module', '#/modules', '2016-03-09 16:00:00'),
(2, 'Application Form', '#/applicationTxns/new', '2016-03-10 16:00:00'),
(3, 'Menu Items', '#/menuItems', '2016-03-10 16:00:00'),
(4, 'Url', '#/urls', '2016-03-10 16:00:00'),
(5, 'Menu Item 2 Urls', '#/menuItem2Urls', '2016-03-10 16:00:00'),
(6, 'Module 2 Menu Items', '#/module2MenuItems', '2016-03-10 16:00:00'),
(7, 'Url 2 Roles', '#/url2Roles', '2016-03-10 16:00:00'),
(8, 'Application Details', '#/applicationTxns', '2016-03-10 16:00:00'),
(9, 'Manage Cash Point', '#/manageCashPoints', '2016-03-10 16:00:00'),
(10, 'Feasibility Study', '#/feasibilityStudys', '2016-03-11 16:00:00'),
(11, 'Prepare Proceedings', '#/proceedingss', '2016-03-15 15:00:00'),
(12, 'Proceeding Form', '#/proceedingss/new', '2016-03-22 15:00:00'),
(13, 'Item Category Master', '#/itemCategoryMasters', '2016-03-30 15:00:00'),
(14, 'Item Sub Category Masters', '#/itemSubCategoryMasters', '2016-03-30 15:00:00'),
(15, 'Item Code Masters', '#/itemCodeMasters', '2016-03-30 15:00:00'),
(16, 'Item Company Masters', '#/itemCompanyMasters', '2016-03-30 15:00:00'),
(17, 'Item Sub Code Master', '#/itemSubCodeMasters', '2016-03-30 15:00:00'),
(18, 'Material Master', '#/materialMasters', '2016-03-30 15:00:00'),
(19, 'Sib Entry', '#/sibEntrys', '2016-03-30 15:00:00'),
(20, 'Receipt', '#/receipts', '2016-04-01 15:00:00'),
(21, 'Access List', '#/accessLists', '2016-03-15 15:00:00'),
(22, 'Bill Full Details', '#/billFullDetailss', '2016-03-15 15:00:00'),
(23, 'Collection Details', '#/collDetailss/new', '2016-03-15 15:00:00'),
(24, 'Current Users', '#/currentUserss', '2016-03-15 15:00:00'),
(25, 'Customer Details', '#/custDetailss', '2016-03-15 15:00:00'),
(26, 'Terminal', '#/terminals', '2016-03-15 15:00:00'),
(27, 'Terminal Log', '#/terminalLogs', '2016-03-15 15:00:00'),
(28, 'Version', '#/versions', '2016-03-15 15:00:00'),
(29, 'Complaint Type Master', '#/complaintTypeMasters', '2016-03-29 15:00:00'),
(30, 'Customer Complaints', '#/customerComplaintss', '2016-03-29 15:00:00'),
(31, 'Bill Run Master', '#/billRunMasters', '2016-04-01 15:00:00'),
(32, 'New Bill Run', '#/billRunMasters/new', '2016-04-01 15:00:00'),
(33, 'Meter Change', '#/meterChanges/new', '2016-04-19 15:00:00'),
(34, 'Without Meter', '#/applicationTxns/withoutMeter', '2016-04-20 15:00:00'),
(35, 'Bill Details', '#/billDetailss/new', '2016-04-18 15:00:00'),
(36, 'Merchant Master', '#/merchantMasters', '2016-04-18 15:00:00'),
(37, 'Online Payment Order', '#/onlinePaymentOrders', '2016-04-18 15:00:00'),
(38, 'Online Payment Response', '#/onlinePaymentResponses', '2016-04-18 15:00:00'),
(39, 'Online Payment Callback', '#/onlinePaymentCallbacks', '2016-04-18 15:00:00'),
(40, 'Customer Category Change', '#/customers/categoryChange', '2016-05-03 15:00:00'),
(41, 'Pipe Size Change', '#/customers/pipeSizeChange', '2016-05-03 15:00:00'),
(42, 'Name Change', '#/customers/nameChange', '2016-05-03 15:00:00'),
(43, 'Connection Termination', '#/connectionTerminates/new', '2016-05-03 15:00:00'),
(44, 'Application Type Master', '#/application_type_masters', '2016-05-03 15:00:00'),
(45, 'Bill Run Details', '#/billRunDetailss', '2016-05-03 15:00:00'),
(46, 'Cash Book Master', '#/cashBookMasters', '2016-05-03 15:00:00'),
(47, 'Category Master', '#/categoryMasters', '2016-05-03 15:00:00'),
(48, 'Category Pipe Size Mapping', '#/categoryPipeSizeMappings', '2016-05-03 15:00:00'),
(49, 'Collection Type Master', '#/collectionTypeMasters', '2016-05-03 15:00:00'),
(50, 'Configuration Details', '#/configurationDetailss', '2016-05-03 15:00:00'),
(51, 'Connection Type Master', '#/connectionTypeMasters', '2016-05-03 15:00:00'),
(52, 'Customer Meter Mapping', '#/custMeterMappings', '2016-05-03 15:00:00'),
(53, 'Customer', '#/customers', '2016-05-03 15:00:00'),
(54, 'Data Base Change Log', '#/databasechangelogs', '2016-05-03 15:00:00'),
(55, 'Data Base Change Log Lock', '#/databasechangeloglocks', '2016-05-03 15:00:00'),
(56, 'Department Type Master', '#/departmentTypeMasters', '2016-05-03 15:00:00'),
(57, 'Departments Hierarchy', '#/departmentsHierarchys', '2016-05-03 15:00:00'),
(58, 'Departments Master', '#/departmentsMasters', '2016-05-03 15:00:00'),
(59, 'Design Category Master', '#/desigCategoryMasters', '2016-05-03 15:00:00'),
(60, 'Designation Mappings', '#/designationMappingss', '2016-05-03 15:00:00'),
(61, 'Designation Master', '#/designationMasters', '2016-05-03 15:00:00'),
(62, 'Division Master', '#/divisionMasters', '2016-05-03 15:00:00'),
(63, 'Docket Code', '#/docketCodes', '2016-05-03 15:00:00'),
(64, 'Employee Master', '#/empMasters', '2016-05-03 15:00:00'),
(65, 'Employee Role Mapping ', '#/empRoleMappings', '2016-05-03 15:00:00'),
(66, 'Expense Detaills', '#/expenseDetailss/new', '2016-05-03 15:00:00'),
(67, 'Feasibility Status', '#/feasibility_statuss', '2016-05-03 15:00:00'),
(68, 'File Number', '#/fileNumbers', '2016-05-03 15:00:00'),
(69, 'File Upload Master', '#/fileUploadMasters', '2016-05-03 15:00:00'),
(70, 'Group Master', '#/groupMasters', '2016-05-03 15:00:00'),
(71, 'Id Proof Master', '#/idProofMasters', '2016-05-03 15:00:00'),
(72, 'Instument Issuer Master ', '#/instrumentIssuerMasters', '2016-05-03 15:00:00'),
(73, 'Item Details', '#/itemDetailss', '2016-05-03 15:00:00'),
(74, 'Item Required', '#/itemRequireds', '2016-05-03 15:00:00'),
(75, 'Main Sewerage Size', '#/mainSewerageSizes', '2016-05-03 15:00:00'),
(76, 'Main Water Size', '#/mainWaterSizes', '2016-05-03 15:00:00'),
(77, 'Make Of Pipe', '#/makeOfPipes', '2016-05-03 15:00:00'),
(78, 'Meter Details', '#/meterDetailss', '2016-05-03 15:00:00'),
(79, 'Meter Status', '#/meterStatuss', '2016-05-03 15:00:00'),
(80, 'MMG Material Master', '#/mmgMaterialMasters', '2016-05-03 15:00:00'),
(81, 'MMG Terms Master', '#/mmgTermsMasters', '2016-05-03 15:00:00'),
(82, 'Organization Hierarchy', '#/orgHierarchys', '2016-05-03 15:00:00'),
(83, 'Organization Role Hierarchy', '#/orgRoleHierarchys', '2016-05-03 15:00:00'),
(84, 'Organization Role Instance', '#/orgRoleInstances', '2016-05-03 15:00:00'),
(85, 'Organization Role Master', '#/orgRolesMasters', '2016-05-03 15:00:00'),
(86, 'Payment Types', '#/paymentTypess', '2016-05-03 15:00:00'),
(87, 'Percentage Master', '#/percentageMasters', '2016-05-03 15:00:00'),
(88, 'Pipe Size Master', '#/pipeSizeMasters', '2016-05-03 15:00:00'),
(89, 'Proceedings', '#/proceedingss', '2016-05-03 15:00:00'),
(90, 'Reallotment', '#/reAllotments', '2016-05-03 15:00:00'),
(91, 'Request Designation Workflow Mapping', '#/reqDesigWorkflowMappings', '2016-05-03 15:00:00'),
(92, 'Request Organization Work Flow Mapping', '#/reqOrgWorkflowMappings', '2016-05-03 15:00:00'),
(93, 'Request Master', '#/requestMasters', '2016-05-03 15:00:00'),
(94, 'Request Work Flow History', '#/requestWorkflowHistorys', '2016-05-03 15:00:00'),
(95, 'Request Work Flow mapping', '#/requestWorkflowMappings', '2016-05-03 15:00:00'),
(96, 'Revenue Type Master', '#/revenueTypeMasters', '2016-05-03 15:00:00'),
(97, 'Role  Work Flow Mapping', '#/roleWorkflowMappings', '2016-05-03 15:00:00'),
(98, 'Schema Master', '#/schemeMasters', '2016-05-03 15:00:00'),
(99, 'Revenue Details', '#/revDetails/new', '2016-05-03 15:00:00'),
(100, 'Change Category List', '#/customers/categoryChanges', '2016-05-03 15:00:00'),
(101, 'Pipe Size Change List', '#/customers/pipeSizes', '2016-05-03 15:00:00'),
(102, 'Name Change List', '#/customers/nameChanges', '2016-05-03 15:00:00'),
(103, 'Meter Change List', '#/meterChanges', '2016-05-03 15:00:00'),
(104, 'ConnectionTerminaation List', '#/connectionTerminates', '2016-05-03 15:00:00'),
(105, 'Get Water Bill Details', '#/billFullDetailss/getWaterBillDetails', '2016-05-03 15:00:00'),
(106, 'Adjustments', '#/adjustmentss', '2016-06-16 09:30:00'),
(107, 'Customer History', '#/customerComplaintss/customerHistory', '2016-05-03 09:30:00'),
(108, 'Customer Info', '#/customerComplaintss/customerInfo', '2016-05-03 09:30:00'),
(109, 'Wofkflow', '#/workflows/new', '2016-07-13 09:30:00'),
(111, 'Request Master', '#/requestMasters', '2016-07-13 09:30:00'),
(112, 'Register Employee', '#/register', '2016-07-14 09:30:00'),
(113, 'Customer Details Report', '#/custDetailss/custDetailsReport', '2016-08-16 09:30:00'),
(114, 'Employee Management', '#/user-management', '2016-07-18 09:30:00'),
(116, 'Workflow Master', '#/workflowMasters', '2016-07-18 09:30:00'),
(117, 'Cancel Collection', '#/collDetailss/cancel', '2016-07-20 09:30:00'),
(118, 'Reversal Details', '#/reversalDetailss', '2016-07-22 09:30:00'),
(119, 'Collection Details Report', '#/custDetailss/collectionDetailsReport', '2016-07-22 04:00:00'),
(120, 'Collection Details Yearly Report', '#/collDetailss/collectionDetailsYearlyReport', '2016-07-22 04:00:00'),
(121, 'Water Leakage Complaint', '#/waterLeakageComplaints', '2016-08-16 09:30:00'),
(122, 'Leakage Complaints Form', '#/waterLeakageComplaints/new', '2016-08-16 09:30:00'),
(123, 'Bill Report', '#/billFullDetailss/billReport', '2016-08-16 09:30:00'),
(124, 'Age Analysis Report', '#/billFullDetailss/ageAnalysisReport', '2016-08-16 09:30:00'),
(125, 'Status Master', '#/statusMasters', '2016-09-10 09:30:00'),
(126, 'Workflow Relations', '#/workflowRelationss', '2016-09-10 09:30:00'),
(127, 'Workflow Relationships', '#/workflowRelationshipss', '2016-09-10 09:30:00'),
(128, 'Tariff Category Masters', '#/tariffCategoryMasters', '2016-09-10 09:30:00'),
(129, 'Street Masters', '#/streetMasters', '2016-09-10 09:30:00'),
(130, 'UOM', '#/uoms', '2016-09-10 09:30:00'),
(131, 'Bank Master', '#/bankMasters', '2016-09-13 12:00:00'),
(135, 'Water Bill Report', '#/billFullDetailss/waterBillReport', '2016-09-15 09:30:00'),
(136, 'New Water Connection', '#/custDetailss/newWaterConnectionReport', '2016-09-15 09:30:00'),
(137, 'Revenue Details Report', '#/collDetailss/revenueSummaryReport', '2016-09-15 09:30:00'),
(138, 'Bills And Collections Report', '#/billFullDetailss/billsAndCollectionsReport', '2016-09-15 09:30:00'),
(139, 'Tariff Type Master', '#/tariffTypeMasters', '2016-09-15 09:30:00'),
(140, 'Tariff Masters', '#/tariffMasters', '2016-09-15 09:30:00');

-- --------------------------------------------------------

--
-- Table structure for table `menu_item2_url`
--

CREATE TABLE `menu_item2_url` (
  `id` bigint(20) NOT NULL,
  `menu_item_id` bigint(20) DEFAULT NULL,
  `url_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `menu_item2_url`
--

INSERT INTO `menu_item2_url` (`id`, `menu_item_id`, `url_id`) VALUES
(1, 1, 1),
(2, 2, 8),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 2),
(9, 9, 9),
(10, 10, 10),
(11, 11, 11),
(12, 12, 12),
(13, 13, 13),
(14, 14, 14),
(15, 15, 15),
(16, 16, 16),
(17, 17, 17),
(18, 18, 18),
(19, 19, 19),
(20, 20, 20),
(21, 21, 21),
(22, 22, 22),
(23, 23, 23),
(24, 24, 24),
(25, 25, 25),
(26, 26, 26),
(27, 27, 27),
(28, 28, 28),
(29, 29, 29),
(30, 30, 30),
(31, 31, 31),
(32, 32, 32),
(33, 33, 33),
(34, 34, 34),
(35, 35, 35),
(36, 36, 39),
(37, 37, 40),
(38, 38, 41),
(39, 39, 42),
(40, 40, 43),
(41, 41, 44),
(42, 42, 45),
(43, 43, 46),
(44, 99, 101),
(45, 66, 69),
(46, 100, 102),
(47, 101, 103),
(48, 102, 104),
(49, 103, 105),
(50, 104, 106),
(51, 105, 107),
(52, 106, 108),
(53, 107, 109),
(54, 108, 110),
(55, 109, 111),
(57, 95, 97),
(58, 92, 94),
(59, 91, 93),
(60, 64, 67),
(61, 111, 113),
(62, 112, 114),
(63, 65, 68),
(64, 113, 115),
(65, 114, 116),
(66, 116, 117),
(67, 117, 118),
(68, 118, 119),
(69, 84, 86),
(70, 119, 120),
(71, 120, 121),
(72, 121, 122),
(73, 122, 123),
(74, 123, 124),
(75, 124, 125),
(76, 125, 126),
(77, 126, 127),
(78, 127, 128),
(79, 128, 129),
(80, 129, 130),
(81, 130, 131),
(82, 71, 74),
(83, 62, 65),
(84, 88, 90),
(85, 78, 80),
(86, 83, 85),
(87, 61, 64),
(88, 86, 88),
(89, 131, 132),
(90, 50, 53),
(91, 139, 133),
(92, 140, 134),
(93, 135, 135),
(94, 136, 136),
(95, 137, 137),
(96, 138, 138);

-- --------------------------------------------------------

--
-- Table structure for table `merchant_master`
--

CREATE TABLE `merchant_master` (
  `id` bigint(20) NOT NULL,
  `merchant_code` varchar(255) DEFAULT NULL,
  `merchant_name` varchar(255) DEFAULT NULL,
  `merchant_key` varchar(255) DEFAULT NULL,
  `currency` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `merchant_master`
--

INSERT INTO `merchant_master` (`id`, `merchant_code`, `merchant_name`, `merchant_key`, `currency`) VALUES
(2, 'Test001', 'testmerchant', '5b56ca5b-a882-4224-b3e7-b558e93e6cb0', 'TSh');

-- --------------------------------------------------------

--
-- Table structure for table `meter_change`
--

CREATE TABLE `meter_change` (
  `id` bigint(20) NOT NULL,
  `can` varchar(255) DEFAULT NULL,
  `reason_for_change` varchar(255) DEFAULT NULL,
  `prev_meter_reading` decimal(20,3) DEFAULT NULL,
  `new_meter_reading` decimal(20,3) DEFAULT NULL,
  `remarks` varchar(255) DEFAULT NULL,
  `approved_date` date DEFAULT NULL,
  `status` varchar(255) NOT NULL,
  `cust_details_id` bigint(20) DEFAULT NULL,
  `prev_meter_no_id` bigint(20) DEFAULT NULL,
  `new_meter_no_id` bigint(20) DEFAULT NULL,
  `bill_full_details_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `meter_details`
--

CREATE TABLE `meter_details` (
  `id` bigint(20) NOT NULL,
  `meter_id` varchar(255) NOT NULL,
  `meter_no` varchar(255) NOT NULL,
  `meter_type` varchar(255) DEFAULT NULL,
  `meter_make` varchar(255) DEFAULT NULL,
  `max` float DEFAULT NULL,
  `meter_status_id` bigint(20) DEFAULT NULL,
  `pipe_size_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `meter_details`
--

INSERT INTO `meter_details` (`id`, `meter_id`, `meter_no`, `meter_type`, `meter_make`, `max`, `meter_status_id`, `pipe_size_master_id`) VALUES
(11629, '2374', '3-856041', NULL, NULL, NULL, NULL, 1);

-- --------------------------------------------------------

--
-- Table structure for table `meter_status`
--

CREATE TABLE `meter_status` (
  `id` bigint(20) NOT NULL,
  `status` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `meter_status`
--

INSERT INTO `meter_status` (`id`, `status`) VALUES
(1, 'Allotted'),
(2, 'Unallotted'),
(3, 'Processing');

-- --------------------------------------------------------

--
-- Table structure for table `mmg_material_master`
--

CREATE TABLE `mmg_material_master` (
  `id` bigint(10) NOT NULL,
  `material_name` varchar(200) DEFAULT NULL,
  `consumable_flag` varchar(5) DEFAULT NULL,
  `uom_id` bigint(10) DEFAULT NULL,
  `category_id` bigint(10) DEFAULT NULL,
  `sub_category_id` bigint(10) DEFAULT NULL,
  `item_code_id` bigint(10) DEFAULT NULL,
  `item_sub_code_id` bigint(10) DEFAULT NULL,
  `rate_contract_flag` varchar(5) DEFAULT NULL,
  `unit_rate` bigint(126) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `status` bigint(10) DEFAULT NULL,
  `creation_date` datetime DEFAULT NULL,
  `last_modified_date` datetime DEFAULT NULL,
  `company_code_id` bigint(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `mmg_terms_master`
--

CREATE TABLE `mmg_terms_master` (
  `id` bigint(10) NOT NULL,
  `name` varchar(25) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `status` bigint(10) DEFAULT NULL,
  `creation_date` datetime DEFAULT NULL,
  `last_modified_date` datetime DEFAULT NULL,
  `tax_type_id` bigint(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `module`
--

CREATE TABLE `module` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `priority` int(11) DEFAULT NULL,
  `modified_date` timestamp NULL DEFAULT NULL,
  `server_url` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `module`
--

INSERT INTO `module` (`id`, `name`, `priority`, `modified_date`, `server_url`) VALUES
(1, 'Role Management', 1, '2016-03-09 16:00:00', 'roleManagement'),
(2, 'Connection', 4, '2016-03-10 16:00:00', 'connection'),
(3, 'Items Details', 5, '2016-03-30 15:00:00', 'itemDetails'),
(4, 'Billing and Collection', 6, '2016-03-15 15:00:00', 'billingAndCollection'),
(5, 'Customer Care', 7, '2016-03-29 15:00:00', 'customerCare'),
(6, 'Bill Cycle Run', 8, '2016-04-04 15:00:00', 'billCycleRun'),
(7, 'Online Payment', 9, '2016-04-04 15:00:00', 'onlinePayment'),
(8, 'Change Customer Info.', 10, '2016-04-04 15:00:00', 'changeCases'),
(9, 'Employee Management', 2, '2016-07-18 09:30:00', 'employeeManagement'),
(10, 'Workflow Management', 3, '2016-07-17 09:30:00', 'workflowManagement'),
(11, 'Reports', 14, '2016-07-28 09:30:00', 'reports');

-- --------------------------------------------------------

--
-- Table structure for table `module2_menu_item`
--

CREATE TABLE `module2_menu_item` (
  `id` bigint(20) NOT NULL,
  `priority` int(11) DEFAULT NULL,
  `module_id` bigint(20) DEFAULT NULL,
  `menu_item_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `module2_menu_item`
--

INSERT INTO `module2_menu_item` (`id`, `priority`, `module_id`, `menu_item_id`) VALUES
(1, 1, 2, 2),
(2, 1, 1, 1),
(3, 2, 1, 3),
(4, 3, 1, 4),
(5, 4, 1, 5),
(6, 5, 1, 6),
(7, 6, 1, 7),
(8, 2, 2, 8),
(13, 1, 3, 13),
(14, 2, 3, 14),
(15, 3, 3, 15),
(16, 4, 3, 16),
(17, 5, 3, 17),
(18, 6, 3, 18),
(19, 7, 3, 19),
(21, 1, 4, 21),
(22, 2, 4, 22),
(23, 3, 4, 23),
(24, 4, 4, 24),
(25, 5, 4, 25),
(26, 6, 4, 26),
(27, 7, 4, 27),
(28, 8, 4, 28),
(29, 6, 5, 29),
(30, 1, 5, 30),
(31, 2, 6, 31),
(32, 1, 6, 32),
(33, 5, 8, 33),
(34, 3, 2, 34),
(35, 9, 4, 35),
(36, 1, 7, 36),
(37, 2, 7, 37),
(38, 3, 7, 38),
(39, 4, 7, 39),
(40, 1, 8, 40),
(41, 2, 8, 41),
(42, 3, 8, 42),
(43, 4, 8, 43),
(44, 10, 4, 99),
(45, 11, 4, 66),
(46, 6, 8, 100),
(47, 7, 8, 101),
(48, 8, 8, 102),
(49, 9, 8, 103),
(50, 10, 8, 104),
(51, 12, 4, 105),
(52, 13, 4, 106),
(53, 2, 5, 107),
(54, 3, 5, 108),
(55, 1, 10, 109),
(57, 2, 10, 95),
(58, 3, 10, 92),
(59, 4, 10, 91),
(60, 3, 9, 64),
(61, 5, 10, 111),
(62, 1, 9, 112),
(63, 4, 9, 65),
(64, 14, 11, 113),
(65, 2, 9, 114),
(66, 5, 5, 121),
(67, 6, 10, 116),
(68, 14, 4, 117),
(69, 15, 4, 118),
(70, 7, 9, 84),
(71, 16, 4, 119),
(72, 17, 4, 120),
(73, 4, 5, 122),
(74, 18, 4, 123),
(75, 19, 4, 124),
(76, 4, 2, 128),
(77, 5, 2, 71),
(78, 6, 2, 62),
(79, 7, 2, 129),
(80, 8, 2, 88),
(81, 9, 2, 78),
(82, 5, 9, 83),
(83, 6, 9, 61),
(84, 10, 10, 126),
(85, 11, 2, 50),
(86, 11, 10, 127),
(87, 12, 10, 125),
(88, 20, 4, 86),
(89, 8, 3, 130),
(90, 21, 4, 131),
(91, 12, 2, 139),
(92, 12, 2, 140),
(93, 22, 4, 135),
(94, 23, 4, 136),
(95, 24, 4, 137),
(96, 25, 4, 138);

-- --------------------------------------------------------

--
-- Table structure for table `online_payment_callback`
--

CREATE TABLE `online_payment_callback` (
  `id` bigint(20) NOT NULL,
  `currency` varchar(255) DEFAULT NULL,
  `payment_mode` varchar(255) DEFAULT NULL,
  `service_code` varchar(255) DEFAULT NULL,
  `message` varchar(255) DEFAULT NULL,
  `response_code` varchar(255) DEFAULT NULL,
  `total_amount_paid` decimal(20,3) DEFAULT NULL,
  `user_defined_field` varchar(255) DEFAULT NULL,
  `merchant_txn_ref` varchar(255) DEFAULT NULL,
  `merchant_master_id` bigint(20) DEFAULT NULL,
  `online_payment_order_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `online_payment_order`
--

CREATE TABLE `online_payment_order` (
  `id` bigint(20) NOT NULL,
  `service_code` varchar(255) NOT NULL,
  `amount` float NOT NULL,
  `pay_by` varchar(255) NOT NULL,
  `user_defined_field` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `order_time` timestamp NULL DEFAULT NULL,
  `merchant_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `online_payment_order`
--

INSERT INTO `online_payment_order` (`id`, `service_code`, `amount`, `pay_by`, `user_defined_field`, `email`, `phone`, `order_time`, `merchant_master_id`) VALUES
(1, 'TESTS001', 1610, 'TIGOPESADIR', '04060001', 'test@gmail.com', 1234567890, '2016-05-03 07:47:25', 2);

-- --------------------------------------------------------

--
-- Table structure for table `online_payment_response`
--

CREATE TABLE `online_payment_response` (
  `id` bigint(20) NOT NULL,
  `response_code` varchar(255) DEFAULT NULL,
  `response_time` timestamp NULL DEFAULT NULL,
  `redirect_url` varchar(255) DEFAULT NULL,
  `merchant_txn_ref` varchar(255) DEFAULT NULL,
  `online_payment_order_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `org_hierarchy`
--

CREATE TABLE `org_hierarchy` (
  `id` bigint(20) NOT NULL,
  `hierarchy_name` varchar(255) DEFAULT NULL,
  `parent_hierarchy_id` int(11) DEFAULT NULL,
  `creation_date` timestamp NULL DEFAULT NULL,
  `last_modified_date` timestamp NULL DEFAULT NULL,
  `status_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `org_hierarchy`
--

INSERT INTO `org_hierarchy` (`id`, `hierarchy_name`, `parent_hierarchy_id`, `creation_date`, `last_modified_date`, `status_master_id`) VALUES
(1, 'Minister for Water & Irrigation', 0, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 2),
(2, 'Board of Directors', 1, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 2),
(3, 'Energy & Water Utilities Regulatory Authority', 2, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 2),
(4, 'Managing Director', 2, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 2),
(5, 'Internal Auditor', 4, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 2),
(6, 'Legal Secretary', 4, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 2),
(7, 'Public Relation Officer', 4, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 2),
(8, 'HPMU', 4, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 2),
(9, 'Technical Manager', 8, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 2),
(10, 'Commercial Manager', 4, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 2),
(11, 'Financial Manager', 4, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 2),
(12, 'Human Resource & Administration Manager', 4, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 2),
(13, 'Production & Prog. Engineer', 4, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 2),
(14, 'Water Network Engineer', 10, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 2),
(15, 'O&M Sanitation Engineer', 10, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 2),
(16, 'Planning & Construction Engineer', 11, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 2),
(17, 'O&M Production Engineer ', 11, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 2),
(18, 'Billing Officer', 11, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 2),
(19, 'Credit Control Officer', 12, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 2),
(20, 'C R O M', 13, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 2),
(21, 'Exp. Assistant Accountant', 16, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 2),
(22, 'Pre-Audit. Acc', 19, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 2),
(23, 'Rev. Ass. Acc.', 19, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 2),
(24, 'HR & Administration Officer', 15, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 2),
(25, 'Stores & Supplies Officer', 10, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 2),
(26, 'Cashier', NULL, NULL, NULL, NULL),
(27, 'Off.Attendant', NULL, NULL, NULL, NULL),
(28, 'PS', NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `org_roles_master`
--

CREATE TABLE `org_roles_master` (
  `id` bigint(20) NOT NULL,
  `org_role_name` varchar(255) DEFAULT NULL,
  `hierarchy_id` int(11) DEFAULT NULL,
  `creation_date` timestamp NULL DEFAULT NULL,
  `last_modified_date` timestamp NULL DEFAULT NULL,
  `status_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `org_role_hierarchy`
--

CREATE TABLE `org_role_hierarchy` (
  `id` bigint(20) NOT NULL,
  `role_hierarchy_name` varchar(255) DEFAULT NULL,
  `parent_role_hierarchy_id` int(11) DEFAULT NULL,
  `creation_date` timestamp NULL DEFAULT NULL,
  `last_modified_date` timestamp NULL DEFAULT NULL,
  `status_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `org_role_hierarchy`
--

INSERT INTO `org_role_hierarchy` (`id`, `role_hierarchy_name`, `parent_role_hierarchy_id`, `creation_date`, `last_modified_date`, `status_master_id`) VALUES
(1, 'Minister for Water & Irrigation', 0, '2016-08-02 09:30:00', '2016-08-02 09:30:00', 2),
(2, 'Board of Directors', 1, '2016-08-02 09:30:00', '2016-08-02 09:30:00', 2),
(3, 'Energy & Water Utilities Regulatory Authority', 2, '2016-08-02 09:30:00', '2016-08-02 09:30:00', 2),
(4, 'Managing Director', 2, '2016-08-02 09:30:00', '2016-08-02 09:30:00', 2),
(5, 'Internal Auditor', 4, '2016-08-02 09:30:00', '2016-08-02 09:30:00', 2),
(6, 'Legal Secretary', 4, '2016-08-02 09:30:00', '2016-08-02 09:30:00', 2),
(7, 'Public Relation Officer', 4, '2016-08-02 09:30:00', '2016-08-02 09:30:00', 2),
(8, 'HPMU', 4, '2016-08-02 09:30:00', '2016-08-02 09:30:00', 2),
(9, 'Technical Manager', 4, '2016-08-02 09:30:00', '2016-08-02 09:30:00', 2),
(10, 'Commercial Manager', 4, '2016-08-02 09:30:00', '2016-08-02 09:30:00', 2),
(11, 'Financial Manager', 4, '2016-08-02 09:30:00', '2016-08-02 09:30:00', 2),
(12, 'Human Resource & Administration Manager', 4, '2016-08-02 09:30:00', '2016-08-02 09:30:00', 2),
(13, 'Production & Prog. Engineer', 4, '2016-08-02 09:30:00', '2016-08-02 09:30:00', 2),
(14, 'Water Network Engineer', 10, '2016-08-02 09:30:00', '2016-08-02 09:30:00', 2),
(15, 'O&M Sanitation Engineer', 10, '2016-08-02 09:30:00', '2016-08-02 09:30:00', 2),
(16, 'Planning & Construction Engineer', 11, '2016-08-02 09:30:00', '2016-08-02 09:30:00', 2),
(17, 'O&M Production Engineer', 11, '2016-08-02 09:30:00', '2016-08-02 09:30:00', 2),
(18, 'Billing Officer', 11, '2016-08-02 09:30:00', '2016-08-02 09:30:00', 2),
(19, 'Credit Control Officer', 12, '2016-08-02 09:30:00', '2016-08-02 09:30:00', 2),
(20, 'C R O M', 13, '2016-08-02 09:30:00', '2016-08-02 09:30:00', 2),
(21, 'Exp. Assistant Accountant', 16, '2016-08-02 09:30:00', '2016-08-02 09:30:00', 2),
(22, 'Pre-Audit. Acc', 19, '2016-08-02 09:30:00', '2016-08-02 09:30:00', 2),
(23, 'Rev. Ass. Acc.', 19, '2016-08-02 09:30:00', '2016-08-02 09:30:00', 2),
(24, 'HR & Administration Officer', 15, '2016-08-02 09:30:00', '2016-08-02 09:30:00', 2),
(25, 'Stores & Supplies Officer', 8, '2016-08-02 09:30:00', '2016-08-02 09:30:00', 2),
(26, 'Cashier', NULL, '2016-08-02 09:30:00', '2016-08-02 09:30:00', 2),
(27, 'Off.Attendant', NULL, '2016-08-02 09:30:00', '2016-08-02 09:30:00', 2),
(28, 'PS', NULL, '2016-08-02 09:30:00', '2016-08-02 09:30:00', 2);

-- --------------------------------------------------------

--
-- Table structure for table `org_role_instance`
--

CREATE TABLE `org_role_instance` (
  `id` bigint(20) NOT NULL,
  `org_role_name` varchar(255) DEFAULT NULL,
  `parent_org_role_id` int(11) DEFAULT NULL,
  `creation_date` timestamp NULL DEFAULT NULL,
  `last_modified_date` timestamp NULL DEFAULT NULL,
  `is_head` int(11) DEFAULT NULL,
  `status_master_id` bigint(20) DEFAULT NULL,
  `org_role_hierarchy_id` bigint(20) DEFAULT NULL,
  `departments_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `org_role_instance`
--

INSERT INTO `org_role_instance` (`id`, `org_role_name`, `parent_org_role_id`, `creation_date`, `last_modified_date`, `is_head`, `status_master_id`, `org_role_hierarchy_id`, `departments_master_id`) VALUES
(1, 'Minister for Water & Irrigation', 0, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 1, 2, NULL, NULL),
(2, 'Board of Directors', 1, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 1, 2, NULL, NULL),
(3, 'Energy & Water Utilities Regulatory Authority', 2, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 1, 2, NULL, NULL),
(4, 'Managing Director', 2, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 1, 2, NULL, NULL),
(5, 'Internal Auditor', 4, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 1, 2, NULL, NULL),
(6, 'Legal Secretary', 4, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 1, 2, NULL, NULL),
(7, 'Public Relation Officer', 4, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 1, 2, NULL, NULL),
(8, 'HPMU', 4, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 1, 2, NULL, NULL),
(9, 'Technical Manager', 4, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 1, 2, NULL, NULL),
(10, 'Commercial Manager', 4, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 1, 2, NULL, NULL),
(11, 'Financial Manager', 4, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 1, 2, NULL, NULL),
(12, 'Human Resource & Administration Manager', 4, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 1, 2, NULL, NULL),
(13, 'Production & Prog. Engineer', 4, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 1, 2, NULL, NULL),
(14, 'Water Network Engineer', 10, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 1, 2, NULL, NULL),
(15, 'O&M Sanitation Engineer', 10, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 1, 2, NULL, NULL),
(16, 'Planning & Construction Engineer', 11, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 1, 2, NULL, NULL),
(17, 'O&M Production Engineer', 11, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 1, 2, NULL, NULL),
(18, 'Billing Officer', 11, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 1, 2, NULL, NULL),
(19, 'Credit Control Officer', 12, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 1, 2, NULL, NULL),
(20, 'C R O M', 13, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 1, 2, NULL, NULL),
(21, 'Exp. Assistant Accountant', 16, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 1, 2, NULL, NULL),
(22, 'Pre-Audit. Acc', 19, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 1, 2, NULL, NULL),
(23, 'Rev. Ass. Acc.', 19, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 1, 2, NULL, NULL),
(24, 'HR & Administration Officer', 15, '2016-03-21 15:00:00', '2016-03-21 15:00:00', 1, 2, NULL, NULL),
(25, 'Stores & Supplies Officer', 10, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 1, 2, NULL, NULL),
(26, 'Cashier', 1, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 1, 2, NULL, NULL),
(27, 'Off.Attendant', 1, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 1, 2, NULL, NULL),
(28, 'PS', 22, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 1, 2, NULL, NULL),
(29, 'Customer Relation Executive', 19, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 1, 2, NULL, NULL),
(30, 'Administrator', 1, '2016-09-15 09:30:00', '2016-09-15 09:30:00', 1, 2, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `payment_types`
--

CREATE TABLE `payment_types` (
  `id` bigint(20) NOT NULL,
  `payment_mode` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `payment_types`
--

INSERT INTO `payment_types` (`id`, `payment_mode`) VALUES
(1, 'Cash'),
(2, 'Demand Draft (DD)'),
(3, 'Cheque');

-- --------------------------------------------------------

--
-- Table structure for table `percentage_master`
--

CREATE TABLE `percentage_master` (
  `id` bigint(20) NOT NULL,
  `percent_type` varchar(255) DEFAULT NULL,
  `percent_value` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `percentage_master`
--

INSERT INTO `percentage_master` (`id`, `percent_type`, `percent_value`) VALUES
(1, 'SUPERVISION', 10),
(2, 'LABOUR CHARGES', 20),
(3, 'SITE SURVEY', 5),
(4, 'CONNECTION FEE OF A & B', 20),
(5, 'APPLICATION FORM FEE', 1000);

-- --------------------------------------------------------

--
-- Table structure for table `pipe_size_master`
--

CREATE TABLE `pipe_size_master` (
  `id` bigint(20) NOT NULL,
  `pipe_size` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pipe_size_master`
--

INSERT INTO `pipe_size_master` (`id`, `pipe_size`) VALUES
(1, 0.25),
(2, 0.5),
(3, 0.75),
(4, 1),
(5, 1.25),
(6, 1.5),
(7, 1.75),
(8, 2);

-- --------------------------------------------------------

--
-- Table structure for table `proceedings`
--

CREATE TABLE `proceedings` (
  `id` bigint(20) NOT NULL,
  `sub_total_a` decimal(20,3) DEFAULT NULL,
  `supervision_charge` decimal(20,3) DEFAULT NULL,
  `labour_charge` decimal(20,3) DEFAULT NULL,
  `site_survey` decimal(20,3) DEFAULT NULL,
  `sub_total_b` decimal(20,3) DEFAULT NULL,
  `connection_fee` decimal(20,3) DEFAULT NULL,
  `water_meter_shs` decimal(20,3) DEFAULT NULL,
  `application_form_fee` decimal(20,3) DEFAULT NULL,
  `grand_total` decimal(20,3) DEFAULT NULL,
  `supervision_percent` decimal(20,3) DEFAULT NULL,
  `labour_charge_percent` decimal(20,3) DEFAULT NULL,
  `site_survey_percent` decimal(20,3) DEFAULT NULL,
  `connection_fee_percent` decimal(20,3) DEFAULT NULL,
  `application_txn_id` bigint(20) DEFAULT NULL,
  `pipe_size_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `receipt`
--

CREATE TABLE `receipt` (
  `id` bigint(20) NOT NULL,
  `amount` decimal(20,3) DEFAULT NULL,
  `bank_name` varchar(255) DEFAULT NULL,
  `branch_name` varchar(255) DEFAULT NULL,
  `check_or_dd_date` date DEFAULT NULL,
  `check_or_dd_no` varchar(255) DEFAULT NULL,
  `receipt_date` date DEFAULT NULL,
  `can` varchar(255) DEFAULT NULL,
  `application_txn_id` bigint(20) DEFAULT NULL,
  `payment_types_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `request_master`
--

CREATE TABLE `request_master` (
  `id` bigint(20) NOT NULL,
  `request_type` varchar(255) DEFAULT NULL,
  `creation_date` timestamp NULL DEFAULT NULL,
  `last_modified_date` timestamp NULL DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `internal_flag` int(11) DEFAULT NULL,
  `status_master_id` bigint(20) DEFAULT NULL,
  `module_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `request_master`
--

INSERT INTO `request_master` (`id`, `request_type`, `creation_date`, `last_modified_date`, `description`, `internal_flag`, `status_master_id`, `module_id`) VALUES
(1, 'REQUISITION', '2016-03-21 15:00:00', '2016-03-21 15:00:00', NULL, 0, 2, 2),
(3, 'INCORRECT BILL', '2016-03-31 15:00:00', '2016-03-31 15:00:00', NULL, 0, 2, 5),
(4, 'WATER LEAKAGE', '2016-03-31 15:00:00', '2016-03-31 15:00:00', NULL, 0, 2, 5),
(5, 'SERVICE UNAVAILABILITY', '2016-03-31 15:00:00', '2016-03-31 15:00:00', NULL, 0, 2, 5),
(6, 'WITHOUTMETER', '2016-03-31 15:00:00', '2016-03-31 15:00:00', NULL, 0, 2, 2),
(7, 'METER CHANGE', '2016-03-31 15:00:00', '2016-03-31 15:00:00', NULL, 0, 2, 8),
(8, 'CONNECTION CATEGORY', '2016-03-31 15:00:00', '2016-03-31 15:00:00', NULL, 0, 2, 8),
(9, 'PIPE SIZE', '2016-03-31 15:00:00', '2016-03-31 15:00:00', NULL, 0, 2, 8),
(10, 'CHANGE NAME', '2016-03-31 15:00:00', '2016-03-31 15:00:00', NULL, 0, 2, 8),
(11, 'CONNECTION TERMINATION', '2016-03-31 15:00:00', '2016-03-31 15:00:00', NULL, 0, 2, 8),
(12, 'JOB CARD', '2016-03-31 15:00:00', '2016-03-31 15:00:00', NULL, 0, 2, 5);

-- --------------------------------------------------------

--
-- Table structure for table `request_workflow_history`
--

CREATE TABLE `request_workflow_history` (
  `id` bigint(20) NOT NULL,
  `request_stage` int(11) DEFAULT NULL,
  `assigned_date` timestamp NULL DEFAULT NULL,
  `actioned_date` timestamp NULL DEFAULT NULL,
  `remarks` varchar(255) DEFAULT NULL,
  `ip_address` varchar(255) DEFAULT NULL,
  `assigned_role` int(11) DEFAULT NULL,
  `domain_object` bigint(20) DEFAULT NULL,
  `assigned_from_id` bigint(20) DEFAULT NULL,
  `assigned_to_id` bigint(20) DEFAULT NULL,
  `status_master_id` bigint(20) DEFAULT NULL,
  `request_master_id` bigint(20) DEFAULT NULL,
  `workflow_master_id` bigint(20) DEFAULT NULL,
  `workflow_stage_master_id` bigint(20) DEFAULT NULL,
  `applied_by_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `request_workflow_mapping`
--

CREATE TABLE `request_workflow_mapping` (
  `id` bigint(20) NOT NULL,
  `creation_date` timestamp NULL DEFAULT NULL,
  `last_modified_date` timestamp NULL DEFAULT NULL,
  `status_master_id` bigint(20) DEFAULT NULL,
  `workflow_master_id` bigint(20) DEFAULT NULL,
  `request_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `request_workflow_mapping`
--

INSERT INTO `request_workflow_mapping` (`id`, `creation_date`, `last_modified_date`, `status_master_id`, `workflow_master_id`, `request_master_id`) VALUES
(1, '2016-07-28 09:30:00', '2016-07-28 09:30:00', 2, 1, 1),
(2, '2016-08-01 09:30:00', '2016-08-01 09:30:00', 2, 4, 3),
(3, '2016-08-01 09:30:00', '2016-08-01 09:30:00', 2, 5, 6),
(4, '2016-08-01 09:30:00', '2016-08-01 09:30:00', 2, 6, 7),
(5, '2016-08-01 09:30:00', '2016-08-01 09:30:00', 2, 7, 4),
(6, '2016-08-01 09:30:00', '2016-08-01 09:30:00', 2, 8, 8),
(7, '2016-08-01 09:30:00', '2016-08-01 09:30:00', 2, 9, 9),
(8, '2016-08-01 09:30:00', '2016-08-01 09:30:00', 2, 11, 11),
(9, '2016-08-01 09:30:00', '2016-08-01 09:30:00', 2, 10, 10),
(10, '2016-08-16 09:30:00', '2016-08-16 09:30:00', 2, 13, 12);

-- --------------------------------------------------------

--
-- Table structure for table `req_desig_workflow_mapping`
--

CREATE TABLE `req_desig_workflow_mapping` (
  `id` bigint(20) NOT NULL,
  `creation_date` timestamp NULL DEFAULT NULL,
  `last_modified_date` timestamp NULL DEFAULT NULL,
  `workflow_master_id` bigint(20) DEFAULT NULL,
  `request_master_id` bigint(20) DEFAULT NULL,
  `designation_master_id` bigint(20) DEFAULT NULL,
  `status_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `req_org_workflow_mapping`
--

CREATE TABLE `req_org_workflow_mapping` (
  `id` bigint(20) NOT NULL,
  `creation_date` timestamp NULL DEFAULT NULL,
  `last_modified_date` timestamp NULL DEFAULT NULL,
  `workflow_master_id` bigint(20) DEFAULT NULL,
  `request_master_id` bigint(20) DEFAULT NULL,
  `org_role_instance_id` bigint(20) DEFAULT NULL,
  `status_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `req_org_workflow_mapping`
--

INSERT INTO `req_org_workflow_mapping` (`id`, `creation_date`, `last_modified_date`, `workflow_master_id`, `request_master_id`, `org_role_instance_id`, `status_master_id`) VALUES
(1, '2016-03-21 15:00:00', '2016-03-21 15:00:00', 1, 1, 25, 1),
(2, '2016-03-21 15:00:00', '2016-03-21 15:00:00', 1, 1, 10, 1),
(3, '2016-03-21 15:00:00', '2016-03-21 15:00:00', 4, 3, 25, 1),
(4, '2016-03-21 15:00:00', '2016-03-21 15:00:00', 5, 6, 15, 1),
(5, '2016-03-21 15:00:00', '2016-03-21 15:00:00', 6, 7, 25, 1),
(6, '2016-03-21 15:00:00', '2016-03-21 15:00:00', 5, 6, 10, 1),
(7, '2016-03-21 15:00:00', '2016-03-21 15:00:00', 5, 6, 25, 1),
(8, '2016-03-21 15:00:00', '2016-03-21 15:00:00', 7, 4, 25, 1),
(9, '2016-03-21 15:00:00', '2016-03-21 15:00:00', 8, 8, 25, 1),
(10, '2016-04-29 15:00:00', '2016-04-29 15:00:00', 9, 9, 25, 1),
(11, '2016-04-29 09:30:00', '2016-04-29 09:30:00', 10, 10, 25, 1),
(12, '2016-04-29 09:30:00', '2016-04-29 09:30:00', 11, 11, 25, 1);

-- --------------------------------------------------------

--
-- Table structure for table `revenue_type_master`
--

CREATE TABLE `revenue_type_master` (
  `id` bigint(20) NOT NULL,
  `revenue_type` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `revenue_type_master`
--

INSERT INTO `revenue_type_master` (`id`, `revenue_type`) VALUES
(1, 'Rent'),
(2, 'Scrap Sale');

-- --------------------------------------------------------

--
-- Table structure for table `reversal_details`
--

CREATE TABLE `reversal_details` (
  `id` bigint(20) NOT NULL,
  `cancelled_date` date NOT NULL,
  `remarks` varchar(255) NOT NULL,
  `coll_details_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `re_allotment`
--

CREATE TABLE `re_allotment` (
  `id` bigint(20) NOT NULL,
  `file_number_id` bigint(20) DEFAULT NULL,
  `customer_id` bigint(20) DEFAULT NULL,
  `feasibility_status_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `role_workflow_mapping`
--

CREATE TABLE `role_workflow_mapping` (
  `id` bigint(20) NOT NULL,
  `creation_date` timestamp NULL DEFAULT NULL,
  `last_modified_date` timestamp NULL DEFAULT NULL,
  `status_master_id` bigint(20) DEFAULT NULL,
  `org_role_instance_id` bigint(20) DEFAULT NULL,
  `workflow_master_id` bigint(20) DEFAULT NULL,
  `request_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `scheme_master`
--

CREATE TABLE `scheme_master` (
  `id` bigint(20) NOT NULL,
  `scheme_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `scheme_master`
--

INSERT INTO `scheme_master` (`id`, `scheme_name`) VALUES
(1, 'Scheme 1'),
(2, 'Scheme 2');

-- --------------------------------------------------------

--
-- Table structure for table `sewer_size`
--

CREATE TABLE `sewer_size` (
  `id` bigint(20) NOT NULL,
  `sewer_size` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sewer_size`
--

INSERT INTO `sewer_size` (`id`, `sewer_size`) VALUES
(3, '100'),
(4, '150'),
(5, '200'),
(6, '250'),
(7, '300'),
(31, '450');

-- --------------------------------------------------------

--
-- Table structure for table `sib_entry`
--

CREATE TABLE `sib_entry` (
  `id` bigint(20) NOT NULL,
  `sib_id` bigint(20) DEFAULT NULL,
  `so_no` varchar(255) DEFAULT NULL,
  `so_date` timestamp NULL DEFAULT NULL,
  `demand_date` timestamp NULL DEFAULT NULL,
  `dir` varchar(255) DEFAULT NULL,
  `div_name` varchar(255) DEFAULT NULL,
  `inv_no` bigint(20) DEFAULT NULL,
  `sib_date` timestamp NULL DEFAULT NULL,
  `sib_no` varchar(255) DEFAULT NULL,
  `ir_date` timestamp NULL DEFAULT NULL,
  `ir_no` varchar(255) DEFAULT NULL,
  `vendor_code` varchar(255) DEFAULT NULL,
  `remarks` varchar(255) DEFAULT NULL,
  `to_user` timestamp NULL DEFAULT NULL,
  `from_user` timestamp NULL DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `creation_date` timestamp NULL DEFAULT NULL,
  `last_modified_date` timestamp NULL DEFAULT NULL,
  `dc_no` varchar(255) DEFAULT NULL,
  `dc_date` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `status_master`
--

CREATE TABLE `status_master` (
  `id` bigint(20) NOT NULL,
  `status` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `status_master`
--

INSERT INTO `status_master` (`id`, `status`, `description`) VALUES
(1, 'DISABLED', 'GENERAL'),
(2, 'ENABLED', 'GENERAL'),
(3, 'PENDING', 'WORKFLOW'),
(4, 'PROCESSING', 'WORKFLOW'),
(5, 'APPROVED', 'WORKFLOW'),
(6, 'DELEGATED', 'WORKFLOW'),
(7, 'DECLINED', 'WORKFLOW'),
(8, 'ESCALATED', 'WORKFLOW'),
(9, 'COMPLETED', 'WORKFLOW'),
(10, 'CANCELLED', 'WORKFLOW'),
(11, 'MANUAL', 'WORKFLOW'),
(12, 'AUTOMATIC', 'WORKFLOW'),
(13, 'RETIRED', 'EMPLOYEE STATUS'),
(14, 'TRANSFERED', 'EMPLOYEE STATUS'),
(15, 'RESIGNED', 'EMPLOYEE STATUS'),
(16, 'DEATH', 'EMPLOYEE STATUS');

-- --------------------------------------------------------

--
-- Table structure for table `street_master`
--

CREATE TABLE `street_master` (
  `id` bigint(20) NOT NULL,
  `street_name` varchar(255) DEFAULT NULL,
  `street_no` varchar(255) DEFAULT NULL,
  `division_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `street_master`
--

INSERT INTO `street_master` (`id`, `street_name`, `street_no`, `division_master_id`) VALUES
(1, 'Street1', '01', 1),
(2, 'Street2', '02', 2),
(3, 'Street3', '03', 3),
(4, 'Street4', '04', 3),
(5, 'Street5', '05', 5),
(6, 'Street6', '06', 4),
(7, 'Street7', '07', 6),
(8, 'Street8', '08', 7),
(9, 'Street9', '09', 8),
(10, 'Street10', '10', 9),
(11, 'Street11', '11', 10),
(12, 'StNo6', '06', 6),
(13, 'StNo02', '02', 6),
(14, 'General', '99', 11);

-- --------------------------------------------------------

--
-- Table structure for table `sub_desig_category_master`
--

CREATE TABLE `sub_desig_category_master` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `creation_date` timestamp NULL DEFAULT NULL,
  `last_modified_date` timestamp NULL DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `alias` varchar(255) DEFAULT NULL,
  `order_by` int(11) DEFAULT NULL,
  `status_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `tariff_category_master`
--

CREATE TABLE `tariff_category_master` (
  `id` bigint(20) NOT NULL,
  `tariff_category` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tariff_category_master`
--

INSERT INTO `tariff_category_master` (`id`, `tariff_category`, `type`) VALUES
(1, 'Domestic', 'METERED'),
(2, 'Diplomats', 'METERED'),
(3, 'Commercial', 'METERED'),
(4, 'Industrial', 'METERED'),
(5, 'Institutional', 'METERED'),
(6, 'Kiosks', 'METERED'),
(7, 'Domestic - Unmetered', 'UNMETERED'),
(8, 'Institutional - Unmetered', 'UNMETERED'),
(9, 'Commercial - Unmetered', 'UNMETERED'),
(10, 'Industrial - Unmetered', 'UNMETERED'),
(12, 'Kiosks - Unmetered', 'UNMETERED');

-- --------------------------------------------------------

--
-- Table structure for table `tariff_charges`
--

CREATE TABLE `tariff_charges` (
  `id` bigint(20) NOT NULL,
  `tariff_desc` varchar(255) NOT NULL,
  `slab_min` int(11) NOT NULL,
  `slab_max` int(11) NOT NULL,
  `rate` decimal(20,3) NOT NULL,
  `min_kl` decimal(20,3) NOT NULL,
  `min_unmetered_kl` decimal(20,3) NOT NULL,
  `slab_base_charge` decimal(20,3) NOT NULL,
  `tariff_master_id` bigint(20) DEFAULT NULL,
  `tariff_type_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `tariff_master`
--

CREATE TABLE `tariff_master` (
  `id` bigint(20) NOT NULL,
  `tariff_name` varchar(255) NOT NULL,
  `valid_from` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `valid_to` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `active` varchar(255) NOT NULL,
  `tariff_category_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `tariff_type_master`
--

CREATE TABLE `tariff_type_master` (
  `id` bigint(20) NOT NULL,
  `tariff_type` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tariff_type_master`
--

INSERT INTO `tariff_type_master` (`id`, `tariff_type`) VALUES
(1, 'Usage Charges'),
(2, 'Fixed Charges'),
(3, 'Service Charges');

-- --------------------------------------------------------

--
-- Table structure for table `terminal`
--

CREATE TABLE `terminal` (
  `id` bigint(20) NOT NULL,
  `amount` float DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `user_id` varchar(255) DEFAULT NULL,
  `mr_code` varchar(255) DEFAULT NULL,
  `sec_code` varchar(255) DEFAULT NULL,
  `div_code` varchar(255) DEFAULT NULL,
  `sec_name` varchar(255) DEFAULT NULL,
  `user_name` varchar(255) DEFAULT NULL,
  `mobile_no` varchar(255) DEFAULT NULL,
  `ver` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `terminal`
--

INSERT INTO `terminal` (`id`, `amount`, `status`, `user_id`, `mr_code`, `sec_code`, `div_code`, `sec_name`, `user_name`, `mobile_no`, `ver`) VALUES
(1, 1111, 'Status1', 'UserId1', 'MrCode1', 'SecCode1', 'DivCode1', 'SecName1', 'UserName1', 'MobileNo1', 'Ver1');

-- --------------------------------------------------------

--
-- Table structure for table `terminal_log`
--

CREATE TABLE `terminal_log` (
  `id` bigint(20) NOT NULL,
  `amount` float DEFAULT NULL,
  `last_modified` timestamp NULL DEFAULT NULL,
  `modified_by` varchar(255) DEFAULT NULL,
  `user_id` varchar(255) DEFAULT NULL,
  `bank_deposit_date` date DEFAULT NULL,
  `before_update` varchar(255) DEFAULT NULL,
  `after_update` varchar(255) DEFAULT NULL,
  `mr_code` varchar(255) DEFAULT NULL,
  `remark` varchar(255) DEFAULT NULL,
  `txn_type` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `transaction_type_master`
--

CREATE TABLE `transaction_type_master` (
  `id` bigint(20) NOT NULL,
  `type_of_txn` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `transaction_type_master`
--

INSERT INTO `transaction_type_master` (`id`, `type_of_txn`) VALUES
(1, 'Credit'),
(2, 'Debit');

-- --------------------------------------------------------

--
-- Table structure for table `uom`
--

CREATE TABLE `uom` (
  `id` bigint(20) NOT NULL,
  `value` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `uom`
--

INSERT INTO `uom` (`id`, `value`) VALUES
(1, 'Meter'),
(2, 'Centi Meter'),
(3, 'Piece');

-- --------------------------------------------------------

--
-- Table structure for table `url`
--

CREATE TABLE `url` (
  `id` bigint(20) NOT NULL,
  `url_pattern` varchar(255) NOT NULL,
  `version` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `url2_role`
--

CREATE TABLE `url2_role` (
  `id` bigint(20) NOT NULL,
  `url_id` bigint(20) DEFAULT NULL,
  `authority_name` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `valve_complaint`
--

CREATE TABLE `valve_complaint` (
  `id` bigint(20) NOT NULL,
  `closed_time` timestamp NULL DEFAULT NULL,
  `open_time` timestamp NULL DEFAULT NULL,
  `colour_code` varchar(255) DEFAULT NULL,
  `side` varchar(255) DEFAULT NULL,
  `no_of_turns` int(11) DEFAULT NULL,
  `valve_size` float DEFAULT NULL,
  `valve_no` int(11) DEFAULT NULL,
  `repair_code` varchar(255) DEFAULT NULL,
  `distance_left` varchar(255) DEFAULT NULL,
  `distance_sb` varchar(255) DEFAULT NULL,
  `distance_z` varchar(255) DEFAULT NULL,
  `water_leakage_complaint_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `version`
--

CREATE TABLE `version` (
  `id` bigint(20) NOT NULL,
  `version_low` varchar(255) DEFAULT NULL,
  `version_high` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `version`
--

INSERT INTO `version` (`id`, `version_low`, `version_high`) VALUES
(1, '1', '533'),
(2, '1', '19'),
(6, '11', '33');

-- --------------------------------------------------------

--
-- Table structure for table `water_leakage_complaint`
--

CREATE TABLE `water_leakage_complaint` (
  `id` bigint(20) NOT NULL,
  `leakage_type` varchar(255) DEFAULT NULL,
  `coordinate_x` varchar(255) DEFAULT NULL,
  `coordinate_y` varchar(255) DEFAULT NULL,
  `leak_magnitude` varchar(255) DEFAULT NULL,
  `complaint_date_time` timestamp NULL DEFAULT NULL,
  `days_required` int(11) DEFAULT NULL,
  `staff_required` int(11) DEFAULT NULL,
  `complaint_by` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `division_master_id` bigint(20) DEFAULT NULL,
  `street_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `workflow`
--

CREATE TABLE `workflow` (
  `id` bigint(20) NOT NULL,
  `stage_id` int(11) DEFAULT NULL,
  `workflow_master_id` bigint(20) DEFAULT NULL,
  `relative_from_role_id` bigint(20) DEFAULT NULL,
  `absolute_from_role_id` bigint(20) DEFAULT NULL,
  `relationship_type_id` bigint(20) DEFAULT NULL,
  `relative_to_role_id` bigint(20) DEFAULT NULL,
  `absolute_to_role_id` bigint(20) DEFAULT NULL,
  `escalation_relationship_type_id` bigint(20) DEFAULT NULL,
  `relative_escalation_to_id` bigint(20) DEFAULT NULL,
  `absolute_escalation_to_id` bigint(20) DEFAULT NULL,
  `workflow_stage_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `workflow`
--

INSERT INTO `workflow` (`id`, `stage_id`, `workflow_master_id`, `relative_from_role_id`, `absolute_from_role_id`, `relationship_type_id`, `relative_to_role_id`, `absolute_to_role_id`, `escalation_relationship_type_id`, `relative_escalation_to_id`, `absolute_escalation_to_id`, `workflow_stage_master_id`) VALUES
(1, 1, 1, NULL, NULL, 2, NULL, 9, NULL, NULL, 24, 4),
(2, 2, 1, NULL, 9, 2, NULL, 14, NULL, NULL, NULL, 5),
(3, 3, 1, NULL, 14, 2, NULL, 16, NULL, NULL, NULL, 2),
(4, 4, 1, NULL, 16, 2, NULL, 9, NULL, NULL, NULL, 2),
(5, 5, 1, NULL, 9, 2, NULL, 23, NULL, NULL, NULL, NULL),
(6, 6, 1, NULL, 23, 2, NULL, 25, NULL, NULL, NULL, NULL),
(7, 7, 1, NULL, 25, 2, NULL, 16, NULL, NULL, NULL, NULL),
(8, 8, 1, NULL, 16, 2, NULL, 18, NULL, NULL, NULL, NULL),
(9, 1, 4, NULL, NULL, 2, NULL, 20, NULL, NULL, NULL, 4),
(10, 2, 4, NULL, 20, 2, NULL, 10, NULL, NULL, NULL, 5),
(11, 3, 4, NULL, 10, 2, NULL, 11, NULL, NULL, NULL, 5),
(12, 4, 4, NULL, 11, 2, NULL, 4, NULL, NULL, NULL, 5),
(13, 5, 4, NULL, 4, 2, NULL, 18, NULL, NULL, NULL, NULL),
(14, 1, 7, NULL, NULL, 2, NULL, 20, NULL, NULL, NULL, 5),
(15, 2, 7, NULL, 20, 2, NULL, 9, NULL, NULL, NULL, 5),
(16, 3, 7, NULL, 9, 2, NULL, 14, NULL, NULL, NULL, 5),
(17, 4, 7, NULL, 14, 2, NULL, 9, NULL, NULL, NULL, 5),
(18, 1, 5, NULL, NULL, 2, NULL, 9, NULL, NULL, NULL, 2),
(19, 2, 5, NULL, 9, 2, NULL, 18, NULL, NULL, NULL, NULL),
(20, 1, 6, NULL, NULL, 2, NULL, 16, NULL, NULL, NULL, 4),
(21, 1, 8, NULL, NULL, 2, NULL, 9, NULL, NULL, NULL, 1),
(22, 2, 8, NULL, 9, 2, NULL, 18, NULL, NULL, NULL, 2),
(23, 1, 9, NULL, NULL, 2, NULL, 9, NULL, NULL, NULL, 1),
(24, 2, 9, NULL, 9, 2, NULL, 18, NULL, NULL, NULL, 2),
(25, 1, 10, NULL, NULL, 2, NULL, 9, NULL, NULL, NULL, 5),
(26, 2, 10, NULL, 9, 2, NULL, 23, NULL, NULL, NULL, 2),
(27, 3, 10, NULL, 23, 2, NULL, 18, NULL, NULL, NULL, 2),
(28, 2, 6, NULL, 16, 2, NULL, 9, NULL, NULL, NULL, 2),
(29, 1, 11, NULL, NULL, 2, NULL, 9, NULL, NULL, NULL, 2),
(58, 1, 13, NULL, NULL, 2, NULL, 20, NULL, NULL, NULL, NULL),
(59, 2, 13, NULL, 20, 2, NULL, 15, NULL, NULL, NULL, NULL),
(60, 3, 13, NULL, 15, 2, NULL, 9, NULL, NULL, NULL, NULL),
(61, 4, 13, NULL, 9, 2, NULL, 4, NULL, NULL, NULL, NULL),
(62, 5, 13, NULL, 4, 2, NULL, 25, NULL, NULL, NULL, NULL),
(63, 6, 13, NULL, 25, 2, NULL, 15, NULL, NULL, NULL, NULL),
(77, 1, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL),
(78, 2, NULL, NULL, NULL, 2, NULL, NULL, NULL, NULL, NULL, NULL),
(79, 1, NULL, NULL, NULL, 2, NULL, 3, NULL, NULL, NULL, NULL),
(80, 2, NULL, NULL, 3, 2, NULL, 3, NULL, NULL, NULL, NULL),
(81, 1, NULL, NULL, NULL, 1, 3, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `workflow_master`
--

CREATE TABLE `workflow_master` (
  `id` bigint(20) NOT NULL,
  `workflow_name` varchar(255) NOT NULL,
  `to_workflow` int(11) DEFAULT NULL,
  `creation_date` timestamp NULL DEFAULT NULL,
  `last_modified_date` timestamp NULL DEFAULT NULL,
  `status_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `workflow_master`
--

INSERT INTO `workflow_master` (`id`, `workflow_name`, `to_workflow`, `creation_date`, `last_modified_date`, `status_master_id`) VALUES
(1, 'REQUISITION', 0, '2016-03-18 15:00:00', '2016-03-18 15:00:00', 2),
(2, 'NEW', 0, '2016-03-26 15:00:00', '2016-03-26 15:00:00', 1),
(4, 'INCORRECT BILL', 0, '2016-03-31 15:00:00', '2016-03-31 15:00:00', 2),
(5, 'WITHOUTMETER', 0, '2016-03-31 15:00:00', '2016-03-31 15:00:00', 2),
(6, 'METER CHANGE', 0, '2016-03-31 15:00:00', '2016-03-31 15:00:00', 2),
(7, 'WATER LEAKAGE', 0, '2016-04-29 15:00:00', '2016-04-29 15:00:00', 2),
(8, 'CONNECTION CATEGORY', 0, '2016-04-29 15:00:00', '2016-04-29 15:00:00', 2),
(9, 'PIPE SIZE', 0, '2016-04-29 15:00:00', '2016-04-29 15:00:00', 2),
(10, 'CHANGE NAME', 0, '2016-04-29 15:00:00', '2016-04-29 15:00:00', 2),
(11, 'CONNECTION TERMINATION', 0, '2016-04-29 15:00:00', '2016-04-29 15:00:00', 2),
(13, 'JOB CARD', 0, '2016-08-16 22:26:20', '2016-08-16 22:26:20', 2);

-- --------------------------------------------------------

--
-- Table structure for table `workflow_relations`
--

CREATE TABLE `workflow_relations` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `status_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `workflow_relations`
--

INSERT INTO `workflow_relations` (`id`, `name`, `status_master_id`) VALUES
(1, 'DIRECTOR', 1),
(3, 'PROGRAMME DIRECTOR', 1),
(5, 'ASSOCIATE DIRECTOR', 1),
(7, 'PROJECT DIRECTOR', 1),
(9, 'TECHNICAL DIRECTORATE', 1),
(13, 'DIVISION HEAD', 1),
(20, 'BOSS', 2),
(21, 'BOSSES BOSS', 2),
(22, 'ADMIN', 2);

-- --------------------------------------------------------

--
-- Table structure for table `workflow_relationships`
--

CREATE TABLE `workflow_relationships` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `status_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `workflow_relationships`
--

INSERT INTO `workflow_relationships` (`id`, `name`, `status_master_id`) VALUES
(1, 'Relative', 2),
(2, 'Absolute', 2);

-- --------------------------------------------------------

--
-- Table structure for table `workflow_stage_master`
--

CREATE TABLE `workflow_stage_master` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `creation_date` timestamp NULL DEFAULT NULL,
  `last_modified_date` timestamp NULL DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `status_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `workflow_stage_master`
--

INSERT INTO `workflow_stage_master` (`id`, `name`, `creation_date`, `last_modified_date`, `description`, `status_master_id`) VALUES
(1, 'Recommended', '2016-03-21 15:00:00', '2016-03-21 15:00:00', NULL, 2),
(2, 'Approved', '2016-03-21 15:00:00', '2016-03-21 15:00:00', NULL, 2),
(3, 'Sanctioned', '2016-03-21 15:00:00', '2016-03-21 15:00:00', NULL, 2),
(4, 'Waiting', '2016-03-21 15:00:00', '2016-03-21 15:00:00', NULL, 2),
(5, 'Forwarded', '2016-03-21 15:00:00', '2016-03-21 15:00:00', NULL, 2),
(6, 'Completed', '2016-03-21 15:00:00', '2016-03-21 15:00:00', NULL, 2);

-- --------------------------------------------------------

--
-- Table structure for table `workflow_txn_details`
--

CREATE TABLE `workflow_txn_details` (
  `id` bigint(20) NOT NULL,
  `request_id` int(11) DEFAULT NULL,
  `reference_number` varchar(255) DEFAULT NULL,
  `row_number` int(11) DEFAULT NULL,
  `column_name` varchar(255) DEFAULT NULL,
  `previous_value` varchar(255) DEFAULT NULL,
  `new_value` varchar(255) DEFAULT NULL,
  `ip_address` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `request_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `workflow_type_master`
--

CREATE TABLE `workflow_type_master` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `creation_date` timestamp NULL DEFAULT NULL,
  `last_modified_date` timestamp NULL DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `status_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `workflow_type_master`
--

INSERT INTO `workflow_type_master` (`id`, `name`, `creation_date`, `last_modified_date`, `description`, `status_master_id`) VALUES
(1, 'GENERIC', '2016-03-26 15:00:00', '2016-03-26 15:00:00', NULL, 2),
(2, 'ROLE', '2016-03-26 15:00:00', '2016-03-26 15:00:00', NULL, 2);

-- --------------------------------------------------------

--
-- Table structure for table `zone_master`
--

CREATE TABLE `zone_master` (
  `id` bigint(20) NOT NULL,
  `zone_name` varchar(255) DEFAULT NULL,
  `zone_code` varchar(255) DEFAULT NULL,
  `division_master_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `access_list`
--
ALTER TABLE `access_list`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `adjustments`
--
ALTER TABLE `adjustments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_adjustments_custdetails_id` (`cust_details_id`),
  ADD KEY `fk_adjustments_billfulldetails_id` (`bill_full_details_id`),
  ADD KEY `fk_adjustments_transactiontypemaster_id` (`transaction_type_master_id`),
  ADD KEY `fk_adjustments_user_id` (`user_id`),
  ADD KEY `fk_adjustments_customercomplaints_id` (`customer_complaints_id`);

--
-- Indexes for table `application_txn`
--
ALTER TABLE `application_txn`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_applicationtxn_tariffcategorymaster_id` (`tariff_category_master_id`),
  ADD KEY `fk_applicationtxn_meterdetails_id` (`meter_details_id`),
  ADD KEY `fk_applicationtxn_user_id` (`user_id`),
  ADD KEY `fk_applicationtxn_requestat_id` (`request_at_id`),
  ADD KEY `fk_applicationtxn_divisionmaster_id` (`division_master_id`),
  ADD KEY `fk_applicationtxn_streetmaster_id` (`street_master_id`),
  ADD KEY `fk_applicationtxn_idproofmaster_id` (`id_proof_master_id`);

--
-- Indexes for table `application_type_master`
--
ALTER TABLE `application_type_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `bank_master`
--
ALTER TABLE `bank_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `bill_details`
--
ALTER TABLE `bill_details`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_billdetails_mtrreader_id` (`mtr_reader_id`);

--
-- Indexes for table `bill_full_details`
--
ALTER TABLE `bill_full_details`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_billfulldetails_meterdetails_id` (`meter_details_id`);

--
-- Indexes for table `bill_run_details`
--
ALTER TABLE `bill_run_details`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_billrundetails_billfulldetails_id` (`bill_full_details_id`),
  ADD KEY `fk_billrundetails_billrunmaster_id` (`bill_run_master_id`),
  ADD KEY `fk_billrundetails_billdetails_id` (`bill_details_id`);

--
-- Indexes for table `bill_run_master`
--
ALTER TABLE `bill_run_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `burst_complaint`
--
ALTER TABLE `burst_complaint`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_burstcomplaint_waterleakagecomplaint_id` (`water_leakage_complaint_id`);

--
-- Indexes for table `cash_book_master`
--
ALTER TABLE `cash_book_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `category_master`
--
ALTER TABLE `category_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `category_pipe_size_mapping`
--
ALTER TABLE `category_pipe_size_mapping`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_categorypipesizemapping_categorymaster_id` (`category_master_id`),
  ADD KEY `fk_categorypipesizemapping_pipesizemaster_id` (`pipe_size_master_id`);

--
-- Indexes for table `charge_base`
--
ALTER TABLE `charge_base`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `collection_type_master`
--
ALTER TABLE `collection_type_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `coll_details`
--
ALTER TABLE `coll_details`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_colldetails_paymenttypes_id` (`payment_types_id`),
  ADD KEY `fk_colldetails_bankmaster_id` (`bank_master_id`),
  ADD KEY `fk_colldetails_collectiontypemaster_id` (`collection_type_master_id`);

--
-- Indexes for table `complaint_type_master`
--
ALTER TABLE `complaint_type_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `configuration_details`
--
ALTER TABLE `configuration_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `connection_terminate`
--
ALTER TABLE `connection_terminate`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_connectionterminate_meterdetails_id` (`meter_details_id`);

--
-- Indexes for table `connection_type_master`
--
ALTER TABLE `connection_type_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `current_users`
--
ALTER TABLE `current_users`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_customer_oldtariffcategory_id` (`old_tariff_category_id`),
  ADD KEY `fk_customer_newtariffcategory_id` (`new_tariff_category_id`),
  ADD KEY `fk_customer_newproofmaster_id` (`new_proof_master_id`),
  ADD KEY `fk_customer_oldpipesizemaster_id` (`old_pipe_size_master_id`),
  ADD KEY `fk_customer_requestedpipesizemaster_id` (`requested_pipe_size_master_id`);

--
-- Indexes for table `customer_complaints`
--
ALTER TABLE `customer_complaints`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_customercomplaints_complainttypemaster_id` (`complaint_type_master_id`);

--
-- Indexes for table `cust_details`
--
ALTER TABLE `cust_details`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_custdetails_tariffcategorymaster_id` (`tariff_category_master_id`),
  ADD KEY `fk_custdetails_pipesizemaster_id` (`pipe_size_master_id`),
  ADD KEY `fk_custdetails_divisionmaster_id` (`division_master_id`),
  ADD KEY `fk_custdetails_streetmaster_id` (`street_master_id`),
  ADD KEY `fk_custdetails_meterdetails_id` (`meter_details_id`);

--
-- Indexes for table `cust_meter_mapping`
--
ALTER TABLE `cust_meter_mapping`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_custmetermapping_custdetails_id` (`cust_details_id`),
  ADD KEY `fk_custmetermapping_meterdetails_id` (`meter_details_id`);

--
-- Indexes for table `databasechangeloglock`
--
ALTER TABLE `databasechangeloglock`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `departments_hierarchy`
--
ALTER TABLE `departments_hierarchy`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_departmentshierarchy_statusmaster_id` (`status_master_id`);

--
-- Indexes for table `departments_master`
--
ALTER TABLE `departments_master`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_departmentsmaster_departmentshierarchy_id` (`departments_hierarchy_id`),
  ADD KEY `fk_departmentsmaster_departmenttypemaster_id` (`department_type_master_id`),
  ADD KEY `fk_departmentsmaster_statusmaster_id` (`status_master_id`);

--
-- Indexes for table `department_type_master`
--
ALTER TABLE `department_type_master`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_departmenttypemaster_statusmaster_id` (`status_master_id`);

--
-- Indexes for table `designation_mappings`
--
ALTER TABLE `designation_mappings`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_designationmappings_desigcategorymaster_id` (`desig_category_master_id`),
  ADD KEY `fk_designationmappings_subdesigcategorymaster_id` (`sub_desig_category_master_id`),
  ADD KEY `fk_designationmappings_designationmaster_id` (`designation_master_id`),
  ADD KEY `fk_designationmappings_groupmaster_id` (`group_master_id`);

--
-- Indexes for table `designation_master`
--
ALTER TABLE `designation_master`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_designationmaster_statusmaster_id` (`status_master_id`);

--
-- Indexes for table `desig_category_master`
--
ALTER TABLE `desig_category_master`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_desigcategorymaster_statusmaster_id` (`status_master_id`);

--
-- Indexes for table `division_master`
--
ALTER TABLE `division_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `docket_code`
--
ALTER TABLE `docket_code`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `emp_master`
--
ALTER TABLE `emp_master`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_empmaster_user_id` (`user_id`),
  ADD KEY `fk_empmaster_officeid_id` (`office_id_id`),
  ADD KEY `fk_empmaster_designationmaster_id` (`designation_master_id`),
  ADD KEY `fk_empmaster_directorateid_id` (`directorate_id_id`),
  ADD KEY `fk_empmaster_statusmaster_id` (`status_master_id`),
  ADD KEY `fk_empmaster_reportingto_id` (`reporting_to_id`);

--
-- Indexes for table `emp_role_mapping`
--
ALTER TABLE `emp_role_mapping`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_emprolemapping_user_id` (`user_id`),
  ADD KEY `fk_emprolemapping_parentuser_id` (`parent_user_id`),
  ADD KEY `fk_emprolemapping_orgroleinstance_id` (`org_role_instance_id`),
  ADD KEY `fk_emprolemapping_statusmaster_id` (`status_master_id`);

--
-- Indexes for table `expense_details`
--
ALTER TABLE `expense_details`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_expensedetails_paymenttypes_id` (`payment_types_id`),
  ADD KEY `fk_expensedetails_bankmaster_id` (`bank_master_id`),
  ADD KEY `fk_expensedetails_collectiontypemaster_id` (`collection_type_master_id`);

--
-- Indexes for table `feasibility_status`
--
ALTER TABLE `feasibility_status`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `feasibility_study`
--
ALTER TABLE `feasibility_study`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_feasibilitystudy_divisionmaster_id` (`division_master_id`),
  ADD KEY `fk_feasibilitystudy_zonemaster_id` (`zone_master_id`),
  ADD KEY `fk_feasibilitystudy_streetmaster_id` (`street_master_id`),
  ADD KEY `fk_feasibilitystudy_applicationtxn_id` (`application_txn_id`),
  ADD KEY `fk_feasibilitystudy_preparedby_id` (`prepared_by_id`),
  ADD KEY `fk_feasibilitystudy_approvedbyzonalhead_id` (`approved_by_zonal_head_id`),
  ADD KEY `fk_feasibilitystudy_inspectionbydepartmenthead_id` (`inspection_by_department_head_id`),
  ADD KEY `fk_feasibilitystudy_approvedbyoperationmanager_id` (`approved_by_operation_manager_id`),
  ADD KEY `fk_feasibilitystudy_categorymaster_id` (`category_master_id`);

--
-- Indexes for table `file_number`
--
ALTER TABLE `file_number`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `file_upload_master`
--
ALTER TABLE `file_upload_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `group_master`
--
ALTER TABLE `group_master`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_groupmaster_statusmaster_id` (`status_master_id`);

--
-- Indexes for table `hydrant_complaint`
--
ALTER TABLE `hydrant_complaint`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_hydrantcomplaint_waterleakagecomplaint_id` (`water_leakage_complaint_id`);

--
-- Indexes for table `id_proof_master`
--
ALTER TABLE `id_proof_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `instrument_issuer_master`
--
ALTER TABLE `instrument_issuer_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `invoice_payments`
--
ALTER TABLE `invoice_payments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_invoicepayments_custdetails_id` (`cust_details_id`),
  ADD KEY `fk_invoicepayments_billfulldetails_id` (`bill_full_details_id`),
  ADD KEY `fk_invoicepayments_colldetails_id` (`coll_details_id`);

--
-- Indexes for table `item_category_master`
--
ALTER TABLE `item_category_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `item_code_master`
--
ALTER TABLE `item_code_master`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_itemcodemaster_itemcategorymaster_id` (`item_category_master_id`),
  ADD KEY `fk_itemcodemaster_itemsubcategorymaster_id` (`item_sub_category_master_id`);

--
-- Indexes for table `item_company_master`
--
ALTER TABLE `item_company_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `item_details`
--
ALTER TABLE `item_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `item_required`
--
ALTER TABLE `item_required`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_itemrequired_materialmaster_id` (`material_master_id`),
  ADD KEY `fk_itemrequired_applicationtxn_id` (`application_txn_id`),
  ADD KEY `fk_itemrequired_feasibilitystudy_id` (`feasibility_study_id`),
  ADD KEY `fk_itemrequired_proceedings_id` (`proceedings_id`),
  ADD KEY `fk_itemrequired_uom_id` (`uom_id`);

--
-- Indexes for table `item_sub_category_master`
--
ALTER TABLE `item_sub_category_master`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_itemsubcategorymaster_itemcategorymaster_id` (`item_category_master_id`);

--
-- Indexes for table `item_sub_code_master`
--
ALTER TABLE `item_sub_code_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `jhi_authority`
--
ALTER TABLE `jhi_authority`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `jhi_persistent_audit_event`
--
ALTER TABLE `jhi_persistent_audit_event`
  ADD PRIMARY KEY (`event_id`),
  ADD KEY `idx_persistent_audit_event` (`principal`,`event_date`);

--
-- Indexes for table `jhi_persistent_audit_evt_data`
--
ALTER TABLE `jhi_persistent_audit_evt_data`
  ADD PRIMARY KEY (`event_id`,`name`),
  ADD KEY `idx_persistent_audit_evt_data` (`event_id`);

--
-- Indexes for table `jhi_persistent_token`
--
ALTER TABLE `jhi_persistent_token`
  ADD PRIMARY KEY (`series`),
  ADD KEY `fk_user_persistent_token` (`user_id`);

--
-- Indexes for table `jhi_user`
--
ALTER TABLE `jhi_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `login` (`login`),
  ADD UNIQUE KEY `idx_user_login` (`login`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `idx_user_email` (`email`);

--
-- Indexes for table `jhi_user_authority`
--
ALTER TABLE `jhi_user_authority`
  ADD PRIMARY KEY (`user_id`,`authority_name`),
  ADD KEY `fk_authority_name` (`authority_name`);

--
-- Indexes for table `job_card_item_requirement`
--
ALTER TABLE `job_card_item_requirement`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_jobcarditemrequirement_materialmaster_id` (`material_master_id`),
  ADD KEY `fk_jobcarditemrequirement_uom_id` (`uom_id`),
  ADD KEY `fk_jobcarditemrequirement_waterleakagecomplaint_id` (`water_leakage_complaint_id`);

--
-- Indexes for table `job_card_site_status`
--
ALTER TABLE `job_card_site_status`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_jobcardsitestatus_waterleakagecomplaint_id` (`water_leakage_complaint_id`);

--
-- Indexes for table `main_sewerage_size`
--
ALTER TABLE `main_sewerage_size`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `main_water_size`
--
ALTER TABLE `main_water_size`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `make_of_pipe`
--
ALTER TABLE `make_of_pipe`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `manage_cash_point`
--
ALTER TABLE `manage_cash_point`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_managecashpoint_transactiontypemaster_id` (`transaction_type_master_id`),
  ADD KEY `fk_managecashpoint_cashbookmaster_id` (`cash_book_master_id`),
  ADD KEY `fk_managecashpoint_paymenttypes_id` (`payment_types_id`),
  ADD KEY `fk_managecashpoint_filenumber_id` (`file_number_id`),
  ADD KEY `fk_managecashpoint_customer_id` (`customer_id`);

--
-- Indexes for table `material_master`
--
ALTER TABLE `material_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `menu_item`
--
ALTER TABLE `menu_item`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `menu_item2_url`
--
ALTER TABLE `menu_item2_url`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_menuitem2url_menuitem_id` (`menu_item_id`),
  ADD KEY `fk_menuitem2url_url_id` (`url_id`);

--
-- Indexes for table `merchant_master`
--
ALTER TABLE `merchant_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `meter_change`
--
ALTER TABLE `meter_change`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_meterchange_custdetails_id` (`cust_details_id`),
  ADD KEY `fk_meterchange_prevmeterno_id` (`prev_meter_no_id`),
  ADD KEY `fk_meterchange_newmeterno_id` (`new_meter_no_id`),
  ADD KEY `fk_meterchange_billfulldetails_id` (`bill_full_details_id`),
  ADD KEY `fk_meterchange_user_id` (`user_id`);

--
-- Indexes for table `meter_details`
--
ALTER TABLE `meter_details`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_meterdetails_meterstatus_id` (`meter_status_id`),
  ADD KEY `fk_meterdetails_pipesizemaster_id` (`pipe_size_master_id`);

--
-- Indexes for table `meter_status`
--
ALTER TABLE `meter_status`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `mmg_terms_master`
--
ALTER TABLE `mmg_terms_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `module`
--
ALTER TABLE `module`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `module2_menu_item`
--
ALTER TABLE `module2_menu_item`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_module2menuitem_module_id` (`module_id`),
  ADD KEY `fk_module2menuitem_menuitem_id` (`menu_item_id`);

--
-- Indexes for table `online_payment_callback`
--
ALTER TABLE `online_payment_callback`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_onlinepaymentcallback_merchantmaster_id` (`merchant_master_id`),
  ADD KEY `fk_onlinepaymentcallback_onlinepaymentorder_id` (`online_payment_order_id`);

--
-- Indexes for table `online_payment_order`
--
ALTER TABLE `online_payment_order`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_onlinepaymentorder_merchantmaster_id` (`merchant_master_id`);

--
-- Indexes for table `online_payment_response`
--
ALTER TABLE `online_payment_response`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_onlinepaymentresponse_onlinepaymentorder_id` (`online_payment_order_id`);

--
-- Indexes for table `org_hierarchy`
--
ALTER TABLE `org_hierarchy`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_orghierarchy_statusmaster_id` (`status_master_id`);

--
-- Indexes for table `org_roles_master`
--
ALTER TABLE `org_roles_master`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_orgrolesmaster_statusmaster_id` (`status_master_id`);

--
-- Indexes for table `org_role_hierarchy`
--
ALTER TABLE `org_role_hierarchy`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_orgrolehierarchy_statusmaster_id` (`status_master_id`);

--
-- Indexes for table `org_role_instance`
--
ALTER TABLE `org_role_instance`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_orgroleinstance_statusmaster_id` (`status_master_id`),
  ADD KEY `fk_orgroleinstance_orgrolehierarchy_id` (`org_role_hierarchy_id`),
  ADD KEY `fk_orgroleinstance_departmentsmaster_id` (`departments_master_id`);

--
-- Indexes for table `payment_types`
--
ALTER TABLE `payment_types`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `percentage_master`
--
ALTER TABLE `percentage_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pipe_size_master`
--
ALTER TABLE `pipe_size_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `proceedings`
--
ALTER TABLE `proceedings`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_proceedings_applicationtxn_id` (`application_txn_id`),
  ADD KEY `fk_proceedings_pipesizemaster_id` (`pipe_size_master_id`);

--
-- Indexes for table `receipt`
--
ALTER TABLE `receipt`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_receipt_applicationtxn_id` (`application_txn_id`),
  ADD KEY `fk_receipt_paymenttypes_id` (`payment_types_id`);

--
-- Indexes for table `request_master`
--
ALTER TABLE `request_master`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_requestmaster_statusmaster_id` (`status_master_id`),
  ADD KEY `fk_requestmaster_module_id` (`module_id`);

--
-- Indexes for table `request_workflow_history`
--
ALTER TABLE `request_workflow_history`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_requestworkflowhistory_assignedfrom_id` (`assigned_from_id`),
  ADD KEY `fk_requestworkflowhistory_assignedto_id` (`assigned_to_id`),
  ADD KEY `fk_requestworkflowhistory_statusmaster_id` (`status_master_id`),
  ADD KEY `fk_requestworkflowhistory_requestmaster_id` (`request_master_id`),
  ADD KEY `fk_requestworkflowhistory_workflowmaster_id` (`workflow_master_id`),
  ADD KEY `fk_requestworkflowhistory_workflowstagemaster_id` (`workflow_stage_master_id`),
  ADD KEY `fk_requestworkflowhistory_appliedby_id` (`applied_by_id`);

--
-- Indexes for table `request_workflow_mapping`
--
ALTER TABLE `request_workflow_mapping`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_requestworkflowmapping_statusmaster_id` (`status_master_id`),
  ADD KEY `fk_requestworkflowmapping_workflowmaster_id` (`workflow_master_id`),
  ADD KEY `fk_requestworkflowmapping_requestmaster_id` (`request_master_id`);

--
-- Indexes for table `req_desig_workflow_mapping`
--
ALTER TABLE `req_desig_workflow_mapping`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_reqdesigworkflowmapping_workflowmaster_id` (`workflow_master_id`),
  ADD KEY `fk_reqdesigworkflowmapping_requestmaster_id` (`request_master_id`),
  ADD KEY `fk_reqdesigworkflowmapping_designationmaster_id` (`designation_master_id`),
  ADD KEY `fk_reqdesigworkflowmapping_statusmaster_id` (`status_master_id`);

--
-- Indexes for table `req_org_workflow_mapping`
--
ALTER TABLE `req_org_workflow_mapping`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_reqorgworkflowmapping_workflowmaster_id` (`workflow_master_id`),
  ADD KEY `fk_reqorgworkflowmapping_requestmaster_id` (`request_master_id`),
  ADD KEY `fk_reqorgworkflowmapping_orgroleinstance_id` (`org_role_instance_id`),
  ADD KEY `fk_reqorgworkflowmapping_statusmaster_id` (`status_master_id`);

--
-- Indexes for table `revenue_type_master`
--
ALTER TABLE `revenue_type_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `reversal_details`
--
ALTER TABLE `reversal_details`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_reversaldetails_colldetails_id` (`coll_details_id`),
  ADD KEY `fk_reversaldetails_user_id` (`user_id`);

--
-- Indexes for table `re_allotment`
--
ALTER TABLE `re_allotment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_reallotment_filenumber_id` (`file_number_id`),
  ADD KEY `fk_reallotment_customer_id` (`customer_id`),
  ADD KEY `fk_reallotment_feasibilitystatus_id` (`feasibility_status_id`);

--
-- Indexes for table `role_workflow_mapping`
--
ALTER TABLE `role_workflow_mapping`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_roleworkflowmapping_statusmaster_id` (`status_master_id`),
  ADD KEY `fk_roleworkflowmapping_orgroleinstance_id` (`org_role_instance_id`),
  ADD KEY `fk_roleworkflowmapping_workflowmaster_id` (`workflow_master_id`),
  ADD KEY `fk_roleworkflowmapping_requestmaster_id` (`request_master_id`);

--
-- Indexes for table `scheme_master`
--
ALTER TABLE `scheme_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sewer_size`
--
ALTER TABLE `sewer_size`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sib_entry`
--
ALTER TABLE `sib_entry`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `status_master`
--
ALTER TABLE `status_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `street_master`
--
ALTER TABLE `street_master`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_streetmaster_divisionmaster_id` (`division_master_id`);

--
-- Indexes for table `sub_desig_category_master`
--
ALTER TABLE `sub_desig_category_master`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_subdesigcategorymaster_statusmaster_id` (`status_master_id`);

--
-- Indexes for table `tariff_category_master`
--
ALTER TABLE `tariff_category_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tariff_charges`
--
ALTER TABLE `tariff_charges`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_tariffcharges_tariffmaster_id` (`tariff_master_id`),
  ADD KEY `fk_tariffcharges_tarifftypemaster_id` (`tariff_type_master_id`);

--
-- Indexes for table `tariff_master`
--
ALTER TABLE `tariff_master`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_tariffmaster_tariffcategorymaster_id` (`tariff_category_master_id`);

--
-- Indexes for table `tariff_type_master`
--
ALTER TABLE `tariff_type_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `terminal`
--
ALTER TABLE `terminal`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `terminal_log`
--
ALTER TABLE `terminal_log`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `transaction_type_master`
--
ALTER TABLE `transaction_type_master`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `uom`
--
ALTER TABLE `uom`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `url`
--
ALTER TABLE `url`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `url2_role`
--
ALTER TABLE `url2_role`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_url2role_url_id` (`url_id`),
  ADD KEY `fk_url2role_authority_name` (`authority_name`);

--
-- Indexes for table `valve_complaint`
--
ALTER TABLE `valve_complaint`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_valvecomplaint_waterleakagecomplaint_id` (`water_leakage_complaint_id`);

--
-- Indexes for table `version`
--
ALTER TABLE `version`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `water_leakage_complaint`
--
ALTER TABLE `water_leakage_complaint`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_waterleakagecomplaint_divisionmaster_id` (`division_master_id`),
  ADD KEY `fk_waterleakagecomplaint_streetmaster_id` (`street_master_id`);

--
-- Indexes for table `workflow`
--
ALTER TABLE `workflow`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_workflow_workflowmaster_id` (`workflow_master_id`),
  ADD KEY `fk_workflow_relativefromrole_id` (`relative_from_role_id`),
  ADD KEY `fk_workflow_absolutefromrole_id` (`absolute_from_role_id`),
  ADD KEY `fk_workflow_relationshiptype_id` (`relationship_type_id`),
  ADD KEY `fk_workflow_relativetorole_id` (`relative_to_role_id`),
  ADD KEY `fk_workflow_absolutetorole_id` (`absolute_to_role_id`),
  ADD KEY `fk_workflow_escalationrelationshiptype_id` (`escalation_relationship_type_id`),
  ADD KEY `fk_workflow_relativeescalationto_id` (`relative_escalation_to_id`),
  ADD KEY `fk_workflow_absoluteescalationto_id` (`absolute_escalation_to_id`),
  ADD KEY `fk_workflow_workflowstagemaster_id` (`workflow_stage_master_id`);

--
-- Indexes for table `workflow_master`
--
ALTER TABLE `workflow_master`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_workflowmaster_statusmaster_id` (`status_master_id`);

--
-- Indexes for table `workflow_relations`
--
ALTER TABLE `workflow_relations`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_workflowrelations_statusmaster_id` (`status_master_id`);

--
-- Indexes for table `workflow_relationships`
--
ALTER TABLE `workflow_relationships`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_workflowrelationships_statusmaster_id` (`status_master_id`);

--
-- Indexes for table `workflow_stage_master`
--
ALTER TABLE `workflow_stage_master`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_workflowstagemaster_statusmaster_id` (`status_master_id`);

--
-- Indexes for table `workflow_txn_details`
--
ALTER TABLE `workflow_txn_details`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_workflowtxndetails_requestmaster_id` (`request_master_id`);

--
-- Indexes for table `workflow_type_master`
--
ALTER TABLE `workflow_type_master`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_workflowtypemaster_statusmaster_id` (`status_master_id`);

--
-- Indexes for table `zone_master`
--
ALTER TABLE `zone_master`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_zonemaster_divisionmaster_id` (`division_master_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `access_list`
--
ALTER TABLE `access_list`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
--
-- AUTO_INCREMENT for table `adjustments`
--
ALTER TABLE `adjustments`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20236;
--
-- AUTO_INCREMENT for table `application_txn`
--
ALTER TABLE `application_txn`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `application_type_master`
--
ALTER TABLE `application_type_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `bank_master`
--
ALTER TABLE `bank_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=89;
--
-- AUTO_INCREMENT for table `bill_details`
--
ALTER TABLE `bill_details`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6459;
--
-- AUTO_INCREMENT for table `bill_full_details`
--
ALTER TABLE `bill_full_details`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=294;
--
-- AUTO_INCREMENT for table `bill_run_details`
--
ALTER TABLE `bill_run_details`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `bill_run_master`
--
ALTER TABLE `bill_run_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=73;
--
-- AUTO_INCREMENT for table `burst_complaint`
--
ALTER TABLE `burst_complaint`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `cash_book_master`
--
ALTER TABLE `cash_book_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `category_master`
--
ALTER TABLE `category_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `category_pipe_size_mapping`
--
ALTER TABLE `category_pipe_size_mapping`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `charge_base`
--
ALTER TABLE `charge_base`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `collection_type_master`
--
ALTER TABLE `collection_type_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=109;
--
-- AUTO_INCREMENT for table `coll_details`
--
ALTER TABLE `coll_details`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=261;
--
-- AUTO_INCREMENT for table `complaint_type_master`
--
ALTER TABLE `complaint_type_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `configuration_details`
--
ALTER TABLE `configuration_details`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
--
-- AUTO_INCREMENT for table `connection_terminate`
--
ALTER TABLE `connection_terminate`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `connection_type_master`
--
ALTER TABLE `connection_type_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `current_users`
--
ALTER TABLE `current_users`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `customer_complaints`
--
ALTER TABLE `customer_complaints`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- AUTO_INCREMENT for table `cust_details`
--
ALTER TABLE `cust_details`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8609;
--
-- AUTO_INCREMENT for table `cust_meter_mapping`
--
ALTER TABLE `cust_meter_mapping`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3937;
--
-- AUTO_INCREMENT for table `departments_hierarchy`
--
ALTER TABLE `departments_hierarchy`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `departments_master`
--
ALTER TABLE `departments_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `department_type_master`
--
ALTER TABLE `department_type_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `designation_mappings`
--
ALTER TABLE `designation_mappings`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `designation_master`
--
ALTER TABLE `designation_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;
--
-- AUTO_INCREMENT for table `desig_category_master`
--
ALTER TABLE `desig_category_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `division_master`
--
ALTER TABLE `division_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
--
-- AUTO_INCREMENT for table `docket_code`
--
ALTER TABLE `docket_code`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `emp_master`
--
ALTER TABLE `emp_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=63;
--
-- AUTO_INCREMENT for table `emp_role_mapping`
--
ALTER TABLE `emp_role_mapping`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;
--
-- AUTO_INCREMENT for table `expense_details`
--
ALTER TABLE `expense_details`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `feasibility_status`
--
ALTER TABLE `feasibility_status`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `feasibility_study`
--
ALTER TABLE `feasibility_study`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `file_number`
--
ALTER TABLE `file_number`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `file_upload_master`
--
ALTER TABLE `file_upload_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `group_master`
--
ALTER TABLE `group_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `hydrant_complaint`
--
ALTER TABLE `hydrant_complaint`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `id_proof_master`
--
ALTER TABLE `id_proof_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `instrument_issuer_master`
--
ALTER TABLE `instrument_issuer_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `invoice_payments`
--
ALTER TABLE `invoice_payments`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `item_category_master`
--
ALTER TABLE `item_category_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `item_code_master`
--
ALTER TABLE `item_code_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `item_company_master`
--
ALTER TABLE `item_company_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `item_details`
--
ALTER TABLE `item_details`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `item_required`
--
ALTER TABLE `item_required`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `item_sub_category_master`
--
ALTER TABLE `item_sub_category_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `item_sub_code_master`
--
ALTER TABLE `item_sub_code_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `jhi_persistent_audit_event`
--
ALTER TABLE `jhi_persistent_audit_event`
  MODIFY `event_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1762;
--
-- AUTO_INCREMENT for table `jhi_user`
--
ALTER TABLE `jhi_user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;
--
-- AUTO_INCREMENT for table `job_card_item_requirement`
--
ALTER TABLE `job_card_item_requirement`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `job_card_site_status`
--
ALTER TABLE `job_card_site_status`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `main_sewerage_size`
--
ALTER TABLE `main_sewerage_size`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `main_water_size`
--
ALTER TABLE `main_water_size`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `make_of_pipe`
--
ALTER TABLE `make_of_pipe`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `manage_cash_point`
--
ALTER TABLE `manage_cash_point`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `material_master`
--
ALTER TABLE `material_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
--
-- AUTO_INCREMENT for table `menu_item`
--
ALTER TABLE `menu_item`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=141;
--
-- AUTO_INCREMENT for table `menu_item2_url`
--
ALTER TABLE `menu_item2_url`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=97;
--
-- AUTO_INCREMENT for table `merchant_master`
--
ALTER TABLE `merchant_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `meter_change`
--
ALTER TABLE `meter_change`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `meter_details`
--
ALTER TABLE `meter_details`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16556;
--
-- AUTO_INCREMENT for table `meter_status`
--
ALTER TABLE `meter_status`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `mmg_terms_master`
--
ALTER TABLE `mmg_terms_master`
  MODIFY `id` bigint(10) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `module`
--
ALTER TABLE `module`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
--
-- AUTO_INCREMENT for table `module2_menu_item`
--
ALTER TABLE `module2_menu_item`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=97;
--
-- AUTO_INCREMENT for table `online_payment_callback`
--
ALTER TABLE `online_payment_callback`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `online_payment_order`
--
ALTER TABLE `online_payment_order`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
--
-- AUTO_INCREMENT for table `online_payment_response`
--
ALTER TABLE `online_payment_response`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
--
-- AUTO_INCREMENT for table `org_hierarchy`
--
ALTER TABLE `org_hierarchy`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;
--
-- AUTO_INCREMENT for table `org_roles_master`
--
ALTER TABLE `org_roles_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `org_role_hierarchy`
--
ALTER TABLE `org_role_hierarchy`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;
--
-- AUTO_INCREMENT for table `org_role_instance`
--
ALTER TABLE `org_role_instance`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;
--
-- AUTO_INCREMENT for table `payment_types`
--
ALTER TABLE `payment_types`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `percentage_master`
--
ALTER TABLE `percentage_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `pipe_size_master`
--
ALTER TABLE `pipe_size_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `proceedings`
--
ALTER TABLE `proceedings`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `receipt`
--
ALTER TABLE `receipt`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `request_master`
--
ALTER TABLE `request_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
--
-- AUTO_INCREMENT for table `request_workflow_history`
--
ALTER TABLE `request_workflow_history`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=699;
--
-- AUTO_INCREMENT for table `request_workflow_mapping`
--
ALTER TABLE `request_workflow_mapping`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `req_desig_workflow_mapping`
--
ALTER TABLE `req_desig_workflow_mapping`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `req_org_workflow_mapping`
--
ALTER TABLE `req_org_workflow_mapping`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
--
-- AUTO_INCREMENT for table `revenue_type_master`
--
ALTER TABLE `revenue_type_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `reversal_details`
--
ALTER TABLE `reversal_details`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `re_allotment`
--
ALTER TABLE `re_allotment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `role_workflow_mapping`
--
ALTER TABLE `role_workflow_mapping`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `scheme_master`
--
ALTER TABLE `scheme_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `sewer_size`
--
ALTER TABLE `sewer_size`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;
--
-- AUTO_INCREMENT for table `sib_entry`
--
ALTER TABLE `sib_entry`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `status_master`
--
ALTER TABLE `status_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
--
-- AUTO_INCREMENT for table `street_master`
--
ALTER TABLE `street_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
--
-- AUTO_INCREMENT for table `sub_desig_category_master`
--
ALTER TABLE `sub_desig_category_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `tariff_category_master`
--
ALTER TABLE `tariff_category_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
--
-- AUTO_INCREMENT for table `tariff_charges`
--
ALTER TABLE `tariff_charges`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `tariff_master`
--
ALTER TABLE `tariff_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `tariff_type_master`
--
ALTER TABLE `tariff_type_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `terminal`
--
ALTER TABLE `terminal`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `terminal_log`
--
ALTER TABLE `terminal_log`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `transaction_type_master`
--
ALTER TABLE `transaction_type_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `uom`
--
ALTER TABLE `uom`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `url`
--
ALTER TABLE `url`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=139;
--
-- AUTO_INCREMENT for table `url2_role`
--
ALTER TABLE `url2_role`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=132;
--
-- AUTO_INCREMENT for table `valve_complaint`
--
ALTER TABLE `valve_complaint`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `version`
--
ALTER TABLE `version`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `water_leakage_complaint`
--
ALTER TABLE `water_leakage_complaint`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `workflow`
--
ALTER TABLE `workflow`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=82;
--
-- AUTO_INCREMENT for table `workflow_master`
--
ALTER TABLE `workflow_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
--
-- AUTO_INCREMENT for table `workflow_relations`
--
ALTER TABLE `workflow_relations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
--
-- AUTO_INCREMENT for table `workflow_relationships`
--
ALTER TABLE `workflow_relationships`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `workflow_stage_master`
--
ALTER TABLE `workflow_stage_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `workflow_txn_details`
--
ALTER TABLE `workflow_txn_details`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `workflow_type_master`
--
ALTER TABLE `workflow_type_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `zone_master`
--
ALTER TABLE `zone_master`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `adjustments`
--
ALTER TABLE `adjustments`
  ADD CONSTRAINT `fk_adjustments_billfulldetails_id` FOREIGN KEY (`bill_full_details_id`) REFERENCES `bill_full_details` (`id`),
  ADD CONSTRAINT `fk_adjustments_custdetails_id` FOREIGN KEY (`cust_details_id`) REFERENCES `cust_details` (`id`),
  ADD CONSTRAINT `fk_adjustments_customercomplaints_id` FOREIGN KEY (`customer_complaints_id`) REFERENCES `customer_complaints` (`id`),
  ADD CONSTRAINT `fk_adjustments_transactiontypemaster_id` FOREIGN KEY (`transaction_type_master_id`) REFERENCES `transaction_type_master` (`id`),
  ADD CONSTRAINT `fk_adjustments_user_id` FOREIGN KEY (`user_id`) REFERENCES `jhi_user` (`id`);

--
-- Constraints for table `application_txn`
--
ALTER TABLE `application_txn`
  ADD CONSTRAINT `fk_applicationtxn_divisionmaster_id` FOREIGN KEY (`division_master_id`) REFERENCES `division_master` (`id`),
  ADD CONSTRAINT `fk_applicationtxn_idproofmaster_id` FOREIGN KEY (`id_proof_master_id`) REFERENCES `id_proof_master` (`id`),
  ADD CONSTRAINT `fk_applicationtxn_meterdetails_id` FOREIGN KEY (`meter_details_id`) REFERENCES `meter_details` (`id`),
  ADD CONSTRAINT `fk_applicationtxn_requestat_id` FOREIGN KEY (`request_at_id`) REFERENCES `jhi_user` (`id`),
  ADD CONSTRAINT `fk_applicationtxn_streetmaster_id` FOREIGN KEY (`street_master_id`) REFERENCES `street_master` (`id`),
  ADD CONSTRAINT `fk_applicationtxn_tariffcategorymaster_id` FOREIGN KEY (`tariff_category_master_id`) REFERENCES `tariff_category_master` (`id`),
  ADD CONSTRAINT `fk_applicationtxn_user_id` FOREIGN KEY (`user_id`) REFERENCES `jhi_user` (`id`);

--
-- Constraints for table `bill_details`
--
ALTER TABLE `bill_details`
  ADD CONSTRAINT `fk_billdetails_mtrreader_id` FOREIGN KEY (`mtr_reader_id`) REFERENCES `jhi_user` (`id`);

--
-- Constraints for table `bill_full_details`
--
ALTER TABLE `bill_full_details`
  ADD CONSTRAINT `fk_billfulldetails_meterdetails_id` FOREIGN KEY (`meter_details_id`) REFERENCES `meter_details` (`id`);

--
-- Constraints for table `bill_run_details`
--
ALTER TABLE `bill_run_details`
  ADD CONSTRAINT `fk_billrundetails_billdetails_id` FOREIGN KEY (`bill_details_id`) REFERENCES `bill_details` (`id`),
  ADD CONSTRAINT `fk_billrundetails_billfulldetails_id` FOREIGN KEY (`bill_full_details_id`) REFERENCES `bill_full_details` (`id`),
  ADD CONSTRAINT `fk_billrundetails_billrunmaster_id` FOREIGN KEY (`bill_run_master_id`) REFERENCES `bill_run_master` (`id`);

--
-- Constraints for table `burst_complaint`
--
ALTER TABLE `burst_complaint`
  ADD CONSTRAINT `fk_burstcomplaint_waterleakagecomplaint_id` FOREIGN KEY (`water_leakage_complaint_id`) REFERENCES `water_leakage_complaint` (`id`);

--
-- Constraints for table `category_pipe_size_mapping`
--
ALTER TABLE `category_pipe_size_mapping`
  ADD CONSTRAINT `fk_categorypipesizemapping_categorymaster_id` FOREIGN KEY (`category_master_id`) REFERENCES `category_master` (`id`),
  ADD CONSTRAINT `fk_categorypipesizemapping_pipesizemaster_id` FOREIGN KEY (`pipe_size_master_id`) REFERENCES `pipe_size_master` (`id`);

--
-- Constraints for table `coll_details`
--
ALTER TABLE `coll_details`
  ADD CONSTRAINT `fk_colldetails_bankmaster_id` FOREIGN KEY (`bank_master_id`) REFERENCES `bank_master` (`id`),
  ADD CONSTRAINT `fk_colldetails_collectiontypemaster_id` FOREIGN KEY (`collection_type_master_id`) REFERENCES `collection_type_master` (`id`),
  ADD CONSTRAINT `fk_colldetails_paymenttypes_id` FOREIGN KEY (`payment_types_id`) REFERENCES `payment_types` (`id`);

--
-- Constraints for table `connection_terminate`
--
ALTER TABLE `connection_terminate`
  ADD CONSTRAINT `fk_connectionterminate_meterdetails_id` FOREIGN KEY (`meter_details_id`) REFERENCES `meter_details` (`id`);

--
-- Constraints for table `customer`
--
ALTER TABLE `customer`
  ADD CONSTRAINT `fk_customer_newproofmaster_id` FOREIGN KEY (`new_proof_master_id`) REFERENCES `id_proof_master` (`id`),
  ADD CONSTRAINT `fk_customer_newtariffcategory_id` FOREIGN KEY (`new_tariff_category_id`) REFERENCES `tariff_category_master` (`id`),
  ADD CONSTRAINT `fk_customer_oldpipesizemaster_id` FOREIGN KEY (`old_pipe_size_master_id`) REFERENCES `pipe_size_master` (`id`),
  ADD CONSTRAINT `fk_customer_oldtariffcategory_id` FOREIGN KEY (`old_tariff_category_id`) REFERENCES `tariff_category_master` (`id`),
  ADD CONSTRAINT `fk_customer_requestedpipesizemaster_id` FOREIGN KEY (`requested_pipe_size_master_id`) REFERENCES `pipe_size_master` (`id`);

--
-- Constraints for table `customer_complaints`
--
ALTER TABLE `customer_complaints`
  ADD CONSTRAINT `fk_customercomplaints_complainttypemaster_id` FOREIGN KEY (`complaint_type_master_id`) REFERENCES `complaint_type_master` (`id`);

--
-- Constraints for table `cust_details`
--
ALTER TABLE `cust_details`
  ADD CONSTRAINT `fk_custdetails_divisionmaster_id` FOREIGN KEY (`division_master_id`) REFERENCES `division_master` (`id`),
  ADD CONSTRAINT `fk_custdetails_meterdetails_id` FOREIGN KEY (`meter_details_id`) REFERENCES `meter_details` (`id`),
  ADD CONSTRAINT `fk_custdetails_pipesizemaster_id` FOREIGN KEY (`pipe_size_master_id`) REFERENCES `pipe_size_master` (`id`),
  ADD CONSTRAINT `fk_custdetails_streetmaster_id` FOREIGN KEY (`street_master_id`) REFERENCES `street_master` (`id`),
  ADD CONSTRAINT `fk_custdetails_tariffcategorymaster_id` FOREIGN KEY (`tariff_category_master_id`) REFERENCES `tariff_category_master` (`id`);

--
-- Constraints for table `cust_meter_mapping`
--
ALTER TABLE `cust_meter_mapping`
  ADD CONSTRAINT `fk_custmetermapping_custdetails_id` FOREIGN KEY (`cust_details_id`) REFERENCES `cust_details` (`id`),
  ADD CONSTRAINT `fk_custmetermapping_meterdetails_id` FOREIGN KEY (`meter_details_id`) REFERENCES `meter_details` (`id`);

--
-- Constraints for table `departments_hierarchy`
--
ALTER TABLE `departments_hierarchy`
  ADD CONSTRAINT `fk_departmentshierarchy_statusmaster_id` FOREIGN KEY (`status_master_id`) REFERENCES `status_master` (`id`);

--
-- Constraints for table `departments_master`
--
ALTER TABLE `departments_master`
  ADD CONSTRAINT `fk_departmentsmaster_departmentshierarchy_id` FOREIGN KEY (`departments_hierarchy_id`) REFERENCES `departments_hierarchy` (`id`),
  ADD CONSTRAINT `fk_departmentsmaster_departmenttypemaster_id` FOREIGN KEY (`department_type_master_id`) REFERENCES `department_type_master` (`id`),
  ADD CONSTRAINT `fk_departmentsmaster_statusmaster_id` FOREIGN KEY (`status_master_id`) REFERENCES `status_master` (`id`);

--
-- Constraints for table `department_type_master`
--
ALTER TABLE `department_type_master`
  ADD CONSTRAINT `fk_departmenttypemaster_statusmaster_id` FOREIGN KEY (`status_master_id`) REFERENCES `status_master` (`id`);

--
-- Constraints for table `designation_mappings`
--
ALTER TABLE `designation_mappings`
  ADD CONSTRAINT `fk_designationmappings_desigcategorymaster_id` FOREIGN KEY (`desig_category_master_id`) REFERENCES `desig_category_master` (`id`),
  ADD CONSTRAINT `fk_designationmappings_designationmaster_id` FOREIGN KEY (`designation_master_id`) REFERENCES `designation_master` (`id`),
  ADD CONSTRAINT `fk_designationmappings_groupmaster_id` FOREIGN KEY (`group_master_id`) REFERENCES `group_master` (`id`),
  ADD CONSTRAINT `fk_designationmappings_subdesigcategorymaster_id` FOREIGN KEY (`sub_desig_category_master_id`) REFERENCES `sub_desig_category_master` (`id`);

--
-- Constraints for table `designation_master`
--
ALTER TABLE `designation_master`
  ADD CONSTRAINT `fk_designationmaster_statusmaster_id` FOREIGN KEY (`status_master_id`) REFERENCES `status_master` (`id`);

--
-- Constraints for table `desig_category_master`
--
ALTER TABLE `desig_category_master`
  ADD CONSTRAINT `fk_desigcategorymaster_statusmaster_id` FOREIGN KEY (`status_master_id`) REFERENCES `status_master` (`id`);

--
-- Constraints for table `emp_master`
--
ALTER TABLE `emp_master`
  ADD CONSTRAINT `fk_empmaster_designationmaster_id` FOREIGN KEY (`designation_master_id`) REFERENCES `designation_master` (`id`),
  ADD CONSTRAINT `fk_empmaster_directorateid_id` FOREIGN KEY (`directorate_id_id`) REFERENCES `org_role_instance` (`id`),
  ADD CONSTRAINT `fk_empmaster_officeid_id` FOREIGN KEY (`office_id_id`) REFERENCES `org_role_instance` (`id`),
  ADD CONSTRAINT `fk_empmaster_reportingto_id` FOREIGN KEY (`reporting_to_id`) REFERENCES `designation_master` (`id`),
  ADD CONSTRAINT `fk_empmaster_statusmaster_id` FOREIGN KEY (`status_master_id`) REFERENCES `status_master` (`id`),
  ADD CONSTRAINT `fk_empmaster_user_id` FOREIGN KEY (`user_id`) REFERENCES `jhi_user` (`id`);

--
-- Constraints for table `emp_role_mapping`
--
ALTER TABLE `emp_role_mapping`
  ADD CONSTRAINT `fk_emprolemapping_orgroleinstance_id` FOREIGN KEY (`org_role_instance_id`) REFERENCES `org_role_instance` (`id`),
  ADD CONSTRAINT `fk_emprolemapping_parentuser_id` FOREIGN KEY (`parent_user_id`) REFERENCES `jhi_user` (`id`),
  ADD CONSTRAINT `fk_emprolemapping_statusmaster_id` FOREIGN KEY (`status_master_id`) REFERENCES `status_master` (`id`),
  ADD CONSTRAINT `fk_emprolemapping_user_id` FOREIGN KEY (`user_id`) REFERENCES `jhi_user` (`id`);

--
-- Constraints for table `expense_details`
--
ALTER TABLE `expense_details`
  ADD CONSTRAINT `fk_expensedetails_bankmaster_id` FOREIGN KEY (`bank_master_id`) REFERENCES `bank_master` (`id`),
  ADD CONSTRAINT `fk_expensedetails_collectiontypemaster_id` FOREIGN KEY (`collection_type_master_id`) REFERENCES `collection_type_master` (`id`),
  ADD CONSTRAINT `fk_expensedetails_paymenttypes_id` FOREIGN KEY (`payment_types_id`) REFERENCES `payment_types` (`id`);

--
-- Constraints for table `feasibility_study`
--
ALTER TABLE `feasibility_study`
  ADD CONSTRAINT `fk_feasibilitystudy_applicationtxn_id` FOREIGN KEY (`application_txn_id`) REFERENCES `application_txn` (`id`),
  ADD CONSTRAINT `fk_feasibilitystudy_approvedbyoperationmanager_id` FOREIGN KEY (`approved_by_operation_manager_id`) REFERENCES `jhi_user` (`id`),
  ADD CONSTRAINT `fk_feasibilitystudy_approvedbyzonalhead_id` FOREIGN KEY (`approved_by_zonal_head_id`) REFERENCES `jhi_user` (`id`),
  ADD CONSTRAINT `fk_feasibilitystudy_categorymaster_id` FOREIGN KEY (`category_master_id`) REFERENCES `category_master` (`id`),
  ADD CONSTRAINT `fk_feasibilitystudy_divisionmaster_id` FOREIGN KEY (`division_master_id`) REFERENCES `division_master` (`id`),
  ADD CONSTRAINT `fk_feasibilitystudy_inspectionbydepartmenthead_id` FOREIGN KEY (`inspection_by_department_head_id`) REFERENCES `jhi_user` (`id`),
  ADD CONSTRAINT `fk_feasibilitystudy_preparedby_id` FOREIGN KEY (`prepared_by_id`) REFERENCES `jhi_user` (`id`),
  ADD CONSTRAINT `fk_feasibilitystudy_streetmaster_id` FOREIGN KEY (`street_master_id`) REFERENCES `street_master` (`id`),
  ADD CONSTRAINT `fk_feasibilitystudy_zonemaster_id` FOREIGN KEY (`zone_master_id`) REFERENCES `zone_master` (`id`);

--
-- Constraints for table `group_master`
--
ALTER TABLE `group_master`
  ADD CONSTRAINT `fk_groupmaster_statusmaster_id` FOREIGN KEY (`status_master_id`) REFERENCES `status_master` (`id`);

--
-- Constraints for table `hydrant_complaint`
--
ALTER TABLE `hydrant_complaint`
  ADD CONSTRAINT `fk_hydrantcomplaint_waterleakagecomplaint_id` FOREIGN KEY (`water_leakage_complaint_id`) REFERENCES `water_leakage_complaint` (`id`);

--
-- Constraints for table `invoice_payments`
--
ALTER TABLE `invoice_payments`
  ADD CONSTRAINT `fk_invoicepayments_billfulldetails_id` FOREIGN KEY (`bill_full_details_id`) REFERENCES `bill_full_details` (`id`),
  ADD CONSTRAINT `fk_invoicepayments_colldetails_id` FOREIGN KEY (`coll_details_id`) REFERENCES `coll_details` (`id`),
  ADD CONSTRAINT `fk_invoicepayments_custdetails_id` FOREIGN KEY (`cust_details_id`) REFERENCES `cust_details` (`id`);

--
-- Constraints for table `item_code_master`
--
ALTER TABLE `item_code_master`
  ADD CONSTRAINT `fk_itemcodemaster_itemcategorymaster_id` FOREIGN KEY (`item_category_master_id`) REFERENCES `item_category_master` (`id`),
  ADD CONSTRAINT `fk_itemcodemaster_itemsubcategorymaster_id` FOREIGN KEY (`item_sub_category_master_id`) REFERENCES `item_sub_category_master` (`id`);

--
-- Constraints for table `item_required`
--
ALTER TABLE `item_required`
  ADD CONSTRAINT `fk_itemrequired_applicationtxn_id` FOREIGN KEY (`application_txn_id`) REFERENCES `application_txn` (`id`),
  ADD CONSTRAINT `fk_itemrequired_feasibilitystudy_id` FOREIGN KEY (`feasibility_study_id`) REFERENCES `feasibility_study` (`id`),
  ADD CONSTRAINT `fk_itemrequired_materialmaster_id` FOREIGN KEY (`material_master_id`) REFERENCES `material_master` (`id`),
  ADD CONSTRAINT `fk_itemrequired_proceedings_id` FOREIGN KEY (`proceedings_id`) REFERENCES `proceedings` (`id`),
  ADD CONSTRAINT `fk_itemrequired_uom_id` FOREIGN KEY (`uom_id`) REFERENCES `uom` (`id`);

--
-- Constraints for table `item_sub_category_master`
--
ALTER TABLE `item_sub_category_master`
  ADD CONSTRAINT `fk_itemsubcategorymaster_itemcategorymaster_id` FOREIGN KEY (`item_category_master_id`) REFERENCES `item_category_master` (`id`);

--
-- Constraints for table `jhi_persistent_audit_evt_data`
--
ALTER TABLE `jhi_persistent_audit_evt_data`
  ADD CONSTRAINT `fk_evt_pers_audit_evt_data` FOREIGN KEY (`event_id`) REFERENCES `jhi_persistent_audit_event` (`event_id`);

--
-- Constraints for table `jhi_persistent_token`
--
ALTER TABLE `jhi_persistent_token`
  ADD CONSTRAINT `fk_user_persistent_token` FOREIGN KEY (`user_id`) REFERENCES `jhi_user` (`id`);

--
-- Constraints for table `jhi_user_authority`
--
ALTER TABLE `jhi_user_authority`
  ADD CONSTRAINT `fk_authority_name` FOREIGN KEY (`authority_name`) REFERENCES `jhi_authority` (`name`),
  ADD CONSTRAINT `fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `jhi_user` (`id`);

--
-- Constraints for table `job_card_item_requirement`
--
ALTER TABLE `job_card_item_requirement`
  ADD CONSTRAINT `fk_jobcarditemrequirement_materialmaster_id` FOREIGN KEY (`material_master_id`) REFERENCES `material_master` (`id`),
  ADD CONSTRAINT `fk_jobcarditemrequirement_uom_id` FOREIGN KEY (`uom_id`) REFERENCES `uom` (`id`),
  ADD CONSTRAINT `fk_jobcarditemrequirement_waterleakagecomplaint_id` FOREIGN KEY (`water_leakage_complaint_id`) REFERENCES `water_leakage_complaint` (`id`);

--
-- Constraints for table `job_card_site_status`
--
ALTER TABLE `job_card_site_status`
  ADD CONSTRAINT `fk_jobcardsitestatus_waterleakagecomplaint_id` FOREIGN KEY (`water_leakage_complaint_id`) REFERENCES `water_leakage_complaint` (`id`);

--
-- Constraints for table `manage_cash_point`
--
ALTER TABLE `manage_cash_point`
  ADD CONSTRAINT `fk_managecashpoint_cashbookmaster_id` FOREIGN KEY (`cash_book_master_id`) REFERENCES `cash_book_master` (`id`),
  ADD CONSTRAINT `fk_managecashpoint_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`),
  ADD CONSTRAINT `fk_managecashpoint_filenumber_id` FOREIGN KEY (`file_number_id`) REFERENCES `file_number` (`id`),
  ADD CONSTRAINT `fk_managecashpoint_paymenttypes_id` FOREIGN KEY (`payment_types_id`) REFERENCES `payment_types` (`id`),
  ADD CONSTRAINT `fk_managecashpoint_transactiontypemaster_id` FOREIGN KEY (`transaction_type_master_id`) REFERENCES `transaction_type_master` (`id`);

--
-- Constraints for table `menu_item2_url`
--
ALTER TABLE `menu_item2_url`
  ADD CONSTRAINT `fk_menuitem2url_menuitem_id` FOREIGN KEY (`menu_item_id`) REFERENCES `menu_item` (`id`),
  ADD CONSTRAINT `fk_menuitem2url_url_id` FOREIGN KEY (`url_id`) REFERENCES `url` (`id`);

--
-- Constraints for table `meter_change`
--
ALTER TABLE `meter_change`
  ADD CONSTRAINT `fk_meterchange_billfulldetails_id` FOREIGN KEY (`bill_full_details_id`) REFERENCES `bill_full_details` (`id`),
  ADD CONSTRAINT `fk_meterchange_custdetails_id` FOREIGN KEY (`cust_details_id`) REFERENCES `cust_details` (`id`),
  ADD CONSTRAINT `fk_meterchange_newmeterno_id` FOREIGN KEY (`new_meter_no_id`) REFERENCES `meter_details` (`id`),
  ADD CONSTRAINT `fk_meterchange_prevmeterno_id` FOREIGN KEY (`prev_meter_no_id`) REFERENCES `meter_details` (`id`),
  ADD CONSTRAINT `fk_meterchange_user_id` FOREIGN KEY (`user_id`) REFERENCES `jhi_user` (`id`);

--
-- Constraints for table `meter_details`
--
ALTER TABLE `meter_details`
  ADD CONSTRAINT `fk_meterdetails_meterstatus_id` FOREIGN KEY (`meter_status_id`) REFERENCES `meter_status` (`id`),
  ADD CONSTRAINT `fk_meterdetails_pipesizemaster_id` FOREIGN KEY (`pipe_size_master_id`) REFERENCES `pipe_size_master` (`id`);

--
-- Constraints for table `module2_menu_item`
--
ALTER TABLE `module2_menu_item`
  ADD CONSTRAINT `fk_module2menuitem_menuitem_id` FOREIGN KEY (`menu_item_id`) REFERENCES `menu_item` (`id`),
  ADD CONSTRAINT `fk_module2menuitem_module_id` FOREIGN KEY (`module_id`) REFERENCES `module` (`id`);

--
-- Constraints for table `online_payment_callback`
--
ALTER TABLE `online_payment_callback`
  ADD CONSTRAINT `fk_onlinepaymentcallback_merchantmaster_id` FOREIGN KEY (`merchant_master_id`) REFERENCES `merchant_master` (`id`),
  ADD CONSTRAINT `fk_onlinepaymentcallback_onlinepaymentorder_id` FOREIGN KEY (`online_payment_order_id`) REFERENCES `online_payment_order` (`id`);

--
-- Constraints for table `online_payment_order`
--
ALTER TABLE `online_payment_order`
  ADD CONSTRAINT `fk_onlinepaymentorder_merchantmaster_id` FOREIGN KEY (`merchant_master_id`) REFERENCES `merchant_master` (`id`);

--
-- Constraints for table `online_payment_response`
--
ALTER TABLE `online_payment_response`
  ADD CONSTRAINT `fk_onlinepaymentresponse_onlinepaymentorder_id` FOREIGN KEY (`online_payment_order_id`) REFERENCES `online_payment_order` (`id`);

--
-- Constraints for table `org_hierarchy`
--
ALTER TABLE `org_hierarchy`
  ADD CONSTRAINT `fk_orghierarchy_statusmaster_id` FOREIGN KEY (`status_master_id`) REFERENCES `status_master` (`id`);

--
-- Constraints for table `org_roles_master`
--
ALTER TABLE `org_roles_master`
  ADD CONSTRAINT `fk_orgrolesmaster_statusmaster_id` FOREIGN KEY (`status_master_id`) REFERENCES `status_master` (`id`);

--
-- Constraints for table `org_role_hierarchy`
--
ALTER TABLE `org_role_hierarchy`
  ADD CONSTRAINT `fk_orgrolehierarchy_statusmaster_id` FOREIGN KEY (`status_master_id`) REFERENCES `status_master` (`id`);

--
-- Constraints for table `org_role_instance`
--
ALTER TABLE `org_role_instance`
  ADD CONSTRAINT `fk_orgroleinstance_departmentsmaster_id` FOREIGN KEY (`departments_master_id`) REFERENCES `departments_master` (`id`),
  ADD CONSTRAINT `fk_orgroleinstance_orgrolehierarchy_id` FOREIGN KEY (`org_role_hierarchy_id`) REFERENCES `org_role_hierarchy` (`id`),
  ADD CONSTRAINT `fk_orgroleinstance_statusmaster_id` FOREIGN KEY (`status_master_id`) REFERENCES `status_master` (`id`);

--
-- Constraints for table `proceedings`
--
ALTER TABLE `proceedings`
  ADD CONSTRAINT `fk_proceedings_applicationtxn_id` FOREIGN KEY (`application_txn_id`) REFERENCES `application_txn` (`id`),
  ADD CONSTRAINT `fk_proceedings_pipesizemaster_id` FOREIGN KEY (`pipe_size_master_id`) REFERENCES `pipe_size_master` (`id`);

--
-- Constraints for table `receipt`
--
ALTER TABLE `receipt`
  ADD CONSTRAINT `fk_receipt_applicationtxn_id` FOREIGN KEY (`application_txn_id`) REFERENCES `application_txn` (`id`),
  ADD CONSTRAINT `fk_receipt_paymenttypes_id` FOREIGN KEY (`payment_types_id`) REFERENCES `payment_types` (`id`);

--
-- Constraints for table `request_master`
--
ALTER TABLE `request_master`
  ADD CONSTRAINT `fk_requestmaster_module_id` FOREIGN KEY (`module_id`) REFERENCES `module` (`id`),
  ADD CONSTRAINT `fk_requestmaster_statusmaster_id` FOREIGN KEY (`status_master_id`) REFERENCES `status_master` (`id`);

--
-- Constraints for table `request_workflow_history`
--
ALTER TABLE `request_workflow_history`
  ADD CONSTRAINT `fk_requestworkflowhistory_appliedby_id` FOREIGN KEY (`applied_by_id`) REFERENCES `jhi_user` (`id`),
  ADD CONSTRAINT `fk_requestworkflowhistory_assignedfrom_id` FOREIGN KEY (`assigned_from_id`) REFERENCES `jhi_user` (`id`),
  ADD CONSTRAINT `fk_requestworkflowhistory_assignedto_id` FOREIGN KEY (`assigned_to_id`) REFERENCES `jhi_user` (`id`),
  ADD CONSTRAINT `fk_requestworkflowhistory_requestmaster_id` FOREIGN KEY (`request_master_id`) REFERENCES `request_master` (`id`),
  ADD CONSTRAINT `fk_requestworkflowhistory_statusmaster_id` FOREIGN KEY (`status_master_id`) REFERENCES `status_master` (`id`),
  ADD CONSTRAINT `fk_requestworkflowhistory_workflowmaster_id` FOREIGN KEY (`workflow_master_id`) REFERENCES `workflow_master` (`id`),
  ADD CONSTRAINT `fk_requestworkflowhistory_workflowstagemaster_id` FOREIGN KEY (`workflow_stage_master_id`) REFERENCES `workflow_stage_master` (`id`);

--
-- Constraints for table `request_workflow_mapping`
--
ALTER TABLE `request_workflow_mapping`
  ADD CONSTRAINT `fk_requestworkflowmapping_requestmaster_id` FOREIGN KEY (`request_master_id`) REFERENCES `request_master` (`id`),
  ADD CONSTRAINT `fk_requestworkflowmapping_statusmaster_id` FOREIGN KEY (`status_master_id`) REFERENCES `status_master` (`id`),
  ADD CONSTRAINT `fk_requestworkflowmapping_workflowmaster_id` FOREIGN KEY (`workflow_master_id`) REFERENCES `workflow_master` (`id`);

--
-- Constraints for table `req_desig_workflow_mapping`
--
ALTER TABLE `req_desig_workflow_mapping`
  ADD CONSTRAINT `fk_reqdesigworkflowmapping_designationmaster_id` FOREIGN KEY (`designation_master_id`) REFERENCES `designation_master` (`id`),
  ADD CONSTRAINT `fk_reqdesigworkflowmapping_requestmaster_id` FOREIGN KEY (`request_master_id`) REFERENCES `request_master` (`id`),
  ADD CONSTRAINT `fk_reqdesigworkflowmapping_statusmaster_id` FOREIGN KEY (`status_master_id`) REFERENCES `status_master` (`id`),
  ADD CONSTRAINT `fk_reqdesigworkflowmapping_workflowmaster_id` FOREIGN KEY (`workflow_master_id`) REFERENCES `workflow_master` (`id`);

--
-- Constraints for table `req_org_workflow_mapping`
--
ALTER TABLE `req_org_workflow_mapping`
  ADD CONSTRAINT `fk_reqorgworkflowmapping_orgroleinstance_id` FOREIGN KEY (`org_role_instance_id`) REFERENCES `org_role_instance` (`id`),
  ADD CONSTRAINT `fk_reqorgworkflowmapping_requestmaster_id` FOREIGN KEY (`request_master_id`) REFERENCES `request_master` (`id`),
  ADD CONSTRAINT `fk_reqorgworkflowmapping_statusmaster_id` FOREIGN KEY (`status_master_id`) REFERENCES `status_master` (`id`),
  ADD CONSTRAINT `fk_reqorgworkflowmapping_workflowmaster_id` FOREIGN KEY (`workflow_master_id`) REFERENCES `workflow_master` (`id`);

--
-- Constraints for table `reversal_details`
--
ALTER TABLE `reversal_details`
  ADD CONSTRAINT `fk_reversaldetails_colldetails_id` FOREIGN KEY (`coll_details_id`) REFERENCES `coll_details` (`id`),
  ADD CONSTRAINT `fk_reversaldetails_user_id` FOREIGN KEY (`user_id`) REFERENCES `jhi_user` (`id`);

--
-- Constraints for table `re_allotment`
--
ALTER TABLE `re_allotment`
  ADD CONSTRAINT `fk_reallotment_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`),
  ADD CONSTRAINT `fk_reallotment_feasibilitystatus_id` FOREIGN KEY (`feasibility_status_id`) REFERENCES `feasibility_status` (`id`),
  ADD CONSTRAINT `fk_reallotment_filenumber_id` FOREIGN KEY (`file_number_id`) REFERENCES `file_number` (`id`);

--
-- Constraints for table `role_workflow_mapping`
--
ALTER TABLE `role_workflow_mapping`
  ADD CONSTRAINT `fk_roleworkflowmapping_orgroleinstance_id` FOREIGN KEY (`org_role_instance_id`) REFERENCES `org_role_instance` (`id`),
  ADD CONSTRAINT `fk_roleworkflowmapping_requestmaster_id` FOREIGN KEY (`request_master_id`) REFERENCES `request_master` (`id`),
  ADD CONSTRAINT `fk_roleworkflowmapping_statusmaster_id` FOREIGN KEY (`status_master_id`) REFERENCES `status_master` (`id`),
  ADD CONSTRAINT `fk_roleworkflowmapping_workflowmaster_id` FOREIGN KEY (`workflow_master_id`) REFERENCES `workflow_master` (`id`);

--
-- Constraints for table `street_master`
--
ALTER TABLE `street_master`
  ADD CONSTRAINT `fk_streetmaster_divisionmaster_id` FOREIGN KEY (`division_master_id`) REFERENCES `division_master` (`id`);

--
-- Constraints for table `sub_desig_category_master`
--
ALTER TABLE `sub_desig_category_master`
  ADD CONSTRAINT `fk_subdesigcategorymaster_statusmaster_id` FOREIGN KEY (`status_master_id`) REFERENCES `status_master` (`id`);

--
-- Constraints for table `tariff_charges`
--
ALTER TABLE `tariff_charges`
  ADD CONSTRAINT `fk_tariffcharges_tariffmaster_id` FOREIGN KEY (`tariff_master_id`) REFERENCES `tariff_master` (`id`),
  ADD CONSTRAINT `fk_tariffcharges_tarifftypemaster_id` FOREIGN KEY (`tariff_type_master_id`) REFERENCES `tariff_type_master` (`id`);

--
-- Constraints for table `tariff_master`
--
ALTER TABLE `tariff_master`
  ADD CONSTRAINT `fk_tariffmaster_tariffcategorymaster_id` FOREIGN KEY (`tariff_category_master_id`) REFERENCES `tariff_category_master` (`id`);

--
-- Constraints for table `url2_role`
--
ALTER TABLE `url2_role`
  ADD CONSTRAINT `fk_url2role_authority_name` FOREIGN KEY (`authority_name`) REFERENCES `jhi_authority` (`name`),
  ADD CONSTRAINT `fk_url2role_url_id` FOREIGN KEY (`url_id`) REFERENCES `url` (`id`);

--
-- Constraints for table `valve_complaint`
--
ALTER TABLE `valve_complaint`
  ADD CONSTRAINT `fk_valvecomplaint_waterleakagecomplaint_id` FOREIGN KEY (`water_leakage_complaint_id`) REFERENCES `water_leakage_complaint` (`id`);

--
-- Constraints for table `water_leakage_complaint`
--
ALTER TABLE `water_leakage_complaint`
  ADD CONSTRAINT `fk_waterleakagecomplaint_divisionmaster_id` FOREIGN KEY (`division_master_id`) REFERENCES `division_master` (`id`),
  ADD CONSTRAINT `fk_waterleakagecomplaint_streetmaster_id` FOREIGN KEY (`street_master_id`) REFERENCES `street_master` (`id`);

--
-- Constraints for table `workflow`
--
ALTER TABLE `workflow`
  ADD CONSTRAINT `fk_workflow_absoluteescalationto_id` FOREIGN KEY (`absolute_escalation_to_id`) REFERENCES `org_role_instance` (`id`),
  ADD CONSTRAINT `fk_workflow_absolutefromrole_id` FOREIGN KEY (`absolute_from_role_id`) REFERENCES `org_role_instance` (`id`),
  ADD CONSTRAINT `fk_workflow_absolutetorole_id` FOREIGN KEY (`absolute_to_role_id`) REFERENCES `org_role_instance` (`id`),
  ADD CONSTRAINT `fk_workflow_escalationrelationshiptype_id` FOREIGN KEY (`escalation_relationship_type_id`) REFERENCES `workflow_relationships` (`id`),
  ADD CONSTRAINT `fk_workflow_relationshiptype_id` FOREIGN KEY (`relationship_type_id`) REFERENCES `workflow_relationships` (`id`),
  ADD CONSTRAINT `fk_workflow_relativeescalationto_id` FOREIGN KEY (`relative_escalation_to_id`) REFERENCES `workflow_relations` (`id`),
  ADD CONSTRAINT `fk_workflow_relativefromrole_id` FOREIGN KEY (`relative_from_role_id`) REFERENCES `workflow_relations` (`id`),
  ADD CONSTRAINT `fk_workflow_relativetorole_id` FOREIGN KEY (`relative_to_role_id`) REFERENCES `workflow_relations` (`id`),
  ADD CONSTRAINT `fk_workflow_workflowmaster_id` FOREIGN KEY (`workflow_master_id`) REFERENCES `workflow_master` (`id`),
  ADD CONSTRAINT `fk_workflow_workflowstagemaster_id` FOREIGN KEY (`workflow_stage_master_id`) REFERENCES `workflow_stage_master` (`id`);

--
-- Constraints for table `workflow_master`
--
ALTER TABLE `workflow_master`
  ADD CONSTRAINT `fk_workflowmaster_statusmaster_id` FOREIGN KEY (`status_master_id`) REFERENCES `status_master` (`id`);

--
-- Constraints for table `workflow_relations`
--
ALTER TABLE `workflow_relations`
  ADD CONSTRAINT `fk_workflowrelations_statusmaster_id` FOREIGN KEY (`status_master_id`) REFERENCES `status_master` (`id`);

--
-- Constraints for table `workflow_relationships`
--
ALTER TABLE `workflow_relationships`
  ADD CONSTRAINT `fk_workflowrelationships_statusmaster_id` FOREIGN KEY (`status_master_id`) REFERENCES `status_master` (`id`);

--
-- Constraints for table `workflow_stage_master`
--
ALTER TABLE `workflow_stage_master`
  ADD CONSTRAINT `fk_workflowstagemaster_statusmaster_id` FOREIGN KEY (`status_master_id`) REFERENCES `status_master` (`id`);

--
-- Constraints for table `workflow_txn_details`
--
ALTER TABLE `workflow_txn_details`
  ADD CONSTRAINT `fk_workflowtxndetails_requestmaster_id` FOREIGN KEY (`request_master_id`) REFERENCES `request_master` (`id`);

--
-- Constraints for table `workflow_type_master`
--
ALTER TABLE `workflow_type_master`
  ADD CONSTRAINT `fk_workflowtypemaster_statusmaster_id` FOREIGN KEY (`status_master_id`) REFERENCES `status_master` (`id`);

--
-- Constraints for table `zone_master`
--
ALTER TABLE `zone_master`
  ADD CONSTRAINT `fk_zonemaster_divisionmaster_id` FOREIGN KEY (`division_master_id`) REFERENCES `division_master` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
