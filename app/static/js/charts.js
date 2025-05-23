document.addEventListener("DOMContentLoaded", () => {
    const charts = window.chartData;

    charts.forEach(config => {
        const ctx = document.getElementById(config.id.trim()).getContext('2d');

        new Chart(ctx, {
            type: config.type || 'bar',
            data: {
                labels: config.labels,
                datasets: [{
                    label: config.label,
                    data: config.data,
                    backgroundColor: config.backgroundColor || 'rgba(54, 162, 235, 0.6)',
                    borderColor: config.borderColor || 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                }]
            },
            options: config.options || {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x:{
                        ticks:{
                            font:{
                                size:14
                            }
                        }
                    },
                    y: {
                        beginAtZero: true,
                        ticks:{
                            font:{
                                size: 14
                            }
                        }
                    }
                },
                layout:{
                    padding:{
                        left:5
                    }
                },
                plugins:{
                    legend:{
                        labels:{
                            font:{
                                size: 16
                            }
                        }
                    },
                    title:{
                        display: true,
                        text: config.label || '',
                        align: 'start',
                        padding:{
                            top:10,
                        },
                        font:{
                            size:18
                            
                        }
                    },
                }
            }
        });
    });
});
