from django.db import models

class Tag(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
        

SELECT SUM((cost * amount) - discount) AS total_revenue
FROM nails.record_services
WHERE DATE(created_at) = '2023-10-22';


SELECT SUM((cost * amount) - discount) AS total_revenue
FROM nails.record_services
WHERE DATE(created_at) BETWEEN '2023-10-01' AND '2023-10-31';


#best staff 
SELECT 
    r.staff_id, 
    SUM(rs.cost * rs.amount) AS total_cost
FROM 
    records AS r
JOIN 
    record_services AS rs ON r.id = rs.record_id
JOIN (
    SELECT staff_id
    FROM records
    WHERE DATE_FORMAT(date, '%Y-%m') = '2023-10' -- Replace with the desired year and month
    GROUP BY staff_id
    ORDER BY COUNT(*) DESC
    LIMIT 1
) AS top_master ON r.staff_id = top_master.staff_id
WHERE DATE_FORMAT(r.date, '%Y-%m') = '2023-10' -- Replace with the desired year and month
GROUP BY r.staff_id;

CREATE TABLE `masters` (
  `id` int NOT NULL AUTO_INCREMENT,
  `avatar` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `specialization` varchar(255) DEFAULT NULL,
  `position` varchar(255) DEFAULT NULL,
  `fired` tinyint(1) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `salary` int DEFAULT NULL,
  `saloon_id` int DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `saloon_id` (`saloon_id`),
  CONSTRAINT `masters_ibfk_1` FOREIGN KEY (`saloon_id`) REFERENCES `saloons` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2851535 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `records` (
  `id` int NOT NULL AUTO_INCREMENT,
  `saloon_id` int DEFAULT NULL,
  `staff_id` int DEFAULT NULL,
  `client_id` int DEFAULT NULL,
  `date` datetime NOT NULL,
  `comment` text,
  `services` text,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `client_visit_date` datetime DEFAULT NULL,
  `client_pay_date` datetime DEFAULT NULL,
  `options` json DEFAULT NULL,
  `in_feed` tinyint(1) DEFAULT '1',
  `total_likes` int DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `saloon_id` (`saloon_id`),
  KEY `staff_id` (`staff_id`),
  KEY `client_id` (`client_id`),
  CONSTRAINT `records_ibfk_1` FOREIGN KEY (`saloon_id`) REFERENCES `saloons` (`id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `records_ibfk_2` FOREIGN KEY (`staff_id`) REFERENCES `masters` (`id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `records_ibfk_3` FOREIGN KEY (`client_id`) REFERENCES `clients` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=727065773 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `record_services` (
  `id` int NOT NULL AUTO_INCREMENT,
  `record_id` int DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `cost` int DEFAULT NULL,
  `discount` int DEFAULT NULL,
  `amount` int DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `record_id` (`record_id`),
  CONSTRAINT `record_services_ibfk_1` FOREIGN KEY (`record_id`) REFERENCES `records` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11097334 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
