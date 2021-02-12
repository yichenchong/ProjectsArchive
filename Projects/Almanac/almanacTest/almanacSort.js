var filters=['hide_firstName','hide_lastName','hide_preferredName','hide_email','hide_grade','hide_ID','hide_campus','hide_school'];

function ExcludeRows(cls){
  
  var skipRows=[];
 
  for(i=0;i<filters.length;i++)
      if(filters[i]!=cls) skipRows.push(filters[i]);
 
  var pattern=skipRows.join('|')
 
  return pattern;
}

function Filter(srcField){
    
   var node=srcField.parentNode;
   
   var index=srcField.parentNode.cellIndex;
    //all the DATA rows
    
   var dataRows= document.getElementsByClassName("row");
    
   //ensure that dataRows do not have any filter class added already
   var kids= dataRows.length;
   
   var filter ='hide_'+srcField.id;
    
   var pattern = ExcludeRows(filter);
    
   var skipRow = new RegExp(pattern,"gi"); 

   var searchReg =new RegExp('^'+srcField.value,'gi');
    
   var replaceCls= new RegExp(filter,'gi');
   
   for(i=0; i< kids ; i++){
       //skip if already filter applied  
     
       if(dataRows[i].className.match(skipRow)) continue;
       
       //now we know which column to search 
       //remove current filter
       dataRows[i].className=dataRows[i].className.replace(replaceCls,'');
  
       if(!dataRows[i].cells[index].innerHTML.trim().match(searchReg))
          dataRows[i].className=dataRows[i].className +' '+ filter;
      
    }
         
}

function sortTable(table, col, reverse) {
    var tb = table.tBodies[0], // use `<tbody>` to ignore `<thead>` and `<tfoot>` rows
        tr = Array.prototype.slice.call(tb.rows, 0), // put rows into array
        i;
    reverse = -((+reverse) || -1);
    tr = tr.sort(function (a, b) { // sort rows
        return reverse // `-1 *` if want opposite order
            * (a.cells[col].textContent.trim() // using `.textContent.trim()` for test
                .localeCompare(b.cells[col].textContent.trim())
               );
    });
    for(i = 0; i < tr.length; ++i) tb.appendChild(tr[i]); // append each row in order
}

function makeSortable(table) {
	"use strict";
    var th = table.tHead, i;
    th && (th = th.rows[0]) && (th = th.cells);
    if (th) i = th.length;
    else return; // if no `<thead>` then do nothing
    while (--i >= 0) (function (i) {
        var dir = 1;
        th[i].addEventListener('click', function () {sortTable(table, i, (dir = 1 - dir))});
    }(i));
}

function makeAllSortable(parent) {
	"use strict";
    parent = parent || document.body;
    var t = parent.getElementsByTagName('table'), i = t.length;
    while (--i >= 0) makeSortable(t[i]);
}

window.onload = function () {makeAllSortable();};