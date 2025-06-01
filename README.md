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

## Traefik
To access the prototype at `prototype.localhost`.
You can add `proto-default` to the network and network service list in the `docker-compose.yml` inside your traefik directory.
Or you can just access the app at `localhost:9000`

## Tools
As long as direnv is allowed in the project directory it will add the ./tools directory to your path
Run `shell` for a shell inside the app container
Run `repl` for an IPython REPL inside the Flask application
Run `db` for a mycli SQL shell inside the database (requires mycli to be installed)

## Faker
With a shell inside the app container
Run `flask faker create [TABLE] [NUMBER]` to create NUMBER rows of fake inside TABLE
Valid tables are : teasurment, tser, tite, tartner, tour, track_user, track_tour, track_search 
Run `flask faker tracking_dataset` to create a sizeable data set of all tracking tables and the tables they rely on
