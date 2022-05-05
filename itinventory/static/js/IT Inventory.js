   function Nexttab() {
  var value = parseInt(document.getElementById('number').value, 10);
switch(value) {
case 1:
  var tabafter = document.getElementById("form2");
  var tabbefore = document.getElementById("form1");
  var form1 = document.getElementById("formtab1");

  var form2 = document.getElementById("formtab2");
  var btnNext = document.getElementById("btnBack");

 

  form2.style.display = "block";
  btnNext.style.display = "block";

  form1.style.display = "none";

  tabbefore.classList.remove("current-item1");
  tabafter.classList.add("current-item1");
  value++;
document.getElementById('number').value = value;
console.log(value);

// code block
break;
case 2:
  var tabafter = document.getElementById("form3");
  var tabbefore = document.getElementById("form2");
  var form1 = document.getElementById("formtab2");

  var form2 = document.getElementById("formtab3");
  var btnNext = document.getElementById("btnBack");

  form2.style.display = "block";
  btnNext.style.display = "block";

  form1.style.display = "none";

  tabbefore.classList.remove("current-item1");
  tabafter.classList.add("current-item1");
  value++;
document.getElementById('number').value = value;
console.log(value);

break;
case 3:
  var tabafter = document.getElementById("form4");
  var tabbefore = document.getElementById("form3");
  var form1 = document.getElementById("formtab3");

  var form2 = document.getElementById("formtab4");
  var btnBack = document.getElementById("btnBack");
  var btnNext = document.getElementById("btnNext");


  form2.style.display = "block";
  btnBack.style.display = "block";
  btnNext.style.display = "none";


  form1.style.display = "none";

  tabbefore.classList.remove("current-item1");
  tabafter.classList.add("current-item1");
  // take input box for computer detail
var pic = document.getElementById("pic").value;
var Previous_PIC = document.getElementById("Previous_PIC").value;
var Computer_ID = document.getElementById("Computer_ID").value;
var Current_Computer_ID = document.getElementById("Current_Computer_ID").value;
var Brand = document.getElementById("Brand").value;
var Model = document.getElementById("Model").value;
var Serial_Number = document.getElementById("Serial_Number").value;
var Asset_No = document.getElementById("Asset_No").value;
var Vendor = document.getElementById("Vendor").value;
var Machine_Type = document.getElementById("Machine_Type").value;
var Processor_Type = document.getElementById("Processor_Type").value;
var RAM_Type = document.getElementById("RAM_Type").value;
var RAM_Slot = document.getElementById("RAM_Slot").value;
var TOTAL_RAM = document.getElementById("TOTAL_RAM").value;
var Storage_Type = document.getElementById("Storage_Type").value;
var Storage_space = document.getElementById("Storage_space").value;
var DOP = document.getElementById("DOP").value;
var DOP_Years = document.getElementById("DOP_Years").value;
var PO = document.getElementById("PO").value;
var Invoice = document.getElementById("Invoice").value;
var Block = document.getElementById("Block").value;
var Location = document.getElementById("Location").value;

// take input box for software detail
var Standard_Installation = document.getElementById("Standard_Installation");
var Microsoft_Office = document.getElementById("Microsoft_Office");
var Microsoft_Office_Keys = document.getElementById("Microsoft_Office_Keys");

// take input box for connection detail
var LAN_MAC_Address = document.getElementById("LAN_MAC_Address");
var LAN_IP_Address = document.getElementById("LAN_IP_Address");
var WLAN_MAC_Address = document.getElementById("WLAN_MAC_Address");
var WLAN_IP_Address = document.getElementById("WLAN_IP_Address");
var Joined_Domain = document.getElementById("Joined_Domain");
var Connection_Type = document.getElementById("Connection_Type");

// assign the data from input box
console.log(pic)

//computer detail
 document.getElementById("final_pic").value = "DIGUUS";
 document.getElementById("final_previous_pIC").value = Previous_PIC.value;
 document.getElementById("final_Computer_ID").value = Computer_ID.value;
document.getElementById("final_Current_Computer").value = Current_Computer_ID.value;
document.getElementById("final_Brand").value = Brand.value;
document.getElementById("final_Model").value = Model.value;
document.getElementById("final_serial_number").value = Serial_Number.value;
document.getElementById("final_asset_no").value = Asset_No.value;
document.getElementById("final_vendor").value = Vendor.value;
document.getElementById("final_machineType").value = Machine_Type.value;
document.getElementById("final_processor_type").value = Processor_Type.value;
document.getElementById("final_ram_type").value = RAM_Type.value;
document.getElementById("final_ram_slot").value = RAM_Slot.value;
document.getElementById("final_total_RAM").value = TOTAL_RAM.value;
document.getElementById("final_storageType").value = Storage_Type.value;
document.getElementById("final_storageSpace").value = Storage_space.value;
document.getElementById("final_dop").value = DOP.value;
document.getElementById("final_dopYear").value = DOP_Years.value;
document.getElementById("final_po").value = PO.value;
document.getElementById("final_invoice").value = Invoice.value;
document.getElementById("final_block").value = Block.value;
document.getElementById("final_location").value = Location.value;
console.log(pic)
// code block
  value++;
document.getElementById('number').value = value;
console.log(value);

break;
default:
// code block
}

}

   function Backtab() {
  var value = parseInt(document.getElementById('number').value, 10);
switch(value) {
case 2:
  var tabafter = document.getElementById("form1");
  var tabbefore = document.getElementById("form2");
  var form1 = document.getElementById("formtab1");

  var form2 = document.getElementById("formtab2");
  var btnNext = document.getElementById("btnBack");

  form2.style.display = "none";
  btnNext.style.display = "none";

  form1.style.display = "block";

  tabbefore.classList.remove("current-item1");
  tabafter.classList.add("current-item1");
  value--;
  console.log("Back");
  
document.getElementById('number').value = value;
console.log(value);


// code block
break;
case 3:
  var tabafter = document.getElementById("form2");
  var tabbefore = document.getElementById("form3");
  var form1 = document.getElementById("formtab2");

  var form2 = document.getElementById("formtab3");
  var btnNext = document.getElementById("btnBack");

  form2.style.display = "none";
 

  form1.style.display = "block";

  tabbefore.classList.remove("current-item1");
  tabafter.classList.add("current-item1");
  value--;
  console.log("Back");
  
document.getElementById('number').value = value;
console.log(value);
// code block
break;
case 4:
  var tabafter = document.getElementById("form3");
  var tabbefore = document.getElementById("form4");
  var form1 = document.getElementById("formtab3");

  var form2 = document.getElementById("formtab4");
  var btnBack = document.getElementById("btnBack");
  var btnNext = document.getElementById("btnNext");


  form2.style.display = "none";
  btnNext.style.display = "block";

  form1.style.display = "block";

  tabbefore.classList.remove("current-item1");
  tabafter.classList.add("current-item1");
  value--;
  console.log("Back");
  
document.getElementById('number').value = value;
console.log(value);
// code block
break;
default:
// code block
}

}