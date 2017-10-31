// Toggle the dashboard when clicked
$("#menu-toggle").click(function(e) {
        e.preventDefault();
    // Hide/show the sidebar when the menu toggle is clicked
        $("#wrapper").toggleClass("toggled");

    // Change the direction of the arrow on the toggle on click
        $(this).toggleClass("glyphicon-minus");
    });

// Toggle the calendar when date field (date_for_review) is clicked
$("#date_for_review").click(function(e) {
    e.preventDefault();
    $( '#date_for_review' ).datepicker();
});

// Toggle the calendar when date field (deadline) is clicked
$("#deadline_date").click(function(e) {
    e.preventDefault();
    $( '#deadline_date' ).datepicker();
});

// Create variable for new XMLHttpRequest object
var xhttp;
if (window.XMLHttpRequest) {
    xhttp = new XMLHttpRequest();
    } else {
    // for IE6 and IE5
     xhttp = new ActiveXObject("Microsoft.XMLHTTP");
 }