<template>
  <div>
    <line-chart :chart-data="datacollection" :options="options"></line-chart>
  </div>
</template>

<script>
import { Line } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, PointElement, LinearScale, CategoryScale } from 'chart.js';
import axios from 'axios';

ChartJS.register(Title, Tooltip, Legend, LineElement, PointElement, LinearScale, CategoryScale);

export default {
  name: 'DataVisualization',
  components: {
    LineChart: Line
  },
  data() {
    return {
      datacollection: {
        labels: [],
        datasets: []
      },
      options: {
        responsive: true,
        maintainAspectRatio: false
      }
    };
  },
  methods: {
    fetchData() {
      axios.get('http://localhost:8000/visualize/1') // Assurez-vous que l'URL est correcte
        .then(response => {
          const visualizationData = response.data.visualization_data;
          const labels = [];
          const datasets = [];

          for (const key in visualizationData) {
            const dataPoints = visualizationData[key];
            const data = dataPoints.map(dp => dp.value);
            const times = dataPoints.map(dp => dp.time);

            labels.push(...times);

            datasets.push({
              label: key,
              backgroundColor: this.getRandomColor(),
              data: data,
              fill: false
            });
          }

          // Assurez-vous que les labels sont uniques
          this.datacollection.labels = [...new Set(labels)];
          this.datacollection.datasets = datasets;
        })
        .catch(error => {
          console.error("Failed to fetch visualization data", error);
        });
    },
    getRandomColor() {
      const letters = '0123456789ABCDEF';
      let color = '#';
      for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
      }
      return color;
    }
  },
  mounted() {
    this.fetchData();
  }
};
</script>

<style scoped>
/* Ajoutez vos styles ici */
</style>
