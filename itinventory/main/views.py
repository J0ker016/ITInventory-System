from genericpath import exists
from pathlib import Path
import os
from re import X
from typing import List
from unittest.mock import patch
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from numpy import array
from .models import *
from specification.models import *
from django.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import pandas as pd
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
import csv, io
from datetime import datetime
from datetime import *
import pyqrcode
import png
from pyqrcode import QRCode
import shutil
import base64
from PIL import Image
from .form import *
import glob
from fpdf import FPDF
from django.conf import settings
from fpdf import FPDF  # fpdf class
from django.http.response import HttpResponse
import mimetypes
from reportlab.pdfgen import canvas
from reportlab.lib.units import *

# homepage
def homepage(request):
    if request.session.get('name'):
        username =  format(request.session.get('name'))
    if (format(request.session.get('role')) == "staff"):
        style = format(request.session.get('styledivstaff'))
    else:
        style = format(request.session.get('styledivNotstaff'))


    context ={
        "Username": username, "Style" : style
    }
    # startupcreateQR()
    # create_qrcode()
    return render(request, 'pages-blank.html', context)

# Computer Page
def computerdetail(request):
    pctype = ModelPC.objects.all()
    processorType = Processor_type.objects.all()
    brand = Brand.objects.all()
    ram_type = Ram_type.objects.all()
    microsoft_office = Microsoft_office.objects.all()
    location = Location.objects.all()
    window = Windows.objects.all()
    displaydata = Computer.objects.all()
    storage_value = storagevalue.objects.all()
    tableend = Computer.objects.all().count()
    tablestart = 0
    Vendor = vendor.objects.all()
    tablerange = range(tablestart, tableend)
    runing_number = Asset_running_number.objects.filter(asset_type='PC').get()
   
 
    username =  format(request.session.get('name'))
    if (format(request.session.get('role')) == "staff"):
        style = format(request.session.get('styledivstaff'))
    else:
        style = format(request.session.get('styledivNotstaff'))
    context = {'pctype':pctype,
     'processorType':processorType,
      'brand':brand,
      'ram_type':ram_type,
      'processorType':processorType,
      'microsoft_office':microsoft_office,
      'location':location,
      'window':window,
      'Vendor':Vendor,
      'runing_number':runing_number,
      'tablerange':tablerange,
      
      'displaydata':displaydata,
      'storage_value': storage_value,  "Username": username,
        "Style" : style}

    return render(request, 'Computer Page.html', context)

def addcomputerform(request):
    if request.method == "POST":
       
        runing_number = Asset_running_number.objects.filter(asset_type='PC').get()
        data = Computer()
        data.pic = request.POST['pic']
        data.previous_pic = request.POST['Previous_PIC']
        data.computer_id = request.POST['Computer_ID']
        data.current_computer_id = request.POST['Current_Computer_ID']
        data.type_of_purchase = request.POST['type_of_purchase']
        data.Brand = request.POST['Brand']
        data.Model = request.POST['model']
        data.serial_number = request.POST['serial_number']
        data.asset_no = request.POST['asset_no']
        data.vendor = request.POST['vendor']
        data.pctype = request.POST['machineType']
        data.processor_type = request.POST['processor']
        data.ram_type = request.POST['ram_type']
        data.ram_slot = request.POST['ram_slot']
        data.total_ram = request.POST['total_RAM']
        data.storage_type = request.POST['storage_type']
        data.storage_space = request.POST['storageSpace']
        data.dop = request.POST['dop']
        data.dop_Warranty_end_date = request.POST['dopYear']
        data.po = request.POST['po']
        data.invoice = request.POST['invoice']
        data.block = request.POST['block']
        data.location = request.POST['location']
        data.standard_installation = request.POST['Standard_Installation']
        data.cdunlock = request.POST['cd_unlock']
        data.usbunlock = request.POST['usb_unlock']
        data.microsoft_office = request.POST['Microsoft_Office']
        data.microsoft_office_keys = request.POST['Licensed_key']
        standaad_installation = data.standard_installation
        data.windows = request.POST['Window_version']
        data.lan_mac_address = request.POST['lan_mac_address']
        data.lan_ip_address = request.POST['lan_ip_address']
        data.wlan_mac_address = request.POST['wlan_mac_address']

        data.wlan_ip_address = request.POST['wlan_ip_address']
        data.joined_domain = request.POST['Joined_Domain']
        data.connection_type = request.POST['ConnectionType']
        data.pccurrentstatus = request.POST['Computer_Status']
      
        if(request.POST['ConnectionType'] == "Offline"):
            if not Computer.objects.filter(computer_id=request.POST['Computer_ID']).exists():
                data.lan_ip_address = "offline"

                data.save()
                num = int(runing_number.running_number)+1
                updatenum = Asset_running_number.objects.get(asset_type='PC')
                updatenum.running_number = num
                updatenum.save()
                log_history = loghistory()
                log_history.Time = datetime.now()
                log_history.Username = format(request.session.get('name'))
                log_history.Activity = "Add A Computer By ID " + request.POST['Computer_ID']
                log_history.save() 
                if standaad_installation == "Yes" or standaad_installation == "yes":
                            trend_micro = softwareUser()
                            trend_micro.Software_Type = "Non-Concurrent"
                            trend_micro.User_Type = "Machine"
                            trend_micro.Software_Name = "Trend Micro"
                            trend_micro.Software_Version = "Apex one"
                            trend_micro.User_ID = data.computer_id
                            trend_micro.save()
                            teamviewer = softwareUser()
                            teamviewer.Software_Type = "Non-Concurrent"
                            teamviewer.User_Type = "Machine"
                            teamviewer.Software_Name = "Teamviewer"
                            teamviewer.Software_Version = "Teamviewer Host"
                            teamviewer.User_ID = data.computer_id
                            teamviewer.save()
                            vnc = softwareUser()
                            vnc.Software_Type = "Non-Concurrent"
                            vnc.User_Type = "Machine"
                            vnc.Software_Name = "TightVNC"
                            vnc.Software_Version = "tightvnc-2.8.63"
                            vnc.User_ID = data.computer_id
                            vnc.save()
                            marimba = softwareUser()
                            marimba.Software_Type = "Non-Concurrent"
                            marimba.User_Type = "Machine"
                            marimba.Software_Name = "Marimba"
                            marimba.Software_Version = "SFSInventory_x64"
                            marimba.User_ID = data.computer_id
                            marimba.save()
                arraydataQR = [ request.POST['Computer_ID'], request.POST['serial_number'], request.POST['Brand'], request.POST['model'] ]
                type_create = 'Create'
                create_qrcodePC(arraydataQR, type_create) 
                return HttpResponse('hai')
        else:
            if not Computer.objects.filter(computer_id=request.POST['Computer_ID']).exists():
                data.save()
                num = int(runing_number.running_number)+1
                updatenum = Asset_running_number.objects.get(asset_type='PC')
                updatenum.running_number = num
                updatenum.save()

                ip = IP.objects.get(ip_address=request.POST['lan_ip_address'])
                ip.status = "In-use"
                ip.ip_assisgned = data.computer_id
                ip.save()
                log_history = loghistory()
                log_history.Time = datetime.now()
                log_history.Username = format(request.session.get('name'))
                log_history.Activity = "Add A Computer By ID " + request.POST['Computer_ID']
                log_history.save()
                if standaad_installation == "Yes" or standaad_installation == "yes":
                            trend_micro = softwareUser()
                            trend_micro.Software_Type = "Non-Concurrent"
                            trend_micro.User_Type = "Machine"
                            trend_micro.Software_Name = "Trend Micro"
                            trend_micro.Software_Version = "Apex one"
                            trend_micro.User_ID = data.computer_id
                            trend_micro.save()
                            teamviewer = softwareUser()
                            teamviewer.Software_Type = "Non-Concurrent"
                            teamviewer.User_Type = "Machine"
                            teamviewer.Software_Name = "Teamviewer"
                            teamviewer.Software_Version = "Teamviewer Host"
                            teamviewer.User_ID = data.computer_id
                            teamviewer.save()
                            vnc = softwareUser()
                            vnc.Software_Type = "Non-Concurrent"
                            vnc.User_Type = "Machine"
                            vnc.Software_Name = "TightVNC"
                            vnc.Software_Version = "tightvnc-2.8.63"
                            vnc.User_ID = data.computer_id
                            vnc.save()
                            marimba = softwareUser()
                            marimba.Software_Type = "Non-Concurrent"
                            marimba.User_Type = "Machine"
                            marimba.Software_Name = "Marimba"
                            marimba.Software_Version = "SFSInventory_x64"
                            marimba.User_ID = data.computer_id
                            marimba.save()
                
                arraydataQR = [ request.POST['Computer_ID'], request.POST['serial_number'], request.POST['Brand'], request.POST['model'] ]
                type_create = 'Create'
                create_qrcodePC(arraydataQR, type_create) 


                return HttpResponse('hai')

def rundatatoform(request):
    if request.method == "POST":
       id = request.POST["type"]
       computerdata = Asset_running_number.objects.filter(asset_type = id).get()
       ip = IP.objects.filter(status = 'Not-inuse' )
       data = { 'runnumber' : computerdata.running_number, 'ip' : list(ip.values()) }
       return JsonResponse(data)

def updateformpc(request):
        if request.method == "POST":
            data = Computer.objects.filter(computer_id= request.POST['Computer_ID']).get()
            data.pic = request.POST['pic']
            data.type_of_purchase = request.POST['type_of_purchase']
            data.previous_pic = request.POST['Previous_PIC']
            data.computer_id = request.POST['Computer_ID']
            data.current_computer_id = request.POST['Current_Computer_ID']
            data.Brand = request.POST['Brand']
            data.Model = request.POST['model']
            data.serial_number = request.POST['serial_number']
            data.asset_no = request.POST['asset_no']
            data.vendor = request.POST['vendor']
            data.pctype = request.POST['machineType']
            data.processor_type = request.POST['processor']
            data.ram_type = request.POST['ram_type']
            data.ram_slot = request.POST['ram_slot']
            data.total_ram = request.POST['total_RAM']
            data.storage_type = request.POST['storage_type']
            data.storage_space = request.POST['storageSpace']
            data.dop = request.POST['dop']
            data.dop_Warranty_end_date = request.POST['dopYear']
            data.po = request.POST['po']
            data.invoice = request.POST['invoice']
            data.block = request.POST['block']
            data.location = request.POST['location']
            data.standard_installation = request.POST['Standard_Installation']
            standaad_installation = request.POST['Standard_Installation']
            data.microsoft_office = request.POST['Microsoft_Office']
            data.microsoft_office_keys = request.POST['Licensed_key']
            data.cdunlock = request.POST['cd_unlock']
            data.usbunlock = request.POST['usb_unlock']
            data.windows = request.POST['Window_version']
            data.lan_mac_address = request.POST['lan_mac_address']
            data.connection_type = request.POST['ConnectionType']
            datainternetCon = request.POST['ConnectionType']
            if standaad_installation == "Yes" or standaad_installation == "yes":
                            trend_micro = softwareUser()
                            trend_micro.Software_Type = "Non-Concurrent"
                            trend_micro.User_Type = "Machine"
                            trend_micro.Software_Name = "Trend Micro"
                            trend_micro.Software_Version = "Apex one"
                            trend_micro.User_ID = data.computer_id
                            trend_micro.save()
                            teamviewer = softwareUser()
                            teamviewer.Software_Type = "Non-Concurrent"
                            teamviewer.User_Type = "Machine"
                            teamviewer.Software_Name = "Teamviewer"
                            teamviewer.Software_Version = "Teamviewer Host"
                            teamviewer.User_ID = data.computer_id
                            teamviewer.save()
                            vnc = softwareUser()
                            vnc.Software_Type = "Non-Concurrent"
                            vnc.User_Type = "Machine"
                            vnc.Software_Name = "TightVNC"
                            vnc.Software_Version = "tightvnc-2.8.63"
                            vnc.User_ID = data.computer_id
                            vnc.save()
                            marimba = softwareUser()
                            marimba.Software_Type = "Non-Concurrent"
                            marimba.User_Type = "Machine"
                            marimba.Software_Name = "Marimba"
                            marimba.Software_Version = "SFSInventory_x64"
                            marimba.User_ID = data.computer_id
                            marimba.save()
            if (datainternetCon == "Intranet"):

                if(request.POST['lan_ip_address'] == "Offline"):
                    Previous_IP = data.lan_ip_address
                    if  IP.objects.filter(ip_address=Previous_IP).exists():
                        ip = IP.objects.get(ip_address=Previous_IP)
                        ip.status = "Not-inuse"
                        ip.ip_assisgned = "None"
                        ip.save()
                        data.lan_ip_address = "Offline"
                    else:
                        data.lan_ip_address = "Offline"



                    
                elif((data.lan_ip_address == "Offline") ):
                    
                    ip = IP.objects.get(ip_address=request.POST['lan_ip_address'])
                    ip.status = "In-use"
                    ip.ip_assisgned = data.computer_id
                    ip.save()
                    data.lan_ip_address = request.POST['lan_ip_address']
                  

                elif(request.POST['lan_ip_address'] == "Release"):
                    Previous_IP = data.lan_ip_address
                    ip = IP.objects.get(ip_address=Previous_IP)
                    ip.status = "Not-inuse"
                    ip.ip_assisgned = "None"
                    ip.save()
                    data.lan_ip_address = request.POST['lan_ip_address']
                 

                elif( (data.lan_ip_address == "Release") and (data.pccurrentstatus !="Pending Dispose") and (data.pccurrentstatus !="Dispose") ):
                
                    data.lan_ip_address = request.POST['lan_ip_address']
                    ip = IP.objects.get(ip_address=request.POST['lan_ip_address'])
                    ip.status = "In-use"
                    ip.ip_assisgned = data.computer_id
                    ip.save()
         

            
                
                elif( data.lan_ip_address != request.POST['lan_ip_address']):
                    Previous_IP = data.lan_ip_address
                    if Previous_IP == "Release" or  Previous_IP == "None":
                        data.lan_ip_address = request.POST['lan_ip_address']
                        ip = IP.objects.get(ip_address=request.POST['lan_ip_address'])
                        ip.status = "In-use"
                        ip.ip_assisgned = data.computer_id
                        ip.save()
                        data.lan_ip_address = request.POST['lan_ip_address']
                    else:

                       

                        
                        data.lan_ip_address = request.POST['lan_ip_address']
                        ip = IP.objects.get(ip_address=request.POST['lan_ip_address'])
                        ip.status = "In-use"
                        ip.ip_assisgned = data.computer_id

                        ip.save()
                        Change_IP_status = IP.objects.get(ip_address= Previous_IP)
                        Change_IP_status.status = "Not-inuse"
                        Change_IP_status.ip_assisgned = "None"

                        Change_IP_status.save()
                        data.lan_ip_address = request.POST['lan_ip_address']
                   
                else :
                    data.lan_ip_address = request.POST['lan_ip_address']

                data.wlan_mac_address = request.POST['wlan_mac_address']

                data.wlan_ip_address = request.POST['wlan_ip_address']
                data.joined_domain = request.POST['Joined_Domain']
                data.pccurrentstatus = request.POST['Computer_Status']
               
            
                data.save()
                log_history = loghistory()
                log_history.Time = datetime.now()
                log_history.Username = format(request.session.get('name'))
                log_history.Activity = "Update A Computer By ID " + request.POST['Computer_ID']
                log_history.save()   
                arraydataQR = [ request.POST['Computer_ID'], request.POST['serial_number'], request.POST['Brand'], request.POST['model'] ]
                type_create = 'Update'
                create_qrcodePC(arraydataQR, type_create) 
                


                return HttpResponse('hai')   

            elif (datainternetCon == "Internet"):
                if(request.POST['lan_ip_address'] == "Offline"):
                    Previous_IP = data.lan_ip_address
                    if  IP.objects.filter(ip_address=Previous_IP).exists():
                        ip = IP.objects.get(ip_address=Previous_IP)
                        ip.status = "Not-inuse"
                        ip.ip_assisgned = "None"
                        ip.save()
                        data.lan_ip_address = "Offline"
                    else:
                        data.lan_ip_address = "Offline"



                    
                elif((data.lan_ip_address == "Offline") ):
                    
                    ip = IP.objects.get(ip_address=request.POST['lan_ip_address'])
                    ip.status = "In-use"
                    ip.ip_assisgned = data.computer_id
                    ip.save()
                    data.lan_ip_address = request.POST['lan_ip_address']
                    

                elif(request.POST['lan_ip_address'] == "Release"):
                    Previous_IP = data.lan_ip_address
                    ip = IP.objects.get(ip_address=Previous_IP)
                    ip.status = "Not-inuse"
                    ip.ip_assisgned = "None"
                    ip.save()
                    data.lan_ip_address = request.POST['lan_ip_address']
               

                elif( (data.lan_ip_address == "Release") and (data.pccurrentstatus !="Pending Dispose") and (data.pccurrentstatus !="Dispose") ):
                
                    data.lan_ip_address = request.POST['lan_ip_address']
                    ip = IP.objects.get(ip_address=request.POST['lan_ip_address'])
                    ip.status = "In-use"
                    ip.ip_assisgned = data.computer_id
                    ip.save()
                 

            
                
                elif( data.lan_ip_address != request.POST['lan_ip_address']):
                    Previous_IP = data.lan_ip_address
                    if (Previous_IP == "Offline" or Previous_IP == "None" ):
                      
                        data.lan_ip_address = request.POST['lan_ip_address']
                        ip = IP.objects.get(ip_address=request.POST['lan_ip_address'])
                        ip.status = "In-use"
                        ip.ip_assisgned = data.computer_id
                    else:
                    
                        data.lan_ip_address = request.POST['lan_ip_address']
                        ip = IP.objects.get(ip_address=request.POST['lan_ip_address'])
                        ip.status = "In-use"
                        ip.ip_assisgned = data.computer_id

                        ip.save()
                        Change_IP_status = IP.objects.get(ip_address= Previous_IP)
                        Change_IP_status.status = "Not-inuse"
                        Change_IP_status.ip_assisgned = "None"

                        Change_IP_status.save()
                     
                else :
                    data.lan_ip_address = request.POST['lan_ip_address']

                data.wlan_mac_address = request.POST['wlan_mac_address']

                data.wlan_ip_address = request.POST['wlan_ip_address']
                data.joined_domain = request.POST['Joined_Domain']
                data.pccurrentstatus = request.POST['Computer_Status']
              
            
                data.save()
                log_history = loghistory()
                log_history.Time = datetime.now()
                log_history.Username = format(request.session.get('name'))
                log_history.Activity = "Update A Computer By ID " + request.POST['Computer_ID']
                log_history.save()
                arraydataQR = [ request.POST['Computer_ID'], request.POST['serial_number'], request.POST['Brand'], request.POST['model'] ]
                type_create = 'Update'
                create_qrcodePC(arraydataQR, type_create) 



                return HttpResponse('hai')   

            else:
                if(request.POST['lan_ip_address'] == "Offline"):
                    Previous_IP = data.lan_ip_address
                    if  IP.objects.filter(ip_address=Previous_IP).exists():
                        ip = IP.objects.get(ip_address=Previous_IP)
                        ip.status = "Not-inuse"
                        ip.ip_assisgned = "None"
                        ip.save()
                        data.lan_ip_address = "Offline"
                    else:
                        data.lan_ip_address = "Offline"
                data.wlan_mac_address = request.POST['wlan_mac_address']

                data.wlan_ip_address = request.POST['wlan_ip_address']
                data.joined_domain = request.POST['Joined_Domain']
                data.pccurrentstatus = request.POST['Computer_Status']
               
            
                data.save()
                log_history = loghistory()
                log_history.Time = datetime.now()
                log_history.Username = format(request.session.get('name'))
                log_history.Activity = "Update A Computer By ID " + request.POST['Computer_ID']
                log_history.save() 
                arraydataQR = [ request.POST['Computer_ID'], request.POST['serial_number'], request.POST['Brand'], request.POST['model'] ]
                type_create = 'Update'
                create_qrcodePC(arraydataQR, type_create) 



                return HttpResponse('hai')   

