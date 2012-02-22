python manage.py schemamigration models --initial //in first time when create a migration

python manage.py schemamigration models --auto
python manage.py migrate models

If table are already created
Run 
./manage.py convert_to_south models 
South will automatically make and pretend to apply your first migration.


The convert_to_south command only works entirely on the first machine you run it on.
 Once you’ve committed the initial migrations it made into your VCS, you’ll have to run 
 ./manage.py migrate myapp 0001 --fake 
 on every machine that has a copy of the codebase (make sure they were up-to-date with models and schema first).
(For the interested, this is required because the initial migration that convert_to_south makes will try and create all the existing tables; instead, 
you tell South that it’s already applied using –fake, so the next migrations apply correctly.)
Remember that new installations of the codebase after this don’t need these steps; you need only do a syncdb then a normal migrate.