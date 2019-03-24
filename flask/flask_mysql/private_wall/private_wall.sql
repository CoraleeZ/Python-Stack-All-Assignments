CREATE DATABASE  IF NOT EXISTS `private_wall` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `private_wall`;
-- MySQL dump 10.13  Distrib 8.0.14, for Win64 (x86_64)
--
-- Host: localhost    Database: private_wall
-- ------------------------------------------------------
-- Server version	8.0.14

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `commet` varchar(255) DEFAULT NULL,
  `creat_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `info_receiver_id` int(11) NOT NULL,
  `info_creator_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_comments_infos_idx` (`info_receiver_id`),
  KEY `fk_comments_infos1_idx` (`info_creator_id`),
  CONSTRAINT `fk_comments_infos` FOREIGN KEY (`info_receiver_id`) REFERENCES `infos` (`id`),
  CONSTRAINT `fk_comments_infos1` FOREIGN KEY (`info_creator_id`) REFERENCES `infos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (20,'hi, lili','2019-02-12 18:40:01',3,4),(21,'hi, lili','2019-02-12 18:40:51',3,5),(22,'hi,jia','2019-02-12 18:42:20',2,5),(23,'hi,jia','2019-02-12 18:42:26',4,5),(24,'hi,jia','2019-02-12 18:42:51',2,3),(25,'hi, jia I;m lili','2019-02-12 18:42:54',5,3),(26,'hi, lili','2019-02-12 18:42:58',4,3);
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `infos`
--

DROP TABLE IF EXISTS `infos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `infos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `creat_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `update_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `infos`
--

LOCK TABLES `infos` WRITE;
/*!40000 ALTER TABLE `infos` DISABLE KEYS */;
INSERT INTO `infos` VALUES (2,'jia','hao','hellojh@gmail.com','$2b$12$iF8EVeysX5sP9A9w3zNrfeFZpjYhwMrVFMXm8xd7GFDqRXRvocIrq','2019-02-12 16:25:02','2019-02-12 16:25:02'),(3,'lili','li','hellolili@gmail.com','$2b$12$G8F84JiSSXlwTMnUpIwD3uRj9dDaMPXY8CqNKLcalUqzshcLt/96m','2019-02-12 16:48:45','2019-02-12 16:48:45'),(4,'wawa','wa','hellowawa@gmail.com','$2b$12$xq0xCOnyA8BmESREibe9oe/I4P8wr2huZ.zkIF8S28ZAuaFmsbgu2','2019-02-12 16:57:46','2019-02-12 16:57:46'),(5,'nuonuo','nuo','hellonuonuo@gmail.com','$2b$12$xgXJ8jv9D/cf0KH2psHfgeZ0MpV6ZAneC5WRJx98bJj24FggQHxFe','2019-02-12 18:38:03','2019-02-12 18:38:03'),(6,'mumu','mu','hellomumu@gmail.com','$2b$12$kHGLxvEigsziediYCZVJ2.AnR/C8l99XxiZGngGtN6gXHZyw7KD5C','2019-02-12 18:46:37','2019-02-12 18:46:37');
/*!40000 ALTER TABLE `infos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-02-12 19:30:34