def getdataupdate(request):
    if request.method == "POST":
       id = request.POST["id"]
       computerdata = Computer.objects.filter(computer_id = id).get()
       ip = IP.objects.filter(status = 'Not-inuse' )
       data = {
           "pic": computerdata.pic, "previous_pic": computerdata.previous_pic, "computer_id": computerdata.computer_id,
            "current_computer_id": computerdata.current_computer_id, "Brand": computerdata.Brand, "Model": computerdata.Model,
             "serial_number": computerdata.serial_number, "asset_no": computerdata.asset_no, "vendor": computerdata.vendor,
              "pctype": computerdata.pctype, "processor_type": computerdata.processor_type, "ram_type": computerdata.ram_type,
               "ram_slot": computerdata.ram_slot, "total_ram": computerdata.total_ram, "storage_type": computerdata.storage_type,
                "storage_space": computerdata.storage_space, "dop": computerdata.dop, "dop_Warranty_end_date": computerdata.dop_Warranty_end_date,
                 "po": computerdata.po, "invoice": computerdata.invoice, "block": computerdata.block,
                  "location": computerdata.location, "standard_installation": computerdata.standard_installation, "microsoft_office": computerdata.microsoft_office,
                   "microsoft_office_keys": computerdata.microsoft_office_keys, "windows": computerdata.windows, "lan_mac_address": computerdata.lan_mac_address,
                    "lan_ip_address": computerdata.lan_ip_address, "wlan_mac_address": computerdata.wlan_mac_address, "wlan_ip_address": computerdata.wlan_ip_address,
                    "joined_domain": computerdata.joined_domain, "connection_type": computerdata.connection_type, "pccurrentstatus": computerdata.pccurrentstatus, 'ip' : list(ip.values()), 'type_of_purchase': computerdata.type_of_purchase,
                    'usbunlock': computerdata.usbunlock, 'cdunlock': computerdata.cdunlock
                    
                  

                     }
        
       return JsonResponse(data)

def getcomputerdata(request):
    
    computerdata = Computer.objects.all()
   

    # imagelocation = 
    return JsonResponse({"data":list(computerdata.values())})

def getcustomPCdata(request):
    if request.method == "POST":
        data1 = int(request.POST["data1"])
        data2 = int(request.POST["data2"])
       
        arraydata = []
        while data1 <= data2:
            if data1 <= 480:

                if data1 < 10:
                    data = "UTM-PC00"+ str(data1)
                elif ((data1 >= 10) and (data1 < 100)):
                    data= "UTM-PC0"+ str(data1)
                elif ((data1 >= 100) and (data1 < 1000)):
                    data= "UTM-PC"+ str(data1)
                elif ((data1 >= 1000) and (data1 < 10000)):
                    data= "UTM-PC"+ str(data1)
                data1 = data1 + 1
                arraydata.append(data)
            else:
                if data1 < 10:
                    data = "UTM-PC000"+ str(data1)
                elif ((data1 >= 10) and (data1 < 100)):
                    data= "UTM-PC00"+ str(data1)
                elif ((data1 >= 100) and (data1 < 1000)):
                    data= "UTM-PC0"+ str(data1)
                elif ((data1 >= 1000) and (data1 < 10000)):
                    data= "UTM-PC"+ str(data1)
                data1 = data1 + 1
                arraydata.append(data)

       


        
        computerdata = Computer.objects.filter(computer_id__in=arraydata)
        return JsonResponse({"data":list(computerdata.values())})

def exportdatapc(request):
   
     
        if request.POST["type"] == 'all':

            computerdata = Computer.objects.all()
            data = []
            for key in computerdata:
                arraydata = [key.computer_id, key.current_computer_id, key.pctype,key.pic,key.previous_pic,
                 key.Brand, key.Model, key.serial_number,key.asset_no, key.dop, key.dop_Warranty_end_date,
                 key.vendor, key.po, key.invoice, key.type_of_purchase, key.block, key.location,
                key.standard_installation, key.usbunlock, key.cdunlock, key.windows, key.microsoft_office, key.microsoft_office_keys,
                  key.processor_type, key.ram_type, key.ram_slot, key.total_ram, key.storage_type,
                   key.storage_space, key.connection_type, key.joined_domain, key.lan_mac_address,
                 key.lan_ip_address, key.wlan_mac_address, key.wlan_ip_address, key.pccurrentstatus]
                data.append(arraydata)
        
            
            return JsonResponse({"data":data})
        if request.POST["type"] == 'custom':
            data1 = int(request.POST["datafinal1"])
            data2 = int(request.POST["datafinal2"])
        
            arraydata = []
            while data1 <= data2:
                if data1 <= 480:

                    if data1 < 10:
                        data = "UTM-PC00"+ str(data1)
                    elif ((data1 >= 10) and (data1 < 100)):
                        data= "UTM-PC0"+ str(data1)
                    elif ((data1 >= 100) and (data1 < 1000)):
                        data= "UTM-PC"+ str(data1)
                    elif ((data1 >= 1000) and (data1 < 10000)):
                        data= "UTM-PC"+ str(data1)
                    data1 = data1 + 1
                    arraydata.append(data)
                else:
                    if data1 < 10:
                        data = "UTM-PC000"+ str(data1)
                    elif ((data1 >= 10) and (data1 < 100)):
                        data= "UTM-PC00"+ str(data1)
                    elif ((data1 >= 100) and (data1 < 1000)):
                        data= "UTM-PC0"+ str(data1)
                    elif ((data1 >= 1000) and (data1 < 10000)):
                        data= "UTM-PC"+ str(data1)
                    data1 = data1 + 1
                    arraydata.append(data)
            computerdata = Computer.objects.filter(computer_id__in=arraydata)
            data = []
            for key in computerdata:
                arraydata = [key.computer_id, key.current_computer_id, key.pctype,key.pic,key.previous_pic, key.Brand, key.Model, key.serial_number,
                key.asset_no, key.dop, key.dop_Warranty_end_date, key.vendor, key.po, key.invoice, key.type_of_purchase, key.block, key.location,
                key.standard_installation,  key.usbunlock, key.cdunlock, key.windows, key.microsoft_office, key.microsoft_office_keys, key.processor_type, key.ram_type, key.ram_slot, key.total_ram, key.storage_type
                , key.storage_space, key.connection_type, key.joined_domain, key.lan_mac_address, key.lan_ip_address, key.wlan_mac_address, key.wlan_ip_address, key.pccurrentstatus]
                data.append(arraydata)
        
            
            return JsonResponse({"data":data})


def GetQRPCData(request):
    if request.method == "POST":
        if request.POST["type"] == "All":
            computerdata = Computer.objects.all()
            return JsonResponse({"data":list(computerdata.values())})

        elif request.POST["type"] == "Custom":
            data1 = int(request.POST["data1"])
            data2 = int(request.POST["data2"])
        
            arraydata = []
            while data1 <= data2:
                if data1 <= 480:

                    if data1 < 10:
                        data = "UTM-PC00"+ str(data1)
                    elif ((data1 >= 10) and (data1 < 100)):
                        data= "UTM-PC0"+ str(data1)
                    elif ((data1 >= 100) and (data1 < 1000)):
                        data= "UTM-PC"+ str(data1)
                    elif ((data1 >= 1000) and (data1 < 10000)):
                        data= "UTM-PC"+ str(data1)
                    data1 = data1 + 1
                    arraydata.append(data)
                else:
                    if data1 < 10:
                        data = "UTM-PC000"+ str(data1)
                    elif ((data1 >= 10) and (data1 < 100)):
                        data= "UTM-PC00"+ str(data1)
                    elif ((data1 >= 100) and (data1 < 1000)):
                        data= "UTM-PC0"+ str(data1)
                    elif ((data1 >= 1000) and (data1 < 10000)):
                        data= "UTM-PC"+ str(data1)
                    data1 = data1 + 1
                    arraydata.append(data)

          


            
            computerdata = Computer.objects.filter(computer_id__in=arraydata)
            return JsonResponse({"data":list(computerdata.values())})

def searchPCdata(request):
    data = request.POST['data']
    if Computer.objects.filter(computer_id__icontains=data).exists():
        data1 = Computer.objects.filter(computer_id__icontains=data)
        return JsonResponse({"data":list(data1.values())})
    elif Computer.objects.filter(lan_ip_address__icontains=data).exists():
        data1 = Computer.objects.filter(lan_ip_address__icontains=data)
    elif Computer.objects.filter(current_computer_id__icontains=data).exists():
        data1 = Computer.objects.filter(current_computer_id__icontains=data)
        return JsonResponse({"data":list(data1.values())})
    else:
       return HttpResponse('')
      
  
