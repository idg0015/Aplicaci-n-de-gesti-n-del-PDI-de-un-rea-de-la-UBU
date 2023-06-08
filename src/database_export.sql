CREATE TABLE `abreviatura` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `abreviatura` varchar(256) NOT NULL,
  `id_asignatura` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_asignatura` (`id_asignatura`),
  CONSTRAINT `abreviatura_ibfk_1` FOREIGN KEY (`id_asignatura`) REFERENCES `asignatura` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO abreviatura VALUES
(1, INFORM�TICA, 1),
(2, PROGRAMACI�N, 2),
(3, SIST. OPERATIV., 3),
(4, MET. PROG., 4),
(5, BASES DATOS, 5),
(6, SIST. INTELIG., 6),
(7, GEST., 7),
(8, SIST. Y REDES, 8),
(9, PROC. LENGUAJE, 9),
(10, PROG. CONCUR., 10),
(11, SEGURIDAD, 11),
(12, APL. BASES DAT., 12),
(13, ALGORITMIA, 13),
(14, VALID. Y PRUEB., 14),
(15, DIS-MAN SOFT, 15),
(16, PROG. S.O., 16),
(17, SIST. DISTRIB., 17),
(18, MINER�A, 18),
(19, D.A.SISTEMAS, 19),
;

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO alembic_version VALUES
(333a0e002d6c),
;

CREATE TABLE `area` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(256) NOT NULL,
  `abreviatura` varchar(80) NOT NULL,
  `id_departamento` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_departamento` (`id_departamento`),
  CONSTRAINT `area_ibfk_1` FOREIGN KEY (`id_departamento`) REFERENCES `departamento` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO area VALUES
(1, Lenguajes y Sistemas Inform�ticos, LySI, 1),
;

CREATE TABLE `asignatura` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` int(11) NOT NULL,
  `nombre` varchar(256) NOT NULL,
  `tipo` varchar(256) NOT NULL,
  `creditos_teoria` int(11) NOT NULL,
  `creditos_practica` int(11) NOT NULL,
  `curso` varchar(80) NOT NULL,
  `semestre` varchar(80) NOT NULL,
  `id_titulacion` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_titulacion` (`id_titulacion`),
  CONSTRAINT `asignatura_ibfk_1` FOREIGN KEY (`id_titulacion`) REFERENCES `titulacion` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO asignatura VALUES
(1, 6346, Inform�tica B�sica, FB, 3, 3, 1, 1, 1),
(2, 6351, Programaci�n, FB, 3, 3, 1, 2, 1),
(3, 6353, Sistemas Operativos, Ob, 3, 3, 1, 2, 1),
(4, 6354, Metodolog�a de la Programaci�n, Ob, 3, 3, 2, 1, 1),
(5, 6357, BASES DE DATOS , Ob, 3, 3, 2, 1, 1),
(6, 6365, SISTEMAS INTELIGENTES , Ob, 3, 3, 3, 1, 1),
(7, 6366, GESTI�N DE PROYECTOS , Ob, 2, 2, 1, 1, 1),
(8, 6367, DISE�O Y ADMINISTRACI�N DE SISTEMAS Y REDES, Ob, 3, 3, 3, 1, 1),
(9, 6368, PROCESADORES DEL LENGUAJE , Ob, 3, 3, 3, 1, 1),
(10, 6369, PROGRAMACI�N CONCURRENTE Y DE TIEMPO REAL , Ob, 2, 2, 3, 2, 1),
(11, 6370, SEGURIDAD INFORM�TICA , Ob, 3, 3, 3, 2, 1),
(12, 6371, APLICACIONES DE BASES DE DATOS , Ob, 3, 3, 3, 2, 1),
(13, 6372, ALGORITMIA , Ob, 3, 3, 3, 2, 1),
(14, 6376, VALIDACI�N Y PRUEBAS, Op, 3, 3, 4, 1, 1),
(15, 6378, DISE�O Y MANTENIMIENTO DEL SOFTWARE, Op, 3, 3, 4, 1, 1),
(16, 6383, PROGRAMACI�N DE SISTEMAS OPERATIVOS , Op, 3, 3, 4, 1, 1),
(17, 6384, SISTEMAS DISTRIBUIDOS, Op, 3, 3, 4, 2, 1),
(18, 6388, MINER�A DE DATOS , Op, 3, 3, 4, 2, 1),
(19, 6389, DESARROLLO AVANZADO DE SISTEMAS SOFTWARE , Op, 3, 3, 4, 2, 1),
(20, 6390, PR�CTICAS EN EMPRESA , Op, 0, 0, 4, 1.2, 1),
(21, 6391, TRABAJO FIN DE GRADO , Ob, 0, 0, 4, 1.2, 1),
;

