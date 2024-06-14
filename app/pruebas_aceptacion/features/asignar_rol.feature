Característica: Asignar rol a un usuario
    Como administrador del sistema CACEI WEB SERVER
    quiero agregar roles ya sean PTC o estudiantes, 
    de tal manera que pueda darles acceso a funciones y herramientas a sus roles correspondientes

    Escenario: Asignar rol PTC
        Dado que ingreso al sistema "http://192.168.33.10:8000"
        Y presiono la opcion para loguearme LOGIN
        Y escribo mi usuario "cord" y mi contraseña "cord123"
        Y presiono el boton Login
        Y selecciono la opción de Tutores
        Y selecciono la opcion editar del usuario
        Y selecciono tutor en tipo user
        Cuando presiono el botón Registrarse
        Entonces puedo ver la lista de Usuarios

    Escenario: Asignar rol Estudiante
        Dado que ingreso al sistema "http://192.168.33.10:8000"
        Y presiono la opcion para loguearme LOGIN
        Y escribo mi usuario "cord" y mi contraseña "cord123"
        Y presiono el boton Login
        Y selecciono la opción de Tutores
        Y selecciono la opcion editar del usuario
        Y selecciono Estudiante en tipo user
        Cuando presiono el botón Registrarse
        Entonces puedo ver la lista de Usuarios