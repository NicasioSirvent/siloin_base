```mermaid
erDiagram
    user {
        Int id PK
        String name
        String password
        String email
    }

 
    user }o--o{ floor : puede_ver_mapa_de

    user_floor {
        Int user_id
        Int floor_id
    }

    building {
        Int id PK
        String name
    }

    floor {
        Int id PK
        Int num
        String plano_url
        Point coord_sup_izq
        Point coord_sup_der
        Point coord_inf_izq
        Point coord_sup_der 
        Int building_id FK
    }
    building ||--o{ floor : has

    device {
        Int id PK
        String name
        Int battery_level
    }

    point {
        Int id PK
        Int x
        Int y
        Int device_id FK
        Date Timestamp 
    }
    device ||--o{ point : is_located

    
```

* Relaciones 1-M con FK en tabla *
* Relaciones M-M con tabla auxiliar con indices de tablas
* SQLAlchemy se encarga de crear estas tablas si se definene las relaciones M-M correctamente en models.py
 
