from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import (Machine, Maintenance, Claim, MachineModel, EngineModel, TransmissionModel, DrivingAxleModel,
                     SteeringAxleModel, ServiceCompany, MaintenanceType, BreakdownUnit, RecoverMethod)
from .forms import (MachineForm, MaintenanceForm, ClaimForm, MachineModelForm, EngineModelForm, TransmissionModelForm,
                    DrivingAxleModelForm, SteeringAxleModelForm, ServiceCompanyForm, MaintenanceTypeForm,
                    BreakdownUnitForm, RecoverMethodForm)
from .filters import (MachineFilter, MaintenanceFilter, ClaimFilter, MachineModelFilter, EngineModelFilter,
                      TransmissionModelFilter, DrivingAxleModelFilter, SteeringAxleModelFilter, ServiceCompanyFilter,
                      MaintenanceTypeFilter, BreakdownUnitFilter, RecoverMethodFilter)


class MaintenanceListView(LoginRequiredMixin, ListView):
    model = Maintenance
    template_name = "./maintenance/maintenances.html"

    def get_context_data(self, *args, **kwargs):
        filter = MaintenanceFilter(self.request.GET, queryset=self.get_queryset())
        manager = self.request.user.groups.filter(name="Менеджер")
        if not manager.exists():
            is_manager = "НЕ менеджер"
        else:
            is_manager = "Менеджер"
        context = {"filter": filter, "is_manager": is_manager}
        return context


class MaintenanceCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ("src.add_maintenance",)
    template_name = "./maintenance/maintenance_create.html"
    form_class = MaintenanceForm


class MaintenanceUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ("src.change_maintenance",)
    template_name = "./maintenance/maintenance_create.html"
    form_class = MaintenanceForm

    def get_object(self, *args, **kwargs):
        id = self.kwargs.get("pk")
        return Maintenance.objects.get(pk=id)


class MaintenanceDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ("src.delete_maintenance",)
    template_name = "./maintenance/maintenance_delete.html"
    queryset = Maintenance.objects.all()
    success_url = "/maintenance/"


def maintenance_detail(request, maintenance_id):
    is_authenticated = request.user.groups.exists()
    manager = request.user.groups.filter(name="Менеджер")
    if not manager.exists():
        is_manager = "НЕ менеджер"
    else:
        is_manager = "Менеджер"
    if is_authenticated:
        maintenance_d = Maintenance.objects.get(pk=maintenance_id)
        machine = Machine.objects.get(machine_serial_number=maintenance_d.machine)
        maintenance = MaintenanceType.objects.get(name=maintenance_d.type_of_maintenance)
        service_company = ServiceCompany.objects.get(name=maintenance_d.maintenance_organization)
        context = {"maintenance_d": maintenance_d,
                   "machine": machine,
                   "is_authenticated": is_authenticated,
                   "maintenance": maintenance,
                   "service_company": service_company,
                   "is_manager": is_manager
                   }
    else:
        maintenance_d = "Для этого действия требуется авторизация"
        context = {"maintenance_d": maintenance_d}
    return render(request, "./maintenance/maintenance_detail.html", context)


def machine_maintenance_list(request, machine_id):
    is_authenticated = request.user.groups.exists()
    manager = request.user.groups.filter(name="Менеджер")
    if not manager.exists():
        is_manager = "НЕ менеджер"
    else:
        is_manager = "Менеджер"
    if is_authenticated:
        maintenance_list = Maintenance.objects.filter(machine=machine_id)
        machine = Machine.objects.get(pk=machine_id)
        context = {"maintenance_list": maintenance_list,
                   "machine": machine,
                   "is_authenticated": is_authenticated,
                   "is_manager": is_manager
                   }
    else:
        maintenance_list = "Для этого действия требуется авторизация"
        context = {"maintenance_list": maintenance_list}
    return render(request, "./maintenance/machine_maintenance_list.html", context)


