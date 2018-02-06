from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ..view.Ui_RepairMaterialDialog import *
from ..utils.PluginUtils import PluginUtils
from ..model.core_classes import CoRepairMaterial
from sqlalchemy.exc import SQLAlchemyError
from ..model.DatabaseHelper import *
from ..model.WntException import *


class RepairMaterialDialog(QDialog, Ui_RepairMaterialDialog, DatabaseHelper):

    def __init__(self, material_id, referenced_id, referenced_table_name, parent=None):

        super(RepairMaterialDialog, self).__init__(parent)
        DatabaseHelper.__init__(self)
        self.setupUi(self)
        self.__material_id = material_id
        self.__referenced_id = referenced_id
        self.__referenced_table_name = referenced_table_name
        try:
            PluginUtils.run_query(self.__populate_material_cbox)
            if material_id is not None:
                PluginUtils.run_query(self.__populate_material_details)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)

    def __populate_material_cbox(self):

        for material, in self.session.query(CoRepairMaterial.material.distinct()).order_by(CoRepairMaterial.material):
            self.material_cbox.addItem(material)

        self.material_cbox.setCurrentIndex(-1)

    def __populate_material_details(self):

        co_material = self.session.query(CoRepairMaterial).get(self.__material_id)

        self.amount_sbox.setValue(co_material.amount)
        self.material_cbox.setCurrentIndex(self.material_cbox.findText(co_material.material))
        if co_material.cost_total_tzs is not None:
            self.cost_sbox.setValue(co_material.cost_total_tzs)

    def material_id(self):

        return self.__material_id

    def accept(self):

        if not self.__validate_user_input():
            return

        try:
            PluginUtils.run_query(self.__save_material)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])
            return

        QDialog.accept(self)

    def __save_material(self):

        amount = self.amount_sbox.value()
        material = self.material_cbox.lineEdit().text()
        cost_total_tzs = self.cost_sbox.value()

        self.create_savepoint()
        try:
            if self.__material_id is None:
                co_repair_material = CoRepairMaterial()
            else:
                co_repair_material = self.session.query(CoRepairMaterial).get(self.__material_id)

            co_repair_material.amount = amount
            co_repair_material.material = material
            co_repair_material.cost_total_tzs = cost_total_tzs
            if self.__referenced_table_name == 'co_damage':
                co_repair_material.damage = self.__referenced_id
            else:
                co_repair_material.maintenance = self.__referenced_id

            self.session.add(co_repair_material)
            self.__material_id = co_repair_material.id
            self.release_savepoint()

        except SQLAlchemyError as e:
            self.rollback_to_savepoint()
            raise e

    def __validate_user_input(self):

        self.material_cbox.lineEdit().setText(self.material_cbox.lineEdit().text().strip())

        if len(self.material_cbox.lineEdit().text()) == 0:
            PluginUtils.show_message(self, self.tr('No material entered/selected'), self.tr('Please enter the material used!'))
            return False

        return True

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_F1:
            PluginUtils.show_help("Add_Edit_Repair_Material.htm")
