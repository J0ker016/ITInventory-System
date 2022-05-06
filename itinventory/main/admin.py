from django.contrib import admin
from .models import *
from specification.models import *

#Change the look of the model in the admin page
class runing_number(admin.ModelAdmin):
    list_display = ('asset_type', 'running_number')
    def get_author(self, obj):
        return obj.specification_asset_running_number
class testtable(admin.ModelAdmin):
    list_display = ('name_image', 'image_tag')
    search_fields = ('name_image', 'image_file')
    list_per_page = 25

   
    def get_author(self, obj):
        return obj.main_testdb
class networkmodel(admin.ModelAdmin):
    list_display = ('model', 'asset_type')
    def get_author(self, obj):
        return obj.specification_NetworkHardwareModel

class ipmodel(admin.ModelAdmin):
    list_display = ('ip_address', 'ip_assisgned', 'status', 'remark')
    search_fields = ['ip_address', 'ip_assisgned', 'status', 'remark']

    def get_author(self, obj):
        return obj.main_IP

class PCDisplay(admin.ModelAdmin):
    list_display = ('computer_id', 'current_computer_id','type_of_purchase', 'pic', 'previous_pic',
    'pccurrentstatus','pctype','Brand','Model','windows','serial_number','asset_no','block','location','standard_installation','usbunlock','cdunlock','microsoft_office','microsoft_office_keys',
    'dop','dop_Warranty_end_date','po','invoice','vendor','processor_type','ram_type','ram_slot','total_ram','storage_type','storage_space','lan_mac_address',
    'lan_ip_address','wlan_mac_address','wlan_ip_address','joined_domain','connection_type','image_tag')
    search_fields = ('computer_id', 'lan_ip_address','wlan_ip_address',  'pic', 'previous_pic',)
    list_per_page = 8
    
    def get_author(self, obj):
        return obj.main_Computer

class LaptopDisplay(admin.ModelAdmin):
    list_display = ('computer_id', 'current_computer_id', 'pic', 'previous_pic',
    'pccurrentstatus','Brand','Model','windows','serial_number','asset_no','block','location','standard_installation','usbunlock','cdunlock','microsoft_office','microsoft_office_keys',
    'dop','dop_Warranty_end_date','po','invoice','vendor','processor_type','ram_type','ram_slot','total_ram','storage_type','storage_space','lan_mac_address',
    'lan_ip_address','wlan_mac_address','wlan_ip_address','joined_domain','connection_type','image_tag')
    search_fields = ('computer_id', 'lan_ip_address','wlan_ip_address',  'pic', 'previous_pic',)
    list_per_page = 8
    
    def get_author(self, obj):
        return obj.main_Laptop

# Register your models here.     
admin.site.register(Computer, PCDisplay)

admin.site.register(Laptop, LaptopDisplay)
admin.site.register(NetworkHardware)
admin.site.register(UserAsset)
admin.site.register(Loan)
admin.site.register(IP, ipmodel)
admin.site.register(Brand)
admin.site.register(ModelPC)
admin.site.register(Modellaptop)
admin.site.register(ModelPCMachine)
admin.site.register(Software)
admin.site.register(Processor_type)
admin.site.register(Ram_type)
admin.site.register(Microsoft_office)
admin.site.register(Location)
admin.site.register(Windows)
admin.site.register(vendor)
admin.site.register(Hardware_type)
admin.site.register(NetworkAsset_brand)
admin.site.register(Asset_running_number, runing_number)
admin.site.register(NetworkHardwareModel, networkmodel)
admin.site.register(NetworkAsset_vendor)
admin.site.register(NetworkAsset_location)
admin.site.register(NetworkAsset_block)
admin.site.register(storagevalue)
admin.site.register(softwareUser)
admin.site.register(loghistory)
admin.site.register(testdb, testtable)
# Register your models here.