#mass upload page
def uploadcsvdata(request):
    if request.method == "POST":
        if request.POST['typeofupload'] == 'Add':
                if request.POST['Main_database'] == 'Computer':
                    csv_file = request.FILES["csv_file"]
                    df = pd.read_csv(csv_file)
                    data1 = df.values.tolist()
                    for k in data1:
                        FinData = k 
                        length = len(FinData)
                        if  Computer.objects.filter(computer_id=FinData[0]).exists():
                            
                                errordata = "Yes"
                             
                                context ={
                                    "error" : errordata,

                                }
                                return render(request, "Mass upload page.html", context)

                    for keys in data1:
                        x=2
                        FinData = keys 
                        length = len(FinData)
                    
                        #proceed to insert the data
                        data = Computer()
                        if FinData[0] == "None":
                            runing_number = Asset_running_number.objects.filter(asset_type='PC').get()
                            num = int(runing_number.running_number)
                            if num < 10:
                                data_cid = "UTM-PC000"+ str(num)
                            elif ((num >= 10) and (num < 100)):
                                data_cid= "UTM-PC00"+ str(num)
                            elif ((num >= 100) and (num < 1000)):
                                data_cid= "UTM-PC0"+ str(num)
                            elif ((num >= 1000) and (num < 10000)):
                                data_cid= "UTM-PC"+ str(num)
                            data.computer_id = data_cid
                            runing_number.running_number = num +1
                            runing_number.save()
                        else:
                            data.computer_id = FinData[0]
                        
                        if FinData[1] == "None":
                            
                            data.current_computer_id =  data.computer_id
                         
                        else:
                            data.current_computer_id = FinData[1]
                        
                        data.pctype = FinData[2]
                        data.pic = FinData[3]
                        data.previous_pic = FinData[4]
                        data.Brand = FinData[5]
                        data.Model = FinData[6]
                        data.serial_number = FinData[7]
                        data.asset_no = FinData[8]
                        if FinData[9] == "None" or FinData[9] ==  "-":
                            data.dop = FinData[9]
                        else:
                            date_time_obj = datetime.strptime(FinData[9], '%d/%m/%Y')
                            change_date_format = date_time_obj.strftime('%d/%m/%Y')
                            data.dop = change_date_format
                              
                        if FinData[10] == "None" or FinData[10] ==  "-":
                            data.dop_Warranty_end_date = FinData[10]
                        else:
                            date_time_obj = datetime.strptime(FinData[10], '%d/%m/%Y')
                            change_date_format = date_time_obj.strftime('%d/%m/%Y')
                            data.dop_Warranty_end_date = change_date_format

                        data.vendor = FinData[11]
                        data.po = FinData[12]
                        data.invoice = FinData[13]
                        data.type_of_purchase = FinData[14]

                        data.block = FinData[15]
                        data.location = FinData[16]
                        data.standard_installation = FinData[17]
                        if FinData[17] == "Yes" or FinData[17] == "yes":
                            if not softwareUser.objects.filter(User_ID=FinData[0], Software_Name="Trend Micro" ).exists():
                                trend_micro = softwareUser()
                                trend_micro.Software_Type = "Non-Concurrent"
                                trend_micro.User_Type = "Machine"
                                trend_micro.Software_Name = "Trend Micro"
                                trend_micro.Software_Version = "Apex one"
                                trend_micro.User_ID = data.computer_id
                                trend_micro.save()
                            if not softwareUser.objects.filter(User_ID=FinData[0], Software_Name="Teamviewer" ).exists():
                                teamviewer = softwareUser()
                                teamviewer.Software_Type = "Non-Concurrent"
                                teamviewer.User_Type = "Machine"
                                teamviewer.Software_Name = "Teamviewer"
                                teamviewer.Software_Version = "Teamviewer Host"
                                teamviewer.User_ID = data.computer_id
                                teamviewer.save()
                            if not softwareUser.objects.filter(User_ID=FinData[0], Software_Name="TightVNC" ).exists():
                                vnc = softwareUser()
                                vnc.Software_Type = "Non-Concurrent"
                                vnc.User_Type = "Machine"
                                vnc.Software_Name = "TightVNC"
                                vnc.Software_Version = "tightvnc-2.8.63"
                                vnc.User_ID = data.computer_id
                                vnc.save()
                            if not softwareUser.objects.filter(User_ID=FinData[0], Software_Name="Marimba" ).exists():
                                marimba = softwareUser()
                                marimba.Software_Type = "Non-Concurrent"
                                marimba.User_Type = "Machine"
                                marimba.Software_Name = "Marimba"
                                marimba.Software_Version = "SFSInventory_x64"
                                marimba.User_ID = data.computer_id
                                marimba.save()
                        data.usbunlock = FinData[18]
                        data.cdunlock = FinData[19]
                        data.windows = FinData[20]
                        data.microsoft_office = FinData[21]
                        data.microsoft_office_keys = FinData[22]
                        data.processor_type = FinData[23]
                        data.ram_type = FinData[24]
                        data.ram_slot = FinData[25]
                        data.total_ram = FinData[26]
                        data.storage_type = FinData[27]
                        data.storage_space = FinData[28]
                        data.connection_type = FinData[29]
                        data.joined_domain = FinData[30]
                        data.lan_mac_address = FinData[31]
                        if FinData[32] != "None":
                            if  IP.objects.filter(ip_address=FinData[32], status = "Not-inuse").exists():
                                ip = IP.objects.get(ip_address=FinData[32])
                                ipdata= ip.ip_address
                                data.lan_ip_address = ipdata
                                ip.status = "In-use"
                                ip.ip_assisgned = data.computer_id
                                ip.save()
                            else:
                                errordata = "Yes"
                                typeerror = 'IP'
                                row = x
                                iperror = FinData[30]
                                ip = IP.objects.get(ip_address=FinData[32])
                                computer_assignto =ip.ip_assisgned
                          
                                context ={
                                    "error" : errordata,
                                    "typeerror" : typeerror,
                                    "row" : row,
                                    "iperror" : iperror,
                                    "Computer_assign": computer_assignto



                                }
                                return render(request, "Mass upload page.html", context)
                        else:
                            data.lan_ip_address = FinData[32]
                        data.wlan_mac_address = FinData[33]
                        if FinData[34] != "None":
                            if  IP.objects.filter(ip_address=FinData[34], status = "Not-inuse").exists():
                                ip = IP.objects.get(ip_address=FinData[34])
                                ipdata= ip.ip_address
                                data.wlan_ip_address = ipdata
                                ip.status = "In-use"
                                ip.ip_assisgned = data.computer_id
                                ip.save()
                            else:
                                errordata = "Yes"
                                typeerror = 'IP'
                                row = x
                                iperror = FinData[34]
                                
                                ip = IP.objects.get(ip_address=FinData[34])
                                computer_assignto =ip.ip_assisgned
                             
                                context ={
                                    "error" : errordata,
                                    "typeerror" : typeerror,
                                    "row" : row,
                                    "iperror" : iperror,
                                    "Computer_assign": computer_assignto



                                }
                                return render(request, "Mass upload page.html", context)
                        else:
                            data.wlan_ip_address = FinData[34]
                        data.pccurrentstatus = FinData[35]


                       
                        if not Computer.objects.filter(computer_id=data.computer_id).exists():
                            data.save()
                      
                            x=x+1
    
                            dataarray = [data.computer_id, FinData[7], FinData[5], FinData[6]]
                            type_create = 'Create'
                            create_qrcodePC(dataarray, type_create)

                        else:
                          
                            errordata = "Yes"
                            x=x+1

                            

                
                    
                    return redirect('uploadcsvdata')

                if request.POST['Main_database'] == 'Laptop':
                    csv_file = request.FILES["csv_file"]
                 
                    df = pd.read_csv(csv_file, encoding='unicode_escape')
                    data1 = df.values.tolist()
                    for k in data1:
                        FinData = k 
                        length = len(FinData)
                        if  Laptop.objects.filter(computer_id=FinData[0]).exists():
                                
                                errordata = "Yes"
                            
                                context ={
                                    "error" : errordata,

                                }
                                return render(request, "Mass upload page.html", context)

                    for keys in data1:
                        x =1
                        FinData = keys 
                        length = len(FinData)
                 
                        #proceed to insert the data
                        data = Laptop()
                        if FinData[0] == "None" or FinData[0] == "None":
                            runing_number = Asset_running_number.objects.filter(asset_type='Laptop').get()
                            num = int(runing_number.running_number)
                            if num < 10:
                                data_cid = "UTM-NB000"+ str(num)
                            elif ((num >= 10) and (num < 100)):
                                data_cid= "UTM-NB00"+ str(num)
                            elif ((num >= 100) and (num < 1000)):
                                data_cid= "UTM-NB0"+ str(num)
                            elif ((num >= 1000) and (num < 10000)):
                                data_cid= "UTM-NB"+ str(num)
                            data.computer_id = data_cid
                            runing_number.running_number = num +1
                            runing_number.save()
                        else:
                            data.computer_id = FinData[0]
                        
                        if FinData[1] == "None":
                            
                            data.current_computer_id =  data.computer_id
                         
                        else:
                            data.current_computer_id = FinData[1]
                        data.pic = FinData[2]
                        data.previous_pic = FinData[3]
                        data.Brand = FinData[4]
                        data.Model = FinData[5]
                        data.serial_number = FinData[6]
                        data.asset_no = FinData[7]
                        if FinData[8] == "None" or FinData[8] ==  "-":
                            data.dop = FinData[8]
                        else:
                            date_time_obj = datetime.strptime(FinData[8], '%d/%m/%Y')
                            change_date_format = date_time_obj.strftime('%d/%m/%Y')
                            data.dop = change_date_format
                              
                        if FinData[9] == "None" or FinData[9] ==  "-":
                            data.dop_Warranty_end_date = FinData[9]
                           
                        else:
                            date_time_obj = datetime.strptime(FinData[9], '%d/%m/%Y')
                            change_date_format = date_time_obj.strftime('%d/%m/%Y')
                            data.dop_Warranty_end_date = change_date_format
                            
                       
                        
                        data.vendor = FinData[10]
                        data.po = FinData[11]
                        data.invoice = FinData[12]
                        data.type_of_purchase = FinData[13]

                        data.block = FinData[14]
                        data.location = FinData[15]
                        data.standard_installation = FinData[16]
                        if FinData[16] == "Yes" or FinData[16] == "yes":
                            if not softwareUser.objects.filter(User_ID=FinData[0], Software_Name="Trend Micro" ).exists():
                                trend_micro = softwareUser()
                                trend_micro.Software_Type = "Non-Concurrent"
                                trend_micro.User_Type = "Machine"
                                trend_micro.Software_Name = "Trend Micro"
                                trend_micro.Software_Version = "Apex one"
                                trend_micro.User_ID = data.computer_id
                                trend_micro.save()
                            if not softwareUser.objects.filter(User_ID=FinData[0], Software_Name="Teamviewer" ).exists():
                                teamviewer = softwareUser()
                                teamviewer.Software_Type = "Non-Concurrent"
                                teamviewer.User_Type = "Machine"
                                teamviewer.Software_Name = "Teamviewer"
                                teamviewer.Software_Version = "Teamviewer Host"
                                teamviewer.User_ID = data.computer_id
                                teamviewer.save()
                            if not softwareUser.objects.filter(User_ID=FinData[0], Software_Name="TightVNC" ).exists():
                                vnc = softwareUser()
                                vnc.Software_Type = "Non-Concurrent"
                                vnc.User_Type = "Machine"
                                vnc.Software_Name = "TightVNC"
                                vnc.Software_Version = "tightvnc-2.8.63"
                                vnc.User_ID = data.computer_id
                                vnc.save()
                            if not softwareUser.objects.filter(User_ID=FinData[0], Software_Name="Marimba" ).exists():
                                marimba = softwareUser()
                                marimba.Software_Type = "Non-Concurrent"
                                marimba.User_Type = "Machine"
                                marimba.Software_Name = "Marimba"
                                marimba.Software_Version = "SFSInventory_x64"
                                marimba.User_ID = data.computer_id
                                marimba.save()
                        data.usbunlock = FinData[17]
                        data.cdunlock = FinData[18]
                        data.windows = FinData[19]
                        data.microsoft_office = FinData[20]
                        data.microsoft_office_keys = FinData[21]
                        data.processor_type = FinData[22]
                        data.ram_type = FinData[23]
                        data.ram_slot = FinData[24]
                        data.total_ram = FinData[25]
                        data.storage_type = FinData[26]
                        data.storage_space = FinData[27]
                        data.connection_type = FinData[28]
                        data.joined_domain = FinData[29]
                        data.lan_mac_address = FinData[30]
                        if FinData[31] != "None":
                            if FinData[31] == "Offline" or FinData[31] == "offline" :
                                data.lan_ip_address = FinData[31]

                            elif  IP.objects.filter(ip_address=FinData[31], status = "Not-inuse").exists():
                                ip = IP.objects.get(ip_address=FinData[31])
                                ipdata= ip.ip_address
                                data.lan_ip_address = ipdata
                                ip.status = "In-use"
                                ip.ip_assisgned = data.computer_id
                                ip.save()
                            else:
                                errordata = "Yes"
                                typeerror = 'IP'
                                row = x
                                iperror = FinData[31]
                                ip = IP.objects.get(ip_address=FinData[31])
                                computer_assignto =ip.ip_assisgned
                            
                                context ={
                                    "error" : errordata,
                                    "typeerror" : typeerror,
                                    "row" : row,
                                    "iperror" : iperror,
                                    "Computer_assign": computer_assignto



                                }
                                return render(request, "Mass upload page.html", context)
                        else:
                            data.lan_ip_address = FinData[31]
                        data.wlan_mac_address = FinData[32]
                        if FinData[33] != "None":
                            if FinData[33] == "Offline" or FinData[33] == "offline" :
                                data.wlan_ip_address = FinData[33]
                            elif  IP.objects.filter(ip_address=FinData[33], status = "Not-inuse").exists():
                                ip = IP.objects.get(ip_address=FinData[33])
                                ipdata= ip.ip_address
                                data.wlan_ip_address = ipdata
                                ip.status = "In-use"
                                ip.ip_assisgned = data.computer_id
                                ip.save()
                            
                            else:
                                errordata = "Yes"
                                typeerror = 'IP'
                                row = x
                                iperror = FinData[33]
                                
                                ip = IP.objects.get(ip_address=FinData[33])
                                computer_assignto =ip.ip_assisgned
                              
                                context ={
                                    "error" : errordata,
                                    "typeerror" : typeerror,
                                    "row" : row,
                                    "iperror" : iperror,
                                    "Computer_assign": computer_assignto



                                }
                                return render(request, "Mass upload page.html", context)
                        else:
                            data.wlan_ip_address = FinData[33]
                        data.pccurrentstatus = FinData[34]
                        if not Laptop.objects.filter(computer_id=data.computer_id).exists():
                            data.save()
                          
                            x = x+1
                            dataarray = [data.computer_id, FinData[6], FinData[4], FinData[5]]
                            type_create = "Create"
                            create_qrcodeLaptop(dataarray, type_create)
                        else:
                           
                            errordata = "Yes"
                            x = x+1

                            

                
                    
                    return redirect('uploadcsvdata')
                        
                
                    
                    return HttpResponse(context)
                if request.POST['Main_database'] == 'NetworkHardware':
                    csv_file = request.FILES["csv_file"]
                    df = pd.read_csv(csv_file)
                    data1 = df.values.tolist()
                    for k in data1:
                        FinData = k 
                        length = len(FinData)
                        if  NetworkHardware.objects.filter(hardware_id=FinData[0]).exists():
                                
                                errordata = "Yes"
                               
                                context ={
                                    "error" : errordata,

                                }
                                return render(request, "Mass upload page.html", context)
                    x =1 
                    for keys in data1:
                        FinData = keys 
                        length = len(FinData)
                 
                        
                        #proceed to insert the data
                        data = NetworkHardware()
                        if FinData[0] == "None":
                           
                            if FinData[1] == "CCTV_DVR":
                                runing_number = Asset_running_number.objects.filter(asset_type='CCTV_DVR').get()
                                num = int(runing_number.running_number)
                                if num < 10:
                                    data_cid = "CCTV000"+ str(num)
                                elif ((num >= 10) and (num < 100)):
                                    data_cid= "CCTV00"+ str(num)
                                elif ((num >= 100) and (num < 1000)):
                                    data_cid= "CCTV0"+ str(num)
                                elif ((num >= 1000) and (num < 10000)):
                                    data_cid= "CCTV"+ str(num)
                                data.hardware_id = data_cid
                                runing_number.running_number = num +1
                                runing_number.save()
                            elif FinData[1] == "CCTV":
                                runing_number = Asset_running_number.objects.filter(asset_type='CCTV').get()
                                num = int(runing_number.running_number)
                                if num < 10:
                                    data_cid = "UTM-CM000"+ str(num)
                                elif ((num >= 10) and (num < 100)):
                                    data_cid= "UTM-CM00"+ str(num)
                                elif ((num >= 100) and (num < 1000)):
                                    data_cid= "UTM-CM0"+ str(num)
                                elif ((num >= 1000) and (num < 10000)):
                                    data_cid= "UTM-CM"+ str(num)
                                data.hardware_id = data_cid
                                runing_number.running_number = num +1
                                runing_number.save()
                            elif FinData[1] == "AP":
                                runing_number = Asset_running_number.objects.filter(asset_type='AP').get()
                                num = int(runing_number.running_number)
                                if num < 10:
                                    data_cid = "UTM-AP000"+ str(num)
                                elif ((num >= 10) and (num < 100)):
                                    data_cid= "UTM-AP00"+ str(num)
                                elif ((num >= 100) and (num < 1000)):
                                    data_cid= "UTM-AP0"+ str(num)
                                elif ((num >= 1000) and (num < 10000)):
                                    data_cid= "UTM-AP"+ str(num)
                                data.hardware_id = data_cid
                                runing_number.running_number = num +1
                                runing_number.save()
                            elif FinData[1] == "CP":
                                runing_number = Asset_running_number.objects.filter(asset_type='CP').get()
                                num = int(runing_number.running_number)
                                if num < 10:
                                    data_cid = "UTM-CP000"+ str(num)
                                elif ((num >= 10) and (num < 100)):
                                    data_cid= "UTM-CP00"+ str(num)
                                elif ((num >= 100) and (num < 1000)):
                                    data_cid= "UTM-CP0"+ str(num)
                                elif ((num >= 1000) and (num < 10000)):
                                    data_cid= "UTM-CP"+ str(num)
                                data.hardware_id = data_cid
                                runing_number.running_number = num +1
                                runing_number.save()
                            elif FinData[1] == "Door_Access":
                                runing_number = Asset_running_number.objects.filter(asset_type='Door_Access').get()
                                num = int(runing_number.running_number)
                                if num < 10:
                                    data_cid = "DoorController000"+ str(num)
                                elif ((num >= 10) and (num < 100)):
                                    data_cid= "DoorControllerP00"+ str(num)
                                elif ((num >= 100) and (num < 1000)):
                                    data_cid= "DoorController0"+ str(num)
                                elif ((num >= 1000) and (num < 10000)):
                                    data_cid= "DoorController"+ str(num)
                                data.hardware_id = data_cid
                                runing_number.running_number = num +1
                                runing_number.save()
                            elif FinData[1] == "Switches":
                                runing_number = Asset_running_number.objects.filter(asset_type='Switches').get()
                                num = int(runing_number.running_number)
                                if num < 10:
                                    data_cid = "UTM-NW000"+ str(num)
                                elif ((num >= 10) and (num < 100)):
                                    data_cid= "UTM-NWP00"+ str(num)
                                elif ((num >= 100) and (num < 1000)):
                                    data_cid= "UTM-NW0"+ str(num)
                                elif ((num >= 1000) and (num < 10000)):
                                    data_cid= "UTM-NW"+ str(num)
                                data.hardware_id = data_cid
                                runing_number.running_number = num +1
                                runing_number.save()
                            elif FinData[1] == "Tape_Library":
                                runing_number = Asset_running_number.objects.filter(asset_type='Tape_Library').get()
                                num = int(runing_number.running_number)
                                if num < 10:
                                    data_cid = "UTM-TL000"+ str(num)
                                elif ((num >= 10) and (num < 100)):
                                    data_cid= "UTM-TL00"+ str(num)
                                elif ((num >= 100) and (num < 1000)):
                                    data_cid= "UTM-TL0"+ str(num)
                                elif ((num >= 1000) and (num < 10000)):
                                    data_cid= "UTM-TL"+ str(num)
                                data.hardware_id = data_cid
                                runing_number.running_number = num +1
                                runing_number.save()
                            elif FinData[1] == "Wireless_Dongle":
                                runing_number = Asset_running_number.objects.filter(asset_type='Wireless_Dongle').get()
                                num = int(runing_number.running_number)
                                if num < 10:
                                    data_cid = "Tenda Wireless000"+ str(num)
                                elif ((num >= 10) and (num < 100)):
                                    data_cid= "Tenda Wireless00"+ str(num)
                                elif ((num >= 100) and (num < 1000)):
                                    data_cid= "Tenda Wireless0"+ str(num)
                                elif ((num >= 1000) and (num < 10000)):
                                    data_cid= "Tenda Wireless"+ str(num)
                                data.hardware_id = data_cid
                                runing_number.running_number = num +1
                                runing_number.save()
                            elif FinData[1] == "Print_Server":
                                runing_number = Asset_running_number.objects.filter(asset_type='Print_Server').get()
                                num = int(runing_number.running_number)
                                if num < 10:
                                    data_cid = "UTM-PS000"+ str(num)
                                elif ((num >= 10) and (num < 100)):
                                    data_cid= "UTM-PS00"+ str(num)
                                elif ((num >= 100) and (num < 1000)):
                                    data_cid= "UTM-PS0"+ str(num)
                                elif ((num >= 1000) and (num < 10000)):
                                    data_cid= "UTM-PS"+ str(num)
                                data.hardware_id = data_cid
                                runing_number.running_number = num +1
                                runing_number.save()
                            elif FinData[1] == "Firewall":
                                runing_number = Asset_running_number.objects.filter(asset_type='Firewall').get()
                                num = int(runing_number.running_number)
                                if num < 10:
                                    data_cid = "UTM-FW000"+ str(num)
                                elif ((num >= 10) and (num < 100)):
                                    data_cid= "UTM-FW00"+ str(num)
                                elif ((num >= 100) and (num < 1000)):
                                    data_cid= "UTM-FW0"+ str(num)
                                elif ((num >= 1000) and (num < 10000)):
                                    data_cid= "UTM-FW"+ str(num)
                                data.hardware_id = data_cid
                                runing_number.running_number = num +1
                                runing_number.save()
                            elif FinData[1] == "UPS":
                                data.hardware_id =  FinData[0]
                            elif FinData[1] == "Server":
                                runing_number = Asset_running_number.objects.filter(asset_type='Server').get()
                                num = int(runing_number.running_number)
                                if num < 10:
                                    data_cid = "UTM-SV000"+ str(num)
                                elif ((num >= 10) and (num < 100)):
                                    data_cid= "UTM-SV00"+ str(num)
                                elif ((num >= 100) and (num < 1000)):
                                    data_cid= "UTM-SV0"+ str(num)
                                elif ((num >= 1000) and (num < 10000)):
                                    data_cid= "UTM-SV"+ str(num)
                                data.hardware_id = data_cid
                                runing_number.running_number = num +1
                                runing_number.save()
                                

                        else:
                            data.hardware_id = FinData[0]
                        data.hardware_type = FinData[1]
                        data.Brand = FinData[2]
                        data.Model = FinData[3]
                        data.serial_number = FinData[4]
                        data.asset_no = FinData[5]
                        if FinData[6] == "None" or FinData[6] ==  "-":
                             data.dop = FinData[8]
                        else:
                            date_time_obj = datetime.strptime(FinData[6], '%d/%m/%Y')
                            change_date_format = date_time_obj.strftime('%d/%m/%Y')
                            data.dop = change_date_format
                             
                        if FinData[7] == "None" or FinData[7] ==  "-":
                            data.dop_Warranty_end_date = FinData[9]
                        else:
                            date_time_obj = datetime.strptime(FinData[7], '%d/%m/%Y')
                            change_date_format = date_time_obj.strftime('%d/%m/%Y')
                            data.dop_Warranty_end_date = change_date_format
                              
                      
                        data.vendor = FinData[8]
                        data.po = FinData[9]
                        data.invoice = FinData[10]
                        data.block = FinData[11]
                        data.location = FinData[12]

                        data.mac_address = FinData[13]
                        if FinData[14] != "None":
                            if  IP.objects.filter(ip_address=FinData[14], status = "Not-inuse").exists():
                                ip = IP.objects.get(ip_address=FinData[14])
                                ipdata= ip.ip_address
                                data.ip_address = ipdata
                                ip.status = "In-use"
                                ip.ip_assisgned = data.hardware_id
                                ip.save()
                            else:
                                errordata = "Yes"
                                typeerror = 'IP'
                                row = x
                                iperror = FinData[14]
                                
                                ip = IP.objects.get(ip_address=FinData[14])
                                computer_assignto =ip.ip_assisgned
                              
                                context ={
                                    "error" : errordata,
                                    "typeerror" : typeerror,
                                    "row" : row,
                                    "iperror" : iperror,
                                    "Computer_assign": computer_assignto



                                }
                                return render(request, "Mass upload page.html", context)
                        else:
                            data.ip_address = FinData[14]
                        data.Current_Status = FinData[15]
                       
                        if not NetworkHardware.objects.filter(hardware_id=data.hardware_id).exists():
                            data.save()
                          
                            x = x +1
                        else:
                          
                            errordata = "Yes"

                            

                
                    
                    return redirect('uploadcsvdata')

                if request.POST['Main_database'] == 'IP':
                    csv_file = request.FILES["csv_file"]
                    df = pd.read_csv(csv_file)
                    data1 = df.values.tolist()
                    for k in data1:
                        FinData = k 
                        length = len(FinData)
                        if  IP.objects.filter(ip_address=FinData[0]).exists():
                            
                                errordata = "Yes"
                            
                                context ={
                                    "error" : errordata,

                                }
                                return render(request, "Mass upload page.html", context)

                    for keys in data1:
                        FinData = keys 
                        length = len(FinData)
                   
                        #proceed to insert the data
                        data = IP()
                        data.ip_address = FinData[0]
                        
                        data.ip_assisgned = FinData[1]
                        
                        data.status = FinData[2]
                        data.remark = FinData[3]
            
                        if not IP.objects.filter(ip_address=data.ip_address).exists():
                            data.save()
                  
                        else:
                    
                            errordata = "Yes"

                            

                
                    
                    return redirect('uploadcsvdata')    
                  
                if request.POST['Main_database'] == 'User':
                    csv_file = request.FILES["csv_file"]
                    df = pd.read_csv(csv_file)
                    data1 = df.values.tolist()
                    for k in data1:
                        FinData = k 
                        length = len(FinData)
                        if  UserAsset.objects.filter(employee_number=FinData[0]).exists():
                            
                                errordata = "Yes"
                      
                                context ={
                                    "error" : errordata,

                                }
                                return render(request, "Mass upload page.html", context)

                    for keys in data1:
                        FinData = keys 
                        length = len(FinData)
                      
                        #proceed to insert the data
                        data = UserAsset()
                        data.employee_number = FinData[0]
                        
                        data.name = FinData[1]
                        
                        data.email = FinData[2]
                        data.designation = FinData[3]
                        data.department = FinData[4]
                        data.block = FinData[5]
                        data.location = FinData[6]
                        data.vpn = FinData[7]
                        data.vpnaccount = FinData[8]

            
                        if not UserAsset.objects.filter(employee_number=data.employee_number).exists():
                            data.save()
                    
                        else:
                      
                            errordata = "Yes"

                            

                
                    
                    return redirect('uploadcsvdata')    
                  
                if request.POST['Main_database'] == 'Software User':
                    csv_file = request.FILES["csv_file"]
                    df = pd.read_csv(csv_file)
                    data1 = df.values.tolist()
                    for k in data1:
                        FinData = k 
                        length = len(FinData)
                        if  softwareUser.objects.filter(Software_Type=FinData[0], User_Type= FinData[1], Software_Name=FinData[2], User_ID=FinData[3]).exists():
                                
                                errordata = "Yes"
                              
                                context ={
                                    "error" : errordata,

                                }
                                return render(request, "Mass upload page.html", context)

                    for keys in data1:
                        FinData = keys 
                        length = len(FinData)
                       
                        #proceed to insert the data
                        data = softwareUser()
                        data.Software_Type = FinData[0]
                        
                        data.User_Type = FinData[1]
                        
                        data.Software_Name = FinData[2]
                        data.User_ID = FinData[3]
                        data.Software_Version = FinData[4]
                        

            
                        if not softwareUser.objects.filter(Software_Type=FinData[0], User_Type= FinData[1], Software_Name=FinData[2], User_ID=FinData[3]).exists():
                            data.save()
                    
                        else:
                     
                            errordata = "Yes"

                            

                
                    
                    return redirect('uploadcsvdata')
                  
        if request.POST['typeofupload'] == 'Update':     
                if request.POST['Main_database'] == 'Computer':
                    csv_file = request.FILES["csv_file"]
                    df = pd.read_csv(csv_file)
                    data1 = df.values.tolist()
                 
                    for keys in data1:
                        x=2
                        FinData = keys 
                        length = len(FinData)
                  
                        #proceed to insert the data
                        data = Computer.objects.filter(computer_id= FinData[0]).get()
                       
                        data.computer_id = FinData[0]
                        
                      
                        data.current_computer_id = FinData[1]
                      
                        
                        data.pctype = FinData[2]
                        data.pic = FinData[3]
                        data.previous_pic = FinData[4]
                        data.Brand = FinData[5]
                        data.Model = FinData[6]
                        data.serial_number = FinData[7]
                        data.asset_no = FinData[8]
                        if FinData[9] == "None" or FinData[9] ==  "-":
                            data.dop = FinData[9]
                        else:
                            date_time_obj = datetime.strptime(FinData[9], '%d/%m/%Y')
                            change_date_format = date_time_obj.strftime('%Y-%m-%d')
                            data.dop = change_date_format
                              
                        if FinData[10] == "None" or FinData[10] ==  "-":
                            data.dop_Warranty_end_date = FinData[10]
                        else:
                            date_time_obj = datetime.strptime(FinData[10], '%d/%m/%Y')
                            change_date_format = date_time_obj.strftime('%Y-%m-%d')
                            data.dop_Warranty_end_date = change_date_format
                              
                       
                       
                        data.vendor = FinData[11]
                        data.po = FinData[12]
                        data.invoice = FinData[13]
                        data.type_of_purchase = FinData[14]

                        data.block = FinData[15]
                        data.location = FinData[16]
                        data.standard_installation = FinData[17]
                        standardinstall = data.standard_installation
                        if FinData[17] == "Yes" or FinData[17] == "yes" :
                            if not softwareUser.objects.filter(User_ID=FinData[0], Software_Name="Trend Micro" ).exists():
                                trend_micro = softwareUser()
                                trend_micro.Software_Type = "Non-Concurrent"
                                trend_micro.User_Type = "Machine"
                                trend_micro.Software_Name = "Trend Micro"
                                trend_micro.Software_Version = "Apex one"
                                trend_micro.User_ID = data.computer_id
                                trend_micro.save()
                            if not softwareUser.objects.filter(User_ID=FinData[0], Software_Name="Teamviewer" ).exists():
                                teamviewer = softwareUser()
                                teamviewer.Software_Type = "Non-Concurrent"
                                teamviewer.User_Type = "Machine"
                                teamviewer.Software_Name = "Teamviewer"
                                teamviewer.Software_Version = "Teamviewer Host"
                                teamviewer.User_ID = data.computer_id
                                teamviewer.save()
                            if not softwareUser.objects.filter(User_ID=FinData[0], Software_Name="TightVNC" ).exists():
                                vnc = softwareUser()
                                vnc.Software_Type = "Non-Concurrent"
                                vnc.User_Type = "Machine"
                                vnc.Software_Name = "TightVNC"
                                vnc.Software_Version = "tightvnc-2.8.63"
                                vnc.User_ID = data.computer_id
                                vnc.save()
                            if not softwareUser.objects.filter(User_ID=FinData[0], Software_Name="Marimba" ).exists():
                                marimba = softwareUser()
                                marimba.Software_Type = "Non-Concurrent"
                                marimba.User_Type = "Machine"
                                marimba.Software_Name = "Marimba"
                                marimba.Software_Version = "SFSInventory_x64"
                                marimba.User_ID = data.computer_id
                                marimba.save()
                        
                        data.usbunlock = FinData[18]
                        data.cdunlock = FinData[19]
                        data.windows = FinData[20]
                        data.microsoft_office = FinData[21]
                        data.microsoft_office_keys = FinData[22]
                        data.processor_type = FinData[23]
                        data.ram_type = FinData[24]
                        data.ram_slot = FinData[25]
                        data.total_ram = FinData[26]
                        data.storage_type = FinData[27]
                        data.storage_space = FinData[28]
                        data.connection_type = FinData[29]
                        data.joined_domain = FinData[30]
                        data.lan_mac_address = FinData[31]
                        if ( FinData[32] == "Release" or FinData[32] == "release"):
                            if (data.lan_ip_address != ""):
                                ip = IP.objects.get(ip_address=data.lan_ip_address)
                                ip.status = "Not-inuse"
                                ip.ip_assisgned = "None"
                                ip.save()
                                data.lan_ip_address = FinData[32]
                        else:
                            previIP = data.lan_ip_address
                            if ( previIP != FinData[32] ):
                                if previIP == "Release":
                                    if FinData[32] == "Offline":
                                        data.lan_ip_address = FinData[32]
                                    else:
                                        ipNew = IP.objects.get(ip_address = FinData[32])
                                        ipNew.status = "In-use"
                                        ipNew.ip_assisgned = FinData[0]
                                        ipNew.save()
                                        data.lan_ip_address = FinData[32]


                                elif previIP == "Offline" or previIP == "None":
                                    if FinData[32]  == "Offline" or FinData[32] == "None":
                                        data.lan_ip_address = FinData[32]
                                    else:
                                        ipNew = IP.objects.get(ip_address = FinData[32])
                                        ipNew.status = "In-use"
                                        ipNew.ip_assisgned = FinData[0]
                                        ipNew.save()
                                        data.lan_ip_address = FinData[32]

                                    
                                else:
                                    ip = IP.objects.get(ip_address=previIP)
                                    ip.status = "Not-inuse"
                                    ip.ip_assisgned = "None"
                                    ip.save()
                                    ipNew = IP.objects.get(ip_address = FinData[32])
                                    ipNew.status = "In-use"
                                    ipNew.ip_assisgned = FinData[0]
                                    ipNew.save()
                                    data.lan_ip_address = FinData[32]


                                
                                
                                
                            else:
                                data.lan_ip_address = FinData[32]

                        
                        data.wlan_mac_address = FinData[33]
                       
                        data.wlan_ip_address = FinData[34]
                        data.pccurrentstatus = FinData[35]


                       
                     
                        data.save()
                        dataarray = [data.computer_id, FinData[7], FinData[5], FinData[6]]
                        type_create = 'Update'
                        create_qrcodePC(dataarray, type_create)
                        
                            

                    
                    return redirect('uploadcsvdata')

                if request.POST['Main_database'] == 'Laptop':
                    csv_file = request.FILES["csv_file"]
                 
                    df = pd.read_csv(csv_file, encoding='unicode_escape')
                    data1 = df.values.tolist()
                    

                    for keys in data1:
                        x =1
                        FinData = keys 
                        length = len(FinData)
                  
                        #proceed to insert the data
                        data = Laptop.objects.filter(computer_id= FinData[0]).get()
                        
                        data.computer_id = FinData[0]
                       
                        data.current_computer_id = FinData[1]
                        data.pic = FinData[2]
                        data.previous_pic = FinData[3]
                        data.Brand = FinData[4]
                        data.Model = FinData[5]
                        data.serial_number = FinData[6]
                        data.asset_no = FinData[7]
                        if FinData[8] == "None" or FinData[8] ==  "-":
                            data.dop = FinData[8]
                        else:
                            date_time_obj = datetime.strptime(FinData[8], '%d/%m/%Y')
                            change_date_format = date_time_obj.strftime('%Y-%m-%d')
                            data.dop = change_date_format
                              
                        if FinData[9] == "None" or FinData[9] ==  "-":
                            data.dop_Warranty_end_date = FinData[9]
                           
                        else:
                            date_time_obj = datetime.strptime(FinData[9], '%d/%m/%Y')
                            change_date_format = date_time_obj.strftime('%Y-%m-%d')
                            data.dop_Warranty_end_date = change_date_format
                            
                       
                        
                        data.vendor = FinData[10]
                        data.po = FinData[11]
                        data.invoice = FinData[12]
                        data.type_of_purchase = FinData[13]

                        data.block = FinData[14]
                        data.location = FinData[15]
                        data.standard_installation = FinData[16]
                        standardinstall =  data.standard_installation
                        if FinData[16] == "Yes" or FinData[16] == "yes" :
                            if not softwareUser.objects.filter(User_ID=FinData[0], Software_Name="Trend Micro" ).exists():
                                trend_micro = softwareUser()
                                trend_micro.Software_Type = "Non-Concurrent"
                                trend_micro.User_Type = "Machine"
                                trend_micro.Software_Name = "Trend Micro"
                                trend_micro.Software_Version = "Apex one"
                                trend_micro.User_ID = data.computer_id
                                trend_micro.save()
                            if not softwareUser.objects.filter(User_ID=FinData[0], Software_Name="Teamviewer" ).exists():
                                teamviewer = softwareUser()
                                teamviewer.Software_Type = "Non-Concurrent"
                                teamviewer.User_Type = "Machine"
                                teamviewer.Software_Name = "Teamviewer"
                                teamviewer.Software_Version = "Teamviewer Host"
                                teamviewer.User_ID = data.computer_id
                                teamviewer.save()
                            if not softwareUser.objects.filter(User_ID=FinData[0], Software_Name="TightVNC" ).exists():
                                vnc = softwareUser()
                                vnc.Software_Type = "Non-Concurrent"
                                vnc.User_Type = "Machine"
                                vnc.Software_Name = "TightVNC"
                                vnc.Software_Version = "tightvnc-2.8.63"
                                vnc.User_ID = data.computer_id
                                vnc.save()
                            if not softwareUser.objects.filter(User_ID=FinData[0], Software_Name="Marimba" ).exists():
                                marimba = softwareUser()
                                marimba.Software_Type = "Non-Concurrent"
                                marimba.User_Type = "Machine"
                                marimba.Software_Name = "Marimba"
                                marimba.Software_Version = "SFSInventory_x64"
                                marimba.User_ID = data.computer_id
                                marimba.save()
                        data.usbunlock = FinData[17]
                        data.cdunlock = FinData[18]
                        data.windows = FinData[19]
                        data.microsoft_office = FinData[20]
                        data.microsoft_office_keys = FinData[21]
                        data.processor_type = FinData[22]
                        data.ram_type = FinData[23]
                        data.ram_slot = FinData[24]
                        data.total_ram = FinData[25]
                        data.storage_type = FinData[26]
                        data.storage_space = FinData[27]
                        data.connection_type = FinData[28]
                 
                        data.joined_domain = FinData[29]
                        data.lan_mac_address = FinData[30]
                        if ( FinData[31] == "Release" or FinData[31] == "release"):
                            if (data.lan_ip_address != ""):
                                ip = IP.objects.get(ip_address=data.lan_ip_address)
                                ip.status = "Not-inuse"
                                ip.ip_assisgned = "None"
                                ip.save()
                                data.lan_ip_address = FinData[31]
                        else:
                            previIP = data.lan_ip_address
                            if ( previIP != FinData[31] ):
                                if previIP == "Release":
                                    if FinData[32] == "Offline":
                                        data.lan_ip_address = FinData[32]
                                    else:
                                        ipNew = IP.objects.get(ip_address = FinData[32])
                                        ipNew.status = "In-use"
                                        ipNew.ip_assisgned = FinData[0]
                                        ipNew.save()
                                        data.lan_ip_address = FinData[32]
                                elif previIP != "Offline" or previIP != "None" :

                                    ip = IP.objects.get(ip_address=previIP)
                                    ip.status = "Not-inuse"
                                    ip.ip_assisgned = "None"
                                    ip.save()
                                    ipNew = IP.objects.get(ip_address = FinData[31])
                                    ipNew.status = "In-use"
                                    ipNew.ip_assisgned = FinData[0]
                                    ipNew.save()
                                    data.lan_ip_address = FinData[31]
                                else:
                                    ipNew = IP.objects.get(ip_address = FinData[31])
                                    ipNew.status = "In-use"
                                    ipNew.ip_assisgned = FinData[0]
                                    ipNew.save()
                                    data.lan_ip_address = FinData[31]
                            else:
                                data.lan_ip_address = FinData[31]
                      
                        data.wlan_mac_address = FinData[32]
                        if ( FinData[33] == "Release" or FinData[33] == "release"):
                            if (data.wlan_ip_address != ""):
                                ip = IP.objects.get(ip_address=data.wlan_ip_address)
                                ip.status = "Not-inuse"
                                ip.ip_assisgned = "None"
                                ip.save()
                                data.wlan_ip_address = FinData[33]
                        else:
                            previIP = data.lan_ip_address
                            if ( previIP != FinData[33]):
                                if FinData[31] != "Offline" :
                                    ip = IP.objects.get(ip_address=previIP)
                                    ip.status = "Not-inuse"
                                    ip.ip_assisgned = "None"
                                    ip.save()
                                    ipNew = IP.objects.get(ip_address = FinData[33])
                                    ipNew.status = "In-use"
                                    ipNew.ip_assisgned = FinData[0]
                                    ipNew.save()
                                    data.wlan_ip_address = FinData[33]
                                else:
                                    ipNew = IP.objects.get(ip_address = FinData[33])
                                    ipNew.status = "In-use"
                                    ipNew.ip_assisgned = FinData[0]
                                    ipNew.save()
                                    data.wlan_ip_address = FinData[33]

                            else:
                                data.wlan_ip_address = FinData[33]
                      
                        data.pccurrentstatus = FinData[34]
                       
                        data.save()
                        dataarray = [data.computer_id, FinData[6], FinData[4], FinData[5]]
                        type_create = "Update"
                        create_qrcodeLaptop(dataarray, type_create)

                            

                
                    
                    return redirect('uploadcsvdata')
                        
                
                    
                    return HttpResponse(context)
                
                if request.POST['Main_database'] == 'NetworkHardware':
                    csv_file = request.FILES["csv_file"]
                    df = pd.read_csv(csv_file)
                    data1 = df.values.tolist()
                   
                    x =1 
                    for keys in data1:
                        FinData = keys 
                        length = len(FinData)
                
                        
                        #proceed to insert the data
                        data = NetworkHardware.objects.filter(hardware_id= FinData[0]).get()
                       
                        data.hardware_id = FinData[0]
                        data.hardware_type = FinData[1]
                        data.Brand = FinData[2]
                        data.Model = FinData[3]
                        data.serial_number = FinData[4]
                        data.asset_no = FinData[5]
                        if FinData[6] == "None" or FinData[6] ==  "-":
                             data.dop = FinData[8]
                        else:
                            date_time_obj = datetime.strptime(FinData[6], '%d/%m/%Y')
                            change_date_format = date_time_obj.strftime('%Y-%m-%d')
                            data.dop = change_date_format
                             
                        if FinData[7] == "None" or FinData[7] ==  "-":
                            data.dop_Warranty_end_date = FinData[9]
                        else:
                            date_time_obj = datetime.strptime(FinData[7], '%d/%m/%Y')
                            change_date_format = date_time_obj.strftime('%Y-%m-%d')
                            data.dop_Warranty_end_date = change_date_format
                              
                      
                        data.vendor = FinData[8]
                        data.po = FinData[9]
                        data.invoice = FinData[10]
                        data.block = FinData[11]
                        data.location = FinData[12]

                        data.mac_address = FinData[13]
                        
                        data.ip_address = FinData[14]
                        data.Current_Status = FinData[15]
                       
                      
                        data.save()
                        

                            

                
                    
                    return redirect('uploadcsvdata')

                if request.POST['Main_database'] == 'IP':
                    csv_file = request.FILES["csv_file"]
                    df = pd.read_csv(csv_file)
                    data1 = df.values.tolist()
                  

                    for keys in data1:
                        FinData = keys 
                        length = len(FinData)
                      
                        #proceed to insert the data
                        data = IP.objects.filter(ip_address= FinData[0]).get()
                        data.ip_address = FinData[0]
                        
                        data.ip_assisgned = FinData[1]
                        
                        data.status = FinData[2]
                        data.remark = FinData[3]
            
                      
                        data.save()
                          

                            

                
                    
                    return redirect('uploadcsvdata')    
                  
                if request.POST['Main_database'] == 'User':
                    csv_file = request.FILES["csv_file"]
                    df = pd.read_csv(csv_file)
                    data1 = df.values.tolist()
                  
                    for keys in data1:
                        FinData = keys 
                        length = len(FinData)
                   
                        #proceed to insert the data
                        data = UserAsset.objects.filter(employee_number= FinData[0]).get()
                        data.employee_number = FinData[0]
                        
                        data.name = FinData[1]
                        
                        data.email = FinData[2]
                        data.designation = FinData[3]
                        data.department = FinData[4]
                        data.block = FinData[5]
                        data.location = FinData[6]
                        data.vpn = FinData[7]
                        data.vpnaccount = FinData[8]

            
                       
                        data.save()
                        

                            

                
                    
                    return redirect('uploadcsvdata')    
                  
                if request.POST['Main_database'] == 'Software User': 
                    csv_file = request.FILES["csv_file"]
                    df = pd.read_csv(csv_file)
                    data1 = df.values.tolist()
                    

                    for keys in data1:
                        FinData = keys 
                        length = len(FinData)
                   
                        #proceed to insert the data
                        data = softwareUser.objects.filter(User_ID= FinData[3], Software_Name= FinData[2]).get()
                        data.Software_Type = FinData[0]
                        
                        data.User_Type = FinData[1]
                        
                        data.Software_Name = FinData[2]
                        data.User_ID = FinData[3]
                        data.Software_Version = FinData[4]
                        

            
                       
                        data.save()
                       
                        
                    return redirect('uploadcsvdata')
             
    return render(request, 'Mass upload page.html')      
  

          
               
           