CREATE TABLE `centro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` int(11) NOT NULL,
  `nombre` varchar(256) NOT NULL,
  `abreviatura` varchar(80) NOT NULL,
  `email` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO centro VALUES
(1, 13, Escuela Polit�cnica Superior, R�o Vena , EPSv , departamentos.eps@ubu.es),
(2, 131, Escuela Polit�cnica Superior, Milanera , EPSm , departamentos.eps@ubu.es),
(3, 43, Facultad de Ciencias, FC , departamentos.ciencias@ubu.es),
(4, 53, Facultad de Ciencias de la Salud , FCS , departamentos.hospitalmilitar@ubu.es),
(5, 55, Facultad de Educaci�n , FE, departamentos.educacion@ubu.es),
(6, 54, Facultad de Humanidades y Comunicaci�n, FHC , departamentos.hospitalmilitar@ubu.es),
;

CREATE TABLE `curso` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ano_inicio` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO curso VALUES
(18, 2023),
;

CREATE TABLE `curso_asignatura` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_asignatura` int(11) NOT NULL,
  `id_curso` int(11) NOT NULL,
  `modalidad` varchar(256) NOT NULL,
  `num_alumnos_previstos` int(11) NOT NULL,
  `num_grupos_teoricos_previstos` int(11) NOT NULL,
  `num_grupos_practicos_previstos` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_asignatura` (`id_asignatura`),
  KEY `id_curso` (`id_curso`),
  CONSTRAINT `curso_asignatura_ibfk_1` FOREIGN KEY (`id_asignatura`) REFERENCES `asignatura` (`id`) ON DELETE CASCADE,
  CONSTRAINT `curso_asignatura_ibfk_2` FOREIGN KEY (`id_curso`) REFERENCES `curso` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=413 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO curso_asignatura VALUES
(1, 1, 18, Presencial, 30, 1, 1),
(5, 3, 18, Presencial, 60, 1, 1),
(6, 3, 18, Online, 30, 1, 1),
(7, 4, 18, Presencial, 60, 1, 1),
(8, 4, 18, Online, 30, 1, 1),
(9, 5, 18, Presencial, 60, 1, 1),
(10, 5, 18, Online, 30, 1, 1),
(11, 6, 18, Presencial, 60, 1, 1),
(12, 6, 18, Online, 30, 1, 1),
(13, 7, 18, Presencial, 60, 1, 1),
(14, 7, 18, Online, 30, 1, 1),
(15, 8, 18, Presencial, 60, 1, 1),
(16, 8, 18, Online, 30, 1, 1),
(17, 9, 18, Presencial, 60, 1, 1),
(18, 9, 18, Online, 30, 1, 1),
(19, 10, 18, Presencial, 60, 1, 1),
(20, 10, 18, Online, 30, 1, 1),
(21, 11, 18, Presencial, 60, 1, 1),
(22, 11, 18, Online, 30, 1, 1),
(23, 12, 18, Presencial, 60, 1, 1),
(24, 12, 18, Online, 30, 1, 1),
(25, 13, 18, Presencial, 60, 1, 1),
(26, 13, 18, Online, 30, 1, 1),
(27, 14, 18, Presencial, 60, 1, 1),
(28, 14, 18, Online, 30, 1, 1),
(29, 15, 18, Presencial, 60, 1, 1),
(30, 15, 18, Online, 30, 1, 1),
(31, 16, 18, Presencial, 60, 1, 1),
(32, 16, 18, Online, 30, 1, 1),
(33, 17, 18, Presencial, 60, 1, 1),
(34, 17, 18, Online, 30, 1, 1),
(35, 18, 18, Presencial, 60, 1, 1),
(36, 18, 18, Online, 30, 1, 1),
(37, 19, 18, Presencial, 60, 1, 1),
(38, 19, 18, Online, 30, 1, 1),
(39, 20, 18, Presencial, 60, 1, 1),
(40, 20, 18, Online, 30, 1, 1),
(41, 21, 18, Presencial, 60, 1, 1),
(42, 21, 18, Online, 30, 1, 1),
(43, 2, 18, Presencial, 20, 1, 1),
;

CREATE TABLE `departamento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(256) NOT NULL,
  `abreviatura` varchar(80) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO departamento VALUES
