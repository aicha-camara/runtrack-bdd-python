/*!40101 SET NAMES utf8 */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET SQL_NOTES=0 */;
DROP TABLE IF EXISTS etage;
CREATE TABLE `etage` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) DEFAULT NULL,
  `numero` int DEFAULT NULL,
  `superficie` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS etudiant;
CREATE TABLE `etudiant` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) NOT NULL,
  `prenom` varchar(25) NOT NULL,
  `age` int NOT NULL,
  `email` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS salle;
CREATE TABLE `salle` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) DEFAULT NULL,
  `id_etage` int DEFAULT NULL,
  `capacite` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO etage(id,nom,numero,superficie) VALUES('1','\'RDC\'','0','500'),('2','\'R+1\'','1','500');

INSERT INTO etudiant(id,nom,prenom,age,email) VALUES('1','\'Betty\'','\'Spaghetti\'','20','\'betty.Spaghetti@laplateforme.io\''),('2','\'Chuck\'','\'Steak\'','45','\'chuck.steak@laplateforme.io\''),('4','\'Binkie\'','\'Barnes\'','16','\'binkie.barnes@laplateforme.io\''),('5','\'Dupuis\'','\'Gertrude\'','20','\'gertrude.dupuis@laplateforme.io\''),('6','\'Dupuis\'','\'Martin\'','18','\'martin.dupuis@laplateforme.io\'');
INSERT INTO salle(id,nom,id_etage,capacite) VALUES('1','\'Lounge\'','1','100'),('2','\'Studio son\'','1','5'),('3','\'Broadcasting\'','2','50'),('4','\'Bocal Peda\'','2','4'),('5','\'Coworking\'','2','80'),('6','\'Studio Video\'','2','5');