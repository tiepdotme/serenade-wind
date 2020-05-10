AmCharts.makeChart("chartdiv",
    {
        "type": "pie",
        "balloonText": "[[title]]<br><span style='font-size:14px'><b>[[value]]</b> ([[percents]]%)</span>",
        "depth3D": 5,
        "gradientType": "linear",
        "baseColor": "#2C3E50",
        "colors": [
            "#5d8ea3",
            "#767676",
            "#fff",
            "#2c3e50",
            "#ad82ad",
            "#2f4074",
            "#448e4d",
            "#b7b83f",
            "#b9783f",
            "#b93e3d",
            "#913167"
        ],
        "titleField": "activity",
        "valueField": "hours",
        "labelColorField": "#FFFFFF",
        "labelTickColor": "#FFFFFF",
        "color": "#FFFFFF",        
        "fontSize": 12,
        "theme": "light",
        "allLabels": [],
        "balloon": {},
        "titles": [],
        "dataProvider": [
            {
                "activity": "Work",
                "hours": "50"
            },
            {
                "activity": "Commute",
                "hours": "20"
            },
            {
                "activity": "Sleep",
                "hours": "50"
            },
            {
                "activity": "Personal Time",
                "hours": "48"
            }
        ]
    }
);