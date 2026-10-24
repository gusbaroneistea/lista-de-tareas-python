"""Punto de entrada de la aplicación Lista de tareas."""

from rich.console import Console
from rich.prompt import IntPrompt, Prompt
from tabulate import tabulate

from logica import agregar_tarea, eliminar_tarea, listar_tareas, marcar_completada

console = Console()


def mostrar_menu() -> None:
    """Muestra las opciones disponibles para el usuario."""
    console.print("\n[bold cyan]=== LISTA DE TAREAS ===[/bold cyan]")
    console.print("1. Ver tareas")
    console.print("2. Agregar tarea")
    console.print("3. Marcar tarea como completada")
    console.print("4. Eliminar tarea")
    console.print("5. Salir")


def mostrar_tareas(tareas: list[dict[str, object]]) -> None:
    """Muestra las tareas en una tabla."""
    if not tareas:
        console.print("[yellow]Todavía no hay tareas cargadas.[/yellow]")
        return

    filas = []
    for indice, tarea in enumerate(tareas, start=1):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        filas.append([indice, tarea["nombre"], estado])

    tabla = tabulate(filas, headers=["N.º", "Tarea", "Estado"], tablefmt="grid")
    console.print("[bold cyan]Mis tareas[/bold cyan]")
    console.print(tabla)


def ejecutar() -> None:
    """Ejecuta el menú principal y procesa las opciones seleccionadas."""
    tareas: list[dict[str, object]] = []

    while True:
        mostrar_menu()
        try:
            opcion = IntPrompt.ask("Elegí una opción", choices=["1", "2", "3", "4", "5"])

            if opcion == 1:
                mostrar_tareas(listar_tareas(tareas))
            elif opcion == 2:
                nombre = Prompt.ask("Escribí el nombre de la tarea").strip()
                if not nombre:
                    console.print("[red]El nombre no puede estar vacío.[/red]")
                else:
                    agregar_tarea(tareas, nombre)
                    console.print("[green]Tarea agregada correctamente.[/green]")
            elif opcion == 3:
                mostrar_tareas(listar_tareas(tareas))
                if tareas:
                    numero = IntPrompt.ask("Número de tarea", default=1)
                    if marcar_completada(tareas, numero):
                        console.print("[green]Tarea marcada como completada.[/green]")
                    else:
                        console.print("[red]Ese número de tarea no existe.[/red]")
            elif opcion == 4:
                mostrar_tareas(listar_tareas(tareas))
                if tareas:
                    numero = IntPrompt.ask("Número de tarea a eliminar", default=1)
                    if eliminar_tarea(tareas, numero):
                        console.print("[green]Tarea eliminada.[/green]")
                    else:
                        console.print("[red]Ese número de tarea no existe.[/red]")
            elif opcion == 5:
                console.print("[bold]¡Hasta luego![/bold]")
                break
        except (ValueError, TypeError) as error:
            console.print(f"[red]Entrada inválida: {error}[/red]")
        except (EOFError, KeyboardInterrupt):
            console.print("\n[yellow]Programa finalizado por el usuario.[/yellow]")
            break


if __name__ == "__main__":
    ejecutar()
