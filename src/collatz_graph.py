import matplotlib.pyplot as plt
import os

def collatz_iterations(n):
    count = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        count += 1
    return count

n_values = list(range(1, 10001))
iterations = [collatz_iterations(n) for n in n_values]

plt.figure(figsize=(10, 6))
plt.scatter(iterations, n_values, s=1, color='blue')
plt.xlabel("Número de Iteraciones")
plt.ylabel("Número Inicial de la Secuencia")
plt.title("Número de Collatz (Conjetura 3n+1)")
plt.grid()
plt.show()

output_dir = "src"
os.makedirs(output_dir, exist_ok=True)

file_path = os.path.join(output_dir, "collatz_graph.py")
with open(file_path, "w") as f:
    f.write("import matplotlib.pyplot as plt\n" +
            "\ndef collatz_iterations(n):\n" +
            "    count = 0\n" +
            "    while n != 1:\n" +
            "        n = n // 2 if n % 2 == 0 else 3 * n + 1\n" +
            "        count += 1\n" +
            "    return count\n\n" +
            "n_values = list(range(1, 10001))\n" +
            "iterations = [collatz_iterations(n) for n in n_values]\n\n" +
            "plt.figure(figsize=(10, 6))\n" +
            "plt.scatter(iterations, n_values, s=1, color='blue')\n" +
            "plt.xlabel(\"Número de Iteraciones\")\n" +
            "plt.ylabel(\"Número Inicial de la Secuencia\")\n" +
            "plt.title(\"Número de Collatz (Conjetura 3n+1)\")\n" +
            "plt.grid()\n" +
            "plt.show()\n")

print(f"Código guardado en {file_path}")
#python src/collatz_graph.py: comando para ejecutar el programa