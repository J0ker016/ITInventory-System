from django.db import models

# Create your models here.

class Brand(models.Model):
    Brand_name = models.CharField(max_length=100)
    def __str__(self):
        return self.Brand_name
       

class ModelPC(models.Model):
    ModelPC_name = models.CharField(max_length=100)
    def __str__(self):
        return self.ModelPC_name

class Modellaptop(models.Model):
    Modellaptop_name = models.CharField(max_length=100)
    def __str__(self):
        return self.Modellaptop_name


class ModelPCMachine(models.Model):
    ModelPCMAchine_name = models.CharField(max_length=100)
    def __str__(self):
        return self.ModelPCMAchine_name

class Processor_type(models.Model):
    Processor_name = models.CharField(max_length=100)
    def __str__(self):
        return self.Processor_name

typespftware = [
    ('Concurrent', 'Concurrent'),
    ('Non-Concurrent', 'Non-Concurrent'),
]
class Software(models.Model):
    Software_name = models.CharField(max_length=100)
    Software_version = models.CharField(max_length=100)
    software_type = models.CharField(max_length=100, choices = typespftware)
 
    software_quantity = models.CharField(max_length=100, blank=True)
    software_quantity_left = models.CharField(max_length=100, blank=True)
    Software_po = models.CharField(max_length=100, blank=True)
    Software_DOP = models.DateField(blank=True, null=True)
    


class Ram_type(models.Model):
    ram_type = models.CharField(max_length=100)
    def __str__(self):
        return self.ram_type
    class Meta:
        db_table = 'Ram_type'
        # Add verbose name
        verbose_name = 'Ram Type'

class Microsoft_office(models.Model):
    microsoft_office = models.CharField(max_length=100)
    def __str__(self):
        return self.microsoft_office
    class Meta:
        db_table = 'Microsoft_office'
        # Add verbose name
        verbose_name = 'Microsoft Office'

class Location(models.Model):
    location = models.CharField(max_length=100)
    def __str__(self):
        return self.location
    class Meta:
        db_table = 'Location'
        # Add verbose name
        verbose_name = 'Location'

class Windows(models.Model):
    windows = models.CharField(max_length=100)
    def __str__(self):
        return self.windows
    class Meta:
        db_table = 'Windows'
        # Add verbose name
        verbose_name = 'Window'

class vendor(models.Model):
    vendorname = models.CharField(max_length=100)
    def __str__(self):
        return self.vendorname
    class Meta:
        db_table = 'vendor'
        # Add verbose name
        verbose_name = 'Vendor'
class Hardware_type(models.Model):
    hardware_type = models.CharField(max_length=100)
    def __str__(self):
        return self.hardware_type
    class Meta:
        db_table = 'Hardware_type'
        # Add verbose name
        verbose_name = 'Hardware Type'

class NetworkAsset_brand(models.Model):
    networkAsset_brand = models.CharField(max_length=100)
    def __str__(self):
        return self.networkAsset_brand

    class Meta:
        db_table = 'NetworkAsset_brand'
        # Add verbose name
        verbose_name = 'Network Asset Brand Type'

class Asset_running_number(models.Model):
    asset_type = models.CharField(max_length=100)
    running_number = models.CharField(max_length=1000)
    class Meta:
        db_table = 'Asset_running_number'
        # Add verbose name
        verbose_name = 'Asset Running Number'

networktype = [
    ('Wireless Dongle', 'Wireless Dongle'),
    ('Tape Library', 'Tape Library'),
    ('Switches', 'Switches'),
    ('Storage Devices', 'Storage Devices'),
    ('Print Server', 'Print Server'),
    ('Network Monitor', 'Network Monitor'),
    ('Firewall', 'Firewall'),
    ('Door Access', 'Door Access'),
    ('Conference Phone', 'Conference Phone'),
    ('CCTV DVR', 'CCTV DVR'),
    ('CCTV Camera', 'CCTV Camera'),
    ('AP', 'AP'),
    ('Server', 'Server'),
  

]
class NetworkHardwareModel(models.Model):
    model = models.CharField(max_length=100)
    asset_type = models.CharField(max_length=1000,  choices = networktype)
    class Meta:
        db_table = 'NetworkHardwareModel'
        # Add verbose name
        verbose_name = 'Network Hardware Model'
   

class NetworkAsset_vendor(models.Model):
    networkAsset_vendor = models.CharField(max_length=100)
    def __str__(self):
        return self.networkAsset_vendor
    class Meta:
        db_table = 'NetworkAsset_vendor'
        # Add verbose name
        verbose_name = 'Network Asset Vendor'

class NetworkAsset_location(models.Model):
    networkAsset_location = models.CharField(max_length=100)
    def __str__(self):
        return self.networkAsset_location
    class Meta:
        db_table = 'NetworkAsset_location'
        # Add verbose name
        verbose_name = 'Network Asset Location'

class NetworkAsset_block(models.Model):
    networkAsset_block = models.CharField(max_length=100)
    def __str__(self):
        return self.networkAsset_block
    class Meta:
        db_table = 'NetworkAsset_block'
        # Add verbose name
        verbose_name = 'Network Asset Block'

class storagevalue(models.Model):
    Storagevalue = models.CharField(max_length=100)
    def __str__(self):
        return self.Storagevalue
    class Meta:
        db_table = 'storagevalue'
        # Add verbose name
        verbose_name = 'Storage Value'