# Laptop Page
def laptopdetail(request):
        pctype = Modellaptop.objects.all()
        processorType = Processor_type.objects.all()
        brand = Brand.objects.all()
        ram_type = Ram_type.objects.all()
        microsoft_office = Microsoft_office.objects.all()
        location = Location.objects.all()
        window = Windows.objects.all()
        displaydata = Laptop.objects.all()
    
        tableend = Computer.objects.all().count()
        tablestart = 0
        Vendor = vendor.objects.all()
        tablerange = range(tablestart, tableend)
        runing_number = Asset_running_number.objects.filter(asset_type='Laptop').get()
        storage_value = storagevalue.objects.all()
  
        username =  format(request.session.get('name'))
        if (format(request.session.get('role')) == "staff"):
            style = format(request.session.get('styledivstaff'))
        else:
            style = format(request.session.get('styledivNotstaff'))
        context = {'pctype':pctype,
        'processorType':processorType,
        'brand':brand,
        'ram_type':ram_type,
        'processorType':processorType,
        'microsoft_office':microsoft_office,
        'location':location,
        'window':window,
        'Vendor':Vendor,
        'runing_number':runing_number,
        'tablerange':tablerange,
        
        'displaydata':displaydata,
        'storage_value': storage_value,
        'Username':username,"Style" : style}
       
        return render(request, 'Laptop Page.html', context)

