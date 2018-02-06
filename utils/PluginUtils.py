from __future__ import print_function
from builtins import str
from builtins import range
from builtins import object
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ..model import Constants
from ..model.DatabaseHelper import *
from ..model.core_classes import SetGeneralSettings, SetUserSettings, CoNetwork
import os, subprocess, sys
from datetime import *
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.exc import DBAPIError
from ..model.WntException import *


class PluginUtils(object):

    @staticmethod
    def show_message(parent, title, message):

        QMessageBox.information(parent, title, message)

    @staticmethod
    def show_error(parent, title, message):

        QMessageBox.warning(parent, title, message)

    @staticmethod
    def populate_codelist_cbox(cbox, codelist_class, insert_empty_row=False):

        db_helper = DatabaseHelper()
        db_helper.create_savepoint()

        cbox.clear()
        if insert_empty_row:
            cbox.addItem('-')

        try:
            for code, desc in db_helper.session.query(codelist_class.code, codelist_class.description).\
                    order_by(codelist_class.code):
                cbox.addItem(desc, code)
            db_helper.release_savepoint()
        except SQLAlchemyError as e:
            db_helper.rollback_to_savepoint()
            raise e

    @staticmethod
    def populate_network_cbox(cbox):

        db_helper = DatabaseHelper()
        db_helper.create_savepoint()

        try:
            for network in db_helper.session.query(CoNetwork):
                cbox.addItem(network.network_name, network.id)

            # set default network
            count = db_helper.session.query(SetUserSettings).count()
            if count > 0:
                setting = db_helper.session.query(SetUserSettings).one()
                if setting.default_network:
                    cbox.setCurrentIndex(cbox.findData(setting.default_network, Qt.UserRole))

        except SQLAlchemyError as e:
            db_helper.rollback_to_savepoint()
            raise e

    @staticmethod
    def find_item_by_data(lwidget, data):

        for i in range(lwidget.count()):
            item = lwidget.item(i)
            if data == item.data(Qt.UserRole):
                return item
        return None

    @staticmethod
    def groups_by_user(username):

        session = SessionHandler().session_instance()
        sql = "select rolname from pg_user join pg_auth_members on (pg_user.usesysid=pg_auth_members.member) " \
              "join pg_roles on (pg_roles.oid=pg_auth_members.roleid) where pg_user.usename=:bindName"
        result = session.execute(sql, {'bindName': username}).fetchall()

        return result

    @staticmethod
    def convert_qt_date_to_python(qt_date):
        if not qt_date:
            return None
        date_string = qt_date.toString(Constants.DATE_FORMAT)
        # fix_print_with_import
        print('DateString: ' + date_string)
        python_date = datetime.strptime(date_string, Constants.PYTHON_DATE_FORMAT)
        return python_date

    @staticmethod
    def convert_qt_datetime_to_python(qt_date):
        if not qt_date:
            return None
        date_string = qt_date.toString(Constants.DATABASE_DATETIME_FORMAT)
        python_date = datetime.strptime(date_string, Constants.PYTHON_DATETIME_FORMAT)
        return python_date

    @staticmethod
    def convert_qt_time_to_python(qt_time):
        if not qt_time:
            return None
        time_string = qt_time.toString(Constants.DATABASE_TIME_FORMAT)
        python_time = datetime.strptime(time_string, Constants.PYTHON_TIME_FORMAT).time()
        return python_time

    @staticmethod
    def convert_python_date_to_qt(python_date):

        if not python_date:
            return None
        converted_date = QDate.fromString(python_date.strftime(Constants.PYTHON_DATE_FORMAT),
                                          Constants.DATABASE_DATE_FORMAT)
        return converted_date

    @staticmethod
    def convert_python_datetime_to_qt(python_datetime):

        if not python_datetime:
            return None
        converted_datetime = QDateTime.fromString(python_datetime.strftime(Constants.PYTHON_DATETIME_FORMAT),
                                                  Constants.DATABASE_DATETIME_FORMAT)
        return converted_datetime

    @staticmethod
    def convert_python_time_to_qt(python_time):

        if not python_time:
            return None
        converted_time = QTime.fromString(python_time.strftime(Constants.PYTHON_TIME_FORMAT),
                                                  Constants.DATABASE_TIME_FORMAT)
        return converted_time

    @staticmethod
    def open_document(name, content):

        if content is None:
            return

        file_path = QDir.tempPath() + QDir.separator() + name

        file = QFile(file_path)
        if not file.open(QIODevice.WriteOnly):
            return

        file.write(content)
        file.close()

        if sys.platform == "win32":
            os.startfile(file_path)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, file_path])

    @staticmethod
    def open_maxcom(control_no, maxcom_type):

        db_helper = DatabaseHelper()
        db_helper.create_savepoint()

        try:
            setting = db_helper.session.query(SetGeneralSettings).first()
            db_helper.release_savepoint()
            if maxcom_type == 'NEW':
                maxcom_type = '/connectionMain#/applicationTxn/'
            else:
                maxcom_type = '/customerCareMain#/waterLeakageComplaint/'

            os.startfile(setting.base_url + maxcom_type + '{}'.format(control_no))
        except SQLAlchemyError as e:
            db_helper.rollback_to_savepoint()
            raise e

    @staticmethod
    def show_help(help_page):

        if sys.platform == "linux" or sys.platform == "linux2":
            try:
                help_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "manual/wnt_help.chm"))
                subprocess.call("xchm " + help_path, shell=True)
            except Exception as e:
                # fix_print_with_import
                print(str(e))

        elif sys.platform == "win32":
            help_path = os.path.dirname(os.path.realpath(__file__)) + "/../manual/wnt_help.chm::/"
            subprocess.Popen("hh.exe " + help_path + help_page)


    @staticmethod
    def build_topology():

        db_helper = DatabaseHelper()
        db_helper.create_savepoint()

        try:
            sql = "SELECT build_topology(0.01)"  # 1cm tolerance
            db_helper.session.execute(sql)
            db_helper.commit()
        except SQLAlchemyError as e:
            db_helper.rollback_to_savepoint()
            raise e

    @staticmethod
    def reverse_flow_direction(feat_ids, map_canvas):

        db_helper = DatabaseHelper()
        db_helper.create_savepoint()

        try:
            for feat_id in feat_ids:
                sql = "UPDATE co_pipeline_segment SET geometry = ST_Reverse(geometry), " \
                      "from_height = to_height, " \
                      "to_height = from_height WHERE id = {}".format(feat_id)
                db_helper.session.execute(sql)

            db_helper.commit()
            map_canvas.refresh()
        except SQLAlchemyError as e:
            db_helper.rollback_to_savepoint()
            raise e

    @staticmethod
    def run_query(f, retry=2, *args):

        db_helper = DatabaseHelper()

        while retry:
            retry -= 1
            try:
                # print 'len: {}'.format(len(args))
                if len(args) > 0:
                    return f(*args)  # "break" if query was successful and return any results
                else:
                    return f()
            except DBAPIError as e:
                if retry and e.connection_invalidated:
                    db_helper.rollback()
                    QMessageBox.information(None, "Server Disconnect",
                                            "Because of a server disconnect all changes"
                                            " since the last save have been discarded.")
                else:
                    raise WntException('No connection to database server.', 'Database Error')
            except SQLAlchemyError as e:
                raise e
