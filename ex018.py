import math

angulo = float(input("Digite o ângulo (em graus): "))

radianos = math.radians(angulo)

seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print(f"Seno de {angulo}°: {seno:.2f}")
print(f"Cosseno de {angulo}°: {cosseno:.2f}")
print(f"Tangente de {angulo}°: {tangente:.2f}")
