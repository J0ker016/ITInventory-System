from django.db import models

# Create your models here.

# Brand table
class Brand(models.Model):
    Brand_name = models.CharField(max_length=100)
    def __str__(self):
        return self.Brand_name
       
# ModelPC table
class ModelPC(models.Model):
    ModelPC_name = models.CharField(max_length=100)
    def __str__(self):
        return self.ModelPC_name

# Modellaptop table
class Modellaptop(models.Model):
    Modellaptop_name = models.CharField(max_length=100)
    def __str__(self):
        return self.Modellaptop_name

# ModelPCMachine table
class ModelPCMachine(models.Model):
    ModelPCMAchine_name = models.CharField(max_length=100)
    def __str__(self):
        return self.ModelPCMAchine_name

# Processor_type table
class Processor_type(models.Model):
    Processor_name = models.CharField(max_length=100)
    def __str__(self):
        return self.Processor_name


# Software table
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
    

# Ram_type table
class Ram_type(models.Model):
    ram_type = models.CharField(max_length=100)
    def __str__(self):
        return self.ram_type
    class Meta:
        db_table = 'Ram_type'
        # Add verbose name
        verbose_name = 'Ram Type'

# Microsoft_office table
class Microsoft_office(models.Model):
    microsoft_office = models.CharField(max_length=100)
    def __str__(self):
        return self.microsoft_office
    class Meta:
        db_table = 'Microsoft_office'
        # Add verbose name
        verbose_name = 'Microsoft Office'

# Location table
class Location(models.Model):
    location = models.CharField(max_length=100)
    def __str__(self):
        return self.location
    class Meta:
        db_table = 'Location'
        # Add verbose name
        verbose_name = 'Location'

# Windows table
class Windows(models.Model):
    windows = models.CharField(max_length=100)
    def __str__(self):
        return self.windows
    class Meta:
        db_table = 'Windows'
        # Add verbose name
        verbose_name = 'Window'

# vendor table
class vendor(models.Model):
    vendorname = models.CharField(max_length=100)
    def __str__(self):
        return self.vendorname
    class Meta:
        db_table = 'vendor'
        # Add verbose name
        verbose_name = 'Vendor'

# Hardware_type table
class Hardware_type(models.Model):
    hardware_type = models.CharField(max_length=100)
    def __str__(self):
        return self.hardware_type
    class Meta:
        db_table = 'Hardware_type'
        # Add verbose name
        verbose_name = 'Hardware Type'


# NetworkAsset_brand table
class NetworkAsset_brand(models.Model):
    networkAsset_brand = models.CharField(max_length=100)
    def __str__(self):
        return self.networkAsset_brand

    class Meta:
        db_table = 'NetworkAsset_brand'
        # Add verbose name
        verbose_name = 'Network Asset Brand Type'

# Asset_running_number table
class Asset_running_number(models.Model):
    asset_type = models.CharField(max_length=100)
    running_number = models.CharField(max_length=1000)
    class Meta:
        db_table = 'Asset_running_number'
        # Add verbose name
        verbose_name = 'Asset Running Number'

# NetworkHardwareModel table
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
   
# NetworkAsset_vendor table
class NetworkAsset_vendor(models.Model):
    networkAsset_vendor = models.CharField(max_length=100)
    def __str__(self):
        return self.networkAsset_vendor
    class Meta:
        db_table = 'NetworkAsset_vendor'
        # Add verbose name
        verbose_name = 'Network Asset Vendor'

# NetworkAsset_location table
class NetworkAsset_location(models.Model):
    networkAsset_location = models.CharField(max_length=100)
    def __str__(self):
        return self.networkAsset_location
    class Meta:
        db_table = 'NetworkAsset_location'
        # Add verbose name
        verbose_name = 'Network Asset Location'

# NetworkAsset_block table
class NetworkAsset_block(models.Model):
    networkAsset_block = models.CharField(max_length=100)
    def __str__(self):
        return self.networkAsset_block
    class Meta:
        db_table = 'NetworkAsset_block'
        # Add verbose name
        verbose_name = 'Network Asset Block'

# storagevalue table
class storagevalue(models.Model):
    Storagevalue = models.CharField(max_length=100)
    def __str__(self):
        return self.Storagevalue
    class Meta:
        db_table = 'storagevalue'
        # Add verbose name
        verbose_name = 'Storage Value'
