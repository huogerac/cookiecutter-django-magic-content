/* Jquery reference for plugin creation:
    http://learn.jquery.com/plugins/basic-plugin-creation/
   Ajax reference for forms:
    http://learn.jquery.com/ajax/ajax-and-forms/
*/

(function($){

    /* JQuery plugin to handle ajax through Django's views without any server
       side changes!
       It will follow the view's response as html, it's perfect for popups
       and can avoid iframes in most of cases.

       The default scope is "body", that means, any server response will
       override body without a page reload.

       Usage:
       $('#myFormId').formjax();
       $('#myFormId').formjax({
         responseScope: '#someDivId'
       });

       Warning: the form MUST HAVE the "action" attribute filled with the
       form's POST url.
    */

    $.fn.formjax = function(options){

        var settings = $.extend({
            responseScope: 'body',
        }, options);

        var responseScope = $(settings.responseScope);
        var form = this;

        form.on('submit', function(evt){

            evt.preventDefault();

            $.ajax({
                url: form.attr('action'),
                type: 'POST',
                dataType: 'html',
                data: form.serialize(),

                beforeSend: function(xhr){
                    /* TODO: this should be available as a settings too */
                    responseScope.html('<p class="bg-primary" style="padding: 15px;">loading...</p>');
                },

                success: function(response){
                    responseScope.html(response);
                }
            });

        });

    }

}(JQuery));


$(function(){

    /* Shorcut to use formjax without any javascript code!
       Just add a class "formjax" inside your form:
       <form action="/my-cool-post-url/" method="POST" class="formjax">
            <!-- form content goes here -->
       </form>
    */

    $('.formjax').each(function(){
        $(this).formjax();
    });

});