class ClaimListView(LoginRequiredMixin, ListView):
    model = Claim
    context_object_name = "claim"
    template_name = "./claim/claims.html"

    def get_context_data(self, *args, **kwargs):
        filter = ClaimFilter(self.request.GET, queryset=self.get_queryset())
        manager = self.request.user.groups.filter(name="Менеджер")
        if not manager.exists():
            is_manager = "НЕ менеджер"
        else:
            is_manager = "Менеджер"
        context = {"filter": filter, "is_manager": is_manager}
        return context


class ClaimCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ("src.add_claim",)
    template_name = "./claim/claim_create.html"
    form_class = ClaimForm


class ClaimUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ("src.change_claim",)
    template_name = "./claim/claim_create.html"
    form_class = ClaimForm

    def get_object(self, *args, **kwargs):
        id = self.kwargs.get("pk")
        return Claim.objects.get(pk=id)


class ClaimDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ("src.delete_claim",)
    template_name = "./claim/claim_delete.html"
    queryset = Claim.objects.all()
    success_url = "/claim/"


def claim_detail(request, claim_id):
    is_authenticated = request.user.groups.exists()
    manager = request.user.groups.filter(name="Менеджер")
    if not manager.exists():
        is_manager = "НЕ менеджер"
    else:
        is_manager = "Менеджер"
    if is_authenticated:
        claim_d = Claim.objects.get(pk=claim_id)
        machine = Machine.objects.get(machine_serial_number=claim_d.machine)
        unit = BreakdownUnit.objects.get(name=claim_d.breakdown_unit)
        recover = RecoverMethod.objects.get(name=claim_d.recover_method)
        service_company = ServiceCompany.objects.get(name=claim_d.service_company)
        context = {"claim_d": claim_d,
                   "machine": machine,
                   "is_authenticated": is_authenticated,
                   "unit": unit,
                   "recover": recover,
                   "service": service_company,
                   "is_manager": is_manager
                   }
    else:
        claim_d = "Для этого действия требуется авторизация"
        context = {"claim_d": claim_d}
    return render(request, "./claim/claim_detail.html", context)


def machine_claim_list(request, machine_id):
    is_authenticated = request.user.groups.exists()
    manager = request.user.groups.filter(name="Менеджер")
    if not manager.exists():
        is_manager = "НЕ менеджер"
    else:
        is_manager = "Менеджер"
    if is_authenticated:
        claim_list = Claim.objects.filter(machine=machine_id)
        machine = Machine.objects.get(pk=machine_id)
        context = {"claim_list": claim_list,
                   "machine": machine,
                   "is_authenticated": is_authenticated,
                   "is_manager": is_manager
                   }
    else:
        claim_list = "Для этого действия требуется авторизация"
        context = {"claim_list": claim_list}
    return render(request, "./claim/machine_claims.html", context)


class SearchMachines(ListView):
    model = Machine
    template_name = "./machine/search.html"
    context_object_name = "machine"

    def get_queryset(self, *args, **kwargs):
        search_query = self.request.GET.get("search", "")
        if search_query:
            machine = Machine.objects.filter(machine_serial_number__icontains=search_query)
            if not machine.exists():
                machine = "К сожалению ничего не найдено"
        else:
            machine = "К сожалению ничего не найдено"
        context = machine
        return context

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_authenticated"] = self.request.user.groups.exists()
        return context


class MachineCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ("src.add_machine",)
    template_name = "./machine/machine_create.html"
    form_class = MachineForm


class MachineUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ("src.change_machine",)
    template_name = "./machine/machine_create.html"
    form_class = MachineForm

    def get_object(self, *args, **kwargs):
        id = self.kwargs.get("pk")
        return Machine.objects.get(pk=id)


class MachineDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ("src.delete_machine",)
    template_name = "./machine/machine_delete.html"
    queryset = Machine.objects.all()
    success_url = "/machine/"


