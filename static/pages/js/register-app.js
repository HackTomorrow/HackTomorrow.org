const title = document.querySelector('title');
let clicked = false;

$('.message a').click(function(){
    $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
    if (clicked) {
        title.text = "Welcome Back | HackTomorrow";
    }
    else {
        title.text = "Become a Member | HackTomorrow";
    }
    clicked = !clicked;
});