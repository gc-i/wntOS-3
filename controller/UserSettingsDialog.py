from ..view.Ui_UserSettingsDialog import *
from PyQt5.QtWidgets import *
from ..utils.PluginUtils import *


class UserSettingsDialog(QDialog, Ui_UserSettingsDialog, DatabaseHelper):

    def __init__(self, parent=None):

        super(UserSettingsDialog, self).__init__(parent)
        DatabaseHelper.__init__(self)
        self.setupUi(self)
        try:
            PluginUtils.run_query(PluginUtils.populate_network_cbox, 2, self.network_cbox)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)

    def accept(self):

        try:
            PluginUtils.run_query(self.__save_settings)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])
            return

        QDialog.accept(self)

    def __save_settings(self):

        self.create_savepoint()
        try:
            count = self.session.query(SetUserSettings).count()
            if count == 0:
                settings = SetUserSettings()
                settings.username = SessionHandler().current_username()
            else:
                settings = self.session.query(SetUserSettings).one()

            settings.default_network = self.network_cbox.itemData(self.network_cbox.currentIndex(), Qt.UserRole)
            self.session.add(settings)
            self.commit()

        except SQLAlchemyError as e:
            self.rollback_to_savepoint()
            raise e

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_F1:
            PluginUtils.show_help("User_Settings.htm")
