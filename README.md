# IFB398_External_Prototype
External prototype for Tour Amigo QUT Interns 2025. As proof of viability for IFB398. 

## Methodology
We should try to adhere fairly strictly to the Tour Amigo procedures as listed on the confluence.
This will mean
```
feature branches
squashing and merging
only branching from main 
enforcing sqlAlembic migrations for all schema changes
```

## Tech Stack (not exhaustive)
```
Docker
Docker-Compose
Flask
FLask-Migrate
python-dotenv
PyTest
MariaDB
ChartJS
Jinja2
sqlAlchemy
sqlAlembic
```

## Database setup
Run `db_init` script for database inititalisation
Run `db_upgrade` script for database migration
