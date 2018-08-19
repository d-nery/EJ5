const onStateClick = (event, args) => {
    console.log(event);
    console.log(args);

    current_estado = args.shortLabel;
    onStateChange();
}

const onStateChange = () => {
    $('#column-chart').insertFusionCharts({
        type: "column2d",
        renderAt: "map",
        width: "100%",
        height: "100%",
        dataFormat: "jsonurl",
        dataSource: 'http://localhost:8000/static/map1-' + current_estado + '.json',
    });
}

var brazil_map = undefined;
var current_data = 0;
var current_estado = "SP";

$(document).ready(() => {
    $('.list-unstyled > li').each((i, el) => {
        $(el).on('click', () => {
            $('.list-unstyled > li').removeClass('active');
            $(el).addClass('active');
            brazil_map.setChartDataUrl('http://localhost:8000/static/'+ $(el).data('map') + '.json', 'json');
            current_data = i;
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
        dataSource: 'http://localhost:8000/static/map1.json',

        events: {
            entityClick: onStateClick
        }
    });

    brazil_map.render();
});
