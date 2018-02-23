$(document).ready(function() {
    $('.Donebutton').on('click', TaskToDone);
});

function TaskToDone() {
    putNewStatus(this.getAttribute('pk'), $(this).is('Donebutton'));
}

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );
                break;
            }
        }
    }
    return cookieValue;
}

function putNewStatus(ID, markAsDone) {
    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    var todoURL = '/' + ID + '/';
    $.getJSON(todoURL, function(data) {
        data.mark_as_done = markAsDone;
        $.ajax({
            url: todoURL,
            type: 'PUT',
            contentType: 'application/json',
            data: JSON.stringify(data),
            success: function() {
                location.reload();
            }
        });
    });
}
