from django.db import models


class MachineModel(models.Model):
    name = models.TextField(verbose_name="Модель техники")
    description = models.TextField(blank=True, verbose_name="Описание")

    def get_absolute_url(self):
        return f"/machinemodel"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Модель техники"


class EngineModel(models.Model):
    name = models.TextField(verbose_name="Модель двигателя")
    description = models.TextField(blank=True, verbose_name="Описание")

    def get_absolute_url(self):
        return f"/enginemodel"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Модель двигателя"
        
        
class TransmissionModel(models.Model):
    name = models.TextField(verbose_name="Модель трансмиссии")
    description = models.TextField(blank=True, verbose_name="Описание")

    def get_absolute_url(self):
        return f"/transmissionmodel"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Модель трансмиссии"


class DrivingAxleModel(models.Model):
    name = models.TextField(verbose_name="Модель ведущего моста")
    description = models.TextField(blank=True, verbose_name="Описание")

    def get_absolute_url(self):
        return f"/daxlemodel"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Модель ведущего моста"


class SteeringAxleModel(models.Model):
    name = models.TextField(verbose_name="Модель управляемого моста")
    description = models.TextField(blank=True, verbose_name="Описание")

    def get_absolute_url(self):
        return f"/saxlemodel"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Модель управляемого моста"


class ServiceCompany(models.Model):
    name = models.TextField(verbose_name="Название сервисной компании")
    description = models.TextField(blank=True, verbose_name="Описание")

    def get_absolute_url(self):
        return f"/servicecompany"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сервисная компания"


class MaintenanceType(models.Model):
    name = models.TextField(verbose_name="Вид ТО")
    description = models.TextField(verbose_name="Описание")

    def get_absolute_url(self):
        return f"/maintenancetype"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вид ТО"


class BreakdownUnit(models.Model):
    name = models.TextField(verbose_name="Узел отказа")
    description = models.TextField(verbose_name="Описание")

    def get_absolute_url(self):
        return f"/breakdownunit"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Узел отказа"


class RecoverMethod(models.Model):
    name = models.TextField(verbose_name="Способ восстановления")
    description = models.TextField(verbose_name="Описание")

    def get_absolute_url(self):
        return f"/recovermethod"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Способ восстановления"


class Machine(models.Model):
    machine_serial_number = models.TextField(unique=True, verbose_name="Зав. № машины")
    machine_model = models.ForeignKey(MachineModel, verbose_name="Модель техники", on_delete=models.CASCADE)
    engine_model = models.ForeignKey(EngineModel, verbose_name="Модель двигателя", on_delete=models.CASCADE)
    engine_serial_number = models.TextField(verbose_name="Зав. № двигателя")
    transmission_model = models.ForeignKey(TransmissionModel, verbose_name="Модель трансмиссии", on_delete=models.CASCADE)
    transmission_serial_number = models.TextField(verbose_name="Зав. № трансмиссии")
    driving_axle_model = models.ForeignKey(DrivingAxleModel, verbose_name="Модель ведущего моста", on_delete=models.CASCADE)
    driving_axle_serial_number = models.TextField(verbose_name="Зав. № ведущего моста")
    steering_axle_model = models.ForeignKey(SteeringAxleModel, verbose_name="Модель управляемого моста", on_delete=models.CASCADE)
    steering_axle_serial_number = models.TextField(verbose_name="Зав. № управляемого моста")
    contract = models.TextField(verbose_name="Договор поставки №, дата")
    from_factory_shipment_date = models.DateField(verbose_name="Дата отгрузки с завода")
    consignee = models.TextField(verbose_name="Грузополучатель (конечный потребитель)")
    delivery_address = models.TextField(verbose_name="Адрес поставки (эксплуатации)")
    additional_options = models.TextField(verbose_name="Комплектация (доп. опции)")
    client = models.TextField(verbose_name="Клиент")
    service_company = models.ForeignKey(ServiceCompany, verbose_name="Сервисная компания", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return f"/machines"

    def __str__(self):
        return self.machine_serial_number

    class Meta:
        verbose_name = "Машина"
        ordering = ["-from_factory_shipment_date"]


class Maintenance(models.Model):
    type_of_maintenance = models.ForeignKey(MaintenanceType, verbose_name="Вид ТО", on_delete=models.CASCADE)
    maintenance_date = models.DateField(verbose_name="Дата проведения ТО")
    operating_time = models.FloatField(verbose_name="Наработка, м/час")
    order_number = models.TextField(verbose_name="№ заказ-наряда")
    order_date = models.DateField(verbose_name="дата заказ-наряда")
    maintenance_organization = models.ForeignKey(ServiceCompany, verbose_name="Сервисная компания", on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, verbose_name="Зав. № машины", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return f"/maintenance"

    def __str__(self):
        return self.order_number

    class Meta:
        verbose_name = "Техническое обслуживание"
        ordering = ["-maintenance_date"]


class Claim(models.Model):
    failure_date = models.DateField(verbose_name="Дата отказа")
    operating_time = models.FloatField(verbose_name="Наработка, м/час")
    breakdown_unit = models.ForeignKey(BreakdownUnit, verbose_name="Узел отказа", on_delete=models.CASCADE)
    failure_description = models.TextField(verbose_name="Описание отказа")
    recover_method = models.ForeignKey(RecoverMethod, verbose_name="Способ восстановления", on_delete=models.CASCADE)
    used_parts = models.TextField(verbose_name="Используемые запасные части", null=True, blank=True)
    recover_date = models.DateField(verbose_name="Дата восстановления")
    machine = models.ForeignKey(Machine, verbose_name="Зав. № машины", on_delete=models.CASCADE)
    service_company = models.ForeignKey(ServiceCompany, verbose_name="Сервисная компания", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return f"/claim"

    def downtime(self):
        return (self.recover_date - self.failure_date).days

    def __str__(self):
        return self.failure_description

    class Meta:
        verbose_name = "Рекламации"
        ordering = ["-failure_date"]

