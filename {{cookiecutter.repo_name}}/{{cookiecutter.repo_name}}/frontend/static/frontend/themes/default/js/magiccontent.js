$(function() {

  /* open a modal for each control's block */
  /* TODO: change to ajax */
  $('.edit-popup a:not(.exclude-popup)').magnificPopup({
    type: 'iframe',
    closeBtnInside: true,    
    fixedContentPos: true,
    fixedBgPos: true,
    overflowY: 'auto',
    alignTop: true,

    callbacks: {
      open: function() {
          var magnificPopup = $.magnificPopup.instance;
      },      
      close: function () {
      }
    }
  });


  // help screen controllers

  var drawHelperScreenContent = function(linkSelector, videoURL, helpDescription, flag){
    var helpScreen = $('#helperScreen');

    $('p', helpScreen).text(helpDescription);
    $('iframe', helpScreen).attr('src', videoURL);
    $('.disable-help-video', helpScreen).attr('data-flag', flag);
    helpScreen.show();
  }

  var helperScreenHook = function(linkSelector){

    var showScreen = false;
    if (linkSelector.attr('data-show-screen') == 'True'){
      showScreen = true;
    };

    linkSelector.on('click', function(){
      var link = $(this);
      var videoURL = link.attr('data-video-url');
      var helpDescription = link.attr('data-video-description');
      var flag = link.attr('data-screen-flag');
      var showScreen = false;
      if (link.attr('data-show-screen') == 'True'){
        showScreen = true;
      };

      if (showScreen === true){
        drawHelperScreenContent(linkSelector, videoURL, helpDescription, flag);
        linkSelector.each(function(){
          $(this).attr('data-show-screen', 'False');
        });
        return false;
      }
    });

  }

  var disableHelperScreen = function(){
    $('.disable-help-video').on('click', function(evt){
      evt.preventDefault();
      // disable it on background
      var flag = $(this).attr('data-flag');
      var url = $(this).attr('href') + '?flag=' + flag;
      $.get(url);

      $('#helperScreen').hide();
    });
  }

  helperScreenHook($('.edit-block-edit'));
  helperScreenHook($('.edit-block-add'));
  disableHelperScreen();

});