(1, Ingenier�a Inform�tica, II),
;

CREATE TABLE `docente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(256) NOT NULL,
  `apellidos` varchar(256) NOT NULL,
  `email` varchar(256) NOT NULL,
  `reducciones` int(11) NOT NULL,
  `read_flag` tinyint(1) NOT NULL,
  `modification_flag` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO docente VALUES
(1, �lvar, Arnaiz Gonz�lez, alvarag@ubu.es, 3, 0, 0),
(2, Carlos, Pardo Aguilar, cpardo@ubu.es, 20, 1, 0),
(3, Jos� Luis, Garrido Labrador, jlgarrido@ubu.es, 0, 0, 0),
(4, Jes�s Manuel, Maudes Raedo, jmaudes@ubu.es, 6, 1, 0),
(5, Ignacio, D�vila Garc�a, idg0015@alu.ubu.es, 0, 1, 1),
;

CREATE TABLE `grupo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(256) NOT NULL,
  `tipo` varchar(256) NOT NULL,
  `id_curso_asignatura` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_curso_asignatura` (`id_curso_asignatura`),
  CONSTRAINT `grupo_ibfk_1` FOREIGN KEY (`id_curso_asignatura`) REFERENCES `curso_asignatura` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=885 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO grupo VALUES
(9, 1, Te�rico, 5),
(10, 101, Pr�ctico, 5),
(11, 90, Te�rico, 6),
(12, 901, Pr�ctico, 6),
(13, 1, Te�rico, 7),
(14, 101, Pr�ctico, 7),
(15, 90, Te�rico, 8),
(16, 901, Pr�ctico, 8),
(17, 1, Te�rico, 9),
(18, 101, Pr�ctico, 9),
(19, 90, Te�rico, 10),
(20, 901, Pr�ctico, 10),
(21, 1, Te�rico, 11),
(22, 101, Pr�ctico, 11),
(23, 90, Te�rico, 12),
(24, 901, Pr�ctico, 12),
(25, 1, Te�rico, 13),
(26, 101, Pr�ctico, 13),
(27, 90, Te�rico, 14),
(28, 901, Pr�ctico, 14),
(29, 1, Te�rico, 15),
(30, 101, Pr�ctico, 15),
(31, 90, Te�rico, 16),
(32, 901, Pr�ctico, 16),
(33, 1, Te�rico, 17),
(34, 101, Pr�ctico, 17),
(35, 90, Te�rico, 18),
(36, 901, Pr�ctico, 18),
(37, 1, Te�rico, 19),
(38, 101, Pr�ctico, 19),
(39, 90, Te�rico, 20),
(40, 901, Pr�ctico, 20),
(41, 1, Te�rico, 21),
(42, 101, Pr�ctico, 21),
(43, 90, Te�rico, 22),
(44, 901, Pr�ctico, 22),
(45, 1, Te�rico, 23),
(46, 101, Pr�ctico, 23),
(47, 90, Te�rico, 24),
(48, 901, Pr�ctico, 24),
(49, 1, Te�rico, 25),
(50, 101, Pr�ctico, 25),
(51, 90, Te�rico, 26),
(52, 901, Pr�ctico, 26),
(53, 1, Te�rico, 27),
(54, 101, Pr�ctico, 27),
(55, 90, Te�rico, 28),
(56, 901, Pr�ctico, 28),
(57, 1, Te�rico, 29),
(58, 101, Pr�ctico, 29),
(59, 90, Te�rico, 30),
(60, 901, Pr�ctico, 30),
(61, 1, Te�rico, 31),
(62, 101, Pr�ctico, 31),
(63, 90, Te�rico, 32),
(64, 901, Pr�ctico, 32),
(65, 1, Te�rico, 33),
(66, 101, Pr�ctico, 33),
(67, 90, Te�rico, 34),
(68, 901, Pr�ctico, 34),
(69, 1, Te�rico, 35),
(70, 101, Pr�ctico, 35),
(71, 90, Te�rico, 36),
(72, 901, Pr�ctico, 36),
(73, 1, Te�rico, 37),
(74, 101, Pr�ctico, 37),
(75, 90, Te�rico, 38),
(76, 901, Pr�ctico, 38),
(77, 1, Te�rico, 39),
(78, 101, Pr�ctico, 39),
(79, 90, Te�rico, 40),
(80, 901, Pr�ctico, 40),
(81, 1, Te�rico, 41),
(82, 101, Pr�ctico, 41),
(83, 90, Te�rico, 42),
(84, 901, Pr�ctico, 42),
(121, 101, Pr�ctico, 1),
(122, 1, Te�rico, 1),
(123, 102, Pr�ctico, 1),
(125, 103, Pr�ctico, 1),
(127, 1, Te�rico, 43),
(128, 101, Pr�ctico, 43),
;

CREATE TABLE `plaza` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(256) NOT NULL,
  `rpt` varchar(256) NOT NULL,
  `num_concursos_contratacion` int(11) DEFAULT NULL,
  `fecha_incorporacion` date NOT NULL,
  `fecha_cese` date DEFAULT NULL,
  `id_docente` int(11) DEFAULT NULL,
  `id_area` int(11) NOT NULL,
  `id_contrato` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_docente` (`id_docente`),
  KEY `id_area` (`id_area`),
  KEY `id_contrato` (`id_contrato`),
  CONSTRAINT `plaza_ibfk_1` FOREIGN KEY (`id_docente`) REFERENCES `docente` (`id`) ON DELETE CASCADE,
  CONSTRAINT `plaza_ibfk_2` FOREIGN KEY (`id_area`) REFERENCES `area` (`id`) ON DELETE CASCADE,
  CONSTRAINT `plaza_ibfk_3` FOREIGN KEY (`id_contrato`) REFERENCES `tipo_contrato` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO plaza VALUES