def machine_by_user(request):
    is_authenticated = request.user.groups.exists()
    manager = request.user.groups.filter(name="Менеджер")
    if not manager.exists():
        is_manager = "НЕ менеджер"
    else:
        is_manager = "Менеджер"

    filter = MachineFilter(request.GET)
    if is_authenticated:
        if is_manager == "Менеджер":
            machine = 0
        else:
            machine = Machine.objects.filter(client=request.user.first_name)
            if not machine.exists():
                service_list = ServiceCompany.objects.filter(name=request.user.first_name)
                if service_list.exists():
                    service = ServiceCompany.objects.get(name=request.user.first_name)
                    machine = Machine.objects.filter(service_company=service.id)
                else:
                    machine = "К сожалению ничего не найдено"
        context = {"machine": machine,
                   "is_authenticated": is_authenticated,
                   "filter": filter,
                   "is_manager": is_manager
                   }
    else:
        machine = "Для этого действия требуется авторизация"
        context = {"machine": machine}
    return render(request, "machine.html", context)


def machine_detail(request, machine_id):
    is_authenticated = request.user.groups.exists()
    manager = request.user.groups.filter(name="Менеджер")
    if not manager.exists():
        is_manager = "НЕ менеджер"
    else:
        is_manager = "Менеджер"
    if is_authenticated:
        machine_d = Machine.objects.get(pk=machine_id)
        machine = MachineModel.objects.get(name=machine_d.machine_model)
        engine = EngineModel.objects.get(name=machine_d.engine_model)
        transmission = TransmissionModel.objects.get(name=machine_d.transmission_model)
        daxle = DrivingAxleModel.objects.get(name=machine_d.driving_axle_model)
        saxle = SteeringAxleModel.objects.get(name=machine_d.steering_axle_model)
        service = ServiceCompany.objects.get(name=machine_d.service_company)
        context = {"machine_d": machine_d,
                   "machine": machine,
                   "is_authenticated": is_authenticated,
                   "engine": engine,
                   "transmission": transmission,
                   "daxle": daxle,
                   "saxle": saxle,
                   "service": service,
                   "is_manager": is_manager
                   }
    else:
        machine_d = "Для этого действия требуется авторизация"
        context = {"machine_d": machine_d}
    return render(request, "./machine/machine_detail.html", context)


class MachineModelListView(PermissionRequiredMixin, ListView):
    permission_required = ("src.view_machinemodel",)
    model = MachineModel
    context_object_name = "machinemodel"
    template_name = "./lists/machinemodel_list.html"
    queryset = MachineModel.objects.all()
    login_url = "/"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = MachineModelFilter(self.request.GET, queryset=self.get_queryset())
        return context


class MachineModelCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ("src.add_machinemodel",)
    template_name = "./lists/machinemodel_create.html"
    form_class = MachineModelForm
    login_url = "/"
    

class MachineModelUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ("src.change_machinemodel",)
    template_name = "./lists/machinemodel_create.html"
    form_class = MachineModelForm

    def get_object(self, *args, **kwargs):
        id = self.kwargs.get("pk")
        return MachineModel.objects.get(pk=id)
    
    
class MachineModelDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ("src.delete_machinemodel",)
    template_name = "./lists/machinemodel_delete.html"
    queryset = MachineModel.objects.all()
    success_url = "/machinemodel/"
    login_url = "/"


class EngineModelListView(PermissionRequiredMixin, ListView):
    permission_required = ("src.view_enginemodel",)
    model = EngineModel
    context_object_name = "enginemodel"
    template_name = "./lists/enginemodel_list.html"
    queryset = EngineModel.objects.all()
    login_url = "/"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = EngineModelFilter(self.request.GET, queryset=self.get_queryset())
        return context


class EngineModelCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ("src.add_enginemodel",)
    template_name = "./lists/machinemodel_create.html"
    form_class = EngineModelForm
    login_url = "/"


class EngineModelUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ("src.change_enginemodel",)
    template_name = "./lists/machinemodel_create.html"
    form_class = EngineModelForm

    def get_object(self, *args, **kwargs):
        id = self.kwargs.get("pk")
        return EngineModel.objects.get(pk=id)


class EngineModelDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ("src.delete_enginemodel",)
    template_name = "./lists/enginemodel_delete.html"
    queryset = EngineModel.objects.all()
    success_url = "/enginemodel/"
    login_url = "/"


