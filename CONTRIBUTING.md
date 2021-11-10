Nos encantaria recibir tus aportes, por ello hemos preparado este humilde material donde podras conocer algunas consideraciones que debes tener en cuenta para iniciar en tu proceso de colaboración y acompañamiento:

## USAMOS GIT Y GITLAB

En primera instancia, se debe destacar que con la finalidad de optimizar las tareas de integración continua del código fuente realizado por los distintos miembros del Equipo se hace uso de una plataforma web llamada GitLab basada en el sistema de control de versiones Git, sistema orientado a ramas (branch) que respaldan diversas versiones de los repositorios del proyecto.

Esto permite el versionamiento asistido (basado en git) en los proyectos, brindando herramientas para realizar las operaciones de integracion, con un alto nivel de automatización y detección de posibles errores.

## TENEMOS UNA ESTRATEGIA DE RAMIFICACIÓN E INTEGRACIÓN CONTINUA

En este sentido, como parte de una Estrategia de Ramificación e Integración Continua se implementaron las siguientes ramas:
* **Desarrollo** (develop)
* **Principal o Estable** (master)
* **Producción** (production)

A su vez, cada miembro puede tener su propia rama, donde al iniciar cada iteración deberá hacer una actualización de su rama a partir de la rama principal. 

Durante el tiempo de desarrollo de la iteración el podrá realizar cambios y mejoras a su rama, y paulatinamente un miembro seleccionado podra concretar los aportes de cada participante funcionadolos en una unica rama, la rama de desarrollo. 

Posterior a la realización de las pruebas del prototipo, la rama de desarrollo se fusionará con la rama principal causando un incremento en las funcionalidades.

Finalmente, la rama de producción será la encargada de que a partir de la rama principal o estable, esta sea clonada a la misma para la realización de los ajustes pertinentes para el despliegue del sistema en su respectiva plataforma tecnológica.

## TU TAMBIEN PUEDES SER PARTE DEL EQUIPO DE DESARROLLO

**¿Deseas crearte una rama?**
Sip!

Entonces, debes tener en cuenta algunas convenciones adoptada por los miembros del Equipo de Desarrollo:

1.  Nombre de la rama, surge a partir de la inicial del primer nombre, más el primer apellido (Ej. ltorvalds, bgates, sjobs)
2.  Creala siempre en función a lo ultimo, asi lo mismo se encuentre en desarrollo (develop).

**¿Cómo subir tus aportes?**

Es importante que hayas descargado el git, te hayas creado una cuenta y posteriormente una ramas personal y mediante las instrucciones git commit -m "Comentario del cambio que realizaste" y git push origin más el nombre de tu rama, podras facilmente subir y comentar tus aportes. 

Te invitamos a consultar un material inductivo que hemos dejado al final de un post de ayuda almacenado en el Trello: [Primeros Pasos en GitLab] ([Inducción Técnica]).

## AGREDECIMIENTO

Gracias por todo el apoyo.

## CONTACTO 

Podéis encontrar más información en... 
> Tableros del proyecto (https://trello.com)
> Wiki del sistema (https://github.com/) En construcción...
> Repositorios del proyecto (https://gitlab.com/team-pura-via/sti-aurora-digital)

¿Tienes alguna sugerencia? Este proyecto es de código abierto, y sobre todo es orientado a ti venezolano y venezolana hermosa. Ayúdanos a mejorarlo.

Escríbenos déjanos algún comentario, queremos saber de tí.
 
