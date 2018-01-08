$(function () {
    $('.pop').on('click', function () {
        $('.imagepreview').attr('src', $(this).find('img').attr('src'));
        $('#imagemodal').modal('show');
    });
});

$(document).ready(function () {
    $(".btn-pref .btn").click(function () {
        $(".btn-pref .btn").removeClass("btn-primary").addClass("btn-default");
        // $(".tab").addClass("active"); // instead of this do the below
        $(this).removeClass("btn-default").addClass("btn-primary");
    });
});

function fillValuesMatt() {
    document.getElementById("id_username").value = "Matt";
    document.getElementById("id_password").value = "guestguest123123";
}

$("#guestMatt").click(fillValuesMatt);

function fillValuesAnne() {
    document.getElementById("id_username").value = "Anne";
    document.getElementById("id_password").value = "guestguest123123";
}

$("#guestAnne").click(fillValuesAnne);


var $grid = $('.row').masonry({
    // columnWidth: '30%',
    itemSelector: '.grid-item',
    // percentPosition: true
});

// layout Masonry after each image loads
$grid.imagesLoaded().progress( function() {
  $grid.masonry('layout');
});
