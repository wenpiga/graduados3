//verificamos los permisos del usuario y asignamos variables(true, false)
if (jQuery("#grid_perms_add").val() == 'True'){
var add_grid = true ;
}else{
var add_grid = false;
}
 
if (jQuery("#grid_perms_change").val() == 'True'){
var edit_grid = true ;
}else{
var edit_grid = false;
}
 
if (jQuery("#grid_perms_delete").val() == 'True'){
var del_grid = true ;
}else{
var del_grid = false;
}
 
jQuery("#jqgrid_estudiante").jqGrid({
//url que llama a la base de datos y trae el listado de estudiantes, traemos los datos en formato json.
url:'ver/?add=' + jQuery("#grid_perms_add").val() + '&change=' + jQuery("#grid_perms_change").val() + '&delete=' + jQuery("#grid_perms_delete").val(),
datatype: "json",
colNames:['Nº','Código','Ape. Pat.','Ape. Mat.','Nombres','Nacimiento','Sexo','Dirección','Email','Teléfono','Estado Civil','Carrera','Observaciones'],
colModel:[
 
 {name:'id',index:'id',width:40,search:false,align:'center',editable:false,editoptions:{readonly:true,size:10}},
 
 {name:'Codigo',index:'Codigo',width:70,align:'center',editable:true,editoptions:{size:40},editrules:{required:true}},
 
 {name:'ApellidoPaterno',index:'ApellidoPaterno',width:80,align:'center',editable:true,editoptions:{size:40},editrules:{required:true}},
 
 {name:'ApellidoMaterno',index:'ApellidoMaterno',width:80,align:'center',editable:true,editoptions:{size:40},editrules:{required:true}},
 
 {name:'Nombres',index:'Nombres',width:80,align:'center',editable:true,editoptions:{size:40},editrules:{required:true}},
 
 {name:'Nacimiento',index:'Nacimiento',width:90,search:false,align:'center',editable:true,editoptions:{size:40},editrules:{required:false,date:true}},
 
 {name:'Sexo',index:'Sexo',width:55,search:false,editable:true,align:'center',edittype:"select",editoptions:{value:"M:Masculino;F:Femenino"},editrules:{required:true}},
 
 {name:'Direccion',index:'Direccion',search:false,width:150,align:'center',editable:true,editoptions:{size:40},editrules:{required:true}},
 
 {name:'Email',index:'Email',width:125,search:false,editable:true,editoptions:{size:40},editrules:{required:false,email:true}},
 
 {name:'Telefono',index:'Telefono',width:80,search:false,align:'center',editable:true,editoptions:{size:10},editrules:{required:false}},
 
 {name:'EstadoCivil',index:'EstadoCivil',width:70,search:false,align:'center',editable:true,edittype:"select",editoptions:{value: "Soltero:Soltero;Casado:Casado;Viudo:Viudo;Divorciado:Divorciado"},editrules:{required:true}},
 
 {name:'Carrera',index:'Carrera',width:130,search:false,editable:true,edittype:"select",editoptions:{dataUrl:'obtener_carreras/'},editrules:{required:true}},
 
 {name:'Observaciones',index:'Observaciones',width:110,search:false,editable:true,edittype:"textarea",editoptions:{rows:"3",cols:"37"},editrules:{required:false}}
],
rowNum:10,
rowList:[10,20,30],
pager: '#pagernav',
sortname: 'id',
viewrecords: true,
sortorder: 'desc',
caption:'Estudiantes',
//ruta para ejecutar las operaciones de agregar, modificar o eliminar un registro
editurl:'master/?add=' + jQuery("#grid_perms_add").val() + '&change=' + jQuery("#grid_perms_change").val() + '&delete=' + jQuery("#grid_perms_delete").val(),
height:'100%',
width: '100%'
 
});
 
jQuery("#jqgrid_estudiante").jqGrid('navGrid','#pagernav',
{search:true,add:add_grid,edit:edit_grid,del:del_grid}, //options
{width:400,height:430,reloadAfterSubmit:true,closeAfterEdit: true}, // edit options
{width:400,height:430,reloadAfterSubmit:true,closeAfterAdd: true}, // add options
{width:270,reloadAfterSubmit:true}, // del options
{} // search options
);