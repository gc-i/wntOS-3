# coding: utf-8
from sqlalchemy import Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, LargeBinary, \
    Numeric, String, Text, Sequence
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry

Base = declarative_base()
metadata = Base.metadata


class ClDamageType(Base):
    __tablename__ = 'cl_damage_type'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClDamageCause(Base):
    __tablename__ = 'cl_damage_cause'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClDamageStatus(Base):
    __tablename__ = 'cl_damage_status'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(Integer, primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClTypeOfDocument(Base):
    __tablename__ = 'cl_type_of_document'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClTypeOfPipelineSegment(Base):
    __tablename__ = 'cl_type_of_pipeline_segment'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClIntervalUnit(Base):
    __tablename__ = 'cl_interval_unit'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClMaterial(Base):
    __tablename__ = 'cl_material'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(4), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClCorrosionProtectionInside(Base):
    __tablename__ = 'cl_corrosion_protection_inside'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClCorrosionProtectionOutside(Base):
    __tablename__ = 'cl_corrosion_protection_outside'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClTypeOfPlacement(Base):
    __tablename__ = 'cl_type_of_placement'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClOperatingState(Base):
    __tablename__ = 'cl_operating_state'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClPositionalAccuracy(Base):
    __tablename__ = 'cl_positional_accuracy'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClNominalWidthOfPipelineSegment(Base):
    __tablename__ = 'cl_nominal_width_of_pipeline_segment'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(Integer, primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClMountingTypeOfPipelineSegment(Base):
    __tablename__ = 'cl_mounting_type_of_pipeline_segment'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClMountingTypeOfFitting(Base):
    __tablename__ = 'cl_mounting_type_of_fitting'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClPurposeOfFitting(Base):
    __tablename__ = 'cl_purpose_of_fitting'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClNominalWidthOfFitting(Base):
    __tablename__ = 'cl_nominal_width_of_fitting'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(Integer, primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClTypeOfFitting(Base):
    __tablename__ = 'cl_type_of_fitting'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClSwitchingState(Base):
    __tablename__ = 'cl_switching_state'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClConstructionTypeOfManhole(Base):
    __tablename__ = 'cl_construction_type_of_manhole'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClEntryTypeOfManhole(Base):
    __tablename__ = 'cl_entry_type_of_manhole'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClLocation(Base):
    __tablename__ = 'cl_location'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClPurposeOfManhole(Base):
    __tablename__ = 'cl_purpose_of_manhole'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClCapacityUnit(Base):
    __tablename__ = 'cl_capacity_unit'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClTypeOfSource(Base):
    __tablename__ = 'cl_type_of_source'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClTypeOfIntake(Base):
    __tablename__ = 'cl_type_of_intake'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClNominalPressure(Base):
    __tablename__ = 'cl_nominal_pressure'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(Integer, primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClTypeOfCustomer(Base):
    __tablename__ = 'cl_type_of_customer'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClMeterClass(Base):
    __tablename__ = 'cl_meter_class'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClMeterType(Base):
    __tablename__ = 'cl_type_of_meter'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClTypeOfStation(Base):
    __tablename__ = 'cl_type_of_station'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClPurposeOfStation(Base):
    __tablename__ = 'cl_purpose_of_station'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClTypeOfLineCasing(Base):
    __tablename__ = 'cl_type_of_line_casing'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClNominalWidthOfJacketPipe(Base):
    __tablename__ = 'cl_nominal_width_of_jacket_pipe'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClTypeOfConnectionPoint(Base):
    __tablename__ = 'cl_type_of_connection_point'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClNominalWidthOfConnectionPoint(Base):
    __tablename__ = 'cl_nominal_width_of_connection_point'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class ClMountingTypeOfConnectionPoint(Base):
    __tablename__ = 'cl_mounting_type_of_connection_point'
    __table_args__ = {u'schema': 'codelist'}

    code = Column(String(3), primary_key=True)
    description = Column(String(100), nullable=False, unique=True)


class CoNetwork(Base):
    __tablename__ = 'co_network'
    __table_args__ = {u'schema': 'core'}

    id = Column(Integer, Sequence('co_network_id_seq'), primary_key=True)
    network_number = Column(String(50))
    network_name = Column(String(50))

    dimensioning_pressure = Column(ForeignKey(u'codelist.cl_nominal_pressure.code', ondelete=u'RESTRICT',
                                      onupdate=u'CASCADE'))
    operating_pressure = Column(ForeignKey(u'codelist.cl_nominal_pressure.code', ondelete=u'RESTRICT',
                                      onupdate=u'CASCADE'))

    cl_dimensioning_pressure = relationship(u'ClNominalPressure', primaryjoin='CoNetwork.dimensioning_pressure == ClNominalPressure.code')
    cl_operating_pressure = relationship(u'ClNominalPressure', primaryjoin='CoNetwork.operating_pressure == ClNominalPressure.code')


class CoCustomer(Base):
    __tablename__ = 'co_customer'
    __table_args__ = {u'schema': 'core'}

    id = Column(Integer, Sequence('co_customer_id_seq'), primary_key=True)
    customer_number = Column(String(50))
    account_number = Column(String(50))
    organisation_name = Column(String(100))
    surname = Column(String(50))
    first_name = Column(String(50))

    customer_type = Column(ForeignKey(u'codelist.cl_type_of_customer.code', ondelete=u'RESTRICT',
                                      onupdate=u'CASCADE'))

    cl_type_of_customer = relationship(u'ClTypeOfCustomer')


class CoPipelineSegment(Base):
    __tablename__ = 'co_pipeline_segment'
    __table_args__ = {u'schema': 'core'}

    id = Column(Integer, Sequence('co_pipeline_segment_id_seq'), primary_key=True)
    segment_number = Column(String(50))

    pipeline_type = Column(ForeignKey(u'codelist.cl_type_of_pipeline_segment.code', ondelete=u'RESTRICT',
                                      onupdate=u'CASCADE'))
    length = Column(Numeric)
    year_of_manufacture = Column(Integer)
    outside_diameter = Column(Numeric)
    wall_thickness = Column(Numeric)
    installation_date = Column(Date)
    inspection_interval = Column(Integer)
    inspection_interval_unit = Column(ForeignKey(u'codelist.cl_interval_unit.code', ondelete=u'RESTRICT',
                                      onupdate=u'CASCADE'))
    date_of_last_inspection = Column(Date)
    note = Column(Text)
    material = Column(ForeignKey(u'codelist.cl_material.code', ondelete=u'RESTRICT',
                                                 onupdate=u'CASCADE'))
    placement_type = Column(ForeignKey(u'codelist.cl_type_of_placement.code',
                                                     ondelete=u'RESTRICT', onupdate=u'CASCADE'))

    operating_state = Column(ForeignKey(u'codelist.cl_operating_state.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    date_of_status_change = Column(Date)
    positional_accuracy = Column(ForeignKey(u'codelist.cl_positional_accuracy.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    nominal_width = Column(ForeignKey(u'codelist.cl_nominal_width_of_pipeline_segment.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    mounting_type = Column(ForeignKey(u'codelist.cl_mounting_type_of_pipeline_segment.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    from_height = Column(Numeric)
    to_height = Column(Numeric)
    network = Column(ForeignKey(u'core.co_network.id',
                                      ondelete=u'SET NULL', onupdate=u'CASCADE'))
    geometry = Column(Geometry('LINESTRING', 32736))

    cl_type_of_pipeline_segment = relationship(u'ClTypeOfPipelineSegment')
    cl_interval_unit = relationship(u'ClIntervalUnit')
    cl_material = relationship(u'ClMaterial')
    cl_type_of_placement = relationship(u'ClTypeOfPlacement')
    cl_operating_state = relationship(u'ClOperatingState')
    cl_positional_accuracy = relationship(u'ClPositionalAccuracy')
    cl_nominal_width_of_pipeline_segment = relationship(u'ClNominalWidthOfPipelineSegment')
    cl_mounting_type_of_pipeline_segment = relationship(u'ClMountingTypeOfPipelineSegment')
    co_network = relationship(u'CoNetwork')


class CoFitting(Base):
    __tablename__ = 'co_fitting'
    __table_args__ = {u'schema': 'core'}

    id = Column(Integer, Sequence('co_fitting_id_seq'), primary_key=True)
    fitting_number = Column(String(50))
    installation_length = Column(Numeric)
    installation_date = Column(Date)
    inspection_interval = Column(Integer)
    inspection_interval_unit = Column(ForeignKey(u'codelist.cl_interval_unit.code', ondelete=u'RESTRICT',
                                      onupdate=u'CASCADE'))
    date_of_last_inspection = Column(Date)
    note = Column(Text)
    operating_state = Column(ForeignKey(u'codelist.cl_operating_state.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    date_of_status_change = Column(Date)
    switching_state = Column(ForeignKey(u'codelist.cl_switching_state.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    mounting_type = Column(ForeignKey(u'codelist.cl_mounting_type_of_fitting.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    nominal_width = Column(ForeignKey(u'codelist.cl_nominal_width_of_fitting.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    fitting_type = Column(ForeignKey(u'codelist.cl_type_of_fitting.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    fitting_purpose = Column(ForeignKey(u'codelist.cl_purpose_of_fitting.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    height = Column(Numeric)
    network = Column(ForeignKey(u'core.co_network.id',
                                ondelete=u'SET NULL', onupdate=u'CASCADE'))
    geometry = Column(Geometry('POINT', 32736))

    cl_interval_unit = relationship(u'ClIntervalUnit')
    cl_switching_state = relationship(u'ClSwitchingState')
    cl_operating_state = relationship(u'ClOperatingState')
    cl_mounting_type = relationship(u'ClMountingTypeOfFitting')
    cl_fitting_type = relationship(u'ClTypeOfFitting')
    cl_nominal_width = relationship(u'ClNominalWidthOfFitting')
    cl_fitting_purpose = relationship(u'ClPurposeOfFitting')
    co_network = relationship(u'CoNetwork')


class CoManhole(Base):
    __tablename__ = 'co_manhole'
    __table_args__ = {u'schema': 'core'}

    id = Column(Integer, Sequence('co_manhole_id_seq'), primary_key=True)
    manhole_number = Column(String(50))
    installation_date = Column(Date)
    date_of_last_inspection = Column(Date)
    inspection_interval = Column(Integer)
    inspection_interval_unit = Column(ForeignKey(u'codelist.cl_interval_unit.code', ondelete=u'RESTRICT',
                                      onupdate=u'CASCADE'))
    note = Column(Text)
    operating_state = Column(ForeignKey(u'codelist.cl_operating_state.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    date_of_status_change = Column(Date)
    purpose = Column(ForeignKey(u'codelist.cl_purpose_of_manhole.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    construction_type = Column(ForeignKey(u'codelist.cl_construction_type_of_manhole.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    entry_type = Column(ForeignKey(u'codelist.cl_entry_type_of_manhole.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    location = Column(ForeignKey(u'codelist.cl_location.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    height = Column(Numeric)
    network = Column(ForeignKey(u'core.co_network.id',
                                ondelete=u'SET NULL', onupdate=u'CASCADE'))
    geometry = Column(Geometry('POLYGON', 32736))

    cl_interval_unit = relationship(u'ClIntervalUnit')
    cl_operating_state = relationship(u'ClOperatingState')
    cl_construction_type_of_manhole = relationship(u'ClConstructionTypeOfManhole')
    cl_entry_type_of_manhole = relationship(u'ClEntryTypeOfManhole')
    cl_location = relationship(u'ClLocation')
    cl_purpose_of_manhole = relationship(u'ClPurposeOfManhole')
    co_network = relationship(u'CoNetwork')


class CoIntake(Base):
    __tablename__ = 'co_intake'
    __table_args__ = {u'schema': 'core'}

    id = Column(Integer, Sequence('co_intake_id_seq'), primary_key=True)
    intake_number = Column(String(50))
    intake_source = Column(ForeignKey(u'codelist.cl_type_of_source.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    intake_type = Column(ForeignKey(u'codelist.cl_type_of_intake.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    capacity = Column(Numeric)

    capacity_unit = Column(ForeignKey(u'codelist.cl_capacity_unit.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    installation_year = Column(Integer)
    inspection_interval = Column(Integer)
    inspection_interval_unit = Column(ForeignKey(u'codelist.cl_interval_unit.code', ondelete=u'RESTRICT',
                                      onupdate=u'CASCADE'))
    date_of_last_inspection = Column(Date)
    operating_state = Column(ForeignKey(u'codelist.cl_operating_state.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    date_of_status_change = Column(Date)
    height = Column(Numeric)
    note = Column(Text)
    network = Column(ForeignKey(u'core.co_network.id',
                                ondelete=u'SET NULL', onupdate=u'CASCADE'))
    geometry = Column(Geometry('POLYGON', 32736))

    cl_capacity_unit = relationship(u'ClCapacityUnit')
    cl_intake_source = relationship(u'ClTypeOfSource')
    cl_intake_type = relationship(u'ClTypeOfIntake')
    co_network = relationship(u'CoNetwork')
    cl_operating_state = relationship(u'ClOperatingState')
    cl_interval_unit = relationship(u'ClIntervalUnit')


class CoFlatrateConnection(Base):
    __tablename__ = 'co_flatrate_connection'
    __table_args__ = {u'schema': 'core'}

    id = Column(Integer, Sequence('co_flatrate_connection_id_seq'), primary_key=True)
    connection_number = Column(String(50))
    control_no = Column(Integer)
    plot_no = Column(String(50))
    district = Column(String(50))
    zone = Column(String(50))
    ward = Column(String(50))
    street = Column(String(50))

    installation_date = Column(Date)
    inspection_interval = Column(Integer)
    inspection_interval_unit = Column(ForeignKey(u'codelist.cl_interval_unit.code', ondelete=u'RESTRICT',
                                      onupdate=u'CASCADE'))
    date_of_last_inspection = Column(Date)
    note = Column(Text)
    operating_state = Column(ForeignKey(u'codelist.cl_operating_state.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    date_of_status_change = Column(Date)
    height = Column(Numeric)
    maxcom_customer = Column(Integer)
    network = Column(ForeignKey(u'core.co_network.id',
                                ondelete=u'SET NULL', onupdate=u'CASCADE'))
    geometry = Column(Geometry('POINT', 32736))

    cl_interval_unit = relationship(u'ClIntervalUnit')
    co_network = relationship(u'CoNetwork')
    cl_operating_state = relationship(u'ClOperatingState')


class CoMeter(Base):
    __tablename__ = 'co_meter'
    __table_args__ = {u'schema': 'core'}

    id = Column(Integer, Sequence('co_meter_id_seq'), primary_key=True)
    meter_number = Column(String(50))
    control_no = Column(Integer)
    plot_no = Column(String(50))
    district = Column(String(50))
    zone = Column(String(50))
    ward = Column(String(50))
    street = Column(String(50))

    installation_date = Column(Date)
    inspection_interval = Column(Integer)
    inspection_interval_unit = Column(ForeignKey(u'codelist.cl_interval_unit.code', ondelete=u'RESTRICT',
                                      onupdate=u'CASCADE'))
    date_of_last_inspection = Column(Date)
    note = Column(Text)
    operating_state = Column(ForeignKey(u'codelist.cl_operating_state.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    date_of_status_change = Column(Date)

    meter_class = Column(ForeignKey(u'codelist.cl_meter_class.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))

    meter_type = Column(ForeignKey(u'codelist.cl_type_of_meter.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    height = Column(Numeric)
    maxcom_customer = Column(Integer)
    network = Column(ForeignKey(u'core.co_network.id',
                                ondelete=u'SET NULL', onupdate=u'CASCADE'))
    geometry = Column(Geometry('POINT', 32736))

    cl_interval_unit = relationship(u'ClIntervalUnit')
    cl_meter_class = relationship(u'ClMeterClass')
    cl_type_of_meter = relationship(u'ClMeterType')
    co_network = relationship(u'CoNetwork')
    cl_operating_state = relationship(u'ClOperatingState')


class CoDistributionPoint(Base):
    __tablename__ = 'co_distribution_point'
    __table_args__ = {u'schema': 'core'}

    id = Column(Integer, Sequence('co_distribution_point_id_seq'), primary_key=True)
    dist_point_number = Column(String(50))
    installation_date = Column(Date)
    inspection_interval = Column(Integer)
    inspection_interval_unit = Column(ForeignKey(u'codelist.cl_interval_unit.code', ondelete=u'RESTRICT',
                                      onupdate=u'CASCADE'))
    date_of_last_inspection = Column(Date)
    note = Column(Text)
    operating_state = Column(ForeignKey(u'codelist.cl_operating_state.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    date_of_status_change = Column(Date)
    height = Column(Numeric)
    network = Column(ForeignKey(u'core.co_network.id',
                                ondelete=u'SET NULL', onupdate=u'CASCADE'))
    geometry = Column(Geometry('POINT', 32736))

    cl_interval_unit = relationship(u'ClIntervalUnit')
    cl_operating_state = relationship(u'ClOperatingState')
    co_network = relationship(u'CoNetwork')


class CoUtilityStation(Base):
    __tablename__ = 'co_utility_station'
    __table_args__ = {u'schema': 'core'}

    id = Column(Integer, Sequence('co_utility_station_id_seq'), primary_key=True)
    station_number = Column(String(50))
    station_name = Column(String(50))
    installation_year = Column(Integer)
    inspection_interval = Column(Integer)
    inspection_interval_unit = Column(ForeignKey(u'codelist.cl_interval_unit.code', ondelete=u'RESTRICT',
                                      onupdate=u'CASCADE'))
    date_of_last_inspection = Column(Date)
    capacity = Column(Numeric)

    capacity_unit = Column(ForeignKey(u'codelist.cl_capacity_unit.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    operating_state = Column(ForeignKey(u'codelist.cl_operating_state.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    date_of_status_change = Column(Date)
    location = Column(ForeignKey(u'codelist.cl_location.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    station_type = Column(ForeignKey(u'codelist.cl_type_of_station.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    purpose = Column(ForeignKey(u'codelist.cl_purpose_of_station.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    height = Column(Numeric)
    note = Column(Text)
    network = Column(ForeignKey(u'core.co_network.id',
                                ondelete=u'SET NULL', onupdate=u'CASCADE'))
    geometry = Column(Geometry('POLYGON', 32736))

    cl_capacity_unit = relationship(u'ClCapacityUnit')
    cl_type_of_station = relationship(u'ClTypeOfStation')
    co_network = relationship(u'CoNetwork')
    cl_operating_state = relationship(u'ClOperatingState')
    cl_location = relationship(u'ClLocation')
    cl_purpose_of_station = relationship(u'ClPurposeOfStation')
    cl_interval_unit = relationship(u'ClIntervalUnit')


class CoLineCasing(Base):
    __tablename__ = 'co_line_casing'
    __table_args__ = {u'schema': 'core'}

    id = Column(Integer, Sequence('co_line_casing_id_seq'), primary_key=True)
    line_casing_number = Column(String(50))
    length = Column(Numeric)
    outer_height = Column(Numeric)
    outer_width = Column(Numeric)
    installation_date = Column(Date)
    inspection_interval = Column(Integer)
    inspection_interval_unit = Column(ForeignKey(u'codelist.cl_interval_unit.code', ondelete=u'RESTRICT',
                                      onupdate=u'CASCADE'))
    date_of_last_inspection = Column(Date)
    casing_type = Column(ForeignKey(u'codelist.cl_type_of_line_casing.code', ondelete=u'RESTRICT',
                                      onupdate=u'CASCADE'))
    jacket_pipe_diameter = Column(ForeignKey(u'codelist.cl_nominal_width_of_jacket_pipe.code', ondelete=u'RESTRICT',
                                      onupdate=u'CASCADE'))
    network = Column(ForeignKey(u'core.co_network.id',
                                      ondelete=u'SET NULL', onupdate=u'CASCADE'))
    geometry = Column(Geometry('LINESTRING', 32736))

    cl_type_of_line_casing = relationship(u'ClTypeOfLineCasing')
    cl_interval_unit = relationship(u'ClIntervalUnit')
    cl_nominal_width_of_jacket_pipe = relationship(u'ClNominalWidthOfJacketPipe')
    co_network = relationship(u'CoNetwork')


class CoConnectionPoint(Base):
    __tablename__ = 'co_connection_point'
    __table_args__ = {u'schema': 'core'}

    id = Column(Integer, Sequence('co_connection_point_id_seq'), primary_key=True)
    conn_point_number = Column(String(50))
    installation_length = Column(Numeric)
    installation_date = Column(Date)
    inspection_interval = Column(Integer)
    inspection_interval_unit = Column(ForeignKey(u'codelist.cl_interval_unit.code', ondelete=u'RESTRICT',
                                      onupdate=u'CASCADE'))
    date_of_last_inspection = Column(Date)
    note = Column(Text)
    conn_point_type = Column(ForeignKey(u'codelist.cl_type_of_connection_point.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    mounting_type = Column(ForeignKey(u'codelist.cl_mounting_type_of_connection_point.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    nominal_width = Column(ForeignKey(u'codelist.cl_nominal_width_of_connection_point.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    height = Column(Numeric)
    network = Column(ForeignKey(u'core.co_network.id',
                                ondelete=u'SET NULL', onupdate=u'CASCADE'))
    geometry = Column(Geometry('POINT', 32736))


    cl_connection_point_type = relationship(u'ClTypeOfConnectionPoint')
    cl_mounting_type = relationship(u'ClMountingTypeOfConnectionPoint')
    cl_nominal_width = relationship(u'ClNominalWidthOfConnectionPoint')
    co_network = relationship(u'CoNetwork')
    cl_interval_unit = relationship(u'ClIntervalUnit')


class CoBulkWaterMeter(Base):
    __tablename__ = 'co_bulk_water_meter'
    __table_args__ = {u'schema': 'core'}

    id = Column(Integer, Sequence('co_bulk_water_meter_id_seq'), primary_key=True)
    meter_number = Column(String(50))
    installation_date = Column(Date)
    meter_class = Column(ForeignKey(u'codelist.cl_meter_class.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))

    meter_type = Column(ForeignKey(u'codelist.cl_type_of_meter.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    inspection_interval = Column(Integer)
    inspection_interval_unit = Column(ForeignKey(u'codelist.cl_interval_unit.code', ondelete=u'RESTRICT',
                                      onupdate=u'CASCADE'))
    date_of_last_inspection = Column(Date)
    note = Column(Text)
    operating_state = Column(ForeignKey(u'codelist.cl_operating_state.code',
                                       ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    date_of_status_change = Column(Date)
    height = Column(Numeric)
    network = Column(ForeignKey(u'core.co_network.id',
                                ondelete=u'SET NULL', onupdate=u'CASCADE'))
    geometry = Column(Geometry('POINT', 32736))

    cl_interval_unit = relationship(u'ClIntervalUnit')
    cl_meter_class = relationship(u'ClMeterClass')
    cl_type_of_meter = relationship(u'ClMeterType')
    co_network = relationship(u'CoNetwork')
    cl_operating_state = relationship(u'ClOperatingState')


class CoDMA(Base):
    __tablename__ = 'co_dma'
    __table_args__ = {u'schema': 'core'}

    id = Column(Integer, Sequence('co_dma_id_seq'), primary_key=True)
    dma_number = Column(String(50))
    dma_name = Column(String(50))
    area = Column(Numeric)
    network = Column(ForeignKey(u'core.co_network.id',
                                ondelete=u'SET NULL', onupdate=u'CASCADE'))
    geometry = Column(Geometry('POLYGON', 32736))

    co_network = relationship(u'CoNetwork')


class CoDamage(Base):
    __tablename__ = 'co_damage'
    __table_args__ = {u'schema': 'core'}

    id = Column(Integer, Sequence('co_damage_id_seq'), primary_key=True)
    control_no = Column(Integer)
    received_from = Column(String(50))
    occurrence_timestamp = Column(DateTime)
    registration_timestamp = Column(DateTime)
    repair_timestamp = Column(DateTime)
    repaired_by = Column(String(50))
    repair_task = Column(String(100))
    damage_type = Column(ForeignKey(u'codelist.cl_damage_type.code', ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    damage_cause = Column(ForeignKey(u'codelist.cl_damage_cause.code', ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    damage_status = Column(ForeignKey(u'codelist.cl_damage_status.code', ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    buffer = Column(Integer)
    asset_type = Column(String(50))
    asset_id = Column(Integer)
    note = Column(Text)
    height = Column(Numeric)
    network = Column(ForeignKey(u'core.co_network.id',
                                ondelete=u'SET NULL', onupdate=u'CASCADE'))

    co_network = relationship(u'CoNetwork')
    cl_damage_type = relationship(u'ClDamageType')
    cl_damage_cause = relationship(u'ClDamageCause')
    cl_damage_status = relationship(u'ClDamageStatus')


class CoDocument(Base):
    __tablename__ = 'co_document'
    __table_args__ = {u'schema': 'core'}

    id = Column(Integer, Sequence('co_document_id_seq'), primary_key=True)
    document_number = Column(String(50))
    creation_date = Column(Date)
    creator = Column(String(50))
    file_name = Column(String(50))
    note = Column(Text)
    content = Column(LargeBinary)
    document_type = Column(ForeignKey(u'codelist.cl_type_of_document.code', ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    documented_type = Column(String(50))
    documented_id = Column(Integer)

    cl_type_of_document = relationship(u'ClTypeOfDocument')


class CoMaintenance(Base):
    __tablename__ = 'co_maintenance'
    __table_args__ = {u'schema': 'core'}

    id = Column(Integer, Sequence('co_maintenance_id_seq'), primary_key=True)
    maintenance_task = Column(String(100))
    maintenance_timestamp = Column(DateTime)
    maintained_by = Column(String(50))
    asset_type = Column(String(50))
    asset_id = Column(Integer)
    note = Column(Text)


class CoRepairMaterial(Base):
    __tablename__ = 'co_repair_material'
    __table_args__ = {u'schema': 'core'}

    id = Column(Integer, Sequence('co_repair_material_id_seq'), primary_key=True)
    amount = Column(Integer)
    material = Column(String(100))
    cost_total_tzs = Column(Numeric)
    damage = Column(ForeignKey(u'core.co_damage.id', ondelete=u'CASCADE', onupdate=u'CASCADE'))
    maintenance = Column(ForeignKey(u'core.co_maintenance.id', ondelete=u'CASCADE', onupdate=u'CASCADE'))

    co_damage = relationship(u'CoDamage')
    co_maintenance = relationship(u'CoMaintenance')


class SetGeneralSettings(Base):
    __tablename__ = 'set_general_settings'
    __table_args__ = {u'schema': 'settings'}

    id = Column(Integer, Sequence('set_general_settings_id_seq'), primary_key=True)
    base_url = Column(String(100))


class SetUserSettings(Base):
    __tablename__ = 'set_user_settings'
    __table_args__ = {u'schema': 'settings'}

    username = Column(String(50), primary_key=True)
    first_name = Column(String(70))
    surname = Column(String(70))
    default_network = Column(ForeignKey(u'core.co_network.id', ondelete=u'RESTRICT', onupdate=u'CASCADE'))
    co_network = relationship(u'CoNetwork')


class MxCustomer(Base):
    __tablename__ = 'mx_customer'
    __table_args__ = {u'schema': 'maxcom'}

    id = Column(Integer, primary_key=True)
    cons_name = Column(String(255))
    address = Column(String(255))
    house_no = Column(String(255))
    city = Column(String(255))
    status = Column(String(255))
    tariff_category_master_id = Column(Integer)
    id_number = Column(String(255))
    can = Column(String(255))


class MxTariffCategory(Base):
    __tablename__ = 'mx_tariff_category'
    __table_args__ = {u'schema': 'maxcom'}

    id = Column(Integer, primary_key=True)
    tariff_category = Column(String(255))
    type = Column(String(255))


class MxApplication(Base):
    __tablename__ = 'mx_application'
    __table_args__ = {u'schema': 'maxcom'}

    id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    middle_name = Column(String(255))
    last_name = Column(String(255))


class MxComplaint(Base):
    __tablename__ = 'mx_complaint'
    __table_args__ = {u'schema': 'maxcom'}

    id = Column(Integer, primary_key=True)
    complaint_date = Column(Date)


class MxWaterLeakageComplaint(Base):
    __tablename__ = 'mx_water_leakage_complaint'
    __table_args__ = {u'schema': 'maxcom'}

    id = Column(Integer, primary_key=True)
    leakage_type = Column(String(255))


class CoDistributionPointCustomer(Base):
    __tablename__ = 'co_distribution_point_customer'
    __table_args__ = {u'schema': 'core'}

    distribution_point = Column(ForeignKey(u'core.co_distribution_point.id', ondelete=u'CASCADE', onupdate=u'CASCADE'),
                    primary_key=True, nullable=False)
    maxcom_customer = Column(Integer, primary_key=True)

    co_distribution_point = relationship(u'CoDistributionPoint')
