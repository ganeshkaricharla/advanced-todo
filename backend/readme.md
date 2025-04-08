# Advanced Todo

# DB Diagram

```mermaid
erDiagram
    USERS {
        ObjectId _id PK
        string username
        string password_hash
        string email
        datetime created_at
        datetime last_login
    }

    PROJECTS {
        ObjectId _id PK
        string project_name
        string description
        ObjectId user_id FK
        datetime created_at
        datetime updated_at
        string visibility
        boolean is_default
        string project_type
    }

    TASKS {
        ObjectId _id PK
        string title
        string description
        ObjectId project_id FK
        ObjectId user_id FK
        datetime start_date
        datetime end_date
        string status
        datetime created_at
        datetime updated_at
        object metadata
    }

    USERS ||--o{ PROJECTS : creates
    USERS ||--o{ TASKS : owns
    PROJECTS ||--o{ TASKS : contains
```

```mermaid
graph TB
subgraph "Backend (Flask)"
subgraph "API Endpoints"
UE[User Endpoints]
PE[Project Endpoints]
TE[Task Endpoints]
end

        subgraph "Services"
            US[User Service]
            PS[Project Service]
            TS[Task Service]
            DTS[Date/Time Service]
        end

        subgraph "Middleware"
            AUTH[Authentication]
            ERR[Error Handling]
            LOG[Logging]
        end
    end

    subgraph "Database (MongoDB)"
        subgraph "Collections"
            UC[Users Collection]
            PC[Projects Collection]
            TC[Tasks Collection]
        end
    end

    %% Backend connections
    UE --> US
    PE --> PS
    TE --> TS
    TE --> DTS
    US --> PS

    %% Service to Database connections
    US --> UC
    PS --> PC
    TS --> TC

    %% Middleware connections
    AUTH --> UE
    AUTH --> PE
    AUTH --> TE
```
