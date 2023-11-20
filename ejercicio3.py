num1=int(input("ingrese el primer numero:"));
num2=int(input("ingrese el otro numero :"));
num3=int(input("ingrese el otro numero:"));
suma=num1+num2+num3;
if suma%7==0:
    mensaje=("la suma 7 es el muitiple de",suma);
else:
    mensaje=("la suma 7 no es multiple de ",suma);
print(mensaje);
