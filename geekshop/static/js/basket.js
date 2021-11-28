window.onload = function () {
    $('.basket-list').on('click', 'input[type="number"]', function () {

        let t_href = event.target

        $.ajax(
            {
                url: "/baskets/edit/" + t_href.name + "/" + t_href.value + "/",
                success: function (data) {
                    $('.basket_list').html(data.result)
                },

            });
        event.preventDefault()

    })
}