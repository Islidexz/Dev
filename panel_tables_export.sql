CREATE TABLE `panel_media` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `file` varchar(100) NOT NULL,
  `file_type` varchar(50) DEFAULT NULL,
  `file_size` int unsigned DEFAULT NULL,
  `uploaded_at` datetime(6) NOT NULL,
  `page_id` int DEFAULT NULL,
  `slice_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `panel_media_page_id_27b03a9b_fk_panel_page_id` (`page_id`),
  KEY `panel_media_slice_id_7f93eab9_fk_panel_slice_id` (`slice_id`),
  CONSTRAINT `panel_media_page_id_27b03a9b_fk_panel_page_id` FOREIGN KEY (`page_id`) REFERENCES `panel_page` (`id`),
  CONSTRAINT `panel_media_slice_id_7f93eab9_fk_panel_slice_id` FOREIGN KEY (`slice_id`) REFERENCES `panel_slice` (`id`),
  CONSTRAINT `panel_media_chk_1` CHECK ((`file_size` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `panel_page` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `state` varchar(10) NOT NULL,
  `type` varchar(10) NOT NULL,
  `lft` int unsigned NOT NULL,
  `rght` int unsigned NOT NULL,
  `tree_id` int unsigned NOT NULL,
  `level` int unsigned NOT NULL,
  `parent_id` int DEFAULT NULL,
  `parent_ws_id` int DEFAULT NULL,
  `text` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `url` (`url`),
  UNIQUE KEY `panel_page_url_parent_ws_id_dd256707_uniq` (`url`,`parent_ws_id`),
  KEY `panel_page_url_ee927a_idx` (`url`,`parent_id`),
  KEY `panel_page_tree_id_99db9d69` (`tree_id`),
  CONSTRAINT `panel_page_chk_1` CHECK ((`lft` >= 0)),
  CONSTRAINT `panel_page_chk_2` CHECK ((`rght` >= 0)),
  CONSTRAINT `panel_page_chk_3` CHECK ((`tree_id` >= 0)),
  CONSTRAINT `panel_page_chk_4` CHECK ((`level` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `panel_slice` (
  `id` int NOT NULL AUTO_INCREMENT,
  `is_main` tinyint(1) NOT NULL,
  `title` varchar(255) NOT NULL,
  `text` longtext,
  `timestamp` datetime(6) NOT NULL,
  `keywords_block` longtext,
  `parent_page_id` int DEFAULT NULL,
  `price` double DEFAULT NULL,
  `icon` varchar(100) DEFAULT NULL,
  `img` varchar(100) DEFAULT NULL,
  `state` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `panel_website` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `url` varchar(200) DEFAULT NULL,
  `state` varchar(10) NOT NULL,
  `type` varchar(10) NOT NULL,
  `owner_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `url` (`url`),
  KEY `panel_website_owner_id_c59d95ab_fk_auth_user_id` (`owner_id`),
  CONSTRAINT `panel_website_owner_id_c59d95ab_fk_auth_user_id` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Хост: localhost
-- Время создания: Апр 18 2024 г., 12:44
-- Версия сервера: 8.0.36-0ubuntu0.22.04.1
-- Версия PHP: 8.1.2-1ubuntu2.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `panel`
--

-- --------------------------------------------------------

--
-- Структура таблицы `django_migrations`
--

--
-- Дамп данных таблицы `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(41, 'contenttypes', '0001_initial', '2024-04-08 21:58:17.9INSERT INTO `panel`.`panel_media`
(`id`,
`title`,
`file`,
`file_type`,
`file_size`,
`uploaded_at`,
`page_id`,
`slice_id`)
VALUES
(<{id: }>,
<{title: }>,
<{file: }>,
<{file_type: }>,
<{file_size: }>,
<{uploaded_at: }>,
<{page_id: }>,
<{slice_id: }>);

INSERT INTO `panel`.`panel_page`
(`id`,
`title`,
`url`,
`state`,
`type`,
`lft`,
`rght`,
`tree_id`,
`level`,
`parent_id`,
`parent_ws_id`,
`text`)
VALUES
(<{id: }>,
<{title: }>,
<{url: }>,
<{state: }>,
<{type: }>,
<{lft: }>,
<{rght: }>,
<{tree_id: }>,
<{level: }>,
<{parent_id: }>,
<{parent_ws_id: }>,
<{text: }>);

INSERT INTO `panel`.`panel_slice`
(`id`,
`is_main`,
`title`,
`text`,
`timestamp`,
`keywords_block`,
`parent_page_id`,
`price`,
`icon`,
`img`,
`state`)
VALUES
(<{id: }>,
<{is_main: }>,
<{title: }>,
<{text: }>,
<{timestamp: }>,
<{keywords_block: }>,
<{parent_page_id: }>,
<{price: }>,
<{icon: }>,
<{img: }>,
<{state: }>);

INSERT INTO `panel`.`panel_website`
(`id`,
`name`,
`url`,
`state`,
`type`,
`owner_id`)
VALUES
(<{id: }>,
<{name: }>,
<{url: }>,
<{state: }>,
<{type: }>,
<{owner_id: }>);
66899'),
(42, 'auth', '0001_initial', '2024-04-08 21:58:17.984974'),
(43, 'admin', '0001_initial', '2024-04-08 21:58:18.002892'),
(44, 'admin', '0002_logentry_remove_auto_add', '2024-04-08 21:58:18.010020'),
(45, 'admin', '0003_logentry_add_action_flag_choices', '2024-04-08 21:58:18.020136'),
(46, 'contenttypes', '0002_remove_content_type_name', '2024-04-08 21:58:18.025285'),
(47, 'auth', '0002_alter_permission_name_max_length', '2024-04-08 21:58:18.031807'),
(48, 'auth', '0003_alter_user_email_max_length', '2024-04-08 21:58:18.037062'),
(49, 'auth', '0004_alter_user_username_opts', '2024-04-08 21:58:18.044395'),
(50, 'auth', '0005_alter_user_last_login_null', '2024-04-08 21:58:18.049778'),
(51, 'auth', '0006_require_contenttypes_0002', '2024-04-08 21:58:18.055933'),
(52, 'auth', '0007_alter_validators_add_error_messages', '2024-04-08 21:58:18.060934'),
(53, 'auth', '0008_alter_user_username_max_length', '2024-04-08 21:58:18.067371'),
(54, 'auth', '0009_alter_user_last_name_max_length', '2024-04-08 21:58:18.071455'),
(55, 'auth', '0010_alter_group_name_max_length', '2024-04-08 21:58:18.080341'),
(56, 'auth', '0011_update_proxy_permissions', '2024-04-08 21:58:18.087103'),
(57, 'auth', '0012_alter_user_first_name_max_length', '2024-04-08 21:58:18.092656'),
(58, 'panel', '0001_initial', '2024-04-08 21:58:18.098170'),
(59, 'sessions', '0001_initial', '2024-04-08 21:58:18.111122'),
(60, 'panel', '0002_alter_media_file_alter_slice_icon_alter_slice_img', '2024-04-13 09:07:18.559664');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
