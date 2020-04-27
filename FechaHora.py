class FechaHora:
    __Dia = 0
    __Mes = 0
    __Anio = 0
    __Hora = 0
    __Minuto = 0
    __Segundo = 0

    def __init__(self, dia = 1, mes = 1, anio = 2020, hora = 0, minuto = 0, segundo = 0):
        if (anio > 0):
            if (mes in range(1,13)):
                if (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
                    if (dia in range(1,31)):
                        if (hora in range(24)):
                            if (minuto in range(60)):
                                if (segundo in range(60)):
                                    self.__Anio = anio
                                    self.__Mes = mes                    #genera el objeto si es un mes de 30 dias
                                    self.__Dia = dia                    #y los datos ingresados son correctos
                                    self.__Hora = hora
                                    self.__Minuto = minuto
                                    self.__Segundo = segundo
                                else:
                                    print('El rango de valores válidos es de 0 a 59.')
                            else:
                                print('El rango de valores válidos es de 0 a 59.')
                        else:
                            print('El rango de valores válidos es de 0 a 23.')
                    else:
                        print('El mes ' + str(mes) + ' solo tiene 30 días.')
                elif (mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
                    if (dia in range(1,32)):
                        if (hora in range(24)):
                            if (minuto in range(60)):
                                if (segundo in range(60)):
                                    self.__Anio = anio
                                    self.__Mes = mes                    #genera el objeto si es un mes de 31 dias
                                    self.__Dia = dia                    #y los datos ingresados son correctos
                                    self.__Hora = hora
                                    self.__Minuto = minuto
                                    self.__Segundo = segundo
                                else:
                                    print('El rango de valores válidos es de 0 a 59.')
                            else:
                                print('El rango de valores válidos es de 0 a 59.')
                        else:
                            print('El rango de valores válidos es de 0 a 23.')
                    else:
                        print('El mes ' + str(mes) + ' solo tiene 31 días.')
                else:
                    if ((anio%4 == 0) & (anio%100 != 0)) or (anio%400 == 0):
                        if (dia in range(1,30)):
                            if (hora in range(24)):
                                if (minuto in range(60)):
                                    if (segundo in range(60)):
                                        self.__Anio = anio              #genera el objeto si es que es un año bisiesto,
                                        self.__Mes = mes                #es el mes de febrero y los datos ingresados son correctos
                                        self.__Dia = dia
                                        self.__Hora = hora
                                        self.__Minuto = minuto
                                        self.__Segundo = segundo
                                    else:
                                        print('El rango de valores válidos es de 0 a 59.')
                                else:
                                    print('El rango de valores válidos es de 0 a 59.')
                            else:
                                print('El rango de valores válidos es de 0 a 23.')
                        else:
                            print('El mes ' + str(mes) + ' solo tiene 29 días por ser año bisiesto.')
                    else:
                        if (dia in range(1,29)):
                            if (hora in range(24)):
                                if (minuto in range(60)):
                                    if (segundo in range(60)):
                                        self.__Anio = anio
                                        self.__Mes = mes                #genera el objeto si es que no es un año bisiesto,
                                        self.__Dia = dia                #es el mes de febrero y los datos ingresados son correctos
                                        self.__Hora = hora
                                        self.__Minuto = minuto
                                        self.__Segundo = segundo
                                    else:
                                        print('El rango de valores válidos es de 0 a 59.')
                                else:
                                    print('El rango de valores válidos es de 0 a 59.')
                            else:
                                print('El rango de valores válidos es de 0 a 23.')
                        else:
                            print('El mes ' + str(mes) + ' solo tiene 28 días.')
            else:
                print('Los años solo tienen 12 meses.')
        else:
            print('Año inválido.')

    def Mostrar(self):
        print('Año:{} Mes:{} Día:{} Hora:{} Minuto:{} Segundo:{}'.format(self.__Anio,self.__Mes,self.__Dia,self.__Hora,self.__Minuto,self.__Segundo))

    def PonerEnHora(self, nuevaHora = 0, nuevoMinuto = 0, nuevoSegundo = 0):
        if (nuevaHora in range(24)):
            if (nuevoMinuto in range(60)):
                if (nuevoSegundo in range(60)):
                    self.__Hora = nuevaHora
                    self.__Minuto = nuevoMinuto
                    self.__Segundo = nuevoSegundo
                else:
                    print('El rango de valores válidos es de 0 a 59.')
            else:
                print('El rango de valores válidos es de 0 a 59.')
        else:
            print('El rango de valores válidos es de 0 a 23.')

    def AdelantarHora(self, h = 0, m = 0):
        if (h >= 0):
            if (m >= 0):
                    self.__Hora += h
                    self.__Minuto += m
            else:
                print('El valor para minuto es inválido.')
        else:
            print('El valor para hora es inválido.')
        #Actualiza Hora
        if (self.__Minuto >= 60):
            self.__Hora += self.__Minuto // 60
            self.__Minuto = self.__Minuto - ((self.__Minuto//60)* 60)
        #Actualiza Dia
        if(self.__Hora >= 24):
            self.__Dia += self.__Hora // 24
            self.__Hora = self.__Hora - ((self.__Hora//24)*24)
        #Actualiza Mes
        if (self.__Mes == 4) or (self.__Mes == 6) or (self.__Mes == 9) or (self.__Mes == 11):
            if (self.__Dia > 30):
                self.__Mes += self.__Dia // 30
                self.__Dia = self.__Dia - ((self.__Dia // 30)* 30)
        elif (self.__Mes == 1) or (self.__Mes == 3) or (self.__Mes == 5) or (self.__Mes == 7) or (self.__Mes == 8) or (self.__Mes == 10) or (self.__Mes == 12):
            if (self.__Dia > 31):
                self.__Mes += self.__Dia // 31
                self.__Dia = self.__Dia - ((self.__Dia // 31)* 31)
        else:
            if ((self.__Anio%4 == 0) & (self.__Anio%100 != 0)) or (self.__Anio%400 == 0): #Mes Bisiesto
                if (self.__Dia > 29):
                    self.__Mes += self.__Dia // 29
                    self.__Dia = self.__Dia - ((self.__Dia // 29)* 29)
            elif (self.__Dia > 28):
                self.__Mes += self.__Dia // 28
                self.__Dia = self.__Dia - ((self.__Dia // 28)* 28)
        #Actualiza Año
        if (self.__Mes > 12):
            self.__Anio += self.__Mes // 12
            self.__Mes = self.__Mes - ((self.__Mes // 12)* 12)
