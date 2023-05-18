-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-05-2023 a las 19:42:53
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `inventario_jose_diaz`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `accounts_customuser`
--

CREATE TABLE `accounts_customuser` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `nombre_completo` varchar(70) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `telefono` varchar(12) NOT NULL,
  `rol_id` bigint(20) NOT NULL,
  `sucursal_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `accounts_customuser`
--

INSERT INTO `accounts_customuser` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `nombre_completo`, `direccion`, `telefono`, `rol_id`, `sucursal_id`) VALUES
(1, 'pbkdf2_sha256$260000$OjJAYA6PMwvakNVgRCdmUh$Kg4BMS8OToSrZUhAbeUmDExSkVXBjWjj4xx6Zx86hVg=', '2023-05-18 17:38:55.288028', 0, 'josediaz', '', '', '', 0, 1, '2023-05-17 17:37:47.784372', 'José Alejandro Díaz Suazo', 'Villa lago', '920178842', 1, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `accounts_customuser_groups`
--

CREATE TABLE `accounts_customuser_groups` (
  `id` bigint(20) NOT NULL,
  `customuser_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `accounts_customuser_user_permissions`
--

CREATE TABLE `accounts_customuser_user_permissions` (
  `id` bigint(20) NOT NULL,
  `customuser_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add Devolución mercancía', 6, 'add_devolucionmercancia'),
(22, 'Can change Devolución mercancía', 6, 'change_devolucionmercancia'),
(23, 'Can delete Devolución mercancía', 6, 'delete_devolucionmercancia'),
(24, 'Can view Devolución mercancía', 6, 'view_devolucionmercancia'),
(25, 'Can add Entrada mercancía', 7, 'add_entradamercancia'),
(26, 'Can change Entrada mercancía', 7, 'change_entradamercancia'),
(27, 'Can delete Entrada mercancía', 7, 'delete_entradamercancia'),
(28, 'Can view Entrada mercancía', 7, 'view_entradamercancia'),
(29, 'Can add Ingresar proveedor', 8, 'add_proveedores'),
(30, 'Can change Ingresar proveedor', 8, 'change_proveedores'),
(31, 'Can delete Ingresar proveedor', 8, 'delete_proveedores'),
(32, 'Can view Ingresar proveedor', 8, 'view_proveedores'),
(33, 'Can add Salida mercancía', 9, 'add_salidamercancia'),
(34, 'Can change Salida mercancía', 9, 'change_salidamercancia'),
(35, 'Can delete Salida mercancía', 9, 'delete_salidamercancia'),
(36, 'Can view Salida mercancía', 9, 'view_salidamercancia'),
(37, 'Can add sucursal', 10, 'add_sucursales'),
(38, 'Can change sucursal', 10, 'change_sucursales'),
(39, 'Can delete sucursal', 10, 'delete_sucursales'),
(40, 'Can view sucursal', 10, 'view_sucursales'),
(41, 'Can add inventario', 11, 'add_inventario'),
(42, 'Can change inventario', 11, 'change_inventario'),
(43, 'Can delete inventario', 11, 'delete_inventario'),
(44, 'Can view inventario', 11, 'view_inventario'),
(45, 'Can add inventario', 12, 'add_producto_inventario'),
(46, 'Can change inventario', 12, 'change_producto_inventario'),
(47, 'Can delete inventario', 12, 'delete_producto_inventario'),
(48, 'Can view inventario', 12, 'view_producto_inventario'),
(49, 'Can add producto', 13, 'add_productos'),
(50, 'Can change producto', 13, 'change_productos'),
(51, 'Can delete producto', 13, 'delete_productos'),
(52, 'Can view producto', 13, 'view_productos'),
(53, 'Can add proveedor_producto', 14, 'add_proveedor_producto'),
(54, 'Can change proveedor_producto', 14, 'change_proveedor_producto'),
(55, 'Can delete proveedor_producto', 14, 'delete_proveedor_producto'),
(56, 'Can view proveedor_producto', 14, 'view_proveedor_producto'),
(57, 'Can add permiso', 15, 'add_roles'),
(58, 'Can change permiso', 15, 'change_roles'),
(59, 'Can delete permiso', 15, 'delete_roles'),
(60, 'Can view permiso', 15, 'view_roles'),
(61, 'Can add usuarios', 16, 'add_customuser'),
(62, 'Can change usuarios', 16, 'change_customuser'),
(63, 'Can delete usuarios', 16, 'delete_customuser'),
(64, 'Can view usuarios', 16, 'view_customuser');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(16, 'accounts', 'customuser'),
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(6, 'inventarioApp', 'devolucionmercancia'),
(7, 'inventarioApp', 'entradamercancia'),
(11, 'inventarioApp', 'inventario'),
(13, 'inventarioApp', 'productos'),
(12, 'inventarioApp', 'producto_inventario'),
(8, 'inventarioApp', 'proveedores'),
(14, 'inventarioApp', 'proveedor_producto'),
(15, 'inventarioApp', 'roles'),
(9, 'inventarioApp', 'salidamercancia'),
(10, 'inventarioApp', 'sucursales'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'inventarioApp', '0001_initial', '2023-05-16 21:47:42.748058'),
(2, 'inventarioApp', '0002_delete_usuarios', '2023-05-16 21:47:42.758050'),
(3, 'contenttypes', '0001_initial', '2023-05-16 21:47:42.774631'),
(4, 'contenttypes', '0002_remove_content_type_name', '2023-05-16 21:47:42.799507'),
(5, 'auth', '0001_initial', '2023-05-16 21:47:42.888016'),
(6, 'auth', '0002_alter_permission_name_max_length', '2023-05-16 21:47:42.908897'),
(7, 'auth', '0003_alter_user_email_max_length', '2023-05-16 21:47:42.913883'),
(8, 'auth', '0004_alter_user_username_opts', '2023-05-16 21:47:42.917872'),
(9, 'auth', '0005_alter_user_last_login_null', '2023-05-16 21:47:42.923857'),
(10, 'auth', '0006_require_contenttypes_0002', '2023-05-16 21:47:42.925851'),
(11, 'auth', '0007_alter_validators_add_error_messages', '2023-05-16 21:47:42.929826'),
(12, 'auth', '0008_alter_user_username_max_length', '2023-05-16 21:47:42.934810'),
(13, 'auth', '0009_alter_user_last_name_max_length', '2023-05-16 21:47:42.940295'),
(14, 'auth', '0010_alter_group_name_max_length', '2023-05-16 21:47:42.947016'),
(15, 'auth', '0011_update_proxy_permissions', '2023-05-16 21:47:42.956976'),
(16, 'auth', '0012_alter_user_first_name_max_length', '2023-05-16 21:47:42.960907'),
(17, 'accounts', '0001_initial', '2023-05-16 21:47:43.122087'),
(18, 'accounts', '0002_auto_20230516_1747', '2023-05-16 21:47:43.196526'),
(19, 'admin', '0001_initial', '2023-05-16 21:47:43.250873'),
(20, 'admin', '0002_logentry_remove_auto_add', '2023-05-16 21:47:43.258209'),
(21, 'admin', '0003_logentry_add_action_flag_choices', '2023-05-16 21:47:43.266139'),
(22, 'inventarioApp', '0003_auto_20230516_1747', '2023-05-16 21:47:43.633804'),
(23, 'sessions', '0001_initial', '2023-05-16 21:47:43.648296');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('7u6gcnfbazsufl6moq84uo0z54rdkgnf', '.eJxVjMsOwiAQRf-FtSEgb5fu-w1kGAapGkhKuzL-uzbpQrf3nHNfLMK21rgNWuKc2YVJdvrdEuCD2g7yHdqtc-xtXebEd4UfdPCpZ3peD_fvoMKo37oQWluCLC6l4HVCEtKGYA2BRaUVaUvKowHMHoSRCMafyUkqDo1Qhr0__kw4RA:1pzUn3:rwliY6KrDNqw8Vx7hi10L4CHHjCTP1AjHhBiBu4xH5w', '2023-06-01 03:58:57.722306'),
('nrvkw4hqqont4cotblvnf9ppoiiv12kc', '.eJxVjMsOwiAQRf-FtSEgb5fu-w1kGAapGkhKuzL-uzbpQrf3nHNfLMK21rgNWuKc2YVJdvrdEuCD2g7yHdqtc-xtXebEd4UfdPCpZ3peD_fvoMKo37oQWluCLC6l4HVCEtKGYA2BRaUVaUvKowHMHoSRCMafyUkqDo1Qhr0__kw4RA:1pzhaZ:8cOtgaLYU7hpvEx2QhwNoyBM6Q4Th9-zlhhG2sCwxxE', '2023-06-01 17:38:55.291558');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventarioapp_devolucionmercancia`
--

CREATE TABLE `inventarioapp_devolucionmercancia` (
  `id` bigint(20) NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `cantidad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `inventarioapp_devolucionmercancia`
--

INSERT INTO `inventarioapp_devolucionmercancia` (`id`, `fecha`, `cantidad`) VALUES
(1, '2023-05-31 04:38:26.000000', 1500);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventarioapp_entradamercancia`
--

CREATE TABLE `inventarioapp_entradamercancia` (
  `id` bigint(20) NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `cantidad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `inventarioapp_entradamercancia`
--

INSERT INTO `inventarioapp_entradamercancia` (`id`, `fecha`, `cantidad`) VALUES
(1, '2023-05-19 00:33:00.000000', 500);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventarioapp_inventario`
--

CREATE TABLE `inventarioapp_inventario` (
  `id` bigint(20) NOT NULL,
  `id_sucursal_id` bigint(20) NOT NULL,
  `cantidad_maxima` int(11) DEFAULT NULL,
  `cantidad_minima` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `inventarioapp_inventario`
--

INSERT INTO `inventarioapp_inventario` (`id`, `id_sucursal_id`, `cantidad_maxima`, `cantidad_minima`) VALUES
(1, 2, 1000, 50);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventarioapp_productos`
--

CREATE TABLE `inventarioapp_productos` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `valor_unitario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `inventarioapp_productos`
--

INSERT INTO `inventarioapp_productos` (`id`, `nombre`, `valor_unitario`) VALUES
(1, 'ManiChoc', 150),
(2, 'Turrón', 250);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventarioapp_producto_inventario`
--

CREATE TABLE `inventarioapp_producto_inventario` (
  `id` bigint(20) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `inventario_id` bigint(20) NOT NULL,
  `producto_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventarioapp_proveedores`
--

CREATE TABLE `inventarioapp_proveedores` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `telefono` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `inventarioapp_proveedores`
--

INSERT INTO `inventarioapp_proveedores` (`id`, `nombre`, `direccion`, `telefono`) VALUES
(1, 'Fruna', 'Av. San Miguel, Talca', '9133102164');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventarioapp_proveedor_producto`
--

CREATE TABLE `inventarioapp_proveedor_producto` (
  `id` bigint(20) NOT NULL,
  `producto_id` bigint(20) NOT NULL,
  `proveedor_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventarioapp_roles`
--

CREATE TABLE `inventarioapp_roles` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `inventarioapp_roles`
--

INSERT INTO `inventarioapp_roles` (`id`, `nombre`, `descripcion`) VALUES
(1, 'Gestión de sucursales', 'este rol es para gestionar las sucursales');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventarioapp_salidamercancia`
--

CREATE TABLE `inventarioapp_salidamercancia` (
  `id` bigint(20) NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `cantidad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `inventarioapp_salidamercancia`
--

INSERT INTO `inventarioapp_salidamercancia` (`id`, `fecha`, `cantidad`) VALUES
(1, '2023-05-18 00:27:33.000000', 150);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventarioapp_sucursales`
--

CREATE TABLE `inventarioapp_sucursales` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `direccion` varchar(150) NOT NULL,
  `telefono` varchar(12) NOT NULL,
  `responsable` varchar(50) NOT NULL,
  `devolucion_id` bigint(20) DEFAULT NULL,
  `entrada_id` bigint(20) DEFAULT NULL,
  `salida_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `inventarioapp_sucursales`
--

INSERT INTO `inventarioapp_sucursales` (`id`, `nombre`, `direccion`, `telefono`, `responsable`, `devolucion_id`, `entrada_id`, `salida_id`) VALUES
(2, 'Sucursal Chillán', 'Balmaceda 103', '8946456', 'José Díaz', NULL, NULL, NULL);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `accounts_customuser`
--
ALTER TABLE `accounts_customuser`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `accounts_customuser_sucursal_id_2472eae8_fk_inventari` (`sucursal_id`),
  ADD KEY `accounts_customuser_rol_id_1b64e41d_fk_inventarioApp_roles_id` (`rol_id`);

--
-- Indices de la tabla `accounts_customuser_groups`
--
ALTER TABLE `accounts_customuser_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `accounts_customuser_groups_customuser_id_group_id_c074bdcb_uniq` (`customuser_id`,`group_id`),
  ADD KEY `accounts_customuser_groups_group_id_86ba5f9e_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `accounts_customuser_user_permissions`
--
ALTER TABLE `accounts_customuser_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `accounts_customuser_user_customuser_id_permission_9632a709_uniq` (`customuser_id`,`permission_id`),
  ADD KEY `accounts_customuser__permission_id_aea3d0e5_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_accounts_customuser_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `inventarioapp_devolucionmercancia`
--
ALTER TABLE `inventarioapp_devolucionmercancia`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `inventarioapp_entradamercancia`
--
ALTER TABLE `inventarioapp_entradamercancia`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `inventarioapp_inventario`
--
ALTER TABLE `inventarioapp_inventario`
  ADD PRIMARY KEY (`id`),
  ADD KEY `inventarioApp_invent_id_sucursal_id_2b990c82_fk_inventari` (`id_sucursal_id`);

--
-- Indices de la tabla `inventarioapp_productos`
--
ALTER TABLE `inventarioapp_productos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `inventarioapp_producto_inventario`
--
ALTER TABLE `inventarioapp_producto_inventario`
  ADD PRIMARY KEY (`id`),
  ADD KEY `inventarioApp_produc_inventario_id_a3aa1465_fk_inventari` (`inventario_id`),
  ADD KEY `inventarioApp_produc_producto_id_622b3ac2_fk_inventari` (`producto_id`);

--
-- Indices de la tabla `inventarioapp_proveedores`
--
ALTER TABLE `inventarioapp_proveedores`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `inventarioapp_proveedor_producto`
--
ALTER TABLE `inventarioapp_proveedor_producto`
  ADD PRIMARY KEY (`id`),
  ADD KEY `inventarioApp_provee_producto_id_81a398ca_fk_inventari` (`producto_id`),
  ADD KEY `inventarioApp_provee_proveedor_id_5d74656e_fk_inventari` (`proveedor_id`);

--
-- Indices de la tabla `inventarioapp_roles`
--
ALTER TABLE `inventarioapp_roles`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `inventarioapp_salidamercancia`
--
ALTER TABLE `inventarioapp_salidamercancia`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `inventarioapp_sucursales`
--
ALTER TABLE `inventarioapp_sucursales`
  ADD PRIMARY KEY (`id`),
  ADD KEY `inventarioApp_sucurs_devolucion_id_fdfafbc9_fk_inventari` (`devolucion_id`),
  ADD KEY `inventarioApp_sucurs_entrada_id_89b280be_fk_inventari` (`entrada_id`),
  ADD KEY `inventarioApp_sucurs_salida_id_deacd84c_fk_inventari` (`salida_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `accounts_customuser`
--
ALTER TABLE `accounts_customuser`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `accounts_customuser_groups`
--
ALTER TABLE `accounts_customuser_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `accounts_customuser_user_permissions`
--
ALTER TABLE `accounts_customuser_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT de la tabla `inventarioapp_devolucionmercancia`
--
ALTER TABLE `inventarioapp_devolucionmercancia`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `inventarioapp_entradamercancia`
--
ALTER TABLE `inventarioapp_entradamercancia`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `inventarioapp_inventario`
--
ALTER TABLE `inventarioapp_inventario`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `inventarioapp_productos`
--
ALTER TABLE `inventarioapp_productos`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `inventarioapp_producto_inventario`
--
ALTER TABLE `inventarioapp_producto_inventario`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `inventarioapp_proveedores`
--
ALTER TABLE `inventarioapp_proveedores`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `inventarioapp_proveedor_producto`
--
ALTER TABLE `inventarioapp_proveedor_producto`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `inventarioapp_roles`
--
ALTER TABLE `inventarioapp_roles`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `inventarioapp_salidamercancia`
--
ALTER TABLE `inventarioapp_salidamercancia`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `inventarioapp_sucursales`
--
ALTER TABLE `inventarioapp_sucursales`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `accounts_customuser`
--
ALTER TABLE `accounts_customuser`
  ADD CONSTRAINT `accounts_customuser_rol_id_1b64e41d_fk_inventarioApp_roles_id` FOREIGN KEY (`rol_id`) REFERENCES `inventarioapp_roles` (`id`),
  ADD CONSTRAINT `accounts_customuser_sucursal_id_2472eae8_fk_inventari` FOREIGN KEY (`sucursal_id`) REFERENCES `inventarioapp_sucursales` (`id`);

--
-- Filtros para la tabla `accounts_customuser_groups`
--
ALTER TABLE `accounts_customuser_groups`
  ADD CONSTRAINT `accounts_customuser__customuser_id_bc55088e_fk_accounts_` FOREIGN KEY (`customuser_id`) REFERENCES `accounts_customuser` (`id`),
  ADD CONSTRAINT `accounts_customuser_groups_group_id_86ba5f9e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `accounts_customuser_user_permissions`
--
ALTER TABLE `accounts_customuser_user_permissions`
  ADD CONSTRAINT `accounts_customuser__customuser_id_0deaefae_fk_accounts_` FOREIGN KEY (`customuser_id`) REFERENCES `accounts_customuser` (`id`),
  ADD CONSTRAINT `accounts_customuser__permission_id_aea3d0e5_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_accounts_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_customuser` (`id`);

--
-- Filtros para la tabla `inventarioapp_inventario`
--
ALTER TABLE `inventarioapp_inventario`
  ADD CONSTRAINT `inventarioApp_invent_id_sucursal_id_2b990c82_fk_inventari` FOREIGN KEY (`id_sucursal_id`) REFERENCES `inventarioapp_sucursales` (`id`);

--
-- Filtros para la tabla `inventarioapp_producto_inventario`
--
ALTER TABLE `inventarioapp_producto_inventario`
  ADD CONSTRAINT `inventarioApp_produc_inventario_id_a3aa1465_fk_inventari` FOREIGN KEY (`inventario_id`) REFERENCES `inventarioapp_inventario` (`id`),
  ADD CONSTRAINT `inventarioApp_produc_producto_id_622b3ac2_fk_inventari` FOREIGN KEY (`producto_id`) REFERENCES `inventarioapp_productos` (`id`);

--
-- Filtros para la tabla `inventarioapp_proveedor_producto`
--
ALTER TABLE `inventarioapp_proveedor_producto`
  ADD CONSTRAINT `inventarioApp_provee_producto_id_81a398ca_fk_inventari` FOREIGN KEY (`producto_id`) REFERENCES `inventarioapp_productos` (`id`),
  ADD CONSTRAINT `inventarioApp_provee_proveedor_id_5d74656e_fk_inventari` FOREIGN KEY (`proveedor_id`) REFERENCES `inventarioapp_proveedores` (`id`);

--
-- Filtros para la tabla `inventarioapp_sucursales`
--
ALTER TABLE `inventarioapp_sucursales`
  ADD CONSTRAINT `inventarioApp_sucurs_devolucion_id_fdfafbc9_fk_inventari` FOREIGN KEY (`devolucion_id`) REFERENCES `inventarioapp_devolucionmercancia` (`id`),
  ADD CONSTRAINT `inventarioApp_sucurs_entrada_id_89b280be_fk_inventari` FOREIGN KEY (`entrada_id`) REFERENCES `inventarioapp_entradamercancia` (`id`),
  ADD CONSTRAINT `inventarioApp_sucurs_salida_id_deacd84c_fk_inventari` FOREIGN KEY (`salida_id`) REFERENCES `inventarioapp_salidamercancia` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
