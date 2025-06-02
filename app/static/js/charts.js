import { mergeChartOptions } from './chart-config.js';

document.addEventListener("DOMContentLoaded", () => {
    const charts = window.chartData;
    charts.forEach(config => {
        const ctx = document.getElementById(config.id.trim());
        if (!ctx) return;
        const chartCtx = ctx.getContext('2d');

        const options = mergeChartOptions({
            plugins: {
                title: {
                    display: true,
                    text: config.title
                }
            },
            scales: {
                x: {
                    display: true,
                    title: {
                        display: config.xLabel != null ? true : false,
                        text: config.xLabel
                    }
                },
                y: {
                    display: true,
                    title: {
                        display: config.yLabel != null ? true : false,
                        text: config.yLabel
                    }
                },
            }
        });

        new Chart(chartCtx, {
            type: config.type|| 'bar', 
            data: {
                labels: config.labels,
                datasets:[{
                    label: config.datasetLabel,
                    data: config.data,
                    backgroundColor: config.backgroundColor || null,
                    borderwidth: 1
                }]
            },
            options
        });
    });
});
