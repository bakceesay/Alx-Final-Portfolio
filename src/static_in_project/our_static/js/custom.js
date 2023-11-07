
$(document).ready(function() {


    if ($(".success")[0]){
      // alert("Item successfully created.\n Click here to receive this from vendor");
          $(function() {
            $( ".success" ).dialog({
                open: function(event, ui){
                 setTimeout("$('.success').dialog('close')",5000);
                },
                modal: false,
                // position: [100, 100],
                resizeable: false,
                draggable: false,
                autoOpen: true,
                show: {
                  effect: "fade",
                  duration: 1000,
                  },

                hide: {
                  effect: "fade",
                  duration: 500
                }
            });
          });

    // } else {
    //     alert("An Error occured")
    }


    if ($(".error")[0]){
      // alert("Item successfully created.\n Click here to receive this from vendor");
          $(function() {
            $( ".error" ).dialog({
              open: function(event, ui){
                 setTimeout("$('.error').dialog('close')",100000);
                },
                autoOpen: true,
                show: {
                  effect: "bounce",
                  duration: 1000,
                },

                hide: {
                  effect: "bounce",
                  duration: 500
                }
            });
          });
    }

  
  $('.tabs').tabs();
  $('.pannel').accordion({collapsible: true},{heightStyle: 'content'},{icons: {
                                                                                header: "ui-icon-plus",
                                                                                activeHeader: "ui-icon-minus"
                                                                              }
                                                                      }
                        );


    // REMEMBER THE LAST SETTINGS TAB
    function tab() { //tab with cookie function
      $( ".tabs" ).tabs({
        active   : $.cookie('activetab'),
        activate : function( event, ui ){
            $.cookie( 'activetab', ui.newTab.index(),{
                expires : 10
            });
        }
      });
    }


    var url      = window.location.href;     // Returns full URL
      // var pathname = window.location.pathname; // Returns path only

    var store = "store_";
    var fixAsset = "fix_assets";
    var settings = "settings";

    storeResults = url.search(store);
    assetResults = url.search(fixAsset);
    settingsResults = url.search(settings);

    var elementsToReset = $('#id_pay_allowance, #id_date_allowance_paid, #id_pay_contribution, #id_date_allowance_contributed, #id_issue_amount, #id_issue_to, .store-form #id_unit, #id_receive_amount, #id_returned_by, .store-form #id_supplier_name');

    elementsToReset.val('');


  $('#div_id_rank').change(function() {
      var selected = $('#div_id_rank :selected').text();
      var extracted_num = parseInt(selected.replace(/[^0-9\.]/g, ''), 10)

      if (selected == 'GEN, COL, LT COL = USD 1301'){
          $('#id_allowance').val( '1301' );
      }

      else if (selected == 'MAJOR = USD 1210'){
          $('#id_allowance').val( '1210' );
      }

      else if (selected == 'CAPT = USD 1139'){
          $('#id_allowance').val( '1139' );
      }

      else if (selected == 'LT = USD 1081'){
          $('#id_allowance').val( '1081' );
      }

      else if (selected == '2IT = USD 1026'){
          $('#id_allowance').val( '1026' );
      }

      else if (selected == 'OCDT, WO2, SSGT = USD 974'){
          $('#id_allowance').val( '974' );
      }

      else if (selected == 'SGT, CPL, LCPL = USD 876'){
          $('#id_allowance').val( '876' );
      }
  });

    var disableFormFields = ('.form-edit :text, .form-edit .select, .form-edit .textarea, .form-edit .checkboxinput, .form-edit :input[type="number"], form .save, form-edit .update, form #show_update_button');
    $(disableFormFields).prop('disabled', true)
    $('.edit').click(function(){
      $(disableFormFields).prop('disabled', false);
      // $('html, body').animate({scrollTop : 0},800);
      return false;
    });

    $('#show_update_button').click(function(){
      if(document.getElementById('show_update_button').checked) {
        $('.update').show(200)
      }else{
        $('.update').hide(200)
      }

    });

    var store = "store_";
    var fixAsset = "fix_assets";
    var settings = "settings";

    storeResults = url.search(store);
    assetResults = url.search(fixAsset);
    settingsResults = url.search(settings);

    var training_create = "create";
    var training_edit = "edit";
    training_createResults = url.search(training_create);
    training_editResults = url.search(training_edit);
 

    $('#div_id_oversea_training').click(function(){
      if(document.getElementById('id_oversea_training').checked) {
        $('#div_id_rank').show(200)
        $('#div_id_USD_Rate').show(200)
        $('#div_id_host_pay').show(200)
      }else{
        $('#div_id_rank').hide(200)
        $('#div_id_USD_Rate').hide(200)
        $('#div_id_host_pay').hide(200)
      }

    });


    $('#div_id_sponsor').click(function(){
      if(document.getElementById('id_sponsor').checked) {
        $('#div_id_fees').hide(200)
        $('#div_id_fees_paid').hide(200)
        $('#div_id_date_fees_paid').hide(200)
      }else{
        $('#div_id_fees').show(200)
        $('#div_id_fees_paid').show(200)
        $('#div_id_date_fees_paid').show(200)
      }
    });


   // Scroll Top Script
   //Check to see if the window is top if not then display button
    $(window).scroll(function(){
      if ($(this).scrollTop() > 300) {
        $('.scrollToTop').fadeIn();
      } else {
        $('.scrollToTop').fadeOut();
      }
    });

    //Click event to scroll to top
    $('.scrollToTop').click(function(){
      $('html, body').animate({scrollTop : 0},800);
      return false;
    });
   //END Scroll Top Script



    $(".jumbotron, .navbar").hide().fadeIn(1000);
    $('.jumbotron').ready(function () {
      $(".display-icons").hide().fadeIn(1000);
    })
    

    $('ul.nav li.dropdown').hover(function() {
        $(this).find('.dropdown-menu').stop(true, true).delay(300).slideDown(300);
      }, function() {
        $(this).find('.dropdown-menu').stop(true, true).delay(300).slideUp(300);
      });



    // Pagination Script+
    $('.table').paging({limit:100});
    // END Pagination Script
     

    NProgress.start();
    NProgress.done();


    $(".dateinput").datepicker({yearRange: '1930:2100', showButtonPanel: true, changeMonth: true, changeYear: true, dateFormat: 'yy-mm-dd'});
    // $(".datetimeinput").datetimepicker({format:'Y-m-d H:i',}); //Pick date and time manually
    // $("#id_start_date, #id_end_date").datetimepicker({format:'Y-m-d H:i',}); //Pick date and time manually

    // document.getElementById('id_date_received_by_bank_transfer').value = moment().format('YYYY-MM-DD HH:mm');

    var currentDateAndTime = moment().format('YYYY-MM-DD HH:mm');
    

  (function blink() { 
    $('.blink-me').fadeOut(500).fadeIn(500, blink); 
  });


});//Document.ready closing brace
