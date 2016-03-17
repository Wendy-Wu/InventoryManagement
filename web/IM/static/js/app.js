// JavaScript Document

var main = function() {
  
  var cards = new Array();
  cards.push('#Inventories');
  cards.push('#Users');
  cards.push('#MyItems');
  cards.push('#MyMessages');
  
  /* Hide the other cards */
  for(var i=1; i < cards.length; i++){
	  $(cards[i]).hide();
  }


  /* Choose in menu to show the according card*/
  $('#main-menu p').click(function(){
	 $(cards[current_index]).hide();
	 var clicked_item = $(this).html();
	 clicked_item = clicked_item.replace(" ",'');
	 for (var i=0; i<cards.length; i++){
		 if (cards[i] == '#'+ clicked_item){
			 current_index = i;
		 }
	 }
	 $(cards[current_index]).show();
  });
  
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
		  
	  }else{
	      $('.operation').css('visibility', 'hidden');
	  }
  });
  
  /* check-head: select/unselect all*/
  $('#check-head').change(function(){
		 $('.check-item').prop('checked', $(this).prop('checked'));
		 if (this.checked == true){
 			 $('.operation').css('visibility', 'visible')
 		  }else{
 			 $('.operation').css('visibility', 'hidden');
 		  }
  });
  
  /*apply operation on checked items*/
  $('.operation-delete').click(function(){
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
		 }).done(function(data){
			 location.reload();
		 });
  });
  
  $('.operation-edit').click(function(){
	  
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
  
  
  $('#search-inventory').keydown(function(event){
	  if (event.which == 13){
		  $('.inventory-search-table').empty();
		  search_string = $('#search-inventory').val();
		  if (search_string != ''){	
			  //flip the card and show search results
			  $('.flip-container').toggleClass('flip'); 
			  $.ajax({
				 url: "http://127.0.0.1:5000/search-inventory",
				 type: "POST",
				 data: {search_string: search_string},
				 async: false,
			  }).done(function(data){
				  var invs = data.result
				  $( ".inventory-search-table" ).append("<thead>\
					        <tr>\
					        	<th><input type='checkbox' id='check-search-head'/></th>\
					        	<th style='display:none;'>id</th>\
					        	<th>Tag</th>\
					        	<th>Name</th>\
					        	<th>PN</th>\
					        	<th>SN</th>\
					        	<th>Shipping/Source</th>\
					        	<th>Capital/Expense</th>\
					        	<th>Disposition</th>\
					        	<th>Status</th>\
					        	<th>Owner</th>\
					        	<th>User</th>\
					        </tr>\
					    </thead>");
				  for (var i=0; i<invs.length; i++){
					  $( ".inventory-search-table" ).append( "<tr>" +
	     	                  "<td><input type='checkbox' class='check-item'/></td>" +
	     	                  "<td style='display:none;' class='inventory-id'>" + invs[i][0] + "</td>" +
	     	                  "<td align='center'>" + invs[i][1] + "</td>" +
	     	                  "<td align='center'>" + invs[i][2] + "</td>" +
	     	                  "<td align='center'>" + invs[i][3] + "</td>" +
	     	                  "<td align='center'>" + invs[i][4] + "</td>" +
	     	                  "<td align='center'>" + invs[i][5] + "</td>" +
	     	                  "<td align='center'>" + invs[i][6] + "</td>" +
	     	                  "<td align='center'>" + invs[i][7] + "</td>" +
	     	                  "<td align='center'>" + invs[i][8] + "</td>" +
	     	                  "<td align='center'>" + invs[i][9] + "</td>" +
	     	              	  "</tr>" );
				  }
			  }); 
		  }else{
			  $('.inventory-search-table').empty();
			  $('.flip-container').toggleClass('flip'); 
		  }
		  $('.check-item').click(function(){
			  /*check-head change according to check-item*/
			  if ($('.check-item:checked').length == $('.check-item').length) {
			        $('#check-search-head').prop('checked', true);
			  }
			  else {
			        $('#check-search-head').prop('checked', false);
			  }
			  /*operation show and hide according to checked item*/
			  if ($('.check-item:checked').length) {
				  $('.operation').css('visibility', 'visible');
				  
			  }else{
			      $('.operation').css('visibility', 'hidden');
			  }
		  });
		  
		  /* check-head: select/unselect all*/
		  $('#check-search-head').change(function(){
				 $('.check-item').prop('checked', $(this).prop('checked'));
				 if (this.checked == true){
		 			 $('.operation').css('visibility', 'visible')
		 		  }else{
		 			 $('.operation').css('visibility', 'hidden');
		 		  }
		  });
	  }
	  
  });
  
  var tag = $("#tag"),
  name = $("#name"),
  PN = $("#PN"),
  SN = $("#SN"),
  ship = $("#shipping"),
  cap = $("#capital"),
  dis = $("#disposition"),
  status = $("#status"),
  owner = $("#owner"),
  error = $("#dialog-form .error-msg")
  allFields = $([]).add(tag).add(name).add(PN).add(SN).add(ship).add(cap).add(dis).add(status).add(owner);
  
  $('#dialog-form').dialog({
	  autoOpen: false,
	  resizable: false,
	  height: 500,
	  width: 250,
	  modal: true,
      show: {
        effect: "blind",
        duration: 1000
      },
      hide: {
        effect: "blind",
        duration: 500
      },
      buttons: {
    	  "Add an inventory": function() {
    		  error.hide();
              var bValid = true;
//              allFields.removeClass( "ui-state-error" );
//     
//              bValid = bValid && checkLength( tag, "username", 3, 16 );
//              bValid = bValid && checkLength( name, "email", 6, 80 );
//             
//              bValid = bValid && checkRegexp( name, /^[a-z]([0-9a-z_])+$/i, "必须由 a-z、0-9、下划线组成，且必须以字母开头。" );
//              // From jquery.validate.js (by joern), contributed by Scott Gonzalez: http://projects.scottsplayground.com/email_address_validation/
//              //bValid = bValid && checkRegexp( email, /^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i, "eg. ui@jquery.com" );
//              //bValid = bValid && checkRegexp( password, /^([0-9a-zA-Z])+$/, "密码字段只允许： a-z 0-9" );
//     
              if ( bValid ) {
	        	  $.ajax({
	     			 url: "http://127.0.0.1:5000/add-inventory",
	     			 type: "POST",
	     			 data: {tag: tag.val(),
	     				 	name: name.val(),
	     				 	PN: PN.val(),
	     				 	SN: SN.val(),
	     				 	ship: ship.val(),
	     				 	cap: cap.val(),
	     				 	dis: dis.val(),
	     				 	status: status.val(),
	     				 	owner: owner.val(),
	     			 },
	     			 async: true,
	     		  }).done(function(data){
	     			  var inv = data.result
	     			  if (inv) {
	     				 $( ".inventory-table" ).append( "<tr>" +
		     	                  "<td><input type='checkbox' class='check-item'/></td>" +
		     	                  "<td style='display:none;' class='inventory-id'>" + inv[0] + "</td>" +
		     	                  "<td align='center'>" + inv[1] + "</td>" +
		     	                  "<td align='center'>" + inv[2] + "</td>" +
		     	                  "<td align='center'>" + inv[3] + "</td>" +
		     	                  "<td align='center'>" + inv[4] + "</td>" +
		     	                  "<td align='center'>" + inv[5] + "</td>" +
		     	                  "<td align='center'>" + inv[6] + "</td>" +
		     	                  "<td align='center'>" + inv[7] + "</td>" +
		     	                  "<td align='center'>" + inv[8] + "</td>" +
		     	                  "<td align='center'>" + inv[9] + "</td>" +
		     	              	  "</tr>" );
	     				 $( '#dialog-form' ).dialog( "close" );
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
	     						  
	     					  }else{
	     					      $('.operation').css('visibility', 'hidden');
	     					  }
	     				  });
	     			  }
	     			  else {
	     				  error.show();
	     			  }
	     		  });
                
              }
            },
            Cancel: function() {
              $( this ).dialog( "close" );
            }
          },
      close: function() {
        allFields.val( "" ).removeClass( "ui-state-error" );
      }
   });
      
  
  $('.new-btn').click(function(){
	 $('#dialog-form').dialog("open"); 
	 error.hide();
  });

  
  $('#export-excel').click(function(){
	  $.ajax({
			 url: "http://127.0.0.1:5000/export-excel",
			 type: "GET",
			 async: false,
		  });
  });
  
  $('#logout').click(function(){
	  window.location.href="http://127.0.0.1:5000/hello";
  })
  
};


$(document).ready(main);