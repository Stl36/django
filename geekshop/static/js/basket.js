window.onload = function () {
    $('.basket-list').on('click', 'input[type="number"]', function () {

        let t_href = event.target

        console.log(t_href.name)
        console.log(t_href.value)

// Код ниже не отрисовывает корзину при обновлении автоматически. Почему?
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