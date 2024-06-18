// import {getCookie} from './tools.js';

$(document).ready( function() {


    $(".state-description-button").click( function() {
        var container = $(this).closest(".task-container");
        var description = container.find(".task-description");
        var isDescHidden = description.is(":hidden");

        if (isDescHidden == false) {
            description.hide();
        } else {
            description.show();
        }

    });

    $("textarea").each(function () {
        this.setAttribute("style", "height:" + (this.scrollHeight) + "px;overflow-y:hidden;");
      }).on("input", function () {
        this.style.height = 0;
        this.style.height = (this.scrollHeight) + "px";
      });

    var timer = '';

    $('textarea.task-name').on('keyup', function(e) {
    clearTimeout(timer);
    timer = setTimeout(function() {
        var input = $(e.currentTarget);
        var task = input.closest(".task-container").attr('id-task');
        var column = input.closest(".task-container").attr('id-column');
        var name = input.val();
        var description = input.closest(".task-container").find(".task-description").val();


        $.ajax({
            url: "tasks/update",
            type: 'POST',
            data:  {
                  'task': task,
                  'column': column,
                  'name': name,
                  'description': description,
                  'csrfmiddlewaretoken': getCookie('csrftoken'),
                },            
            success: function(data) {
            },
            });
    }, 300); 
    });


    $('textarea.task-description').on('keyup', function(e) {
        clearTimeout(timer);
        timer = setTimeout(function() {
            var input = $(e.currentTarget);
            var task = input.closest(".task-container").attr('id-task');
            var column = input.closest(".task-container").attr('id-column');
            var name = input.closest(".task-container").find(".task-name").val();
            var description = input.val();
    
    
            $.ajax({
                url: "tasks/update",
                type: 'POST',
                data:  {
                      'task': task,
                      'column': column,
                      'name': name,
                      'description': description,
                      'csrfmiddlewaretoken': getCookie('csrftoken'),
                    },            
                success: function(data) {
                },
                });
        }, 300); 
        });



    $(".add-task").click( function() {
        var column = $(this).attr('id-column');
        $.ajax({
            url: "tasks/add",
            type: 'POST',
            data:  {
                  'column': column,
                  'csrfmiddlewaretoken': getCookie('csrftoken'),
                },            
            success: function(data) {
                window.location.href = "/";
            },
            });
    });

    $(".remove-tasks").click( function() {
        var column = $(this).attr('id-column');
        $.ajax({
            url: "tasks/column/delete",
            type: 'POST',
            data:  {
                    'column': column,
                    'csrfmiddlewaretoken': getCookie('csrftoken'),
                },            
            success: function(data) {
                window.location.href = "/";
            },
            });
        });

    $(".remove-task").click( function() {
        var task = $(this).closest(".task-container").attr('id-task');
        $.ajax({
            url: "tasks/delete",
            type: 'POST',
            data:  {
                    'task': task,
                    'csrfmiddlewaretoken': getCookie('csrftoken'),
                },            
            success: function(data) {
                window.location.href = "/";
            },
            });
        });
  

    $(".change-column-button").click( function() {
        var task = $(this).closest(".task-container").attr('id-task');
        var column = $(this).attr('id-column');
        var name = $(this).closest(".task-container").find(".task-name").val();
        var description = $(this).closest(".task-container").find(".task-description").val();

        $.ajax({
            url: "tasks/update",
            type: 'POST',
            data:  {
                    'task': task,
                    'column': column,
                    'name': name,
                    'description': description,
                    'csrfmiddlewaretoken': getCookie('csrftoken'),
                },            
            success: function(data) {
                window.location.href = "/";
            },
            });
    });

  });