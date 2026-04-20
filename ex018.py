import math

angulo = float(input("Digite o ângulo (em graus): "))

radianos = math.radians(angulo)

seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print(f"Seno de \033[1;33m{angulo}°\033[m: \033[1;34m{seno:.2f}\033[m")
print(f"Cosseno de \033[1;33m{angulo}°\033[m: \033[1;34m{cosseno:.2f}\033[m")
print(f"Tangente de \033[1;33m{angulo}°\033[m: \033[1;34m{tangente:.2f}\033[m")
