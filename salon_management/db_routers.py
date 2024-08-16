from django.conf import settings

class DynamicDatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'salon':
            print(hints)
            # Route to the database for the specific salon
            org_name = hints.get('db_name')
            if org_name:
                print(org_name)
                db_alias = f'{org_name}_db'
                if db_alias in settings.DATABASES:
                    return db_alias
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'salon':
            # Route to the database for the specific salon
            org_name = hints.get('db_name')
            if org_name:
                db_alias = f'{org_name}_db'
                if db_alias in settings.DATABASES:
                    return db_alias
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'salon' or obj2._meta.app_label == 'salon':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Apply migrations for `salon` app to dynamic databases
        if app_label == 'salon':
            # Apply migrations to dynamic databases only
            return db in settings.DATABASES and db != 'default'
        
        # Apply migrations for other apps (like `accounts`) to the default database
        if app_label in ['auth', 'corsheaders', 'contenttypes', 'sessions', 'admin_interface', 'colorfield', 'admin', 'accounts']:
            return db == 'default'
        
        return None
