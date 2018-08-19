const onStateClick = (event, args) => {
    console.log(event);
    console.log(args);

    current_estado = args.shortLabel;
    onStateChange();
}

const onStateChange = () => {
    $('#column-chart').insertFusionCharts({
        type: "column2d",
        width: "100%",
        height: "100%",
        dataFormat: "jsonurl",
        dataSource: 'http://127.0.0.1:5000/map' + current_data + '/' + current_estado,
    });
}

var brazil_map = undefined;
var current_data = 1;
var current_estado = "SP";

$(document).ready(() => {
    $('.list-unstyled > li').each((i, el) => {
        $(el).on('click', () => {
            $('.list-unstyled > li').removeClass('active');
            $(el).addClass('active');
            current_data = i + 1;
            brazil_map.setChartDataUrl('http://127.0.0.1:5000/'+ $(el).data('map'), 'json');
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

    brazil_map.render();
});
