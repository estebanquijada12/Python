from reloj import tiempo
from notificaciones import notificacion
from rich.progress import Progress, TextColumn, BarColumn, TimeRemainingColumn
from rich.console import Console
from rich.prompt import Prompt
##import storage
import storage_API as storage ##para usar la API en lugar de la base de datos local, descomenta esta línea y comenta la línea anterior
consola = Console()

def pomodoro(minutos: int = 25, actividad: str = "Trabajo"):
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TimeRemainingColumn(),
        console=consola,
    ) as progreso:
        
        tarea = progreso.add_task("[cyan]Pomodoro", total=minutos * 60)
        for segundos in tiempo(minutos):
            progreso.update(tarea, completed=(minutos * 60) - segundos)
    storage.guardar(actividad, minutos)
    notificacion("Pomodoro terminado", "¡Tiempo de descanso!")
        
        
if __name__ == "__main__":
    
    storage.db_init()
    
    consola.clear()
    consola.print("[bold white]🍅 Temporizador Pomodoro Iniciado[/bold white]\n")
    

    try:
        #25 min de trabajo, 5 de descanso
        tarea = Prompt.ask("[bold cyan]¿En qué vas a trabajar ahora?[/bold cyan]")
        consola.print()
        pomodoro(25,tarea)  
        pomodoro(5, "Descanso")  # 5 minutos de descanso
        
    except KeyboardInterrupt:
        consola.print("\n[bold red]🛑 Pomodoro interrumpido por el usuario.[/bold red]")