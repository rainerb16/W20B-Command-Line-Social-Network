-- MySQL dump 10.13  Distrib 8.0.21, for macos10.15 (x86_64)
--
-- Host: 35.194.31.51    Database: Hacker_Net
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.15-MariaDB-1:10.4.15+maria~stretch

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `exploits`
--

DROP TABLE IF EXISTS `exploits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exploits` (
  `content` text NOT NULL,
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `exploits_FK` (`user_id`),
  CONSTRAINT `exploits_FK` FOREIGN KEY (`user_id`) REFERENCES `hackers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exploits`
--

LOCK TABLES `exploits` WRITE;
/*!40000 ALTER TABLE `exploits` DISABLE KEYS */;
INSERT INTO `exploits` VALUES ('Updating this exploit!',3,2),('apparently you don\'t know how to code',4,1),('~THE~ DIAGRAM',5,1),('BRUH do you even SQL??',6,3),('Wear Black, Listen to Techno',7,4);
/*!40000 ALTER TABLE `exploits` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hackers`
--

DROP TABLE IF EXISTS `hackers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hackers` (
  `alias` varchar(40) NOT NULL,
  `password` varchar(100) NOT NULL,
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hackers_UN` (`alias`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hackers`
--

LOCK TABLES `hackers` WRITE;
/*!40000 ALTER TABLE `hackers` DISABLE KEYS */;
INSERT INTO `hackers` VALUES ('Alex_Hacker','perfect!',1),('Rainer','techno123',2),('Bob','doyousql?',3),('Kloves','techno',4);
/*!40000 ALTER TABLE `hackers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'Hacker_Net'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-07  9:43:30
