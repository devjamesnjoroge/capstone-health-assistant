$(document).ready(function(){

    function wrapLinks(){
        host = 'https://health-assistentee.herokuapp.com/';
        locations = ['home', 'dashboard', 'history', 'posts', 'diet', 'profile']
        locations.map((loc)=>{
            $('#'+loc+'_link').click(function(){
                window.location.replace(host+loc+"/");
            })
        })
    }

    var mql = window.matchMedia("(max-width: 992px)")

    mediaqueryresponse(mql)

    mql.addListener(mediaqueryresponse) 

    function mediaqueryresponse(mql){
        if (mql.matches) {

            $('header').replaceWith($('<footer/>').html($('header').html()));
            wrapLinks()
            
        } else{
            $('footer').replaceWith($('<header/>').html($('footer').html()));
            wrapLinks()
        }
    }

})