def get_color_backgrounds() -> list:
    backgrounds =   [
                        "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(28, 249, 255, 255), stop:0.231156 rgba(81, 255, 199, 255), stop:0.484561 rgba(64, 255, 185, 255), stop:0.720268 rgba(52, 255, 177, 255), stop:0.994987 rgba(42, 255, 104, 255));",
                        "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0.005013 rgba(42, 255, 142, 255), stop:0.116883 rgba(108, 199, 196, 255), stop:0.200371 rgba(141, 171, 222, 255), stop:0.272727 rgba(162, 154, 239, 255), stop:0.352505 rgba(181, 137, 255, 255), stop:0.515439 rgba(170, 111, 255, 255), stop:0.768844 rgba(150, 56, 255, 255), stop:1 rgba(116, 20, 171, 255))" 
                    ]
    return backgrounds

def get_easy_questions() -> list:
    questions = [
                    ("Resuelva el siguiente problema: 10 + 5 x 3 = :",25),
                    ("El reloj de una iglesia tarda un segundo en dar una campanada,\n ¿Cuanto tardara en dar 12 campanadas?\n",11),
                    ("¿Cual es la diferencia entre media docena de docenas de huevo y seis docenas de huevo?\n",0),
                    ("¿Cuanto es?:\n28+45+65+85+110 = ",333),
                    ("¿Cual es la respuesta de la siguiente operacion?\n 3 + 3 * 3 + 3 =",15),
                    ("En un cajon hay 6 calcetines rojos y 6 calcetines verdes,\n¿Cuantos calcetines debes tomar para asegurarte de que te salga un par?\n",3),
                    ("Un oso camina 27 km hacia el norte, despues camina otros 15 km al este pero regresa 5,\nal final sigue hacia el norte por 13 km mas,\n¿Cuantos kilometros recorrio?\n",60),
                    ("Cinco maquinas son capaces de fabricar 5 articulos en 5 minutos. Con este ritmo de produccion,\n ¿Cuantos minutos tardaran 100 maquinas en hacer 100 articulos?\n",5),
                    ("Tienes 5 conejos, 20 cerdos y 5 caballos, si nombras a los cerdos, caballos, ¿Cuantos caballos tienes?\n",5),
                    ("En una habitacion hay 4 gatos, cada gato ve 3 gatos,\n ¿Cuantos gatos hay en total?\n",4)
                ]
    return questions

def get_avrg_questions() -> list:
    questions = [
                    ("En una clase hay más de 20 y menos de 30 alumnos.\nSi se forman cuatro 4 grupos de 4 alumnos, sobran 2 y se agrupan 5 de 5, sobra 1.\n¿Cuántos alumnos hay en la clase?\n",26),
                    ("¿Qué número corresponde para seguir la serie?\n1, 3, 6, 10, 15, 21 … ",28),
                    ("En un número de tres dígitos, el del medio es 4 veces mayor que el tercero y el primero es tres unidades menos que el segundo.\n¿De qué número se trata?\n",141),
                    ("En una librería venden un paquete de 10 cuadernos y 6 carpetas por 100 pesos.\nTambién hay otro paquete de 10 carpetas y 6 cuadernos por 92 pesos.\n¿Cuánto vale cada cuaderno?\n",5),
                    ("Irma tiene el doble de edad que su hermano Manuel, pero la mitad de su padre.\nDentro de 50 años, Manuel tendrá la mitad de edad que su padre.\n¿Qué edad tiene Irma?\n",50),
                    ("El año 1987 tuvo una particularidad, porque si sumas las dos primeras cifras y las dos últimas, obtienes las cifras del medio (19+87=98).\nSegún esto, ¿cuál será el próximo año en el que se cumpla la misma curiosidad matemática?\n",2307),
                    ("Un coleccionista debe embalar con cuidado su colección de jarrones y jarras.\nConsiguió varias cajas: en cada una caben 8 jarrones o 10 jarras. En total, envió 96 piezas.\nSabiendo que hay más jarrones y jarras, sin que quedara ningún hueco vacío.\n¿Cuántas cajas se utilizaron?\n",11),
                    ("En una carrera de coches, un coche rojo que circula a una velocidad constante de 60 km/h adelanta a un coche azul, que circula a 45 km/h.\nEn este preciso momento, los dos coches están juntos.\nEl conductor del coche rojo, necesita parar cinco minutos para hacer sus necesidades.\n¿Cuántos minutos tiene que seguir circulando el coche rojo, para poder detenerse 5 minutos, sin riesgo a ser adelantado por el coche azul?\n",15),
                    ("Una habitación especial de un parque de atracciones está forrada de espejos completamente.\nLas 4 paredes, el techo y el suelo son enormes espejos que lo cubren todo.\n¿Cuántas veces puede verse una persona reflejada si se coloca justo en el centro de la habitación?\n",0),
                    ("Existe un lugar en el planeta formado por 100 islas agrupadas en forma de círculo. En cada isla hay una casa.\nEn total hay 100 personas que viven en este lugar. Algunos siempre mienten y otros siempre dicen la verdad.\nNos proponemos investigar quien miente y quien no y las 100 personas siempre nos dicen lo mismo:\n” Yo no miento, los que mienten son mis dos vecinos, el de la derecha y el de la izquierda”\n¿Sabrías decir cuántos mentirosos hay en las islas?\n",50)
                ]
    return questions