def addlaptopform(request):
    if request.method == "POST":
        test = request.POST['total_RAM']
    
        runing_number = Asset_running_number.objects.filter(asset_type='Laptop').get()
        data = Laptop()
        data.pic = request.POST['pic']
        data.type_of_purchase = request.POST['type_of_purchase']
        data.previous_pic = request.POST['Previous_PIC']
        data.computer_id = request.POST['Computer_ID']
        pc_id =data.computer_id 
        data.current_computer_id = request.POST['Current_Computer_ID']
        data.Brand = request.POST['Brand']
        data.Model = request.POST['model']
        data.serial_number = request.POST['serial_number']
        data.asset_no = request.POST['asset_no']
        data.vendor = request.POST['vendor']
        data.processor_type = request.POST['processor']
        data.ram_type = request.POST['ram_type']
        data.ram_slot = request.POST['ram_slot']
        data.total_ram = request.POST['total_RAM']
        data.storage_type = request.POST['storage_type']
        data.storage_space = request.POST['storageSpace']
        data.dop = request.POST['dop']
        data.dop_Warranty_end_date = request.POST['dopYear']
        data.cdunlock = request.POST['cd_unlock']
        data.usbunlock = request.POST['usb_unlock']
        data.po = request.POST['po']
        data.invoice = request.POST['invoice']
        data.block = request.POST['block']
        data.location = request.POST['location']
        data.standard_installation = request.POST['Standard_Installation']
        standard_installation = data.standard_installation
        data.microsoft_office = request.POST['Microsoft_Office']
        data.microsoft_office_keys = request.POST['Licensed_key']

        data.windows = request.POST['Window_version']
        data.lan_mac_address = request.POST['lan_mac_address']
        data.lan_ip_address = request.POST['lan_ip_address']
        data.wlan_mac_address = request.POST['wlan_mac_address']

        data.wlan_ip_address = request.POST['wlan_ip_address']
        data.joined_domain = request.POST['Joined_Domain']
        data.connection_type = request.POST['ConnectionType']
        data.pccurrentstatus = request.POST['Computer_Status']

        if(request.POST['ConnectionType'] == "Offline"):
              if not Laptop.objects.filter(computer_id=request.POST['Computer_ID']).exists():
                data.save()
                num = int(runing_number.running_number)+1
                updatenum = Asset_running_number.objects.get(asset_type='Laptop')
                updatenum.running_number = num
                updatenum.save()
                log_history = loghistory()
                log_history.Time = datetime.now()
                log_history.Username = format(request.session.get('name'))
                log_history.Activity = "Add A Laptop By ID " + request.POST['Computer_ID']
                log_history.save() 
                if standard_installation == "Yes" or standard_installation == "yes":
                            trend_micro = softwareUser()
                            trend_micro.Software_Type = "Non-Concurrent"
                            trend_micro.User_Type = "Machine"
                            trend_micro.Software_Name = "Trend Micro"
                            trend_micro.Software_Version = "Apex one"
                            trend_micro.User_ID = pc_id
                            trend_micro.save()
                            teamviewer = softwareUser()
                            teamviewer.Software_Type = "Non-Concurrent"
                            teamviewer.User_Type = "Machine"
                            teamviewer.Software_Name = "Teamviewer"
                            teamviewer.Software_Version = "Teamviewer Host"
                            teamviewer.User_ID = pc_id
                            teamviewer.save()
                            vnc = softwareUser()
                            vnc.Software_Type = "Non-Concurrent"
                            vnc.User_Type = "Machine"
                            vnc.Software_Name = "TightVNC"
                            vnc.Software_Version = "tightvnc-2.8.63"
                            vnc.User_ID = pc_id
                            vnc.save()
                            marimba = softwareUser()
                            marimba.Software_Type = "Non-Concurrent"
                            marimba.User_Type = "Machine"
                            marimba.Software_Name = "Marimba"
                            marimba.Software_Version = "SFSInventory_x64"
                            marimba.User_ID = pc_id
                            marimba.save()
                arraydataQR = [ request.POST['Computer_ID'], request.POST['serial_number'], request.POST['Brand'], request.POST['model'] ]
                type_create = "Create"
                create_qrcodeLaptop(arraydataQR, type_create)
                return HttpResponse('hai')

        else :
            if not Laptop.objects.filter(computer_id=request.POST['Computer_ID']).exists():
                data.save()
                num = int(runing_number.running_number)+1
                updatenum = Asset_running_number.objects.get(asset_type='Laptop')
                updatenum.running_number = num
                updatenum.save()
                ip1 = IP.objects.get(ip_address=request.POST['lan_ip_address'])
                ip1.status = "In-use"
                ip1.ip_assisgned = data.computer_id

                ip1.save()
                ip2 = IP.objects.get(ip_address=request.POST['wlan_ip_address'])
                ip2.status = "In-use"
                ip2.ip_assisgned = data.computer_id

                ip2.save()
                log_history = loghistory()
                log_history.Time = datetime.now()
                log_history.Username = format(request.session.get('name'))
                log_history.Activity = "Add A Laptop By ID " + request.POST['Computer_ID']
                log_history.save() 
                if standard_installation == "Yes" or standard_installation == "yes":
                            trend_micro = softwareUser()
                            trend_micro.Software_Type = "Non-Concurrent"
                            trend_micro.User_Type = "Machine"
                            trend_micro.Software_Name = "Trend Micro"
                            trend_micro.Software_Version = "Apex one"
                            trend_micro.User_ID = pc_id
                            trend_micro.save()
                            teamviewer = softwareUser()
                            teamviewer.Software_Type = "Non-Concurrent"
                            teamviewer.User_Type = "Machine"
                            teamviewer.Software_Name = "Teamviewer"
                            teamviewer.Software_Version = "Teamviewer Host"
                            teamviewer.User_ID = pc_id
                            teamviewer.save()
                            vnc = softwareUser()
                            vnc.Software_Type = "Non-Concurrent"
                            vnc.User_Type = "Machine"
                            vnc.Software_Name = "TightVNC"
                            vnc.Software_Version = "tightvnc-2.8.63"
                            vnc.User_ID = pc_id
                            vnc.save()
                            marimba = softwareUser()
                            marimba.Software_Type = "Non-Concurrent"
                            marimba.User_Type = "Machine"
                            marimba.Software_Name = "Marimba"
                            marimba.Software_Version = "SFSInventory_x64"
                            marimba.User_ID = pc_id
                            marimba.save()
                arraydataQR = [ request.POST['Computer_ID'], request.POST['serial_number'], request.POST['Brand'], request.POST['model'] ]
                type_create = "Create"
                create_qrcodeLaptop(arraydataQR, type_create)
                
                return HttpResponse('hai')

def getcustomLaptopdata(request):
    if request.method == "POST":
        data1 = int(request.POST["data1"])
        data2 = int(request.POST["data2"])
       
        arraydata = []
        while data1 <= data2:
            if data1 <= 268:
                if data1 < 10:
                    data = "UTM-NB00"+ str(data1)
                elif ((data1 >= 10) and (data1 < 100)):
                    data= "UTM-NB0"+ str(data1)
                elif ((data1 >= 100) and (data1 < 1000)):
                    data= "UTM-NB"+ str(data1)
                elif ((data1 >= 1000) and (data1 < 10000)):
                    data= "UTM-NB"+ str(data1)
                data1 = data1 + 1
                arraydata.append(data)
            else:
                if data1 < 10:
                    data = "UTM-NB000"+ str(data1)
                elif ((data1 >= 10) and (data1 < 100)):
                    data= "UTM-NB00"+ str(data1)
                elif ((data1 >= 100) and (data1 < 1000)):
                    data= "UTM-NB0"+ str(data1)
                elif ((data1 >= 1000) and (data1 < 10000)):
                    data= "UTM-NB"+ str(data1)
                data1 = data1 + 1
                arraydata.append(data)

  


        
        computerdata = Laptop.objects.filter(computer_id__in=arraydata)
        return JsonResponse({"data":list(computerdata.values())})

def exportdatalaptop(request):
   
     
        if request.POST["type"] == 'all':

            computerdata = Laptop.objects.all()
            data = []
            for key in computerdata:
                arraydata = [key.computer_id, key.current_computer_id, key.pic,key.previous_pic, key.Brand, key.Model, key.serial_number,
                key.asset_no, key.dop, key.dop_Warranty_end_date, key.vendor, key.po, key.invoice, key.type_of_purchase, key.block, key.location,
                key.standard_installation, key.usbunlock, key.cdunlock, key.windows, key.microsoft_office, key.microsoft_office_keys, key.processor_type, key.ram_type, key.ram_slot, key.total_ram, key.storage_type
                , key.storage_space, key.connection_type, key.joined_domain, key.lan_mac_address, key.lan_ip_address, key.wlan_mac_address, key.wlan_ip_address, key.pccurrentstatus]
                data.append(arraydata)
        
            
            return JsonResponse({"data":data})
        if request.POST["type"] == 'custom':
            data1 = int(request.POST["datafinal1"])
            data2 = int(request.POST["datafinal2"])
        
            arraydata = []
            while data1 <= data2:
                if data1 <= 268:
                    if data1 < 10:
                        data = "UTM-NB00"+ str(data1)
                    elif ((data1 >= 10) and (data1 < 100)):
                        data= "UTM-NB0"+ str(data1)
                    elif ((data1 >= 100) and (data1 < 1000)):
                        data= "UTM-NB"+ str(data1)
                    elif ((data1 >= 1000) and (data1 < 10000)):
                        data= "UTM-NB"+ str(data1)
                    data1 = data1 + 1
                    arraydata.append(data)
                else:
                    if data1 < 10:
                        data = "UTM-NB000"+ str(data1)
                    elif ((data1 >= 10) and (data1 < 100)):
                        data= "UTM-NB00"+ str(data1)
                    elif ((data1 >= 100) and (data1 < 1000)):
                        data= "UTM-NB0"+ str(data1)
                    elif ((data1 >= 1000) and (data1 < 10000)):
                        data= "UTM-NB"+ str(data1)
                    data1 = data1 + 1
                    arraydata.append(data)
            computerdata = Laptop.objects.filter(computer_id__in=arraydata)
            data = []
            for key in computerdata:
                arraydata = [key.computer_id, key.current_computer_id, key.pic,key.previous_pic, key.Brand, key.Model, key.serial_number,
                key.asset_no, key.dop, key.dop_Warranty_end_date, key.vendor, key.po, key.invoice, key.type_of_purchase, key.block, key.location,
                key.standard_installation,  key.usbunlock, key.cdunlock, key.windows, key.microsoft_office, key.microsoft_office_keys, key.processor_type, key.ram_type, key.ram_slot, key.total_ram, key.storage_type
                , key.storage_space, key.connection_type, key.joined_domain, key.lan_mac_address, key.lan_ip_address, key.wlan_mac_address, key.wlan_ip_address, key.pccurrentstatus]
                data.append(arraydata)
        
            
            return JsonResponse({"data":data})

def returnloan(request):
    if request.method == "POST":
         id = request.POST["id"]
         data = Loan.objects.filter(pk = id).get()
         asset_id = data.asset_id
         data.delete()
    if(asset_id.find("UTM-PC")!=-1):
                    computerdata = Computer.objects.filter(computer_id=asset_id).get()
                    computerdata.pccurrentstatus = "Loan"
                    computerdata.save()
                    return HttpResponse('hai')
    elif(asset_id.find("UTM-NB")!=-1):
                    computerdata = Laptop.objects.filter(computer_id=asset_id).get()
                    computerdata.pccurrentstatus = "Loan"
                    computerdata.save()
                    return HttpResponse('hai')
    elif(asset_id.find("UTM-AP")!=-1) or (asset_id.find("UTM-CM")!=-1)  or (asset_id.find("CCTV")!=-1) or (asset_id.find("UTM-CP")!=-1) or (asset_id.find("DoorController")!=-1) or (asset_id.find("UTM-NW")!=-1) or (asset_id.find("UTM-TL")!=-1) or (asset_id.find("Tenda Wireless")!=-1) or (asset_id.find("UPS")!=-1) or (asset_id.find("UTM-FW")!=-1): 
                    computerdata = NetworkHardware.objects.filter(computer_id=asset_id).get()
                    computerdata.Current_Status = "Loan"
                    computerdata.save()
                    return HttpResponse('hai')    

def GetEmployeeLoanDetail(request):
    if request.method == "POST":
         id = request.POST["id"]
         data = UserAsset.objects.filter(employee_number = id).get()
         datasent = {
             'employee_number': data.employee_number,'email': data.email, 'designation': data.designation,
             'department': data.department
         }
         return JsonResponse(datasent)
         
def runlaptopform(request):
    if request.method == "POST":
       id = request.POST["type"]
       ip = IP.objects.filter(status = 'Not-inuse' )
       computerdata = Asset_running_number.objects.filter(asset_type = id).get()
       data = { 'runnumber' : computerdata.running_number, "ip":list(ip.values()) }
       return JsonResponse(data)

