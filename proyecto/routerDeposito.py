class RouterDeposito(object):
    def db_for_read(self, model, **hints):
        "Point all operations on myapp models to 'other'"
        if model._meta.app_label == 'deposito':
            return 'deposito'
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on myapp models to 'other'"
        if model._meta.app_label == 'deposito':
            return 'deposito'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in myapp is involved"
        if obj1._meta.app_label == 'deposito' or obj2._meta.app_label == 'deposito':
            return True
        return None

    def allow_syncdb(self, db, model):
        "Make sure the myapp app only appears on the 'other' db"
        if db == 'deposito':
            return model._meta.app_label == 'deposito'
        elif model._meta.app_label == 'deposito':
            return False
        return None