(1, Plaza 1, a, 1, 2023-04-26, 2022-11-17, 1, 1, 1),
(2, Test, test, None, 2023-05-24, None, 3, 1, 1),
(3, Plaza 2, rpt, None, 2023-05-27, None, 2, 1, 1),
(4, Test2, a, None, 2023-05-27, None, 1, 1, 1),
(5, Plaza 3, -, 3, 2023-06-07, None, 4, 1, 1),
;

CREATE TABLE `plaza_grupo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `horas` int(11) DEFAULT NULL,
  `id_grupo` int(11) NOT NULL,
  `id_plaza` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_grupo` (`id_grupo`),
  KEY `id_plaza` (`id_plaza`),
  CONSTRAINT `plaza_grupo_ibfk_1` FOREIGN KEY (`id_grupo`) REFERENCES `grupo` (`id`) ON DELETE CASCADE,
  CONSTRAINT `plaza_grupo_ibfk_2` FOREIGN KEY (`id_plaza`) REFERENCES `plaza` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO plaza_grupo VALUES
(3, 70, 121, 3),
(6, 10, 121, 2),
(10, 10, 122, 3),
(13, 100, 122, 1),
(39, 50, 121, 4),
;

CREATE TABLE `sessions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `session_id` varchar(255) DEFAULT NULL,
  `data` blob DEFAULT NULL,
  `expiry` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `session_id` (`session_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO sessions VALUES
