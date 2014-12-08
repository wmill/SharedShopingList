$(document).foundation();

$(document).ready(function(){

  //closes all open forms
  var resetPage = function(){
    $('.shopping-item-div .view-item').removeClass('hide');
    $('.shopping-item-div .edit-item').addClass('hide');
  };

  $('.shopping-item-div .view-item').click(function(e){
    resetPage();

    var item_id, el, target_selector;

    el = e.currentTarget;
    item_id = $(el).data('item-id');

    target_selector = '#shopping-item-' + item_id;


    $(target_selector + ' .view-item').addClass('hide');
    $(target_selector + ' .edit-item').removeClass('hide');

    var $target_input = $(target_selector + ' .new-item-name');
    $target_input.focus();

    //trick to set focus to the end
    $target_input.val($target_input.val());



    //don't bubble
    e.stopPropagation();
  });

  $('body').click(function(){
    resetPage();
  });

  $('.shopping-item-div').click(function(e){
    //don't bubble
    e.stopPropagation();
  });

});