$(document).ready(function() {


    $('#fn').keyup(function() {
        var data = $('#registation').serialize();
        $.ajax({
                method: 'POST',
                url: '/username',
                data: data
            })
            .done(function(res) {
                $('#namecheck').html(res)
            })

    })

    // $('#search12').keyup(function() {
    //     console.log('history')
    //     var jscode = $('searchform').serialize()
    //     $.ajax({
    //             url: "/usersearch",
    //             method: "POST",
    //             data: jscode
    //         })
    //         .done(function(res) {
    //             $('#searchresult').html(res)
    //         })




    // })



})