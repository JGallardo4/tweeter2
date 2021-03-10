-- MariaDB dump 10.18  Distrib 10.5.8-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: Tweeter2V1
-- ------------------------------------------------------
-- Server version	10.5.8-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Comment_Likes`
--

DROP TABLE IF EXISTS `Comment_Likes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Comment_Likes` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `User_Id` int(11) NOT NULL,
  `Comment_Id` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `Unique_Like` (`User_Id`,`Comment_Id`),
  KEY `FK_Users__Comment_Likes` (`User_Id`),
  KEY `FK_Comments__Comment_Likes` (`Comment_Id`),
  CONSTRAINT `FK_Comments__Comment_Likes` FOREIGN KEY (`Comment_Id`) REFERENCES `Comments` (`Id`) ON DELETE CASCADE,
  CONSTRAINT `FK_Users__Comment_Likes` FOREIGN KEY (`User_Id`) REFERENCES `Users` (`Id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Comment_Likes`
--

LOCK TABLES `Comment_Likes` WRITE;
/*!40000 ALTER TABLE `Comment_Likes` DISABLE KEYS */;
/*!40000 ALTER TABLE `Comment_Likes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Comments`
--

DROP TABLE IF EXISTS `Comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Comments` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Tweet_Id` int(11) NOT NULL,
  `User_Id` int(11) NOT NULL,
  `Content` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Created_At` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `FK_Users__Comments` (`User_Id`),
  KEY `FK_Tweets__Comments` (`Tweet_Id`),
  CONSTRAINT `FK_Tweets__Comments` FOREIGN KEY (`Tweet_Id`) REFERENCES `Tweets` (`Id`) ON DELETE CASCADE,
  CONSTRAINT `FK_Users__Comments` FOREIGN KEY (`User_Id`) REFERENCES `Users` (`Id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Comments`
--

LOCK TABLES `Comments` WRITE;
/*!40000 ALTER TABLE `Comments` DISABLE KEYS */;
INSERT INTO `Comments` VALUES (4,22,6,'my new comment heyo!','2021-03-03 09:24:49'),(7,22,4,'hi there','2021-03-03 16:17:02');
/*!40000 ALTER TABLE `Comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Followings`
--

DROP TABLE IF EXISTS `Followings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Followings` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Follower_Id` int(11) NOT NULL,
  `Followed_Id` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `Follow_Relationship` (`Follower_Id`,`Followed_Id`),
  KEY `FK_Users__Followings_Follower` (`Follower_Id`),
  KEY `FK_Users__Followings_Followed` (`Followed_Id`),
  CONSTRAINT `FK_Users__Followings_Followed` FOREIGN KEY (`Followed_Id`) REFERENCES `Users` (`Id`) ON DELETE CASCADE,
  CONSTRAINT `FK_Users__Followings_Follower` FOREIGN KEY (`Follower_Id`) REFERENCES `Users` (`Id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Followings`
--

LOCK TABLES `Followings` WRITE;
/*!40000 ALTER TABLE `Followings` DISABLE KEYS */;
INSERT INTO `Followings` VALUES (10,4,2),(3,4,6),(2,6,2),(1,6,4),(11,7,4);
/*!40000 ALTER TABLE `Followings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Tweet_Likes`
--

DROP TABLE IF EXISTS `Tweet_Likes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Tweet_Likes` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `User_Id` int(11) NOT NULL,
  `Tweet_Id` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `Unique_Like` (`User_Id`,`Tweet_Id`),
  KEY `FK_Users__Tweet_Likes` (`User_Id`),
  KEY `FK_Tweets__Tweet_Likes` (`Tweet_Id`),
  CONSTRAINT `FK_Tweets__Tweet_Likes` FOREIGN KEY (`Tweet_Id`) REFERENCES `Tweets` (`Id`) ON DELETE CASCADE,
  CONSTRAINT `FK_Users__Tweet_Likes` FOREIGN KEY (`User_Id`) REFERENCES `Users` (`Id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tweet_Likes`
--

LOCK TABLES `Tweet_Likes` WRITE;
/*!40000 ALTER TABLE `Tweet_Likes` DISABLE KEYS */;
INSERT INTO `Tweet_Likes` VALUES (10,4,27),(5,6,26),(4,6,27),(15,7,22);
/*!40000 ALTER TABLE `Tweet_Likes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Tweets`
--

DROP TABLE IF EXISTS `Tweets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Tweets` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `User_Id` int(11) NOT NULL,
  `Content` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Created_At` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `FK_Users__Posts` (`User_Id`),
  CONSTRAINT `FK_Users__Posts` FOREIGN KEY (`User_Id`) REFERENCES `Users` (`Id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tweets`
--

LOCK TABLES `Tweets` WRITE;
/*!40000 ALTER TABLE `Tweets` DISABLE KEYS */;
INSERT INTO `Tweets` VALUES (22,4,'my new tweet!','2021-03-03 02:23:45'),(26,6,'my new tweet heyo!','2021-03-02 21:12:34'),(27,6,'my new tweet heyo!','2021-03-02 21:19:28'),(28,4,'Brand new tweet','2021-03-03 16:17:39'),(29,2,'Joe\'s tweet!','2021-03-04 00:46:27'),(30,4,'It\'s a new day!','2021-03-04 16:22:33'),(31,7,'I had a little lamb','2021-03-04 16:37:23');
/*!40000 ALTER TABLE `Tweets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User_Sessions`
--

DROP TABLE IF EXISTS `User_Sessions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User_Sessions` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `User_Id` int(11) NOT NULL,
  `Login_Token` varchar(110) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `User_Id` (`User_Id`),
  KEY `FK_Users__User_Sessions` (`User_Id`),
  CONSTRAINT `FK_Users__User_Sessions` FOREIGN KEY (`User_Id`) REFERENCES `Users` (`Id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=84 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User_Sessions`
--

LOCK TABLES `User_Sessions` WRITE;
/*!40000 ALTER TABLE `User_Sessions` DISABLE KEYS */;
INSERT INTO `User_Sessions` VALUES (61,6,NULL),(70,2,NULL),(75,7,NULL),(82,4,NULL);
/*!40000 ALTER TABLE `User_Sessions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Users` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Email` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Username` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Bio` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Birthdate` datetime DEFAULT NULL,
  `Password` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `Email` (`Email`),
  UNIQUE KEY `Username` (`Username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES (2,'joe@email.com','Joe','I like going to the park','1993-07-26 00:00:00','$2b$12$EFO9mnMGaM88QmbfHt/bTulzjISsbifQpN9s6lu9C4llsEZpZT952'),(4,'juan@email.com','Juan','Hi, I\'m Juan','1994-04-04 00:00:00','$2b$12$5oVMyOt8RyGPM5WlpExoguYJhfzskaJ9thi9LzVjhYGekvrGmHK/.'),(6,'carson@email.com','Carson','blah','1993-07-26 00:00:00','$2b$12$ef1SjYBbNPWcaSaGCs2dS./por1knq/7e2jqXLnkzEgSPhQrXamNK'),(7,'mary@email.com','Mary','Hello','2021-03-04 00:00:00','$2b$12$DZ4Wsmc/5W6zbNw4IzKCWeZQLgSgmIEBgyqB.l9mrJwIvAWp.Z4eO');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-06 14:30:58
