Feature: Registrar Usuarios

Como Usuario
Deseo registrarme  
Así podré formar parte de la Comunidad
    
Scenario Outline: Validación de campos obligatorios
    Given que el Usuario ha seleccionado la opción registrarse
    When le falto completar algún campo obligatorio (<username>, <first_name>, <last_name>, <email>, <imagen_de_perfil>, <sexo>, <fecha_de_nacimiento>, <password1>, <password2>)
    Then se emite un mensaje de error con el campo incompleto ("<mensaje>")

Examples: 
   | username | first_name | last_name | email              | imagen_de_perfil  | sexo | fecha_de_nacimiento | password1 | password2   | mensaje                                              |
   | None     | Linus      | Torvarld  | linux@correo.com   | ruta.png          | M    | 10/01/1967          | contrasea1 | contrasea1 |¡Complete el campo obligatorio Nombre de Usuario!     |
   | linux    | None       | Torvarld  | linux@correo.com   | ruta.png          | M    | 10/01/1967          | contrasea1 | contrasea1 |¡Complete el campo obligatorio Nombres!               |
   | linux    | Linus      | None      | linux@correo.com   | ruta.png          | M    | 10/01/1967          | contrasea1 | contrasea1 |¡Complete el campo obligatorio Apellidos!             |
   | linux    | Linus      | Torvarld  | None               | ruta.png          | M    | 10/01/1967          | contrasea1 | contrasea1 |¡Complete el campo obligatorio Correo Eléctronico!    |
   | linux    | Linus      | Torvarld  | linux@correo.com   | None              | M    | 10/01/1967          | contrasea1 | contrasea1 |¡Por defecto, le será asignada una foto de perfil!    |
   | linux    | Linus      | Torvarld  | linux@correo.com   | ruta.png          | None | 10/01/1967          | contrasea1 | contrasea1 |¡Complete el campo obligatorio Sexo!                  |
   | linux    | Linus      | Torvarld  | linux@correo.com   | ruta.png          | M    | None                | contrasea1 | contrasea1 |¡Complete campo obligatorio Fecha de Nacimiento!      |
   | linux    | Linus      | Torvarld  | linux@correo.com   | ruta.png          | M    | 10/01/1967          | None       | contrasea1 |¡Complete campo obligatorio Contraseña!               |
   | linux    | Linus      | Torvarld  | linux@correo.com   | ruta.png          | M    | 10/01/1967          | contrasea1 | None       |¡Complete campo obligatorio Contraseña (Confirmación)!|