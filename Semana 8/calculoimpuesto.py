def calculo_Impuesto(monto):
  impuesto = monto * 0.20
  return impuesto

monto_ingresado = 1000
impuesto_calculado = calcular_impuesto(monto_ingresado)

print(f"El impuesto del 20% sobre ${monto_ingresado} es: ${impuesto_calculado:.2f}")