def updateformlaptop(request):
     if request.method == "POST":
       
        
        data = Laptop.objects.filter(computer_id= request.POST['Computer_ID']).get()
        data.pic = request.POST['pic']
        data.previous_pic = request.POST['Previous_PIC']
        data.type_of_purchase = request.POST['type_of_purchase']

        data.computer_id = request.POST['Computer_ID']
        data.current_computer_id = request.POST['Current_Computer_ID']
        data.Brand = request.POST['Brand']
        data.Model = request.POST['model']
        data.serial_number = request.POST['serial_number']
        data.asset_no = request.POST['asset_no']
        data.vendor = request.POST['vendor']
        data.processor_type = request.POST['processor']
        data.ram_type = request.POST['ram_type']
        data.ram_slot = request.POST['ram_slot']
        data.total_ram = request.POST['total_RAM']
        data.storage_type = request.POST['storage_type']
        data.storage_space = request.POST['storageSpace']
        data.dop = request.POST['dop']
        data.dop_Warranty_end_date = request.POST['dopYear']
        data.po = request.POST['po']
        data.invoice = request.POST['invoice']
        data.block = request.POST['block']
        data.location = request.POST['location']
        data.standard_installation = request.POST['Standard_Installation']
        data.microsoft_office = request.POST['Microsoft_Office']
        data.microsoft_office_keys = request.POST['Licensed_key']
        data.cdunlock = request.POST['cd_unlock']
        data.usbunlock = request.POST['usb_unlock']
        data.windows = request.POST['Window_version']
        data.lan_mac_address = request.POST['lan_mac_address']
        if(data.lan_ip_address == "Offline") and (request.POST['lan_ip_address'] == "Offline"):
            data.wlan_ip_address = request.POST['lan_ip_address']
            
        elif(request.POST['lan_ip_address'] == "Offline"):
            Previous_IP = data.lan_ip_address
            ip = IP.objects.get(ip_address=Previous_IP)
            ip.status = "Not-inuse"
            ip.ip_assisgned ="None"

            ip.save()
            data.lan_ip_address = "Offline"

        elif(request.POST['lan_ip_address'] == "Release"):
            Previous_IP = data.lan_ip_address
            ip = IP.objects.get(ip_address=Previous_IP)
            ip.status = "Not-inuse"
            ip.ip_assisgned ="None"

            ip.save()
            data.lan_ip_address = request.POST['lan_ip_address']
        elif( (data.lan_ip_address == "Offline")):
            data.lan_ip_address = request.POST['lan_ip_address']
            ip = IP.objects.get(ip_address=request.POST['lan_ip_address'])
            ip.status = "In-use"
            ip.ip_assisgned =data.computer_id

            ip.save()
        elif( (data.lan_ip_address == "Release") and (data.pccurrentstatus !="Pending Dispose") and (data.pccurrentstatus !="Dispose") ):
            data.lan_ip_address = request.POST['lan_ip_address']
            ip = IP.objects.get(ip_address=request.POST['lan_ip_address'])
            ip.ip_assisgned =data.computer_id
            ip.status = "In-use"
            ip.save()
        elif( data.lan_ip_address != request.POST['lan_ip_address']):
            Previous_IP = data.lan_ip_address
            if Previous_IP == "Offline" or Previous_IP == "None" :
                ip = IP.objects.get(ip_address=request.POST['lan_ip_address'])
                ip.status = "In-use"
                ip.ip_assisgned =data.computer_id
                data.lan_ip_address = request.POST['lan_ip_address']
            else:
                data.lan_ip_address = request.POST['lan_ip_address']
                ip = IP.objects.get(ip_address=request.POST['lan_ip_address'])
                ip.status = "In-use"
                ip.ip_assisgned =data.computer_id
                ip.save()
                Change_IP_status = IP.objects.get(ip_address= Previous_IP)
                Change_IP_status.status = "Not-inuse"
                ip.ip_assisgned ="None"
                Change_IP_status.save()
     
        
        
        data.wlan_mac_address = request.POST['wlan_mac_address']
        if(data.wlan_ip_address == "Offline") and (request.POST['wlan_ip_address'] == "Offline"):
            data.wlan_ip_address = request.POST['wlan_ip_address']
        elif(request.POST['wlan_ip_address'] == "Offline"):
            ip = IP.objects.get(ip_address=data.wlan_ip_address)
            ip.status = "Not-inuse"
            ip.ip_assisgned ="None"
            
            ip.save()
            data.wlan_ip_address = "Offline"
       
        elif(request.POST['wlan_ip_address'] == "Release"):
            ip = IP.objects.get(ip_address=request.POST['wlan_ip_address'])
            ip.status = "Not-inuse"
            ip.ip_assisgned ="None"

            ip.save()
            data.wlan_ip_address = request.POST['wlan_ip_address']
        elif( (data.lan_ip_address == "Offline") and (request.POST['wlan_ip_address'] != "Offline")):
            data.wlan_ip_address = request.POST['wlan_ip_address']

            ip = IP.objects.get(ip_address=request.POST['wlan_ip_address'])
            ip.status = "In-use"
            ip.ip_assisgned =data.computer_id

            ip.save()
        elif( (data.wlan_ip_address == "Release") and (data.pccurrentstatus !="Pending Dispose") and (data.pccurrentstatus !="Dispose") ):
           
            data.wlan_ip_address = request.POST['wlan_ip_address']
            ip = IP.objects.get(ip_address=request.POST['wlan_ip_address'])
            ip.status = "In-use"
            ip.ip_assisgned =data.computer_id

            ip.save()
        elif ( data.wlan_ip_address != request.POST['wlan_ip_address']):
            Previous_IP = data.wlan_ip_address
            if Previous_IP == "Offline":
                ip = IP.objects.get(ip_address=request.POST['wlan_ip_address'])
                ip.status = "In-use"
                ip.ip_assisgned =data.computer_id
                data.wlan_ip_address = request.POST['wlan_ip_address']
            else:
                    
                data.wlan_ip_address = request.POST['wlan_ip_address']
                ip = IP.objects.get(ip_address=request.POST['wlan_ip_address'])
                ip.status = "In-use"
                ip.ip_assisgned =data.computer_id

                ip.save()
                Change_IP_status = IP.objects.get(ip_address= Previous_IP)
                Change_IP_status.status = "Not-inuse"
                Change_IP_status.ip_assisgned ="None"

                Change_IP_status.save()
        
        data.joined_domain = request.POST['Joined_Domain']
        data.connection_type = request.POST['ConnectionType']
        data.pccurrentstatus = request.POST['Computer_Status']
     
       

       
        data.save()
        log_history = loghistory()
        log_history.Time = datetime.now()
        log_history.Username = format(request.session.get('name'))
        log_history.Activity = "Update A Laptop By ID " + request.POST['Computer_ID']
        log_history.save()
      
        arraydataQR = [ request.POST['Computer_ID'], request.POST['serial_number'], request.POST['Brand'], request.POST['model'] ]
        type_create = "Update"
        create_qrcodeLaptop(arraydataQR, type_create)
           



        return HttpResponse('hai')  

def getlaptopdataupdate(request):
    if request.method == "POST":
       id = request.POST["id"]
       computerdata = Laptop.objects.filter(computer_id = id).get()
       ip = IP.objects.filter(status = 'Not-inuse' )
       data = {
           "pic": computerdata.pic, "previous_pic": computerdata.previous_pic, "computer_id": computerdata.computer_id,
            "current_computer_id": computerdata.current_computer_id, "Brand": computerdata.Brand, "Model": computerdata.Model,
             "serial_number": computerdata.serial_number, "asset_no": computerdata.asset_no, "vendor": computerdata.vendor,
              "processor_type": computerdata.processor_type, "ram_type": computerdata.ram_type,
               "ram_slot": computerdata.ram_slot, "total_ram": computerdata.total_ram, "storage_type": computerdata.storage_type,
                "storage_space": computerdata.storage_space, "dop": computerdata.dop, "dop_Warranty_end_date": computerdata.dop_Warranty_end_date,
                 "po": computerdata.po, "invoice": computerdata.invoice, "block": computerdata.block,
                  "location": computerdata.location, "standard_installation": computerdata.standard_installation, "microsoft_office": computerdata.microsoft_office,
                   "microsoft_office_keys": computerdata.microsoft_office_keys, "windows": computerdata.windows, "lan_mac_address": computerdata.lan_mac_address,
                    "lan_ip_address": computerdata.lan_ip_address, "wlan_mac_address": computerdata.wlan_mac_address, "wlan_ip_address": computerdata.wlan_ip_address,
                    "joined_domain": computerdata.joined_domain, "connection_type": computerdata.connection_type, "pccurrentstatus": computerdata.pccurrentstatus,
                    "ip": list(ip.values()),   'usbunlock': computerdata.usbunlock, 'cdunlock': computerdata.cdunlock, 'type_of_purchase' : computerdata.type_of_purchase
                  

                     }
        
       return JsonResponse(data)

def getlaptopdata(request):
    computerdata = Laptop.objects.all()

    return JsonResponse({"data":list(computerdata.values())})

def GetQRLaptopData(request):
    if request.method == "POST":
        if request.POST["type"] == "All":
            computerdata = Laptop.objects.all()
            return JsonResponse({"data":list(computerdata.values())})

        elif request.POST["type"] == "Custom":
            data1 = int(request.POST["data1"])
            data2 = int(request.POST["data2"])
        
            arraydata = []
            while data1 <= data2:
                if data1 <= 268:
                    if data1 < 10:
                        data = "UTM-NB00"+ str(data1)
                    elif ((data1 >= 10) and (data1 < 100)):
                        data= "UTM-NB0"+ str(data1)
                    elif ((data1 >= 100) and (data1 < 1000)):
                        data= "UTM-NB"+ str(data1)
                    elif ((data1 >= 1000) and (data1 < 10000)):
                        data= "UTM-NB"+ str(data1)
                    data1 = data1 + 1
                    arraydata.append(data)
                else:
                    if data1 < 10:
                        data = "UTM-NB000"+ str(data1)
                    elif ((data1 >= 10) and (data1 < 100)):
                        data= "UTM-NB00"+ str(data1)
                    elif ((data1 >= 100) and (data1 < 1000)):
                        data= "UTM-NB0"+ str(data1)
                    elif ((data1 >= 1000) and (data1 < 10000)):
                        data= "UTM-NB"+ str(data1)
                    data1 = data1 + 1
                    arraydata.append(data)

      


            
            computerdata = Laptop.objects.filter(computer_id__in=arraydata)
            return JsonResponse({"data":list(computerdata.values())})

def searchLaptopdata(request):
    data = request.POST['data']
    if Laptop.objects.filter(computer_id__icontains=data).exists():
        data1 = Laptop.objects.filter(computer_id__icontains=data)
        return JsonResponse({"data":list(data1.values())})
    elif Laptop.objects.filter(lan_ip_address__icontains=data).exists():
        data1 = Laptop.objects.filter(lan_ip_address__icontains=data)
    elif Laptop.objects.filter(current_computer_id__icontains=data).exists():
        data1 = Laptop.objects.filter(current_computer_id__icontains=data)
        return JsonResponse({"data":list(data1.values())})
    elif Laptop.objects.filter(wlan_ip_address__icontains=data).exists():
        data1 = Laptop.objects.filter(wlan_ip_address__icontains=data)
        return JsonResponse({"data":list(data1.values())})
    else:
       return HttpResponse('')
   


#Network  Hardware Page
def Networkhardwarepage(request):
    data_location = NetworkAsset_location.objects.all()
    data_block = NetworkAsset_block.objects.all()
    data_vendor = NetworkAsset_vendor.objects.all()
    data_brand = NetworkAsset_brand.objects.all()
    username =  format(request.session.get('name'))
    if (format(request.session.get('name')) == "staff"):
        style = format(request.session.get('styledivstaff'))
    else:
        style = format(request.session.get('styledivNotstaff'))
    context = {'vendor': data_vendor, 'brand': data_brand, 'location': data_location, 'block': data_block, 'Username':username, "Style" : style}

    return render(request, 'Network Hardware Page.html', context)

def runNetworkform(request):
    if request.method == "POST":
       id = request.POST["type"]
       model = request.POST["modeltype"]
       computerdata = Asset_running_number.objects.filter(asset_type = id).get()
       model = NetworkHardwareModel.objects.filter(asset_type = model)
       data = { 'runnumber' : computerdata.running_number, "model" : list(model.values()) }
       return JsonResponse(data)

def Networkhardwareadd(request):
    if request.method == "POST":
       
        runing_number = Asset_running_number.objects.filter(asset_type=request.POST['Network_Hardware_Type']).get()
        data = NetworkHardware()
        data.hardware_id = request.POST['Network_Hardware_ID']
        data.hardware_type = request.POST['Network_Hardware_Type']
        data.Brand = request.POST['Brand']
        data.Model = request.POST['Model']
        data.serial_number = request.POST['serial_number']
        data.asset_no = request.POST['Asset_No']
        data.dop = request.POST['dop']
        data.dop_Warranty_end_date = request.POST['dopYear']
        data.vendor = request.POST['Vendor']
        data.mac_address = request.POST['MAC_Address']
        data.ip_address = request.POST['IP_Address']
        data.block = request.POST['block']
        data.location = request.POST['location']
        data.po = request.POST['PO']
        data.invoice = request.POST['Invoice']
        data.Current_Status = request.POST['networkstatus']
        if request.POST['IP_Address'] == "Offline":
             if not NetworkHardware.objects.filter(hardware_id=request.POST['Network_Hardware_ID']).exists():
                data.save()
                num = int(runing_number.running_number)+1
                updatenum = Asset_running_number.objects.get(asset_type=request.POST['Network_Hardware_Type'])
                updatenum.running_number = num
                updatenum.save()
                log_history = loghistory()
                log_history.Time = datetime.now()
                log_history.Username = format(request.session.get('name'))
                log_history.Activity = "Add A Network Hardware By Type  " + request.POST['Network_Hardware_Type'] + " and By ID " + request.POST['Network_Hardware_ID']
                log_history.save()
                return HttpResponse('hai')

        else:
             if not NetworkHardware.objects.filter(hardware_id=request.POST['Network_Hardware_ID']).exists():
                data.save()
                num = int(runing_number.running_number)+1
                updatenum = Asset_running_number.objects.get(asset_type=request.POST['Network_Hardware_Type'])
                updatenum.running_number = num
                updatenum.save()
                ip1 = IP.objects.get(ip_address=request.POST['IP_Address'])
                ip1.status = "In-use"
                ip1.save()
                log_history = loghistory()
                log_history.Time = datetime.now()
                log_history.Username = format(request.session.get('name'))
                log_history.Activity = "Add A Network Hardware By Type  " + request.POST['Network_Hardware_Type'] + " and By ID " + request.POST['Network_Hardware_ID']
                log_history.save() 



                return HttpResponse('hai')



        
        computerdata = Laptop.objects.filter(computer_id__in=arraydata)
        return JsonResponse({"data":list(computerdata.values())})

def exporthardwaredataNetwork(request):
   
     
        if request.POST["type"] == 'all':

            computerdata = NetworkHardware.objects.all()
            data = []
            for key in computerdata:
                arraydata = [key.hardware_id, key.hardware_type, key.Brand, key.Model, key.serial_number,
                key.asset_no, key.dop,key.dop_Warranty_end_date,key.vendor,key.po,key.invoice,key.block,key.location, 
                key.mac_address, key.ip_address, key.Current_Status]
                data.append(arraydata)
        
            
            return JsonResponse({"data":data})
        if request.POST["type"] == 'custom':
            data1 = request.POST["datafinal1"]
        
        
         
            computerdata = NetworkHardware.objects.filter(hardware_type=data1)
            data = []
            for key in computerdata:
               arraydata = [key.hardware_id, key.hardware_type, key.Brand, key.Model, key.serial_number,
                key.asset_no, key.dop,key.dop_Warranty_end_date,key.vendor,key.po,key.invoice,key.block,key.location, 
                key.mac_address, key.ip_address, key.Current_Status]
               data.append(arraydata)
        
            
            return JsonResponse({"data":data})

def getcustomhardwaredata(request):
    if request.method == "POST":
        data1 = request.POST["HardwareType"]
    
        computerdata = NetworkHardware.objects.filter(hardware_type=data1)
        return JsonResponse({"data":list(computerdata.values())})

def getNetworkdata(request):
    computerdata = NetworkHardware.objects.all()
    ip = IP.objects.filter(status = 'Not-inuse' )

    return JsonResponse({"data":list(computerdata.values()), "ip":list(ip.values())})

def getNetworkdataupdate(request):
    if request.method == "POST":
       id = request.POST["id"]
       dataentry = NetworkHardware.objects.filter(hardware_id = id).get()
       if (dataentry.hardware_type == "CCTV"):
            model = NetworkHardwareModel.objects.filter(asset_type = "CCTV Camera")
         
       elif(dataentry.hardware_type == "CCTV_DVR"):
           model = NetworkHardwareModel.objects.filter(asset_type = "CCTV DVR")
        

       else:
            model = NetworkHardwareModel.objects.filter(asset_type = dataentry.hardware_type)
       ip = IP.objects.filter(status = 'Not-inuse' )
       data = {
         	'hardware_id' : dataentry.hardware_id, 'hardware_type' : dataentry.hardware_type, 
				'serial_number' : dataentry.serial_number, 'asset_no' : dataentry.asset_no, 'block' : dataentry.block,
				'location' : dataentry.location, 'dop' : dataentry.dop, 'dop_Warranty_end_date' : dataentry.dop_Warranty_end_date,
				'brand' : dataentry.Brand, 'Model' : dataentry.Model,
				'vendor' : dataentry.vendor, 'po' : dataentry.po, 'mac_address' : dataentry.mac_address,
				'invoice' : dataentry.invoice, 'ip_address' : dataentry.ip_address, "Current_Status":dataentry.Current_Status,
                "list_model" : list(model.values()),  "ip" : list(ip.values())
                  

                     }
        
       return JsonResponse(data)

