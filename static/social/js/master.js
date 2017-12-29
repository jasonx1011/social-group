$(function () {
    $('.pop').on('click', function () {
        $('.imagepreview').attr('src', $(this).find('img').attr('src'));
        $('#imagemodal').modal('show');
    });
});

$(function () {
    $('.pop-text').on('click', function () {
        $('.imagepreview').attr('src', $(this).find('h4').attr('src'));
        $('#imagemodal').modal('show');
    });
});