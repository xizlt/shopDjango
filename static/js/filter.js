$(function () {
    var max = parseInt($('#filter').data('max-price'))
    var min = parseInt($('#filter').data('min-price'))
    $("#slider-range").slider({
        range: true,
        min: min,
        max: max,
        values: [(max / 2), max - (min)],
        slide: function (event, ui) {
            $("#amount").val("€" + ui.values[0] + " - €" + ui.values[1]);
        }
    });
    $("#amount").val("€" + $("#slider-range").slider("values", 0) +
        " - €" + $("#slider-range").slider("values", 1));


    $('.dropdown-menu a').on('click', function (e) {
        let url = this.action;
        let params = $(this).data('filter');
        // console.log(params)
    })

    $('a.dropdown-item').click(function (e) {
        e.preventDefault();
        $.post(
            $('.dropdown-menu').data('action-url'),
            {filter_name: $(this).data('filter')},
            function (data) {
                if (data) {
                    // var tm = $('#products-row')
                    // tm.empty()
                    // for (var i = 0; i < data.product.length; i++) {
                    //     tm.append('<div>'+ data.product[i].translations__name + '</div>')
                    //    // console.log(data.products[i])
                    // }
                }

            })
    });

});


