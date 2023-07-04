```mermaid
erDiagram
    usuarios {
        Int id PK
        String nombre
        String clave
        String email
        Int id_empresa FK
        Int id_perfil FK
        String movil
        Time creado
        Time ultimo_login
        Int activo
    }

    empresas {
        Int id PK
        String nombre
        String nif
        String direccion
        String provincia
        String pais
        String registro
        String movil
        String web
        Time creado

    }
    empresas ||--o{ usuarios : has
    
    perfiles {
        Int id PK
        String descripcion
        Time cread
        Int activo
    }
    usuarios ||--o{ perfiles : has

    usuarios }o--o{ plantas : puede_ver_mapa_de

    usuarios_plantas {
        Int id_usuario
        Int id_planta
    }

    edificios {
        Int id PK
        String nombre
    }

    plantas {
        Int id PK
        Int numero
        String plano_url
        String coordenadas
        Int id_edificio FK
    }
    edificios ||--o{ plantas : has

    dispositivos {
        Int id PK
        String nombre
        Int id_tipo_dispositivo FK
    }

    tipo_dispositivo {
        Int id PK
        String nombre
    }

    dispositivos ||--o{ tipo_dispositivo : has

    estado_dispositivo {
        Int nivel_bateria    
        Int humedad
        Int temperatura
        Date timestamp
        Int id_dispositivo FK
    }
    dispositivos ||--o{ estado_dispositivo : has

    puntos {
        Int id PK
        Int x
        Int y
        Int z
        Int id_dispositivo FK
        Date timestamp 
    }
    dispositivos ||--o{ puntos : is_located

    
```

* Relaciones 1-M con FK en tabla *
* Relaciones M-M con tabla auxiliar con indices de tablas
* SQLAlchemy se encarga de crear estas tablas si se definene las relaciones M-M correctamente en models.py
 
