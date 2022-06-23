$(document).ready(function(){
    var mql = window.matchMedia("(max-width: 992px)")

    mediaqueryresponse(mql)

    mql.addListener(mediaqueryresponse) 

    function mediaqueryresponse(mql){
        if (mql.matches) {

            $('header').replaceWith($('<footer/>').html($('header').html()));
            
        } else{
            $('footer').replaceWith($('<header/>').html($('footer').html()));
        }
    }

    $('#profile_link').click(function(){
        window.location.replace("http://127.0.0.1:8000/profile/");
    })
    $('#home_link').click(function(){
        window.location.replace("http://127.0.0.1:8000/home/");
    })
})