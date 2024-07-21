import matplotlib.pyplot as plt

# Número complexo (exemplo)
z = 4 + 3j

# Extração das partes real e imaginária
real_part = z.real
imag_part = z.imag

# Plotagem
plt.scatter(real_part, imag_part, color='red', label='Número Complexo')
plt.axhline(y=0, color='gray', linestyle='--')
plt.axvline(x=0, color='gray', linestyle='--')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.title('Plotagem de Número Complexo')
plt.legend()
plt.grid(True)
plt.savefig("test_matplotlib.png")
