# CONTEXT.md — Campeonato Deportivo de Karate

Documento de contexto del proyecto. Actualizado: 2026-09-13.

## 1. Propósito

Sistema backend para la gestión de campeonatos deportivos de karate: dojos,
competidores, categorías y modalidades, con API REST y panel de administración.

## 2. Stack

- **Python** 3.14.6 (venv local `venv/`)
- **Django** 6.1.1
- **Django REST Framework** 3.18.1
- **django-jazzmin** 3.0.5 (tema del admin)
- **djangorestframework-simplejwt** 5.5.1 (auth por JWT)
- **psycopg 3** (`psycopg[binary]==3.3.5`) — driver PostgreSQL (py3.14 requiere psycopg3; psycopg2 no tiene wheels)
- **python-dotenv** 1.2.3 (carga de `.env`)
- **drf-spectacular** 0.30.0 (documentación OpenAPI/Swagger + ReDoc)
- **Base de datos**: PostgreSQL 18.6 en **Neon** (nube)
- **SO**: Windows (PowerShell 5.1)

## 3. Estructura

```
Django-Proyecto/
├── core/          # Paquete del proyecto: settings.py, urls.py, wsgi/asgi
├── deportista/    # App: DojoModel, CompetidoresModel
├── evento/        # App: CampeonatoModel, CategoriaModel, ModalidadModel
├── migrations/    # 0001_initial + 0002 (modelos y opciones)
├── manage.py
├── requirements.txt
├── .env           # DATABASE_URL (NO versionar)
├── .gitignore     # excluye .env, venv, db.sqlite3, __pycache__
└── CONTEXT.md     # este archivo
```

## 4. Modelo de datos (tablas en Neon)

| Tabla          | Modelo            | Campos clave |
|----------------|-------------------|--------------|
| `dojo`         | `DojoModel`       | nombre, fecha_fundacion, distrito, provincia, departamento, pais, jefe_instructor, fecha_creacion |
| `competidores` | `CompetidoresModel` | nombres, apellidos, edad, sexo (M/F), dni (único), fecha_nacimiento, grado, fecha_grado, **FK dojo** (PROTECT) |
| `campeonato`   | `CampeonatoModel` | nombre, fecha_realizacion, ranking (bool), departamento, provincia, distrito |
| `categorias`   | `CategoriaModel`  | nombre, modalidad, tipo, nivel |
| `modalidades`  | `ModalidadModel`  | FK competidor, FK categoria, FK campeonato (PROTECT) |

Relaciones: `competidores.dojo -> dojo`; `modalidades` relaciona competidor+categoria+campeonato.

## 5. API REST (`/api/v1/`)

| Endpoint | Métodos | Nombre |
|----------|---------|--------|
| `competidores/` | GET, POST | competidor-list |
| `competidores/<int:pk>/` | GET, PUT, PATCH, DELETE | competidor-detail |
| `dojos/` | GET, POST | dojo-list |
| `dojos/<int:pk>/` | GET, PUT, PATCH, DELETE | dojo-detail |
| `campeonatos/` | GET, POST | campeonato-list |
| `campeonatos/<int:pk>/` | GET, PUT, PATCH, DELETE | campeonato-detail |
| `categorias/` | GET, POST | categoria-list |
| `categorias/<int:pk>/` | GET, PUT, PATCH, DELETE | categoria-detail |
| `modalidades/` | GET, POST | modalidad-list |
| `modalidades/<int:pk>/` | GET, PUT, PATCH, DELETE | modalidad-detail |

Auth:
- `POST /api/token/` → access/refresh (JWT simplejwt)
- `POST /api/token/refresh/`
- Admin: `/admin/`

### Documentación de la API (drf-spectacular)

| Ruta | Descripción |
|------|-------------|
| `/api/docs/` | Esquema OpenAPI en JSON (o YAML) |
| `/api/docs/swagger/` | Interfaz Swagger UI |
| `/api/docs/redoc/` | Interfaz ReDoc |

