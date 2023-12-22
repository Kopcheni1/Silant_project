from django.contrib import admin
from .models import (Machine, Maintenance, Claim, MachineModel, MaintenanceType, EngineModel, TransmissionModel,
                     DrivingAxleModel, SteeringAxleModel, ServiceCompany, BreakdownUnit, RecoverMethod)


@admin.register(Machine)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ("machine_serial_number", "machine_model", "engine_model", "engine_serial_number",
                    "transmission_model", "transmission_serial_number", "driving_axle_model",
                    "driving_axle_serial_number", "steering_axle_model", "steering_axle_serial_number", "contract",
                    "from_factory_shipment_date", "consignee", "delivery_address", "additional_options", "client",
                    "service_company")
    list_display_links = ("machine_serial_number", "machine_model", "engine_model", "engine_serial_number",
                          "transmission_model", "transmission_serial_number", "driving_axle_model",
                          "driving_axle_serial_number", "steering_axle_model", "steering_axle_serial_number", "contract",
                          "from_factory_shipment_date", "consignee", "delivery_address", "additional_options", "client",
                          "service_company")


@admin.register(Maintenance)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ("type_of_maintenance", "maintenance_date", "operating_time", "order_number", "order_date",
                    "maintenance_organization", "machine")
    list_display_links = ("type_of_maintenance", "maintenance_date", "operating_time", "order_number", "order_date",
                          "maintenance_organization", "machine")


@admin.register(Claim)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ("failure_date", "operating_time", "breakdown_unit", "failure_description", "recover_method",
                    "used_parts", "recover_date", "downtime", "machine", "service_company")
    list_display_links = ("failure_date", "operating_time", "breakdown_unit", "failure_description", "recover_method",
                          "used_parts", "recover_date", "downtime", "machine", "service_company")


@admin.register(MachineModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    list_display_links = ("name", "description")


@admin.register(EngineModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    list_display_links = ("name", "description")


@admin.register(TransmissionModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    list_display_links = ("name", "description")


@admin.register(DrivingAxleModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    list_display_links = ("name", "description")


@admin.register(SteeringAxleModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    list_display_links = ("name", "description")


@admin.register(ServiceCompany)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    list_display_links = ("name", "description")


@admin.register(MaintenanceType)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    list_display_links = ("name", "description")


@admin.register(BreakdownUnit)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    list_display_links = ("name", "description")


@admin.register(RecoverMethod)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    list_display_links = ("name", "description")
