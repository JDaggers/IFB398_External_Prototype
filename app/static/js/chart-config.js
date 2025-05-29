import merge from 'https://cdn.jsdelivr.net/npm/lodash.merge@4.6.2/+esm';

export const baseChartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    title:{
      display: true,
        font:{
        size: 20,
        weight: 'bold'
      }
    },
    legend: {
      position: 'bottom',
      labels: {
        color: '#999',
        font: {
          size: 14,
          family: 'Arial'
        }
      }
    },
    tooltip: {
      backgroundColor: '#222',
      titleColor: '#fff',
      bodyColor: '#ddd'
    }
  },
  scales: {
    x: {
      ticks: {
        color: 'Black',
        font: { size: 12 }
      },
      grid: { color: '#444' }
    },
    y: {
      beginAtZero: true,
      ticks: {
        color: '#aaa',
        font: { size: 12 }
      },
      grid: { color: '#444' }
    }
  }
};

export function mergeChartOptions(customOptions = {}) {
  return merge({}, baseChartOptions, customOptions);
}
