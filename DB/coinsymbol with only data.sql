-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: localhost    Database: crypto-currency
-- ------------------------------------------------------
-- Server version	8.0.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin_app_coinsymbol`
--

DROP TABLE IF EXISTS `admin_app_coinsymbol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin_app_coinsymbol` (
  `c_id` int(11) NOT NULL AUTO_INCREMENT,
  `c_name` varchar(255) DEFAULT NULL,
  `c_symbol` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`c_id`),
  UNIQUE KEY `c_name` (`c_name`),
  UNIQUE KEY `c_symbol` (`c_symbol`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_app_coinsymbol`
--

LOCK TABLES `admin_app_coinsymbol` WRITE;
/*!40000 ALTER TABLE `admin_app_coinsymbol` DISABLE KEYS */;
INSERT INTO `admin_app_coinsymbol` VALUES (1,'Bitcoin','btc'),(2,'Ethereum','eth'),(3,'XRP','xrp'),(4,'Tether','usdt'),(5,'Bitcoin Cash','bch'),(6,'Litecoin','ltc'),(7,'Bitcoin SV','bsv'),(8,'EOS','eos'),(9,'Binance Coin','bnb'),(10,'OKB','okb'),(11,'Tezos','xtz'),(12,'LEOcoin','leo'),(13,'Cardano','ada'),(14,'Stellar','xlm'),(15,'ChainLink','link'),(16,'Huobi Token','ht'),(17,'TRON','trx'),(18,'Monero','xmr'),(19,'USD Coin','usdc'),(20,'Ethereum Classic','etc'),(21,'Qtum','qtum'),(22,'Dash','dash'),(23,'NEO','neo'),(24,'Ontology','ont'),(25,'IOTA','miota');
/*!40000 ALTER TABLE `admin_app_coinsymbol` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-17 18:58:47
