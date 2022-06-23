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
})