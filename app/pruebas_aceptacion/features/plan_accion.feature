Característica: Cargar Plan de Acción
    Como administrador quiero cargar el plan de Acción
    de tal manera que los PTC puedan visualizar las actividades
    que se deben llevar a cabo.

    Escenario: Subir el archivo de Plan de Acción
        Dado que ingreso al sistema "http://192.168.33.10:8000/"
        Y presiono la opcion para loguearme LOGIN
        Y escribo mi usuario "Estudiante" y mi contraseña "est123"
        Y presiono el boton Login
        Y presiono el boton  Subir documento
        Y escribo el nombre del archivo "Plan"
        Y selecciono el archivo "plan1.pdf"
        Cuando presiono el boton Subir
        Entonces puedo ver el mensaje de exito "¡Se ha subido con éxito tu documento!"