Cada endpoint documenta su propósito con `@extend_schema_view(...)` en
`deportista/views.py` y `evento/views.py` (summary + description por operación).

## 6. Configuración / Base de datos

- La cadena de conexión vive en `.env` como `DATABASE_URL`:
  `postgresql://neondb_owner:PASSWORD@ep-orange-surf-aeegqbjn-pooler.c-2.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require`
- `core/settings.py` la parsea con `urllib.parse.urlparse` y añade
  `OPTIONS = {"sslmode": "require", "channel_binding": "require"}`.
- Usa el endpoint **pooler** de Neon (segundo plano `-pooler`).

### Credenciales (dev)
- Superusuario: `admin` / `Admin123456` (email `admin@example.com`) — **cámbialo pronto**.
- BD: host `ep-orange-surf-aeegqbjn-pooler.c-2.us-east-2.aws.neon.tech`, db/user `neondb`/`neondb_owner` (password en `.env`).

## 7. Comandos útiles

```powershell
# Activar entorno e instalar deps
venv\Scripts\python.exe -m pip install -r requirements.txt

# Chequeo
venv\Scripts\python.exe manage.py check

# Migraciones / BD
venv\Scripts\python.exe manage.py makemigrations
venv\Scripts\python.exe manage.py migrate

# Tests (IMPORTANTE: --keepdb en Neon)
venv\Scripts\python.exe manage.py test --keepdb

# Superusuario
$env:DJANGO_SUPERUSER_USERNAME="admin"; $env:DJANGO_SUPERUSER_EMAIL="admin@example.com"; $env:DJANGO_SUPERUSER_PASSWORD="Admin123456"
venv\Scripts\python.exe manage.py createsuperuser --noinput

# Servidor
venv\Scripts\python.exe manage.py runserver
```

## 8. Notas y gotchas

1. **`manage.py test` SIN `--keepdb` falla en Neon** al destruir `test_neondb`
   (`database is being accessed by other users`): el pooler mantiene una sesión
   abierta. Usar `manage.py test --keepdb`.
2. **Nunca versionar `.env`** (contiene el password). Ya está en `.gitignore`.
3. El fix `urlspatterns` → `urlpatterns` en `deportista/urls.py` era bloqueante:
   sin él ningún comando `manage.py` funcionaba.
4. `Model.objects.create()` requiere **instancias** para FKs (no pk); el serializer
   de DRF sí acepta pk. Afecta a tests que crean registros directos.
5. `rest_framework_simplejwt` está en `INSTALLED_APPS` y en `core/urls.py`.
6. El tipado de `sexo` usa `choices` (M/F); `dni` es único a nivel BD.
7. Con **drf-spectacular** + generics CBV, `@extend_schema_view` usa las keys
   de verbos HTTP (`get`/`post`/`put`/`patch`/`delete`), NO los nombres
   `list`/`create`/`retrieve`/`update`/`destroy` (spectacular inspecta
   `view.get`, no `view.list`).

## 9. Estado de fases

- **Fase 1 ✅**: conexión PostgreSQL (Neon), deps, fix del arranque, migraciones 0001.
- **Fase 2 ✅**: migraciones 0002, API CRUD completa (deportista + evento), admin
  registrado, validaciones (dni unique, sexo choices, `__str__` de Modalidad),
  tests 14/14 OK.
- **Fase 3 ✅**: documentación de la API con drf-spectacular — Swagger UI
  (`/api/docs/swagger/`), ReDoc (`/api/docs/redoc/`) y esquema OpenAPI 3
  (`/api/docs/`). Descripción en español de cada endpoint por operación.
- **Pendientes**: seed de datos desde `Data.xlsx`, importar diagrama DER, deploy,
  cambiar password del superusuario, iniciar repo git.

## 10. Archivos de referencia

- `Data.xlsx` — dataset del dominio (pendiente de importar).
- `Diagrama Entidad Relacion - Campeonato deportivo de Karate.jpg` — DER.
- `Data.vsdx` — diagrama editable.