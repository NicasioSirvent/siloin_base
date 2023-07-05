```mermaid
sequenceDiagram
    participant Usuario
    participant Home
    participant Login
    participant App

    Usuario->>Home: Navegar a /home
    Home-->>Usuario: Mostrar página de inicio

    Usuario->>Home: Hacer clic en "Encontrar Dispositivo"
    Home-->>Usuario: Redirigir a /login

    Usuario->>Login: Ingresar credenciales
    Login-->>Usuario: Verificación de credenciales

    Usuario->>App: Acceder a /app
    App-->>Usuario: Mostrar aplicación principal

    Usuario->>Home: Navegar a /home/soluciones
    Home-->>Usuario: Mostrar beneficios y descripción de la aplicación

    Usuario->>Home: Navegar a /home/tecnologia
    Home-->>Usuario: Mostrar descripción de la tecnología UWB

    Usuario->>Home: Navegar a /home/contacto
    Home-->>Usuario: Mostrar formulario de contacto mediante email
