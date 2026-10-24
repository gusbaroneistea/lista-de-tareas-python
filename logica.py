"""Funciones para administrar la lista de tareas."""

from typing import TypedDict


class Tarea(TypedDict):
    """Representa una tarea y su estado de finalización."""

    nombre: str
    completada: bool


def agregar_tarea(tareas: list[Tarea], nombre: str) -> None:
    """Agrega una tarea pendiente a la lista.

    Args:
        tareas: Lista que almacena las tareas.
        nombre: Descripción de la nueva tarea.
    """
    nombre_limpio = nombre.strip()
    if not nombre_limpio:
        raise ValueError("El nombre de la tarea no puede estar vacío.")
    tareas.append({"nombre": nombre_limpio, "completada": False})


def listar_tareas(tareas: list[Tarea]) -> list[Tarea]:
    """Devuelve las tareas existentes.

    Args:
        tareas: Lista que almacena las tareas.

    Returns:
        Una lista con las tareas actuales.
    """
    return list(tareas)


def marcar_completada(tareas: list[Tarea], numero: int) -> bool:
    """Marca una tarea como completada usando su posición desde 1.

    Args:
        tareas: Lista que almacena las tareas.
        numero: Número de tarea mostrado en pantalla.

    Returns:
        True si se encontró la tarea; False si el número no es válido.
    """
    if numero < 1 or numero > len(tareas):
        return False
    tareas[numero - 1]["completada"] = True
    return True


def eliminar_tarea(tareas: list[Tarea], numero: int) -> bool:
    """Elimina una tarea usando su posición desde 1.

    Args:
        tareas: Lista que almacena las tareas.
        numero: Número de tarea mostrado en pantalla.

    Returns:
        True si se eliminó la tarea; False si el número no es válido.
    """
    if numero < 1 or numero > len(tareas):
        return False
    tareas.pop(numero - 1)
    return True
