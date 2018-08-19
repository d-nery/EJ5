var brazil_map = undefined;
var column_chart_map1 = undefined;
var current_data = 1;
var current_estado = "SP";

const onStateClick = (event, args) => {
    current_estado = args.shortLabel;
    onStateChange();
}

const onStateChange = () => {
    column_chart_map1.setChartDataUrl('http://127.0.0.1:5000/map' + current_data + '/' + current_estado, 'json');
}

$(document).ready(() => {
    $('.list-unstyled > li').each((i, el) => {
        $(el).on('click', () => {
            $('.list-unstyled > li').removeClass('active');
            $(el).addClass('active');
            current_data = $(el).data('map').slice(-1);
            brazil_map.setChartDataUrl('http://127.0.0.1:5000/'+ $(el).data('map'), 'json');

            $('#details-btn').off('click')

            if (current_data === "2") {
                $('#button-details').removeClass('hidden');
                $('#column-chart').removeClass('no-btn');
                $('#details-btn').on('click', () => {
                    window.location = window.location.href + 'disparities';
                });
            } else {
                $('#button-details').addClass('hidden');
                $('#column-chart').addClass('no-btn');
            }

            onStateChange();
        });
    });

    onStateChange();
});

FusionCharts.ready(() => {
    brazil_map = new FusionCharts({
        type: "maps/brazil",
        renderAt: "map",
        width: "100%",
        height: "100%",
        dataFormat: "jsonurl",
        dataSource: 'http://127.0.0.1:5000/map1',

        events: {
            entityClick: onStateClick
        }
    });

    column_chart_map1 = new FusionCharts({
        type: "column2d",
        renderAt: "column-chart",
        width: "100%",
        height: "100%",
        dataFormat: "jsonurl",
        dataSource: 'http://127.0.0.1:5000/map' + current_data + '/' + current_estado,
    })

    brazil_map.render();
    column_chart_map1.render();
});
