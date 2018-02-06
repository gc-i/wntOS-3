from PyQt5.QtCore import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from ..model.Singleton import Singleton
from ..model.WntException import *
from future.utils import with_metaclass


class SessionHandler(with_metaclass(Singleton, QObject)):

    def __init__(self, parent=None):

        super(QObject, self).__init__(parent)
        self.session = None
        self.engine = None
        self.password = None
        self.username = None
        self.port = None
        self.host = None
        self.database = None
        self.groups = []

    def current_password(self):

        return self.password

    def current_username(self):

        return self.username

    def current_host(self):

        return self.host

    def current_port(self):

        return self.port

    def current_database(self):

        return self.database

    def session_instance(self):

        return self.session

    def create_session(self, username, password, host, port, database):

        if self.session is not None:
            self.session.close()

        try:
            self.engine = create_engine("postgresql://{0}:{1}@{2}:{3}/{4}".format(username, password, host, port, database))
            Session = sessionmaker(bind=self.engine)
            self.session = Session()
            self.session.autocommit = False

            self.username = username
            self.password = password
            self.host = host
            self.port = port
            self.database = database
            self.__collect_user_rights()

        except SQLAlchemyError as e:
            self.session = None
            self.engine = None
            self.username = None
            self.password = None
            self.host = None
            self.port = None
            self.database = None
            raise WntException(e.args[0], 'Database Error')

    def destroy_session(self):

        if self.session is not None:
            self.session.close()
            self.session = None
            self.username = None
            self.password = None
            self.host = None
            self.port = None
            self.database = None
            self.groups = []

    def __collect_user_rights(self):

        self.groups = []
        sql = "SELECT d.rolname AS group FROM pg_roles c JOIN (SELECT rolname, member FROM pg_auth_members a" \
              " JOIN pg_roles b ON a.roleid = b.oid) d ON d.member = c.oid WHERE lower(c.rolname) = CURRENT_USER"
        result = self.session.execute(sql).fetchall()
        for group in result:
            self.groups.append(group[0])

    def user_rights(self):

        return self.groups
