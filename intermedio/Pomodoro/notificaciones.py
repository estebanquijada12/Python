from plyer import notification

def notificacion(titulo: str, mensaje: str):
    notification.notify(
        title=titulo,
        message=mensaje,
        app_name="Pomodoro",
        timeout=10
    )

