$(document).ready(function() {
    function updateContent() {
        $('.autorefresh').each(function () {
            var el = $(this);
            el.load(el.data('url'));
        });
    }
    updateContent();
    window.setInterval(updateContent, 1000);

    $('.Donebutton').on('click', TaskToDone);
});

function TaskToDone() {
    $.ajax({
        url: $('.Donebutton').data('url'),
        success: function (data) {
            data.mark_as_done = !data.mark_as_done;
            $('.Donebutton').html(data);
        }
    });
}