def get_hard_questions() -> list:
    questions = [
                    ("Para ingresar al colegio San Benito, un grupo de 80 alumnos hicieron 3 examenes para ser admitidos. Al final se supo que\n28 aprobaron el primero, 32 el segundo y 30 el tercero, 8 aprobaron el primero, 32 el segundo y 30 el tercero,\n8 aprobaron el primero y segundo, 10 el segundo y tercero, 4 aporbaron los tres y 18 no aprobaron ninguno.\n¿Cuántos fueron admitidos si solo es necesario aprobar 2 examenes?\n",24),
                    ("En una encuesta realizada de 100 personas acerca de sus inversiones se observo que 45 poseían acciones, 60 bonos y 90 poseían las dos.\n\n¿Cuántas personas no tienen acciones?\n",50),
                    ("Del total de damas de una oficina, 2/3 son morenas, 1/5 tienen ojos azules y 1/6 son morenas con ojos azules.\n\n¿Qué fracción no son ni morenas, ni tienen ojos azules? (Ingrese su respuesta en decimales):\n",.30),
                    ("Complete el siguiente orden númerico: 8, 18, 11, 15, 5, 4, 14, 9, 19, 1, 7, 17, 6, 16 ...",10),
                    ("Un hombre compra un caballo por 60$. Vende el caballo por 70$. Después vuelve a comprar el caballo por 80$ y lo vende, otra vez, por 90$.\nAl final, ¿cuánto dinero ganó o perdió el hombre? (SOLO INGRESE LA CANTIDAD NÚMERICA)\n",20),
                    ("Se llevó a cabo una investigación con 1000 personas, para determinar que medio utilizan para conocer las noticias del día.\nSe encontró que 400 personas escuchan las noticias en forma regular por TV, 300 personas escuchan las noticias por la Radio y 275 se enteran de las noticias por ambos medios.\n¿Cuántas de las personas investigadas no escuchan ni ven las noticias?\n",575),
                    ("Se realizó una encuesta a 11 personas, sobre sus preferencias por dos tipos de productos A y B. \nObteniéndose lo siguientes resultados: \nEl número de personas que prefirieron uno solo de los productos fueron 7. \nEl número de personas que prefirieron ambos productos fue igual al número de personas que no prefirió ninguno de los dos productos. \nEl número de personas que no prefieren el producto A y prefirieron el producto B fueron 3. \n¿Cuántas personas prefirieron el producto B solamente?\n",5),
                    ("Un famoso matemático escribió en 1864: «En algún momento de mi vida, hace algunos años, el cuadrado de mi edad coincidió con dicho año».\n¿En qué año nació el matemático?\n",1806),
                    ("En un avión viajan 120 personas, de los cuales: \n● Los 2/3 de ellos no beben \n● Los 4/5 de ellos no fuman \n● 72 no fuman ni beben \n¿Cuántas personas fuman y beben o, ni fuman ni beben?\n",88),
                    ("De un grupo de 242 alumnos del CPU – USAT, se sabe que 95 practican natación, 82 practican atletismo y 110 no practican estos deportes.\n¿Cuántos alumnos practican estos dos deportes?\n",45)
                ]           
    return questions