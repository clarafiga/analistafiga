#visao math case

mes = int(input("Informe o mes de nascimento"))
match mes:
    case 1:
        signo="aquario"
    case 2:
        signo= "peixes"
    case 3:
        signo="aries"
    case 4:
        signo="touro"
    case 5:
        signo="gemeos"
    case 6:
        signo="cancer"
    case 7:
        signo="leao"
    case 8:
        signo="libra"
       

print(f"{signo}.")