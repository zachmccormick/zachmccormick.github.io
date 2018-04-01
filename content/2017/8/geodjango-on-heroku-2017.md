Title: Running GeoDjango on Heroku (August 2017)
Date: 2017-08-16
Category: Software Development
Tags: heroku, django, gis, geography, devops
Authors: Zach McCormick

### Heroku Setup

There are currently two ways to get the GDAL, GEOS, and PROJ libraries needed by GeoDjango onto your Heroku slug

1.  Via a custom buildpack
([https://github.com/cyberdelia/heroku-geo-buildpack](https://github.com/cyberdelia/heroku-geo-buildpack)) 1.
Via setting the environment variable BUILD_WITH_GEO_LIBRARIES=1 while using the default Python buildpack

This has two issues as of 8–16–2017: The current “stack” on Heroku is heroku-16.  This stack
does not properly copy over libjasper, which is a required linked library by libgdal. One solution is
to set your stack to cedar-14 instead.  Another solution is to use a slightly modified custom buildpack
([https://github.com/dschep/heroku-geo-buildpack](https://github.com/dschep/heroku-geo-buildpack))
or a slightly modified offical buildpack
([https://github.com/TrailblazingTech/heroku-buildpack-python#fix-gdal-jasper]
(https://github.com/TrailblazingTech/heroku-buildpack-python#fix-gdal-jasper)).

If you stick with the heroku-16 stack, you’ll want to add the following to your settings.py:

> GDAL_LIBRARY_PATH = os.getenv(‘GDAL_LIBRARY_PATH’)<br> GEOS_LIBRARY_PATH = > os.getenv(‘GEOS_LIBRARY_PATH’)

Then, if using the official Python buildpack, you will want to set your environment variables like so:

> GDAL_LIBRARY_PATH=/app/.heroku/vendor/lib/libgdal.so<br> > GEOS_LIBRARY_PATH=/app/.heroku/vendor/lib/libgeos_c.so

This may be required as well on cedar-14 — I didn’t take notes during that part of the struggle :-)

### Django Settings Changes

1.  Add ‘django.contrib.gis’ to your INSTALLED_APPS 1.  Change your DATABASES dict to use postgis, like so:

> DATABASES[‘default’] = dj_database_url.config(conn_max_age=600,<br> >
default=’postgis://localhost:5432/{}’.format(APP_NAME))<br>  # VERY IMPORTANT BECAUSE HEROKU WILL USE
‘postgres’ AS THE SCHEME<br> DATABASES[‘default’][‘ENGINE’] = ‘django.contrib.gis.db.backends.postgis’

### Other Django Things

In urls.py, change **from django.contrib import admin** to **from django.contrib.gis import admin** for admin urls

1.  In whatever app makes sense, add the following migration:

> from django.contrib.postgres.operations import CreateExtension<br> from > django.db import migrations

> class Migration(migrations.Migration):<br>  operations = [<br> > CreateExtension(‘postgis’)<br>  ]

### Credits

[cyberdelia](http://twitter.com/cyberdelia) and [dschep](http://twitter.com/dschep) on GitHub for helping provide
and work through the gdal dependency issues with a custom buildpack.

### GitHub Example

[https://github.com/TrailblazingTech/django-gis-heroku](https://github.com/TrailblazingTech/django-gis-heroku)

