from django.urls import path
from . import views
from django.contrib import admin

urlpatterns=[
   
    path('', views.login_user, name='login'),
  
    path('dashboard', views.homepage, name='dashboard'),
    path('DownloadFileQR', views.DownloadFileQR, name='DownloadFileQR'),
    path('create_pdf_based_OnImage', views.create_pdf_based_OnImage, name='create_pdf_based_OnImage'),

    path('testenvironment', views.testenvironment, name='testenvironment'),
    path('usagepcpie', views.usagepcpie, name='usagepcpie'),



    #Computer page
    path('computerpage', views.computerdetail, name='computerpage'),
    path('getcomputerdata', views.getcomputerdata, name='getcomputerdata'),
    path('addcomputerform', views.addcomputerform, name='addcomputerform'),
    path('getdataupdate', views.getdataupdate, name='getdataupdate'),
    path('rundatatoform', views.rundatatoform, name='rundatatoform'),
    path('updateformpc', views.updateformpc, name='updateformpc'),
    path('getcustomPCdata', views.getcustomPCdata, name='getcustomPCdata'),
    path('exportdatapc', views.exportdatapc, name='exportdatapc'),
    path('GetQRPCData', views.GetQRPCData, name='GetQRPCData'),
    path('searchPCdata', views.searchPCdata, name='searchPCdata'),




    
    #Laptop page
    path('laptoppage', views.laptopdetail, name='laptoppage'),
    path('getlaptopdata', views.getlaptopdata, name='getlaptopdata'),
    path('addlaptopform', views.addlaptopform, name='addlaptopform'),
    path('getlaptopdataupdate', views.getlaptopdataupdate, name='getlaptopdataupdate'),
    path('runlaptopform', views.runlaptopform, name='runlaptopform'),
    path('updateformlaptop', views.updateformlaptop, name='updateformlaptopupdateformlaptop'),
    path('getcustomLaptopdata', views.getcustomLaptopdata, name='getcustomLaptopdata'),
    path('exportdatalaptop', views.exportdatalaptop, name='exportdatalaptop'),
    path('GetQRLaptopData', views.GetQRLaptopData, name='GetQRLaptopData'),
    path('searchLaptopdata', views.searchLaptopdata, name='searchLaptopdata'),

    
     #Hardware page
    path('Networkhardwarepage', views.Networkhardwarepage, name='Networkhardwarepage'),
     path('runNetworkform', views.runNetworkform, name='runNetworkform'),
      path('Networkhardwareadd', views.Networkhardwareadd, name='Networkhardwareadd'),
       path('getNetworkdata', views.getNetworkdata, name='getNetworkdata'),
       path('getNetworkdataupdate', views.getNetworkdataupdate, name='getNetworkdataupdate'),
       path('Networkhardwareupdate', views.Networkhardwareupdate, name='Networkhardwareupdate'),
       path('exporthardwaredataNetwork', views.exporthardwaredataNetwork, name='exporthardwaredataNetwork'),
       path('getcustomhardwaredata', views.getcustomhardwaredata, name='getcustomhardwaredata'),




 
     #PC Machine Page

     #Hardware page
   
     #User page
    path('userpage', views.userdetail, name='userpage'),
    path('AddAssetUser', views.AddAssetUser, name='AddAssetUser'),
    path('getUserdata', views.getUserdata, name='getUserdata'),
    path('typeofsoftware', views.typeofsoftware, name='typeofsoftware'),
    path('versionsoftware', views.versionsoftware, name='versionsoftware'),
    path('getUserdataupdate', views.getUserdataupdate, name='getUserdataupdate'),
    path('deleteuser', views.deleteuser, name='deleteuser'),
       path('updateformuser', views.updateformuser, name='updateformuser'),

    
       path('userdetail', views.userdetail, name='userdetail'),





   
     #Loan page
    path('loanpage', views.loandetail, name='loanpage'),
    path('loandata', views.loandata, name='loandata'),
    path('addLoanform', views.addLoanform, name='addLoanform'),
    path('Loandataupdate', views.Loandataupdate, name='Loandataupdate'),
    path('updateformLoan', views.updateformLoan, name='updateformLoan'),
    path('openloandataform', views.openloandataform, name='openloandataform'),
    path('returnloan', views.returnloan, name='returnloan'),
    path('searchUserinput', views.searchUserinput, name='searchUserinput'),
    path('GetEmployeeLoanDetail', views.GetEmployeeLoanDetail, name='GetEmployeeLoanDetail'),




     #IP page
    path('ippage', views.ipdetail, name='ippage'),
    path('getipdata', views.getipdata, name='getipdata'),
    path('addipform', views.addipform, name='addipform'),
    path('getipupdate', views.getipupdate, name='getipupdate'),
    path('updateformip', views.updateformip, name='updateformip'),
    path('exportIPdataNetwork', views.exportIPdataNetwork, name='exportIPdataNetwork'),
    path('getcustomIPdata', views.getcustomIPdata, name='getcustomIPdata'),


    #upload mass data datauploadtomodel
    path('uploadcsvdata', views.uploadcsvdata, name='uploadcsvdata'),
 


  #software page
    path('software', views.software, name='software'),
    path('software_listing', views.software_listing, name='software_listing'),
    path('getsoftwaredata', views.getsoftwaredata, name='getsoftwaredata'),
    path('softwareVersion_listing', views.softwareVersion_listing, name='softwareVersion_listing'),
    path('addUserSoftwareform', views.addUserSoftwareform, name='addUserSoftwareform'),
    path('getSoftUserdataupdate', views.getSoftUserdataupdate, name='getSoftUserdataupdate'),
    path('updateformsoftwareUser', views.updateformsoftwareUser, name='updateformsoftwareUser'),
    path('deleteSoftwareUser', views.deleteSoftwareUser, name='deleteSoftwareUser'),
    path('exportsoftwaredataNetwork', views.exportsoftwaredataNetwork, name='exportsoftwaredataNetwork'),
    path('getcustomsoftwaredata', views.getcustomsoftwaredata, name='getcustomsoftwaredata'),

#history logging
    path('historypage', views.historypage, name='historypage'),
    path('getloghistory', views.getloghistory, name='getloghistory'),

#logout page
    path('logoutsystem', views.logoutsystem, name='logoutsystem'),

]