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
                text: config.label
            }
            }
        });

        new Chart(chartCtx, {
            type: config.type|| 'bar', 
            data: {
                labels: config.labels,
                datasets:[{
                    label: config.label,
                    data: config.data,
                    backgroundColor: config.backgroundColor || 'rgba(54, 162, 235, 0.6)',
                    borderwidth: 1
                }]
            },
            options
        });
    });
});
