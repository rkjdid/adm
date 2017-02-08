--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

--
-- Data for Name: web_accueil; Type: TABLE DATA; Schema: public; Owner: rkjdid
--

INSERT INTO web_accueil VALUES (1, 'Née dans le berceau de la grande distribution et de la VAD, nous sommes une agence sur mesure pour tous les budgets. Une pensée différente mais surtout pas unique. Créatifs, réactifs, nous voulons vous aider à construire votre entreprise, votre institution, vos marques et à les rendre plus belles et plus fortes. Pour vous, une équipe qui a toujours la banane ; ou la frite, c''est plus local. Au revoir
');


--
-- Name: web_accueil_id_seq; Type: SEQUENCE SET; Schema: public; Owner: rkjdid
--

SELECT pg_catalog.setval('web_accueil_id_seq', 1, true);


--
-- Data for Name: web_book; Type: TABLE DATA; Schema: public; Owner: rkjdid
--

INSERT INTO web_book VALUES (2, 'MarketO');
INSERT INTO web_book VALUES (3, 'Photo');
INSERT INTO web_book VALUES (4, 'Web');
INSERT INTO web_book VALUES (5, 'Design');
INSERT INTO web_book VALUES (6, 'MarketD');
INSERT INTO web_book VALUES (1, 'Communication');


--
-- Name: web_book_id_seq; Type: SEQUENCE SET; Schema: public; Owner: rkjdid
--

SELECT pg_catalog.setval('web_book_id_seq', 1, false);


--
-- Data for Name: web_categorieclient; Type: TABLE DATA; Schema: public; Owner: rkjdid
--

INSERT INTO web_categorieclient VALUES (1, '6 petits amis');
INSERT INTO web_categorieclient VALUES (2, 'Trolls !');
INSERT INTO web_categorieclient VALUES (3, 'Creeps');


--
-- Name: web_categorieclient_id_seq; Type: SEQUENCE SET; Schema: public; Owner: rkjdid
--

SELECT pg_catalog.setval('web_categorieclient_id_seq', 1, false);


--
-- Data for Name: web_pagebook; Type: TABLE DATA; Schema: public; Owner: rkjdid
--

INSERT INTO web_pagebook VALUES (8, 'books/front-2.png', 'books/CD2.png', 1);
INSERT INTO web_pagebook VALUES (9, 'books/CD3.png', 'books/front-3.jpg', 1);
INSERT INTO web_pagebook VALUES (10, 'books/front-4.jpg', 'books/CD4.png', 1);
INSERT INTO web_pagebook VALUES (11, 'books/CD5.png', 'books/front-5.png', 1);
INSERT INTO web_pagebook VALUES (12, 'books/CD6.png', 'books/CD7.png', 1);
INSERT INTO web_pagebook VALUES (13, 'books/0.png', 'books/troll0.png', 6);
INSERT INTO web_pagebook VALUES (14, 'books/troll1.png', 'books/1.png', 6);
INSERT INTO web_pagebook VALUES (15, 'books/2.png', 'books/troll2.png', 6);
INSERT INTO web_pagebook VALUES (16, 'books/3.png', 'books/troll3.png', 6);
INSERT INTO web_pagebook VALUES (17, 'books/troll4.png', 'books/4.png', 6);
INSERT INTO web_pagebook VALUES (18, 'books/5.png', 'books/troll5.png', 6);
INSERT INTO web_pagebook VALUES (19, 'books/troll6.png', 'books/6.png', 6);
INSERT INTO web_pagebook VALUES (20, 'books/frog.png', 'books/atlasAutomne.png', 3);
INSERT INTO web_pagebook VALUES (21, 'books/animauxNB.png', 'books/toRightSphinx.png', 3);
INSERT INTO web_pagebook VALUES (22, 'books/atlasNight.png', 'books/animauxCouleur.png', 3);
INSERT INTO web_pagebook VALUES (7, 'books/echos.jpg', 'books/front-1.png', 1);


--
-- Data for Name: web_client; Type: TABLE DATA; Schema: public; Owner: rkjdid
--

INSERT INTO web_client VALUES (1, 'Numero Uno', 'clients/1.mini.png', 1, 7);
INSERT INTO web_client VALUES (2, '2Pac', 'clients/2.mini.png', 1, 8);
INSERT INTO web_client VALUES (3, 'Magic', 'clients/3.mini.png', 1, 9);
INSERT INTO web_client VALUES (4, 'Quatre', 'clients/4.mini.png', 1, 10);
INSERT INTO web_client VALUES (5, 'Jackson', 'clients/5.mini.png', 1, 11);
INSERT INTO web_client VALUES (6, 'Frere de 7', 'clients/6.mini.png', 1, 12);
INSERT INTO web_client VALUES (7, '', 'clients/0.png', 2, 13);
INSERT INTO web_client VALUES (8, '', 'clients/1.png', 2, 14);
INSERT INTO web_client VALUES (9, '', 'clients/2.png', 2, 15);
INSERT INTO web_client VALUES (10, '', 'clients/3.png', 2, 16);
INSERT INTO web_client VALUES (11, '', 'clients/4.png', 2, 17);
INSERT INTO web_client VALUES (12, '', 'clients/5.png', 2, 18);
INSERT INTO web_client VALUES (13, '', 'clients/6.png', 2, 19);
INSERT INTO web_client VALUES (14, '', 'clients/7.png', 2, NULL);
INSERT INTO web_client VALUES (15, '', 'clients/bwfrog.png', 3, 20);
INSERT INTO web_client VALUES (16, '', 'clients/bwwapleg_1.png', 3, NULL);
INSERT INTO web_client VALUES (17, '', 'clients/bwfrogcroa_1.png', 3, NULL);
INSERT INTO web_client VALUES (18, '', 'clients/bwwapnoleg_1.png', 3, 21);
INSERT INTO web_client VALUES (19, '', 'clients/frog.png', 3, NULL);
INSERT INTO web_client VALUES (20, '', 'clients/colorwapleg_1.png', 3, 22);
INSERT INTO web_client VALUES (21, '', 'clients/frogcroa_1.png', 3, NULL);
INSERT INTO web_client VALUES (22, '', 'clients/greenwap_1.png', 3, NULL);


--
-- Name: web_client_id_seq; Type: SEQUENCE SET; Schema: public; Owner: rkjdid
--

SELECT pg_catalog.setval('web_client_id_seq', 1, false);


--
-- Data for Name: web_contact; Type: TABLE DATA; Schema: public; Owner: rkjdid
--

INSERT INTO web_contact VALUES (1, 'adm', 'web design', 'http://www.lesateliersdesmarques.com/');
INSERT INTO web_contact VALUES (2, 'rk', 'développement / intégration', 'romainknezevic@gmail.com');
INSERT INTO web_contact VALUES (3, 'fb', 'happy content !', '-');


--
-- Name: web_contact_id_seq; Type: SEQUENCE SET; Schema: public; Owner: rkjdid
--

SELECT pg_catalog.setval('web_contact_id_seq', 1, false);


--
-- Data for Name: web_membreequipe; Type: TABLE DATA; Schema: public; Owner: rkjdid
--

INSERT INTO web_membreequipe VALUES (1, 'Auteur / Illustrateur', '-', 6, 'Bien qu''ils soient souvent dans la lune, les éditeurs regrettent souvent que les auteurs et les illustrateurs sachent garder les pieds sur terre quand il s''agit de réclamer leurs droits.');
INSERT INTO web_membreequipe VALUES (2, 'Correcteur', 'Betty Biglips', 10, 'Le korecteur sé corigé toute les fotes d''ortograf et de gramère.');
INSERT INTO web_membreequipe VALUES (3, 'Editeur', '-', 9, 'Si on l''écoute en public, il aime tout le monde. Quand il nous parle en privé on comprend qu''il déteste tout le monde.');
INSERT INTO web_membreequipe VALUES (4, 'Graphiste - Maquetiste', '-', 7, 'Caché derrière son ordinateur, il dit qu''il travaille mais on sait bien qu''il se contente de jouer à Counter-Strike.');
INSERT INTO web_membreequipe VALUES (5, 'Imprimeur', '-', 0, 'Pour rendre une copie propre, l''imprimeur ne doit pas hésiter à se salir les mains.');
INSERT INTO web_membreequipe VALUES (6, 'Lecteur', '-', 0, 'S''abime les yeux sur du papier mais lit plus vite que son ombre.');
INSERT INTO web_membreequipe VALUES (7, 'Libraire', '-', 2, 'Les librairies ne se limitent pas à Amazon ou à la Fnac. Malheuresement pour les libraires, on a tendance à l''oublier un peu...');
INSERT INTO web_membreequipe VALUES (8, 'Marketeur', 'Lily Moneymaker', 3, 'Bien qu''il aime beaucoup les chiffres, les possibilités d''emploi du marketeur ne se limitent pas à l''édition scientifique.');
INSERT INTO web_membreequipe VALUES (9, 'Représentant', 'Spirou Globetrott', 5, 'Mercenaire de l''édition, le représentant sillonne les routes de France pour placer vos livres en librairie.');
INSERT INTO web_membreequipe VALUES (10, 'Traducteur', 'Marlene Fussy', 8, 'Pique les écrits des autres, bien qu''on n''appelle pas ça du plagiat.');


--
-- Name: web_membreequipe_id_seq; Type: SEQUENCE SET; Schema: public; Owner: rkjdid
--

SELECT pg_catalog.setval('web_membreequipe_id_seq', 1, false);


--
-- Name: web_pagebook_id_seq; Type: SEQUENCE SET; Schema: public; Owner: rkjdid
--

SELECT pg_catalog.setval('web_pagebook_id_seq', 1, false);


--
-- Data for Name: web_photomembre; Type: TABLE DATA; Schema: public; Owner: rkjdid
--

INSERT INTO web_photomembre VALUES (1, 'equipe/1.auteur.png', 1);
INSERT INTO web_photomembre VALUES (2, 'equipe/3.editeur.png', 3);
INSERT INTO web_photomembre VALUES (3, 'equipe/4.graphiste.png', 4);
INSERT INTO web_photomembre VALUES (4, 'equipe/5.imprimeur.png', 5);
INSERT INTO web_photomembre VALUES (5, 'equipe/6.lecteur.png', 6);
INSERT INTO web_photomembre VALUES (6, 'equipe/7.libraire.png', 7);
INSERT INTO web_photomembre VALUES (7, 'equipe/8.market.png', 8);
INSERT INTO web_photomembre VALUES (8, 'equipe/9.representant.png', 9);
INSERT INTO web_photomembre VALUES (9, 'equipe/10.traducteur.png', 10);
INSERT INTO web_photomembre VALUES (10, 'equipe/2.correcteur.png', 2);



SELECT pg_catalog.setval('web_photomembre_id_seq', 1, false);




