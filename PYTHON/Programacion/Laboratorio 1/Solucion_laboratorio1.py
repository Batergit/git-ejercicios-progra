def CalcularNumeroMagico(fecha):
    # SE SEPARAN LAS FECHAS EN DIA, MES Y ANIO
    dia = fecha%100                 # EXTRAE LOS DOS ULTIMOS DIGITOS
    mes = int(fecha/100)%100        # DESCARTA LOS DOS ULTIMOS DIGITOS Y EXTRAE LOS DOS NUEVOS DIGITOS DEL FINAL
    anio = int(fecha/10000)         # DESCARTA LOS CUATRO ULTIMOS DIGITOS PARA QUEDARNOS CON LOS CORRESPONDIENTES AL ANIO

    # CALCULO DEL VALOR DEL NUMERO MAGICO
    return (dia * mes * anio) / 33

if __name__ == '__main__':
    fecha = int( input('Ingrese la fecha de nacimiento en formato aaaammdd: ') )

    numeroMagico = CalcularNumeroMagico(fecha)
    print("El numero magico es", numeroMagico)