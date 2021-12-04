window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {

        let t_href = event.target

        console.log(t_href.name)
        console.log(t_href.value)

// backup
        $.ajax(
            {
                url: "/baskets/edit/" + t_href.name + "/" + t_href.value + "/",
                success: function (data) {
                    $('.basket_list').html(data.result)
                },

            });
        event.preventDefault()

    })

        $('.card_add_basket').on('click', 'button[type="button"]', function () {

        let t_href = event.target.value
        alert('Товар добавлен в корзину')

        $.ajax(
            {
                url: "/baskets/add/" + t_href + "/",
                success: function (data) {
                    $('.card_add_basket').html(data.result)
                },

            });
        event.preventDefault()

    })

}
