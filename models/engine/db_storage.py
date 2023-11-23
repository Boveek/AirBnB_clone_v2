#!/usr/bin/python3
"""This module defines the DBStorage class"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from os import getenv


class DBStorage:
    """This class defines the DBStorage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new DBStorage instance"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST', default='localhost'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session (self.__session)"""
        from models import classes
        result_dict = {}
        if cls:
            objects = self.__session.query(classes[cls]).all()
        else:
            objects = []
            for clss in classes.values():
                objects.extend(self.__session.query(clss).all())
        for obj in objects:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            result_dict[key] = obj
        return result_dict

    def new(self, obj):
        """Add the object to the current database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session (self.__session)"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and create the current database session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)()

