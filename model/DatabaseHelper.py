from builtins import range
from builtins import object
from ..utils.SessionHandler import SessionHandler


class DatabaseHelper(object):

    transaction_count = 1

    def __init__(self):

        self.session = SessionHandler().session_instance()

    def create_savepoint(self):

        self.session.begin_nested()
        DatabaseHelper.transaction_count += 1

        #print 'CR-SP:Transaction Count: {0}'.format(DatabaseHelper.transaction_count)

    def rollback_to_savepoint(self):

        self.session.rollback()
        DatabaseHelper.transaction_count -= 1

        #print 'RB-2-SP:Transaction Count: {0}'.format(DatabaseHelper.transaction_count)

    def release_savepoint(self):

        self.session.commit()
        DatabaseHelper.transaction_count -= 1

        #print 'RL-SP:Transaction Count: {0}'.format(DatabaseHelper.transaction_count)

    def rollback(self):

        for idx in range(DatabaseHelper.transaction_count):
            self.session.rollback()

        #print 'Rollback completed.'

        DatabaseHelper.transaction_count = 1

    def commit(self):

        for idx in range(DatabaseHelper.transaction_count):
            self.session.commit()

        #print 'Commit completed.'

        DatabaseHelper.transaction_count = 1
