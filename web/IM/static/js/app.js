// JavaScript Document

var main = function() {
  
  /* check items */
  $('.check-item').click(function(){
	  /*check-head change according to check-item*/
	  if ($('.check-item:checked').length == $('.check-item').length) {
	        $('#check-head').prop('checked', true);
	  }
	  else {
	        $('#check-head').prop('checked', false);
	  }
	  /*operation show and hide according to checked item*/
	  if ($('.check-item:checked').length) {
		  $('.operation').css('visibility', 'visible');
		  if ($('.check-item:checked').length > 1){
			  $('.operation-edit').css('visibility', 'hidden');
		  }
	  }else{
	      $('.operation').css('visibility', 'hidden');
	  }
  });
  
  /* check-head*/
  $('#check-head').change(function(){
		 $('.check-item').prop('checked', $(this).prop('checked'));
		 if (this.checked == true){
 			 $('.operation').css('visibility', 'visible');
 			 if ($('.check-item:checked').length > 1){
 				  $('.operation-edit').css('visibility', 'hidden');
 			 }
 		  }else{
 			 $('.operation').css('visibility', 'hidden');
 		  }
  });
  

  
  $('.operation-borrow').click(function(){
	 checked_items = new Array();
	 if($('.check-item:checked').length){
		 $('.check-item:checked').each(function(){
			  var currentRow = this.parentNode.parentNode;  
			  var inv_id = currentRow.getElementsByTagName("td")[1].textContent;
			  var owner = currentRow.getElementsByTagName("td")[10].textContent;  
			  checked_items.push(inv_id);
			  checked_items.push(owner);
		 });
	 }
	 
	 username = $('.user-name').val();
	 
	 $.ajax({
		url: "http://127.0.0.1:5000/borrow",
		type: "POST",
		data: {rows:checked_items, username: username},

		async: true,
	 }).done(function(data){
		 if (data.result == true){
			 alert('Borrow request successfully sent.');
		 }
		 $('.check-item').prop('checked', false);
		 $('.operation').css('visibility', 'hidden');
	 });
  });
  

  $('.new-btn').click(function(){
	 $('#new-inventory').modal(); 
	 $('#add-confirm').click(function(){
		 $.ajax({
			 url: "http://127.0.0.1:5000/add-inventory",
			 type: "POST",
			 data: {tag: $('#inv-tag').val(),
				 	name: $('#inv-name').val(),
				 	PN: $('#inv-PN').val(),
				 	SN: $('#inv-SN').val(),
				 	ship: $('#inv-shipping').val(),
				 	cap: $('#inv-capital').val(),
				 	dis: $('#inv-disposition').val(),
				 	owner: $('#inv-owner').val(),
			 },
			 async: true,
		  }).done(function(){
			  location.reload();
		  });
	 });
  });
  
  $('#export-excel').click(function(){
	  $.ajax({
			 url: "http://127.0.0.1:5000/export-excel",
			 type: "GET",
			 async: false,
		  });
  });
  
  /*apply operation on checked items*/
  $('.operation-delete').click(function(){
	  $('#delete-info').modal();
	  $('#delete-confirm').click(function(){
		  checked_items = new Array();
		  if($('.check-item:checked').length){
			  $('.check-item:checked').each(function(){
				  var currentRow = this.parentNode.parentNode;
				  var column = currentRow.getElementsByTagName("td")[1];
				  var rowID = column.textContent;
			  
				  checked_items.push(rowID);
			  });
		  }
		  
		 $.ajax({
			url: "http://127.0.0.1:5000/delete-inventory",
			type: "POST",
			data: {rows:checked_items},

			async: true,
		 }).done(function(){
			 location.reload();
		 });
	  });
  });
  
  $('.operation-edit').click(function(){
	  var inv_ID, inv_tag, inv_name, inv_PN, inv_SN, inv_shipping, inv_capital, inv_disposition;
	  $('.check-item:checked').each(function(){
		  var currentRow = this.parentNode.parentNode;
		  var column = currentRow.getElementsByTagName("td")[1];
		  inv_ID = column.textContent;
		  column = currentRow.getElementsByTagName("td")[2];
		  inv_tag = column.textContent;
		  column = currentRow.getElementsByTagName("td")[3];
		  inv_name = column.textContent;
		  column = currentRow.getElementsByTagName("td")[4];
		  inv_PN = column.textContent;
		  column = currentRow.getElementsByTagName("td")[5];
		  inv_SN = column.textContent;
		  column = currentRow.getElementsByTagName("td")[6];
		  inv_shipping = column.textContent;
		  column = currentRow.getElementsByTagName("td")[7];
		  inv_capital = column.textContent;
		  column = currentRow.getElementsByTagName("td")[8];
		  inv_disposition = column.textContent;
	  });
	  
	  $('#edit-tag').val(inv_tag);
	  $('#edit-name').val(inv_name);
	  $('#edit-PN').val(inv_PN);
	  $('#edit-SN').val(inv_SN);
	  $('#edit-shipping').val(inv_shipping);
	  $('#edit-capital').val(inv_capital);
	  $('#edit-disposition').val(inv_disposition);  
	  
	  $('#edit-inventory').modal();
	  
	  $('#edit-confirm').click(function(){
		  $.ajax({
				 url: "http://127.0.0.1:5000/edit-inventory",
				 type: "POST",
				 data: {id: inv_ID,
					 	tag: $('#edit-tag').val(),
					 	name: $('#edit-name').val(),
					 	PN: $('#edit-PN').val(),
					 	SN: $('#edit-SN').val(),
					 	ship: $('#edit-shipping').val(),
					 	cap: $('#edit-capital').val(),
					 	dis: $('#edit-disposition').val(),
				 },
				 async: true,
			  }).done(function(){
					 location.reload();
				 });
		  
	  });
	  
  });
  
  $('#logout').click(function(){
	  window.location.href="http://127.0.0.1:5000/login";
  })
  
  var eventOutputContainer = $('#event');
  var evtSrc = new EventSource("/subscribe");

  evtSrc.onmessage = function(e) {
      eventOutputContainer.append("<div class='alert alert-success'>"+
    		  						"<a href='#' class='close' data-dismiss='alert' aria-label='close'>&times;</a>"+
    		  						e.data+" has been edited."+
      							  "</div>");
  };
  
};


$(document).ready(main);