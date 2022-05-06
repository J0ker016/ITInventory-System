from django.db import models
from django.utils.html import format_html

# Create your models here.

# Create your models here/database.

# Computer table
class Computer(models.Model):
    computer_id = models.CharField(max_length=100)
    current_computer_id = models.CharField(max_length=100)
    current_computer_id = models.CharField(max_length=100)

    pic = models.CharField(max_length=100)
    previous_pic = models.CharField(max_length=100)
    pccurrentstatus = models.CharField(max_length=100,default="", editable=False)
    usbunlock = models.CharField(max_length=100,default="", null=True, blank=True)
    cdunlock = models.CharField(max_length=100,default="", null=True, blank=True)

   
    Brand = models.CharField(max_length=100)
    Model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    asset_no = models.CharField(max_length=100)
    vendor = models.CharField(max_length=100)
    pctype = models.CharField(max_length=100)
    processor_type = models.CharField(max_length=100)
    ram_type = models.CharField(max_length=100)
    ram_slot = models.CharField(max_length=100)
    total_ram = models.CharField(max_length=100)
    storage_type = models.CharField(max_length=100)
    storage_space = models.CharField(max_length=100)
    dop = models.CharField(max_length=100)
    dop_Warranty_end_date = models.CharField(max_length=100)
    po = models.CharField(max_length=100)
    invoice = models.CharField(max_length=100)
    block = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    standard_installation = models.CharField(max_length=100)
    microsoft_office = models.CharField(max_length=100)
    microsoft_office_keys = models.CharField(max_length=100)
    windows = models.CharField(max_length=100)
    type_of_purchase = models.CharField(max_length=100)

    lan_mac_address = models.CharField(max_length=100)
    lan_ip_address = models.CharField(max_length=100)
    wlan_mac_address = models.CharField(max_length=100)
    wlan_ip_address = models.CharField(max_length=100)
    joined_domain = models.CharField(max_length=100)
    connection_type = models.CharField(max_length=100)
    qrcode_image = models.ImageField(blank = True,null=True)

    def image_tag(self):
        return format_html('<img href="{0}" src="{0}" width="150" height="150" />'.format(self.qrcode_image.url))
    image_tag.allow_tags = True
    image_tag.short_description = 'QR Code Image'

    class Meta:
        db_table = 'Computer'
        # Add verbose name
        verbose_name = 'Computer'
     



  
# Laptop table
class Laptop(models.Model):
    computer_id = models.CharField(max_length=100)
    pic = models.CharField(max_length=100)
    previous_pic = models.CharField(max_length=100)
    current_computer_id = models.CharField(max_length=100)
    usbunlock = models.CharField(max_length=100,default="", null=True, blank=True)
    cdunlock = models.CharField(max_length=100,default="", null=True, blank=True)
    Brand = models.CharField(max_length=100)
    Model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    asset_no = models.CharField(max_length=100)
    vendor = models.CharField(max_length=100)
    processor_type = models.CharField(max_length=100)
    ram_type = models.CharField(max_length=100)
    ram_slot = models.CharField(max_length=100)
    total_ram = models.CharField(max_length=100)
    storage_type = models.CharField(max_length=100)
    storage_space = models.CharField(max_length=100)
    dop = models.CharField(max_length=100)
    dop_Warranty_end_date = models.CharField(max_length=100)
    po = models.CharField(max_length=100)
    invoice = models.CharField(max_length=100)
    block = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    standard_installation = models.CharField(max_length=100)
    microsoft_office = models.CharField(max_length=100)
    microsoft_office_keys = models.CharField(max_length=100)
    windows = models.CharField(max_length=100)
    type_of_purchase = models.CharField(max_length=100)
    lan_mac_address = models.CharField(max_length=100)
    lan_ip_address = models.CharField(max_length=100)
    wlan_mac_address = models.CharField(max_length=100)
    wlan_ip_address = models.CharField(max_length=100)
    joined_domain = models.CharField(max_length=100)
    connection_type = models.CharField(max_length=100)
    qrcode_image = models.ImageField(blank = True,null=True)
    pccurrentstatus = models.CharField(max_length=100,default="", editable=False)
    def image_tag(self):
        return format_html('<img href="{0}" src="{0}" width="150" height="150" />'.format(self.qrcode_image.url))
    image_tag.allow_tags = True
    image_tag.short_description = 'QR Code Image'
    class Meta:
        db_table = 'Laptop'
        # Add verbose name
        verbose_name = 'Laptop'

# NetworkHardware table
class NetworkHardware(models.Model):
    hardware_id = models.CharField(max_length=100)
    hardware_type = models.CharField(max_length=100)
    Brand = models.CharField(max_length=100)
    Current_Status = models.CharField(max_length=100)
    Model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    asset_no = models.CharField(max_length=100)
    dop = models.CharField(max_length=100)
    dop_Warranty_end_date = models.CharField(max_length=100)
    vendor = models.CharField(max_length=100)
   
    mac_address = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)
 
    block = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
  
    po = models.CharField(max_length=100)
    invoice = models.CharField(max_length=100)
    class Meta:
        db_table = 'Network Hardware'
        # Add verbose name
        verbose_name = 'Network Hardware'
    

# UserAsset table
class UserAsset(models.Model):
    employee_number = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    block = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    
    vpn = models.CharField(max_length=100)
    vpnaccount = models.CharField(max_length=100)
    class Meta:
        db_table = 'UserAsset'
        # Add verbose name
        verbose_name = 'User Asset'

# Loan table
class Loan(models.Model):
    loan_id = models.CharField(max_length=100)
    employee_number = models.CharField(max_length=100)
    asset_id = models.CharField(max_length=100)
    email = models.EmailField()
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    date_start = models.CharField(max_length=100)
    date_end = models.CharField(max_length=100)
   
    status = models.CharField(max_length=100)
    class Meta:
        db_table = 'Loan'
        # Add verbose name
        verbose_name = 'Loan'

# IP table   
class IP(models.Model):
    ip_address = models.GenericIPAddressField()
    ip_assisgned = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    remark = models.CharField(max_length=100, null=True, blank=True)
    class Meta:
        db_table = 'IP'
        # Add verbose name
        verbose_name = 'IP'

# softwareUser table   
class softwareUser(models.Model):
    Software_Type = models.CharField(max_length=100, null=True, blank=True)
    User_Type = models.CharField(max_length=100, null=True, blank=True)
    Software_Name = models.CharField(max_length=100, null=True, blank=True)
    User_ID = models.CharField(max_length=100, null=True, blank=True)
    Software_Version = models.CharField(max_length=100, null=True, blank=True)
    class Meta:
        db_table = 'software User'
        # Add verbose name
        verbose_name = 'software User'

# loghistory table   
class loghistory(models.Model):
    Time = models.CharField(max_length=100, null=True, blank=True)
    Username = models.CharField(max_length=100, null=True, blank=True)
    Activity = models.CharField(max_length=1000, null=True, blank=True)
    class Meta:
        db_table = 'loghistory'
        # Add verbose name
        verbose_name = 'Log History'

# class testdb(models.Model):
#     name_image = models.CharField(max_length=100, null=True, blank=True)
#     image_file = models.ImageField()
#     def image_tag(self):
#         return format_html('<img href="{0}" src="{0}" width="150" height="150" />'.format(self.image_file.url))
#     image_tag.allow_tags = True
#     image_tag.short_description = 'Image'