class TransmissionModelListView(PermissionRequiredMixin, ListView):
    permission_required = ("src.view_transmissionmodel",)
    model = TransmissionModel
    context_object_name = "transmissionmodel"
    template_name = "./lists/transmissionmodel_list.html"
    queryset = TransmissionModel.objects.all()
    login_url = "/"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = TransmissionModelFilter(self.request.GET, queryset=self.get_queryset())
        return context


class TransmissionModelCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ("src.add_transmissionmodel",)
    template_name = "./lists/machinemodel_create.html"
    form_class = TransmissionModelForm
    login_url = "/"


class TransmissionModelUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ("src.change_transmissionmodel",)
    template_name = "./lists/machinemodel_create.html"
    form_class = TransmissionModelForm

    def get_object(self, *args, **kwargs):
        id = self.kwargs.get("pk")
        return TransmissionModel.objects.get(pk=id)


class TransmissionModelDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ("src.delete_transmissionmodel",)
    template_name = "./lists/transmissionmodel_delete.html"
    queryset = TransmissionModel.objects.all()
    success_url = "/transmissionmodel/"
    login_url = "/"


class DrivingAxleModelListView(PermissionRequiredMixin, ListView):
    permission_required = ("src.view_drivingaxlemodel",)
    model = DrivingAxleModel
    context_object_name = "drivingaxlemodel"
    template_name = "./lists/drivingaxlemodel_list.html"
    queryset = DrivingAxleModel.objects.all()
    login_url = "/"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = DrivingAxleModelFilter(self.request.GET, queryset=self.get_queryset())
        return context


class DrivingAxleModelCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ("src.add_drivingaxlemodel",)
    template_name = "./lists/machinemodel_create.html"
    form_class = DrivingAxleModelForm
    login_url = "/"


class DrivingAxleModelUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ("src.change_drivingaxlemodel",)
    template_name = "./lists/machinemodel_create.html"
    form_class = DrivingAxleModelForm

    def get_object(self, *args, **kwargs):
        id = self.kwargs.get("pk")
        return DrivingAxleModel.objects.get(pk=id)


class DrivingAxleModelDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ("src.delete_drivingaxlemodel",)
    template_name = "./lists/drivingaxlemodel_delete.html"
    queryset = DrivingAxleModel.objects.all()
    success_url = "/daxlemodel/"
    login_url = "/"


class SteeringAxleModelListView(PermissionRequiredMixin, ListView):
    permission_required = ("src.view_steeringaxlemodel",)
    model = SteeringAxleModel
    context_object_name = "steeringbridgemodel"
    template_name = "./lists/steeringbridgemodel_list.html"
    queryset = SteeringAxleModel.objects.all()
    login_url = "/"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = SteeringAxleModelFilter(self.request.GET, queryset=self.get_queryset())
        return context


class SteeringAxleModelCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ("src.add_steeringaxlemodel",)
    template_name = "./lists/machinemodel_create.html"
    form_class = SteeringAxleModelForm
    login_url = "/"


class SteeringAxleModelUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ("src.change_steeringaxlemodel",)
    template_name = "./lists/machinemodel_create.html"
    form_class = SteeringAxleModelForm

    def get_object(self, *args, **kwargs):
        id = self.kwargs.get("pk")
        return SteeringAxleModel.objects.get(pk=id)


class SteeringAxleModelDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ("src.delete_steeringaxlemodel",)
    template_name = "./lists/steeringaxlemodel_delete.html"
    queryset = SteeringAxleModel.objects.all()
    success_url = "/saxlemodel/"
    login_url = "/"


class ServiceCompanyListView(PermissionRequiredMixin, ListView):
    permission_required = ("src.view_servicecompany",)
    model = ServiceCompany
    context_object_name = "servicecompany"
    template_name = "./lists/servicecompany_list.html"
    queryset = ServiceCompany.objects.all()
    login_url = "/"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = ServiceCompanyFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ServiceCompanyCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ("src.add_servicecompany",)
    template_name = "./lists/machinemodel_create.html"
    form_class = ServiceCompanyForm
    login_url = "/"


class ServiceCompanyUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ("src.change_servicecompany",)
    template_name = "./lists/machinemodel_create.html"
    form_class = ServiceCompanyForm

    def get_object(self, *args, **kwargs):
        id = self.kwargs.get("pk")
        return ServiceCompany.objects.get(pk=id)


class ServiceCompanyDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ("src.delete_servicecompany",)
    template_name = "./lists/servicecompany_delete.html"
    queryset = ServiceCompany.objects.all()
    success_url = "/servicecompany/"
    login_url = "/"


class MaintenanceTypeListView(PermissionRequiredMixin, ListView):
    permission_required = ("src.view_maintenancetype",)
    model = MaintenanceType
    context_object_name = "maintenancetype"
    template_name = "./lists/maintenancetype_list.html"
    queryset = MaintenanceType.objects.all()
    login_url = "/"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = MaintenanceTypeFilter(self.request.GET, queryset=self.get_queryset())
        return context


class MaintenanceTypeCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ("src.add_maintenancetype",)
    template_name = "./lists/machinemodel_create.html"
    form_class = MaintenanceTypeForm
    login_url = "/"


class MaintenanceTypeUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ("src.change_maintenancetype",)
    template_name = "./lists/machinemodel_create.html"
    form_class = MaintenanceTypeForm

    def get_object(self, *args, **kwargs):
        id = self.kwargs.get("pk")
        return MaintenanceType.objects.get(pk=id)


class MaintenanceTypeDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ("src.delete_maintenancetype",)
    template_name = "./lists/maintenancetype_delete.html"
    queryset = MaintenanceType.objects.all()
    success_url = "/maintenancetype/"
    login_url = "/"


class BreakdownUnitListView(PermissionRequiredMixin, ListView):
    permission_required = ("src.view_breakdownunit",)
    model = BreakdownUnit
    context_object_name = "breakdownunit"
    template_name = "./lists/breakdownunit_list.html"
    queryset = BreakdownUnit.objects.all()
    login_url = "/"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = BreakdownUnitFilter(self.request.GET, queryset=self.get_queryset())
        return context


class BreakdownUnitCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ("src.add_breakdownunit",)
    template_name = "./lists/machinemodel_create.html"
    form_class = BreakdownUnitForm
    login_url = "/"


class BreakdownUnitUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ("src.change_breakdownunit",)
    template_name = "./lists/machinemodel_create.html"
    form_class = BreakdownUnitForm

    def get_object(self, *args, **kwargs):
        id = self.kwargs.get("pk")
        return BreakdownUnit.objects.get(pk=id)


class BreakdownUnitDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ("src.delete_breakdownunit",)
    template_name = "./lists/breakdownunit_delete.html"
    queryset = BreakdownUnit.objects.all()
    success_url = "/breakdownunit/"
    login_url = "/"


class RecoverMethodListView(PermissionRequiredMixin, ListView):
    permission_required = ("src.view_recovermethod",)
    model = RecoverMethod
    context_object_name = "recovermethod"
    template_name = "./lists/recovermethod_list.html"
    queryset = RecoverMethod.objects.all()
    login_url = "/"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = RecoverMethodFilter(self.request.GET, queryset=self.get_queryset())
        return context


class RecoverMethodCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ("src.add_recovermethod",)
    template_name = "./lists/machinemodel_create.html"
    form_class = RecoverMethodForm
    login_url = "/"


class RecoverMethodUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ("src.change_recovermethod",)
    template_name = "./lists/machinemodel_create.html"
    form_class = RecoverMethodForm

    def get_object(self, *args, **kwargs):
        id = self.kwargs.get("pk")
        return RecoverMethod.objects.get(pk=id)


class RecoverMethodDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ("src.delete_recovermethod",)
    template_name = "./lists/recovermethod_delete.html"
    queryset = RecoverMethod.objects.all()
    success_url = "/recovermethod/"
    login_url = "/"