def Networkhardwareupdate(request):
    if request.method == "POST":
       
       
        data =  NetworkHardware.objects.filter(hardware_id = request.POST['Network_Hardware_ID']).get()
        data.hardware_id = request.POST['Network_Hardware_ID']
        data.hardware_type = request.POST['Network_Hardware_Type']
        data.Brand = request.POST['Brand']
        data.Model = request.POST['Model']
        data.serial_number = request.POST['serial_number']
        data.asset_no = request.POST['Asset_No']
        data.dop = request.POST['dop']
        data.dop_Warranty_end_date = request.POST['dopYear']
        data.vendor = request.POST['Vendor']
        data.mac_address = request.POST['MAC_Address']
       
        data.block = request.POST['block']
        data.location = request.POST['location']
        data.po = request.POST['PO']
        data.invoice = request.POST['Invoice']
        data.Current_Status = request.POST['networkstatus']
        
        if(request.POST['IP_Address'] == "Release"):
            Previous_IP = data.ip_address
            
            if IP.objects.filter(ip_address=Previous_IP).exists():
                ip = IP.objects.get(ip_address=Previous_IP)
                ip.status = "Not-inuse"
                ip.ip_assisgned = "None"
                ip.save()
                data.ip_address = request.POST['IP_Address']
            else:
                 data.ip_address = request.POST['IP_Address']
        elif(request.POST['IP_Address'] == "Offline"):
            data.ip_address = request.POST['IP_Address']
        elif( (data.ip_address == "Release") and (data.Current_Status !="Pending Dispose") and (data.Current_Status !="Dispose") ):
           
            data.ip_address = request.POST['IP_Address']
            ip = IP.objects.get(ip_address=request.POST['IP_Address'])
            ip.status = "In-use"
            ip.ip_assisgned = data.hardware_id 

            ip.save()
        elif( (data.ip_address == "Offline") and (data.Current_Status !="Pending Dispose") and (data.Current_Status !="Dispose") ):
           
            data.ip_address = request.POST['IP_Address']
            ip = IP.objects.get(ip_address=request.POST['IP_Address'])
            ip.status = "In-use"
            ip.ip_assisgned = data.hardware_id 

            ip.save()
        elif( data.ip_address != request.POST['IP_Address']):
            Previous_IP = data.ip_address
            data.ip_address = request.POST['IP_Address']
            ip = IP.objects.get(ip_address=request.POST['IP_Address'])
            ip.status = "In-use"
            ip.ip_assisgned = data.hardware_id 

            ip.save()
            Change_IP_status = IP.objects.get(ip_address= Previous_IP)
            Change_IP_status.status = "Not-inuse"
            Change_IP_status.ip_assisgned = "None"

            Change_IP_status.save()
        else :
            data.ip_address = request.POST['IP_Address']
        
      
        data.save()
        log_history = loghistory()
        log_history.Time = datetime.now()
        log_history.Username = format(request.session.get('name'))
        log_history.Activity = "Update A Network Hardware By Type  " + request.POST['Network_Hardware_Type'] + " and By ID " + request.POST['Network_Hardware_ID']
        log_history.save() 
           



        return HttpResponse('hai')




# User Page
def userdetail(request):
  
    data_location = NetworkAsset_location.objects.all()
    data_block = NetworkAsset_block.objects.all()
    username =  format(request.session.get('name'))
    if (format(request.session.get('role')) == "staff"):
        style = format(request.session.get('styledivstaff'))
    else:
        style = format(request.session.get('styledivNotstaff'))
    context = {'location': data_location, 'block': data_block, 'Username':username,"Style" : style}
    return render(request, 'User Page.html', context)

def getUserdata(request):
    computerdata = UserAsset.objects.all()
    return JsonResponse({"data":list(computerdata.values())})

def AddAssetUser(request):
    if request.method == "POST":
        data = UserAsset()
        data.employee_number = request.POST['employee_number']
        data.name = request.POST['name']
        data.email = request.POST['email']
        data.designation = request.POST['designation']
        data.block = request.POST['block']
        data.location = request.POST['location']
        data.department = request.POST['department']
       
        data.vpn = request.POST['vpn']
        data.vpnaccount = request.POST['vpnaccount']
       
        if not UserAsset.objects.filter(employee_number=request.POST['employee_number']).exists():
            data.save()
            log_history = loghistory()
            log_history.Time = datetime.now()
            log_history.Username = format(request.session.get('name'))
            log_history.Activity = "Add A Asset User By Employee Number :   " + request.POST['employee_number']
            log_history.save() 
            return HttpResponse('hai')

def typeofsoftware(request):
    type = request.POST['type']
    data = NetworkHardware.objects.filter(software_type=type)
    return JsonResponse({"data":list(data.values())})

def searchUserinput(request):
    if (request.POST['Type'] == "PC"):
        id = request.POST['User_ID']
        data = Computer.objects.filter(computer_id__icontains=id, pccurrentstatus = "Loan")
        return JsonResponse({"data":list(data.values())})
    if (request.POST['Type'] == "Laptop"):
        id = request.POST['User_ID']
        data = Laptop.objects.filter(computer_id__icontains=id, pccurrentstatus = "Loan")
        return JsonResponse({"data":list(data.values())})
    if (request.POST['Type'] == "Employee"):
        id = request.POST['User_ID']
        data = UserAsset.objects.filter(employee_number__icontains=id)
        return JsonResponse({"data":list(data.values())})

    if (request.POST['Type'] == "AP"):
        id = request.POST['User_ID']
        data = NetworkHardware.objects.filter(hardware_id__icontains=id , hardware_type__icontains = request.POST['Type'], Current_Status = "Loan")
        return JsonResponse({"data":list(data.values())})
    if (request.POST['Type'] == "CCTV"):
        id = request.POST['User_ID']
        data = NetworkHardware.objects.filter(hardware_id__icontains=id , hardware_type__icontains = request.POST['Type'], Current_Status ="Loan")
        return JsonResponse({"data":list(data.values())})
    if (request.POST['Type'] == "CCTV_DVR"):
        id = request.POST['User_ID']
        data = NetworkHardware.objects.filter(hardware_id__icontains=id , hardware_type__icontains = request.POST['Type'], Current_Status ="Loan")
        return JsonResponse({"data":list(data.values())})
    if (request.POST['Type'] == "CP"):
        id = request.POST['User_ID']
        data = NetworkHardware.objects.filter(hardware_id__icontains=id , hardware_type__icontains = request.POST['Type'], Current_Status ="Loan")
        return JsonResponse({"data":list(data.values())})
    if (request.POST['Type'] == "Door_Access"):
        id = request.POST['User_ID']
        data = NetworkHardware.objects.filter(hardware_id__icontains=id , hardware_type__icontains = request.POST['Type'], Current_Status ="Loan")
        return JsonResponse({"data":list(data.values())})
    if (request.POST['Type'] == "Switches"):
        id = request.POST['User_ID']
        data = NetworkHardware.objects.filter(hardware_id__icontains=id , hardware_type__icontains = request.POST['Type'], Current_Status ="Loan")
        return JsonResponse({"data":list(data.values())})
    if (request.POST['Type'] == "Tape_Library"):
        id = request.POST['User_ID']
        data = NetworkHardware.objects.filter(hardware_id__icontains=id , hardware_type__icontains = request.POST['Type'], Current_Status ="Loan")
        return JsonResponse({"data":list(data.values())})
    if (request.POST['Type'] == "Wireless_Dongle"):
        id = request.POST['User_ID']
        data = NetworkHardware.objects.filter(hardware_id__icontains=id , hardware_type__icontains = request.POST['Type'], Current_Status ="Loan")
    if (request.POST['Type'] == "UPS"):
        id = request.POST['User_ID']
        data = NetworkHardware.objects.filter(hardware_id__icontains=id , hardware_type__icontains = request.POST['Type'], Current_Status ="Loan")
        return JsonResponse({"data":list(data.values())})
    if (request.POST['Type'] == "Firewall"):
        id = request.POST['User_ID']
        data = NetworkHardware.objects.filter(hardware_id__icontains=id , hardware_type__icontains = request.POST['Type'], Current_Status = "Loan")
        return JsonResponse({"data":list(data.values())})    
    return HttpResponse('hai')

def updateformuser(request):
    if request.method == "POST":
        data = UserAsset.objects.filter(employee_number= request.POST['employee_number']).get()
        data.employee_number = request.POST['employee_number']
        data.name = request.POST['name']
        data.email = request.POST['email']
        data.designation = request.POST['designation']
        data.block = request.POST['block']
        data.location = request.POST['location']
        data.department = request.POST['department']
        data.vpn = request.POST['vpn']
        data.vpnaccount = request.POST['vpnaccount']

       
      
        data.save()
        log_history = loghistory()
        log_history.Time = datetime.now()
        log_history.Username = format(request.session.get('name'))
        log_history.Activity = "Update A Asset User By Employee Number :   " + request.POST['employee_number']
        log_history.save() 
        return HttpResponse('hai')




# Loan Page
def loandetail(request):
    username =  format(request.session.get('name'))
    if (format(request.session.get('role')) == "staff"):
        style = format(request.session.get('styledivstaff'))
    else:
        style = format(request.session.get('styledivNotstaff'))
    context ={
        "Username": username,"Style" : style
    }
    loan_status_state()
    return render(request, 'Loan Page.html', context)

def openloandataform(request):
     data_update = Asset_running_number.objects.filter(asset_type='Loan').get()
     data = {"running_number" : data_update.running_number }
     return JsonResponse(data)   

def loan_status_state():
    data = Loan.objects.all()
    listdata =list(data.values())
    for y in listdata:
        now = datetime.now()
        date = now.strftime("%Y-%m-%d")
        id = y['id']
        dateendLoan = y['date_end']
        status = y['status']
        current_date = datetime.strptime(date, '%Y-%m-%d')
        date_endLoan = datetime.strptime(dateendLoan, '%Y-%m-%d')
      

        if(current_date < date_endLoan):
            data_update = Loan.objects.filter(pk=id).get()
            data_update.status = "In-Use"
            data_update.save()
        else:
            data_update = Loan.objects.filter(pk=id).get()
            data_update.status = "Overdue"
            data_update.save()

def loandata(request):
    data = Loan.objects.all()
    loan_status_state()
    return JsonResponse({"data":list(data.values())})

def addLoanform(request):
    if request.method == "POST":
       
        data = Loan()
        data.loan_id = request.POST['loan_id']
        data.employee_number = request.POST['employee_number']
        data.asset_id = request.POST['asset_id']
        data.email = request.POST['email']
        data.designation = request.POST['designation']
        data.department = request.POST['department']
        data.date_start = request.POST['date_start']
        data.date_end = request.POST['date_end']
        data.status = request.POST['status']
        if not Loan.objects.filter(loan_id=request.POST['loan_id']).exists():
            data.save()
            data_update = Asset_running_number.objects.filter(asset_type='Loan').get()
            current_run = data_update.running_number
            data_update.running_number = int(current_run) + 1
            data_update.save()
           
            

            log_history = loghistory()
            log_history.Time = datetime.now()
            log_history.Username = format(request.session.get('name'))
            log_history.Activity = "Add a Loan with loan ID : "+ request.POST['loan_id'] +"for Employee Number :   " + request.POST['employee_number'] + " to loan a IT asset by ID : " + request.POST['asset_id']
            log_history.save() 
            id = request.POST['asset_id']
            if(id.find("UTM-PC")!=-1):
                computerdata = Computer.objects.filter(computer_id=id).get()
                computerdata.pccurrentstatus = "In-use"
                computerdata.save()
            elif(id.find("UTM-NB")!=-1):
                computerdata = Laptop.objects.filter(computer_id=id).get()
                computerdata.pccurrentstatus = "In-use"
                computerdata.save()
            elif(id.find("UTM-AP")!=-1) or (id.find("UTM-CM")!=-1)  or (id.find("CCTV")!=-1) or (id.find("UTM-CP")!=-1) or (id.find("DoorController")!=-1) or (id.find("UTM-NW")!=-1) or (id.find("UTM-TL")!=-1) or (id.find("Tenda Wireless")!=-1) or (id.find("UPS")!=-1) or (id.find("UTM-FW")!=-1): 
                computerdata = NetworkHardware.objects.filter(computer_id=id).get()
                computerdata.Current_Status = "In-use"
                computerdata.save()


            return HttpResponse('hai')

def Loandataupdate(request):
    if request.method == "POST":
       id = request.POST["id"]
       data = Loan.objects.filter(pk=id).get()
      
       data = {
'employee_number' : data.employee_number, 'asset_id' : data.asset_id, 'email' : data.email,
				'designation' : data.designation, 'department' : data.department, 'date_start' : data.date_start, 'date_end' :  data.date_end,
				'status' : data.status, 'id' : data.id, 'loan_id': data.loan_id

                     }
        
       return JsonResponse(data)

def updateformLoan(request):
    if request.method == "POST":
       
        
        data = Loan.objects.filter(loan_id= request.POST['id']).get()
        data.employee_number = request.POST['employee_number']
        data.asset_id = request.POST['asset_id']
        data.email = request.POST['email']
        data.designation = request.POST['designation']
        data.department = request.POST['department']
        data.date_start = request.POST['date_start']
        data.date_end = request.POST['date_end']
        data.status = request.POST['status']
        data.save()
        log_history = loghistory()
        log_history.Time = datetime.now()
        log_history.Username = format(request.session.get('name'))
        log_history.Activity = "Update a Loan for Employee Number :   " + request.POST['employee_number'] + " to loan a IT asset by ID : " + request.POST['asset_id']
        log_history.save()
           



        return HttpResponse('hai')  

def typeofsoftware(request):
    if request.method == "POST":
       data = Software.objects.filter(software_type= request.POST['type']) 
           
    data = {
        'software_name' : list(data.values())
    }
    return JsonResponse(data)
    
def versionsoftware(request):
    if request.method == "POST":
       data = Software.objects.filter(Software_name= request.POST['type']) 
           
    data = {
        'version' : list(data.values())
    }
    return JsonResponse(data)

def getUserdataupdate(request):
    if request.method == "POST":
       id = request.POST["id"]
       data = UserAsset.objects.filter(pk=id).get()
       data = {
           'employee_number' : data.employee_number, 'name' : data.name, 'email' :  data.email,
			'designation' : data.designation, 'department' :data.department,'block' : data.block, 
            'location' :data.location, 'vpn' :data.vpn,
            'vpnaccount' :data.vpnaccount,

                     }
        
       return JsonResponse(data) 

def deleteuser(request):
    if request.method == "POST":
       id = request.POST["id"]
       data = UserAsset.objects.filter(pk=id).get()
       log_history = loghistory()
       log_history.Time = datetime.now()
       log_history.Username = format(request.session.get('name'))
       log_history.Activity = "Delete a Loan for Employee Number :   " + data.employee_number 
       log_history.save()
       data.delete()
      
       return HttpResponse('hai')  





# IP Page
def ipdetail(request):
    username =  format(request.session.get('name'))
    if (format(request.session.get('role')) == "staff"):
        style = format(request.session.get('styledivstaff'))
    else:
        style = format(request.session.get('styledivNotstaff'))
   
    context ={
        "Username": username, "Style" : style
    }
    return render(request, 'IP Page.html', context)

def addipform(request):
    if request.method == "POST":
       
        data = IP()
        data.ip_address = request.POST['IP_address']
        data.ip_assisgned = request.POST['Computer_assign']
        data.status = request.POST['Status']
        data.remark = request.POST['Remark']
        if not IP.objects.filter(ip_address=request.POST['IP_address']).exists():
            data.save()
            log_history = loghistory()
            log_history.Time = datetime.now()
            log_history.Username = format(request.session.get('name'))
            log_history.Activity = "Add a IP by the address :   " + request.POST['IP_address']
            log_history.save()
            return HttpResponse('hai')

def updateformip(request):
    if request.method == "POST":
       
        
        data = IP.objects.filter(pk= request.POST['id']).get()
        data.ip_address = request.POST['IP_address']
        data.ip_assisgned = request.POST['Computer_assign']
        data.status = request.POST['Status']
        data.remark = request.POST['Remark']
        data.save()
        log_history = loghistory()
        log_history.Time = datetime.now()
        log_history.Username = format(request.session.get('name'))
        log_history.Activity = "Update a IP by the address :   " + request.POST['IP_address']
        log_history.save()  



        return HttpResponse('hai')   

def getipupdate(request):
    if request.method == "POST":
       id = request.POST["id"]
       print(id)
       data = IP.objects.filter(pk=id).get()
 
       data = {
           'IP_address' : data.ip_address, 'Computer_assign' : data.ip_assisgned, 'Status' :  data.status,
			'Remark' : data.remark, 'id' :id,

                     }
        
       return JsonResponse(data)

def getipdata(request):
    data = IP.objects.all()
    return JsonResponse({"data":list(data.values())})

def exportIPdataNetwork(request):
   
     
        if request.POST["type"] == 'all':

            computerdata = IP.objects.all()
            data = []
            for key in computerdata:
                arraydata = [key.ip_address, key.ip_assisgned, key.status, key.remark]
                data.append(arraydata)
        
            
            return JsonResponse({"data":data})
        if request.POST["type"] == 'custom':
            data1 = request.POST["IPStatus"]
        
        
         
            computerdata = IP.objects.filter(status=data1)
            data = []
            for key in computerdata:
               arraydata =[key.ip_address, key.ip_assisgned, key.status, key.remark]
               data.append(arraydata)
        
            
            return JsonResponse({"data":data})

def getcustomIPdata(request):
    if request.method == "POST":
        data1 = request.POST["IPStatus"]
    
        computerdata = IP.objects.filter(status=data1)
        return JsonResponse({"data":list(computerdata.values())})
  
            
     




# login function
def login_user(request):
    if request.method == "POST":
        username_login = request.POST['username']
        password_login = request.POST['password']
        user = authenticate(request, username=username_login, password=password_login)
        if user is not None:
            login(request, user)
            request.session['name'] = username_login
            if request.user.is_staff:
                request.session['role'] = 'staff'
                request.session['styledivstaff'] = "display:block"
            else:
                request.session['role'] = 'Not staff'
                request.session['styledivNotstaff'] = "display:none"

            


            return redirect("dashboard", )
       
      
        else:
            messages.success(request, ("There was an Error Logging in, Try Again"))
            return redirect("login")

    return render(request, "login.html", {})
            
     




