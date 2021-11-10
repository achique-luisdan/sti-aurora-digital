Feature: Enviar Solicitud

Como Usuario 
Deseo enviar una solicitud 
Así podré aspirar a nuevos permisos y privilegios
    
Scenario Outline: Selección de Aspiración

    Given que el usuario ha suministrados los detalles de su cuenta de usuario de forma satisfactoria
    When no selecciona al menos una Aspiración <aspiraciones>, <comentario>
    Then se emite un mensaje de error invitandolé a seleccionar una Aspiración

Examples: 
   | aspiraciones  | comentario      |
   |   None        | Sin comentarios |
   |    1          | Sin comentarios |
   |    2          | Sin comentarios |
   |    3          | Sin comentarios |