# Lista de tareas por consola

## ¿Qué hace?

Es una aplicación de consola escrita en Python para administrar tareas durante la ejecución del programa. Permite agregar tareas, verlas en una tabla, marcarlas como completadas y eliminarlas.

## Librerías utilizadas

- **Rich**: presenta el menú y los mensajes con colores.
- **Tabulate**: organiza la lista de tareas en una tabla de texto.

## Requisitos

- Python 3.10 o superior.
- `pip`.

## Instalación

1. Clonar o descargar este repositorio.
2. Abrir una terminal dentro de la carpeta del proyecto.
3. Crear el entorno virtual:

   ```powershell
   python -m venv .venv
   ```

4. Activarlo en Windows PowerShell:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

   En Linux o macOS:

   ```bash
   source .venv/bin/activate
   ```

5. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

```bash
python main.py
```

Las tareas se guardan en memoria y se pierden cuando se cierra el programa.

## Estructura

```text
lista_tareas/
├── main.py
├── logica.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Integrantes

- **[Gustavo Sebastian Barone]**

## Autoría y alcance

Proyecto individual realizado con fines educativos para practicar módulos propios, librerías de terceros, manejo de errores, anotaciones de tipos y docstrings.
