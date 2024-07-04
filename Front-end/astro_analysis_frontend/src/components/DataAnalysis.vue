<template>
  <div>
    <h1>Data Analysis</h1>
    <button @click="analyzeData">Analyze Data</button>
    <div v-if="result">
      <h2>Analysis Result:</h2>
      <p>Total Entries: {{ result.total_entries }}</p>
      <p>Average Value: {{ result.average_value }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      result: null
    };
  },
  methods: {
    analyzeData() {
      axios.get('http://localhost:8001/data/') // Fetch existing data from data collection
        .then(response => {
          console.log("Fetched Data:", response.data); // Ajoutez ceci pour déboguer
          return axios.post('http://localhost:8002/analyze/', response.data);
        })
        .then(response => {
          console.log("Analysis Result:", response.data); // Ajoutez ceci pour déboguer
          this.result = response.data;
        })
        .catch(error => {
          console.error('There was an error analyzing the data!', error);
        });
    }
  }
};
</script>

<style scoped>
/* Ajoutez vos styles ici */
</style>
