# How to use multiple schemas with django?

### References
- https://docs.djangoproject.com/en/dev/topics/db/multi-db/
- https://www.amvtek.com/blog/posts/2014/Jun/13/accessing-multiple-postgres-schemas-from-django/
- https://stackoverflow.com/questions/50819748/django-and-postgresql-schemas

### What was done
- adjust `DATABASES` setting
- add extra Meta configuration in model in different schema

### Functionality
- migrations work
- admin works
- orm querying works
