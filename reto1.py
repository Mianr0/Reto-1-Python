reconocimiento_etnico = (input())
estrato_socioeconomico = int(input())
ingresos_del_nucleo_familiar = int(input())
puntaje = float (0)

if (reconocimiento_etnico != "sin reconocimiento" and reconocimiento_etnico != "afrodescendiente" and reconocimiento_etnico != "indigena" and reconocimiento_etnico != "raizal" and reconocimiento_etnico != "palenquero" and reconocimiento_etnico != "gitano"):
    print("Se presento un error")

else:
    if (estrato_socioeconomico != (1) and estrato_socioeconomico != (2) and estrato_socioeconomico != (3) and estrato_socioeconomico != (4) and estrato_socioeconomico != (5) and estrato_socioeconomico != (6)):
        print("Se presento un error")

    else:

        if (reconocimiento_etnico == "sin reconocimiento"):
            puntaje = (puntaje + 0)

        if (reconocimiento_etnico == "afrodescendiente"):
            puntaje = (puntaje + 9)

        if (reconocimiento_etnico == "indigena"):
            puntaje = (puntaje + 10)

        if (reconocimiento_etnico == "raizal"):
            puntaje = (puntaje + 11)

        if (reconocimiento_etnico == "palenquero"):
            puntaje = (puntaje + 12)

        if (reconocimiento_etnico == "gitano"):
            puntaje = (puntaje + 13)

        if (estrato_socioeconomico == 1):
            puntaje = (puntaje + 15)

        if (estrato_socioeconomico == 2):
            puntaje = (puntaje + 13)

        if (estrato_socioeconomico == 3):
            puntaje = (puntaje + 11)

        if (estrato_socioeconomico == 4):
            puntaje = (puntaje + 7)

        if (estrato_socioeconomico == 5):
            puntaje = (puntaje + 0)

        if (estrato_socioeconomico == 6):
            puntaje = (puntaje + 0)

        if (ingresos_del_nucleo_familiar < 908526):
            puntaje = (puntaje + 20)

        if (ingresos_del_nucleo_familiar >= 908526 and ingresos_del_nucleo_familiar < 1817052):
            puntaje = (puntaje + 14)

        if (ingresos_del_nucleo_familiar >= 1817052 and ingresos_del_nucleo_familiar <= 2725578):
            puntaje = (puntaje + 12)

        if (ingresos_del_nucleo_familiar > 2725578 and ingresos_del_nucleo_familiar <= 3634104):
            puntaje = (puntaje + 9)

        if (ingresos_del_nucleo_familiar > 3634104 and ingresos_del_nucleo_familiar <= 4542630):
            puntaje = (puntaje + 0)

        if (puntaje < 30):
            print("El candidato no continua en el proceso de seleccion")

        if (puntaje >= 30):
            print("El candidato continua en el proceso de seleccion")