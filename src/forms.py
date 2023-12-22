from django.forms import ModelForm
from .models import (Machine, Maintenance, Claim, MachineModel, EngineModel, TransmissionModel, DrivingAxleModel,
                     SteeringAxleModel, ServiceCompany, MaintenanceType, BreakdownUnit, RecoverMethod)


class MachineForm(ModelForm):

    class Meta:
        model = Machine
        fields = [
            "machine_serial_number",
            "machine_model",
            "engine_model",
            "engine_serial_number",
            "transmission_model",
            "transmission_serial_number",
            "driving_axle_model",
            "driving_axle_serial_number",
            "steering_axle_model",
            "steering_axle_serial_number",
            "contract",
            "from_factory_shipment_date",
            "consignee",
            "delivery_address",
            "additional_options",
            "client",
            "service_company",
        ]


class MaintenanceForm(ModelForm):

    class Meta:
        model = Maintenance
        fields = [
            "type_of_maintenance",
            "maintenance_date",
            "operating_time",
            "order_number",
            "order_date",
            "maintenance_organization",
            "machine",
        ]


class ClaimForm(ModelForm):

    class Meta:
        model = Claim
        fields = [
            "failure_date",
            "operating_time",
            "breakdown_unit",
            "failure_description",
            "recover_method",
            "used_parts",
            "recover_date",
            "machine",
            "service_company",
        ]


class MachineModelForm(ModelForm):

    class Meta:
        model = MachineModel
        fields = [
            "name",
            "description",
        ]

class EngineModelForm(ModelForm):

    class Meta:
        model = EngineModel
        fields = [
            "name",
            "description",
        ]

class TransmissionModelForm(ModelForm):

    class Meta:
        model = TransmissionModel
        fields = [
            "name",
            "description",
        ]

class DrivingAxleModelForm(ModelForm):

    class Meta:
        model = DrivingAxleModel
        fields = [
            "name",
            "description",
        ]

class SteeringAxleModelForm(ModelForm):

    class Meta:
        model = SteeringAxleModel
        fields = [
            "name",
            "description",
        ]

class ServiceCompanyForm(ModelForm):

    class Meta:
        model = ServiceCompany
        fields = [
            "name",
            "description",
        ]


class MaintenanceTypeForm(ModelForm):

    class Meta:
        model = MaintenanceType
        fields = [
            "name",
            "description",
        ]


class BreakdownUnitForm(ModelForm):

    class Meta:
        model = BreakdownUnit
        fields = [
            "name",
            "description",
        ]


class RecoverMethodForm(ModelForm):

    class Meta:
        model = RecoverMethod
        fields = [
            "name",
            "description",
        ]