#software page
def software(request):
    username =  format(request.session.get('name'))
    
    if (format(request.session.get('role')) == "staff"):
        style = format(request.session.get('styledivstaff'))
    else:
        style = format(request.session.get('styledivNotstaff'))

   
    context ={
        "Username": username,
        "Style" : style
    }
    return render(request, 'software page.html', context)

def software_listing(request):
     if request.method == "POST":
        data = Software.objects.filter(software_type = request.POST['software_type'])  
        return JsonResponse({"data":list(data.values())})
   
def getsoftwaredata(request):
    data = softwareUser.objects.all()
    softwarename =  Software.objects.all()
    return JsonResponse({"data":list(data.values()), "softwarename":list(softwarename.values())})

def softwareVersion_listing(request):
     if request.method == "POST":
        data = Software.objects.filter(Software_name = request.POST['Software_Name'])  
        return JsonResponse({"data":list(data.values())}) 

def addUserSoftwareform(request):
    if request.method == "POST":
       
        data = softwareUser()
        data.Software_Type = request.POST['Software_Type']
        data.Software_Name = request.POST['Software_Name']
        data.User_Type = request.POST['User_Type']
        data.User_ID = request.POST['User_ID']
        data.Software_Version = request.POST['Software_Version']
        if not softwareUser.objects.filter(Software_Name=request.POST['Software_Name'], User_ID = request.POST['User_ID']).exists():
            data.save()
            log_history = loghistory()
            log_history.Time = datetime.now()
            log_history.Username = format(request.session.get('name'))
            log_history.Activity = "Add a Software User by user ID  :   " + request.POST['User_ID'] + " Using a software type : " + request.POST['Software_Type'] + " and software name :  " + request.POST['Software_Name']
            log_history.save()
            return HttpResponse('hai')  
        else:
            return HttpResponse('hai')  
            
def exportsoftwaredataNetwork(request):
   
     
        if request.POST["type"] == 'all':

            computerdata = softwareUser.objects.all()
            data = []
            for key in computerdata:
                arraydata = [key.Software_Type, key.User_Type, key.Software_Name, key.User_ID, key.Software_Version]
                data.append(arraydata)
        
            
            return JsonResponse({"data":data})
        if request.POST["type"] == 'custom':
            data1 = request.POST["SoftwareName"]
        
        
         
            computerdata = softwareUser.objects.filter(Software_Name=data1)
            data = []
            for key in computerdata:
               arraydata =[key.Software_Type, key.User_Type, key.Software_Name, key.User_ID, key.Software_Version]
               data.append(arraydata)
        
            
            return JsonResponse({"data":data})

def getcustomsoftwaredata(request):
    if request.method == "POST":
        data1 = request.POST["SoftwareName"]
       
        computerdata = softwareUser.objects.filter(Software_Name=data1)
       
        return JsonResponse({"data":list(computerdata.values())})

def getSoftUserdataupdate(request):
    if request.method == "POST":
        id = request.POST['id']  
        data = softwareUser.objects.filter(pk=id).get()
        listsoftware = Software.objects.filter(software_type = data.Software_Type)  
        versionsoftware = Software.objects.filter(Software_name = data.Software_Name)  
       
        return JsonResponse( {
            'Software_Type':data.Software_Type, 'User_Type':data.User_Type, 'Software_Name':data.Software_Name,
            'User_ID':data.User_ID, 'Software_Version':data.Software_Version, 'id' :id, "listsoftware":list(listsoftware.values()), "versionsoftware":list(versionsoftware.values()) 
        }) 

def updateformsoftwareUser(request):
    if request.method == "POST":
       
        id = request.POST['id']
        data = softwareUser.objects.filter(pk=id).get()
        data.Software_Type = request.POST['Software_Type']
        data.Software_Name = request.POST['Software_Name']
        data.User_Type = request.POST['User_Type']
        data.User_ID = request.POST['User_ID']
        data.Software_Version = request.POST['Software_Version']

       
        data.save()
        log_history = loghistory()
        log_history.Time = datetime.now()
        log_history.Username = format(request.session.get('name'))
        log_history.Activity = "Update a Software User by user ID  :   " + request.POST['User_ID'] + " Using a software type : " + request.POST['Software_Type'] + " and software name :  " + request.POST['Software_Name']
        log_history.save() 
        return HttpResponse('hai')

def deleteSoftwareUser(request):
    if request.method == "POST":
       
        id = request.POST['id']
        data = softwareUser.objects.filter(pk=id).get()
        log_history = loghistory()
        log_history.Time = datetime.now()
        log_history.Username = format(request.session.get('name'))
        log_history.Activity = "Delete a Software User by user ID  :   " + data.User_ID + " Using a software type : " + data.Software_Type + " and software name :  " + data.Software_Name
        log_history.save()
        data.delete()
       
        return HttpResponse('hai')






#history log
def historypage(request):
    username =  format(request.session.get('name'))
     
    if (format(request.session.get('role')) == "staff"):
        style = format(request.session.get('styledivstaff'))
    else:
        style = format(request.session.get('styledivNotstaff'))
   
    context ={
        "Username": username, "Style" : style
    }
    return render(request, 'log history page.html', context)

def getloghistory(request):
    username =  format(request.session.get('name'))
    log_history = loghistory.objects.filter(Username=username)
    return JsonResponse({"data":list(log_history.values())})




# logout function
def logoutsystem(request):
    del request.session['name']
    if (format(request.session.get('role')) == "staff"):
        del request.session['styledivstaff']
    else:
        del request.session['styledivNotstaff']
    del request.session['role']
    
    


    logout(request)

    return redirect("/")
 

# def startupcreateQR():
#     dirctory = Path(__file__).resolve().parent.parent
#     mediaroot = os.path.join(dirctory, 'media/')
#     mediarootpc = os.path.join(mediaroot, 'Laptop/')
#     data1 = Laptop.objects.all()
#     arraydata  = []
#     datax = list(data1.values())
#     print(type(datax))
#     for x in datax:
#         print(x)
#         arrayx = [ x['computer_id'], x['serial_number'], x['Brand'],x['Model']]
       
#         pngexits = exists(mediarootpc + arrayx[0] + ".png")
#         stringdata = "ID :  " + arrayx[0] + "\n S/N :"+  arrayx[1]  +" \nBrand :"+  arrayx[2] +" \nModel : "+  arrayx[3]
        
#         if (pngexits == False):
                
#                     url = pyqrcode.create(stringdata)
#                     url.png(mediarootpc + arrayx[0]+".png", scale =2)
                    
#         else:
#             pass
            
        
    

# QR PC code function
def create_qrcodePC(data, type_create):
   
    dirctory = Path(__file__).resolve().parent.parent
    mediaroot = os.path.join(dirctory, 'media/')
    mediarootpc = os.path.join(mediaroot, 'pc/')
    pngexits = exists(mediarootpc + data[0] + ".png")
    if (type_create == "Update"):
      
        stringdata = "ID :  " + data[0] + "\n S/N :"+  data[1]  +" \nBrand :"+  data[2] +" \nModel : "+  data[3]
        url = pyqrcode.create(stringdata)
        url.png(mediarootpc+ data[0]+".png", scale =2)
        stringdata = mediarootpc+ data[0]+".png"
        dataindex = data[0]
        type_Upload = "Update"
        

        upload_PCQR(dataindex ,stringdata, type_Upload)
    else:
        stringdata = "ID :  " + data[0] + "\n S/N :"+  data[1]  +" \nBrand :"+  data[2] +" \nModel : "+  data[3]
        if (pngexits == False):
               
                url = pyqrcode.create(stringdata)
                url.png(mediarootpc + data[0]+".png", scale =2)
                
        else:
                pass
        stringdata = data[0]+".png"
        dataindex = data[0]
        type_Upload = "Create"
        upload_PCQR(dataindex ,stringdata, type_Upload)

# QR Laptop code function
def create_qrcodeLaptop(data, type_create):
   
    
    dirctory = Path(__file__).resolve().parent.parent

    mediaroot = os.path.join(dirctory, 'media/')
    mediarootLaptop = os.path.join(mediaroot, 'Laptop/')
    index_data =  data[0] + ".png"

    pngexits = exists(mediarootLaptop + data[0] + ".png")
    if (type_create == "Update"):
      
        stringdata = "ID :  " + data[0] + "\n S/N :"+  data[1]  +" \nBrand :"+  data[2] +" \nModel : "+  data[3]
        url = pyqrcode.create(stringdata)
        url.png(mediarootLaptop+ data[0]+".png", scale =2)
        stringdata = mediarootLaptop+ data[0]+".png"
        dataindex = data[0]
        type_Upload = "Update"
        

        upload_LaptopQR(dataindex ,stringdata, type_Upload)
    else:
        stringdata = "ID :  " + data[0] + "\n S/N :"+  data[1]  +" \nBrand :"+  data[2] +" \nModel : "+  data[3]
        if (pngexits == False):
                url = pyqrcode.create(stringdata)
                url.png(mediarootLaptop+ data[0]+".png", scale =2)
        else:
                pass
        stringdata = mediarootLaptop+ data[0]+".png"
        dataindex = data[0]
        type_Upload = "Create"
        upload_LaptopQR(dataindex ,stringdata, type_Upload)
    

            
           
# upload qr image for PC
def upload_PCQR(dataindex,data, type_Upload):
    if (type_Upload == "Update"):
        form = Computer.objects.filter(computer_id=dataindex).get()
        form.qrcode_image = data
        form.save()
    else:
        form = Computer.objects.filter(computer_id=dataindex).get()
        form.qrcode_image = "PC/" + data
        if not Computer.objects.filter(qrcode_image=data).exists():  
            form.save()
        
# upload qr image for Laptop
def upload_LaptopQR(dataindex,data, type_Upload):

    if (type_Upload == "Update"):
        form = Laptop.objects.filter(computer_id=dataindex).get()
        form.qrcode_image = data
        form.save()
    else:
        form = Laptop.objects.filter(computer_id=dataindex).get()
        form.qrcode_image = "Laptop/" + data
        if not Laptop.objects.filter(qrcode_image=data).exists():  
           
            form.save()
        
            
            

# send download file 
def DownloadFileQR(request):
    
       

       
        # Define Django project base directory
        dirctory = Path(__file__).resolve().parent.parent
        pathmain = os.path.join(dirctory, 'main/')
        pathstatic = os.path.join(pathmain, 'static/')
        pathmedia = os.path.join(pathstatic, 'media/')
        pathpng = os.path.join(pathmedia, 'png/')
        pathsvg = os.path.join(pathmedia, 'svg/')
        mediaroot = os.path.join(dirctory, 'media/')
        mediarootpng = os.path.join(mediaroot, 'file/')
        # Define text file name
        filename = 'QR Download.pdf'
        # Define the full file path
        filepath = mediarootpng +  filename
        # Open the file for reading content
        path = open(filepath, 'rb')
    
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        return response
        
# Create PDF
def create_pdf_based_OnImage(request):
    if request.method == "POST":
        arraydata = []
        
        datatype = request.POST["data_type"]
       
       
        if (datatype == "PC" and request.POST["type_selection"] == "Custom"):
             
                data1 = int(request.POST["data1"])
                data2 = int(request.POST["data2"])
            
                while data1 <= data2:
                    if data1 <= 480:

                        if data1 < 10:
                            data = "UTM-PC00"+ str(data1)
                        elif ((data1 >= 10) and (data1 < 100)):
                            data= "UTM-PC0"+ str(data1)
                        elif ((data1 >= 100) and (data1 < 1000)):
                            data= "UTM-PC"+ str(data1)
                        elif ((data1 >= 1000) and (data1 < 10000)):
                            data= "UTM-PC"+ str(data1)
                        data1 = data1 + 1
                        arraydata.append(data)
                    else:
                        if data1 < 10:
                            data = "UTM-PC000"+ str(data1)
                        elif ((data1 >= 10) and (data1 < 100)):
                            data= "UTM-PC00"+ str(data1)
                        elif ((data1 >= 100) and (data1 < 1000)):
                            data= "UTM-PC0"+ str(data1)
                        elif ((data1 >= 1000) and (data1 < 10000)):
                            data= "UTM-PC"+ str(data1)
                        data1 = data1 + 1
                        arraydata.append(data)
        elif (datatype == "PC" and request.POST["type_selection"] == "All"):
             

                computerdata = Computer.objects.all()
                array_listdata = list(computerdata.values())
         
                for x in computerdata:
                   
                    
                    datax = x.computer_id
                    arraydata.append(datax)

        elif (datatype == "Laptop"  and request.POST["type_selection"] == "Custom"):
             

                data1 = int(request.POST["data1"])
                data2 = int(request.POST["data2"])
                
                while data1 <= data2:
                    if data1 <= 268:
                        if data1 < 10:
                            data = "UTM-NB00"+ str(data1)
                        elif ((data1 >= 10) and (data1 < 100)):
                            data= "UTM-NB0"+ str(data1)
                        elif ((data1 >= 100) and (data1 < 1000)):
                            data= "UTM-NB"+ str(data1)
                        elif ((data1 >= 1000) and (data1 < 10000)):
                            data= "UTM-NB"+ str(data1)
                        data1 = data1 + 1
                        arraydata.append(data)
                    else:
                        if data1 < 10:
                            data = "UTM-NB000"+ str(data1)
                        elif ((data1 >= 10) and (data1 < 100)):
                            data= "UTM-NB00"+ str(data1)
                        elif ((data1 >= 100) and (data1 < 1000)):
                            data= "UTM-NB0"+ str(data1)
                        elif ((data1 >= 1000) and (data1 < 10000)):
                            data= "UTM-NB"+ str(data1)
                        data1 = data1 + 1
                        arraydata.append(data)
            
        elif (datatype == "Laptop" and request.POST["type_selection"] == "All"):
                

                computerdata = Laptop.objects.all()
                array_listdata = list(computerdata.values())
               
                for x in array_listdata:
                    datax = x['computer_id']
                   
                    arraydata.append(datax)
        imagedirect = []
        dirctory = Path(__file__).resolve().parent.parent
        mediaroot = os.path.join(dirctory, 'media/')
        pathPC = os.path.join(mediaroot, 'pc/')
        pathLaptop = os.path.join(mediaroot, 'Laptop/')
        mediarootfile = os.path.join(mediaroot, 'file/')
        pathdirect =""
        if (datatype == 'PC' ):
           
            
            data = Computer.objects.filter(computer_id__in=arraydata)
            array_listdata = list(data.values())
            for x in array_listdata:
               
                filename = x['computer_id'] + ".png"
                imagedirect.append(filename)
        

        elif (datatype == 'Laptop' ):
           
        
            data = Laptop.objects.filter(computer_id__in=arraydata)
            array_listdata = list(data.values())
            
            for x in array_listdata:
              

                filename = x["computer_id"] + ".png"
                imagedirect.append(filename)
        

        
        
        output_file = "QR Download.pdf"
        if (datatype == 'PC' ):
           

            path = os.listdir(pathPC)
            pdf = FPDF( 'P',  'cm', (10.16,20.32))
            # imagelist is the list with all image filenames
            x= 1
            y = 1.5
            ytext = 1
            w =3
            h = 3
            index = 0
            count_index= 1
            pdf.set_font('Arial', 'B', 10)
            pdf.add_page()
            for image in imagedirect:
                
                stringlabel = "PC : "  + image.replace('.png', '')
                if index == 0 :
                    pdf.text(x,ytext, stringlabel)
                    pdf.image(pathPC+image,x,y,w,h)
                    
                    index +=1
                elif index < 4 :
                    y+=4
                    ytext +=4
                    pdf.text(x,ytext, stringlabel)
                    pdf.image(pathPC+image,x,y,w,h)
                    index +=1
                elif index == 4 :
                    y =1.5
                    x = 6
                    ytext =1
                    pdf.text(x,ytext, stringlabel)
                    pdf.image(pathPC+image,x,y,w,h)
                    index +=1
                elif index < 8 :
                    y+=4
                    ytext +=4
                    pdf.text(x,ytext, stringlabel)
                    pdf.image(pathPC+image,x,y,w,h)
                    index +=1
                else:
                    pdf.add_page()
                
                    y=1.5
                    x= 1
                    ytext =1
                    pdf.text(x,ytext, stringlabel)
                    pdf.image(pathPC+image,x,y,w,h)
                    index =1
                    
                count_index +=1

            pdf.output(mediarootfile + output_file, "F") 
            
            return HttpResponse('hai')

            
            
        

        elif (datatype == 'Laptop' ):
            path = os.listdir(pathLaptop)
            pdf = FPDF( 'P',  'cm', (10.16,20.32))
            # imagelist is the list with all image filenames
            x= 1
            y = 1.5
            ytext = 1
            w =3
            h = 3
            index = 0
            count_index= 1
            pdf.set_font('Arial', 'B', 10)
            pdf.add_page()
            for image in imagedirect:
                
                stringlabel = "Laptop : "  + image.replace('.png', '')
                if index == 0 :
                    pdf.text(x,ytext, stringlabel)
                    pdf.image(pathLaptop+image,x,y,w,h)
                    
                    index +=1
                elif index < 4 :
                    y+=4
                    ytext +=4
                    pdf.text(x,ytext, stringlabel)
                    pdf.image(pathLaptop+image,x,y,w,h)
                    index +=1
                elif index == 4 :
                    y =1.5
                    x = 6
                    ytext =1
                    pdf.text(x,ytext, stringlabel)
                    pdf.image(pathLaptop+image,x,y,w,h)
                    index +=1
                elif index < 8 :
                    y+=4
                    ytext +=4
                    pdf.text(x,ytext, stringlabel)
                    pdf.image(pathLaptop+image,x,y,w,h)
                    index +=1
                else:
                    pdf.add_page()
                
                    y=1.5
                    x= 1
                    ytext =1
                    pdf.text(x,ytext, stringlabel)
                    pdf.image(pathLaptop+image,x,y,w,h)
                    index =1
                    
                count_index +=1

            pdf.output(mediarootfile + output_file, "F") 
            
            return HttpResponse('hai')


       
        
                    # first execution embeds the image
  

    
           


