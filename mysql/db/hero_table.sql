CREATE TABLE `Hero` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  `secret_name` varchar(256) NOT NULL,
  `age` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
);

INSERT INTO `Hero` (`name`, `secret_name`, `age`)
VALUES
    ('Deadpond', 'Dive Wilson', NULL),
    ('Spider-Boy', 'Pedro Parqueador', NULL),
    ('Rusty-Man', 'Tommy Sharp', 48);
