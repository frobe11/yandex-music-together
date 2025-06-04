from sqlalchemy.ext.automap import automap_base

Base = automap_base()

def get_user_model():
    if not hasattr(Base, 'classes') or not hasattr(Base.classes, 'users'):
        raise RuntimeError("Database not initialized or 'users' table not found!")
    return Base.classes.users

def get_user_info_model():
    if not hasattr(Base, 'classes') or not hasattr(Base.classes, 'user_info'):
        raise RuntimeError("Database not initialized or 'user_info' table not found!")
    return Base.classes.user_info