(1, session:7f6d8284-c5b8-48e3-acc6-fde7a1235aa4, b'\x80\x04\x95\x82\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\n_permanent\x94\x88\x8c\ncsrf_token\x94\x8c(cd6e4d29910cbb7f43716244f6092e5044ef397c\x94\x8c\x07user_id\x94K\x05\x8c\x05token\x94\x8c 3c4b6af15c353c17f16ea2d36166f91c\x94u.', 2023-07-09 19:58:17),
(2, session:f49e2f86-dc1c-463c-ab1f-e6e110fc2c09, b'\x80\x04\x95K\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\n_permanent\x94\x88\x8c\ncsrf_token\x94\x8c(fea0f73d7a46979d39545041b1c8ada31b04580c\x94u.', 2023-07-08 19:04:18),
;

CREATE TABLE `tipo_contrato` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(256) NOT NULL,
  `abreviatura` varchar(80) NOT NULL,
  `capacidad_anual` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO tipo_contrato VALUES
(1, Tipo 1, T1, 350),
(3, Tipo2, T2, 200),
;

CREATE TABLE `titulacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` int(11) NOT NULL,
  `nombre` varchar(256) NOT NULL,
  `abreviatura` varchar(80) NOT NULL,
  `url` varchar(256) NOT NULL,
  `id_centro` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_centro` (`id_centro`),
  CONSTRAINT `titulacion_ibfk_1` FOREIGN KEY (`id_centro`) REFERENCES `centro` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO titulacion VALUES
(1, 63, G� en Ing, Inform�tica, G�II, https://www.ubu.es/informatica, 1),
(2, 163, Mr.Univ. en Inteligencia de Negocio y Big Data en Entornos Seguros , MrData , https://www.ubu.es/master-universitario-online-en-inteligencia-de-negocio-y-big-data-en-entornos-seguros-business-intelligence-and-big-data-cyber-secure-environments-interuniversitario, 1),
(3, 164, Mr.Univ. en Ing. Inform�tica (2018) , MrII18 , https://www.ubu.es/master-universitario-en-ingenieria-informatica/informacion-basica/adaptacion-al-titulo/adaptacion-del-master-de-ingenieria-informatica-del-2018-desde-el-master-de-ingenieria, 1),
(5, 42, G� en Comunicaci�n Audiovisual , G�CA, https://www.ubu.es/grado-en-comunicacion-audiovisual, 6),
(6, 174, G� en Comunicaci�n Audiovisual (2022), G�CA22, https://www.ubu.es/grado-en-comunicacion-audiovisual, 6),
(7, 153, Mr.Univ. en Comunicaci�n y Desarrollo Multimedia , MrCDM , https://www.ubu.es/master-universitario-en-comunicacion-y-desarrollo-multimedia, 6),
(8, 167, Mr.Univ. en Patrimonio y Comunicaci�n (2019) , MrPC19 , https://www.ubu.es/master-universitario-en-patrimonio-y-comunicacion, 6),
(9, 169, G� en Dise�o de Videojuegos, G�DVj , https://www.ubu.es/grado-en-diseno-de-videojuegos, 6),
(10, 69, G� en Pedagog�a , G�P, https://www.ubu.es/grado-en-pedagogia, 5),
(11, 133, Curso de Formaci�n Pedag�gica y Did�ctica , CFPD, https://www.ubu.es/curso-de-formacion-pedagogica-y-didactica-semipresencial, 5),
(12, 157, Mr.Univ. en Profesor en E.S.O. y Bach., F.P., MrProf, https://www.ubu.es/master-universitario-en-profesor-de-educacion-secundaria-obligatoria-y-bachillerato-formacion-profesional-y-ensenanza-de-idiomas, 5),
(13, 115, Mr.Univ. en Cultura del Vino: Enoturismo en la Cuenca del Duero, MrVino, https://www.ubu.es/master-universitario-en-cultura-del-vino-enoturismo-en-la-cuenca-del-duero-semipresencial, 3),
(14, 162, Mr.Univ. en Ciencias de la Salud: Investigaci�n y Nuevos Retos , MrSalud , https://www.ubu.es/master-universitario-en-ciencias-de-la-salud-investigacion-y-nuevos-retos/master-universitario-en-ciencias-de-la-salud-investigacion-y-nuevos-retos, 4),
;

