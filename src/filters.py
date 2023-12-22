from django_filters import FilterSet
from .models import (Machine, Maintenance, Claim, MachineModel, EngineModel, TransmissionModel,DrivingAxleModel,
                     SteeringAxleModel, ServiceCompany, MaintenanceType, BreakdownUnit, RecoverMethod)


class MachineFilter(FilterSet):

    class Meta:
        model = Machine
        fields = (
           "machine_model",
           "engine_model",
           "transmission_model",
           "driving_axle_model",
           "steering_axle_model",
        )


class MaintenanceFilter(FilterSet):

    class Meta:
        model = Maintenance
        fields = (
            "type_of_maintenance",
            "maintenance_organization",
            "machine",
        )


class ClaimFilter(FilterSet):

    class Meta:
        model = Claim
        fields =(
            "breakdown_unit",
            "recover_method",
            "service_company",
        )


class MachineModelFilter(FilterSet):

    class Meta:
        model = MachineModel
        fields = (
            "name",
            "description",
        )


class EngineModelFilter(FilterSet):

    class Meta:
        model = EngineModel
        fields = (
            "name",
            "description",
        )


class TransmissionModelFilter(FilterSet):

    class Meta:
        model = TransmissionModel
        fields = (
            "name",
            "description",
        )


class DrivingAxleModelFilter(FilterSet):

    class Meta:
        model = DrivingAxleModel
        fields = (
            "name",
            "description",
        )


class SteeringAxleModelFilter(FilterSet):

    class Meta:
        model = SteeringAxleModel
        fields = (
            "name",
            "description",
        )


class ServiceCompanyFilter(FilterSet):

    class Meta:
        model = ServiceCompany
        fields = (
            "name",
            "description",
        )


class MaintenanceTypeFilter(FilterSet):

    class Meta:
        model = MaintenanceType
        fields = (
            "name",
            "description",
        )


class BreakdownUnitFilter(FilterSet):

    class Meta:
        model = BreakdownUnit
        fields = (
            "name",
            "description",
        )


class RecoverMethodFilter(FilterSet):

    class Meta:
        model = RecoverMethod
        fields = (
            "name",
            "description",
        )
