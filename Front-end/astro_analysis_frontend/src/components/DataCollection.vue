<template>
    <div>
      <h1>Data Collection</h1>
      <input v-model="timestamp" placeholder="Timestamp" />
      <input v-model="value" placeholder="Value" />
      <input v-model="instrumentId" placeholder="Instrument ID" />
      <button @click="collectData">Collect Data</button>
      <button @click="fetchData">Fetch Data</button>
      <ul>
        <li v-for="(d, index) in data" :key="index">
          {{ d.timestamp }} - {{ d.value }} - {{ d.instrument_id }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        data: [],
        timestamp: '',
        value: '',
        instrumentId: ''
      };
    },
    methods: {
      collectData() {
        axios.post('http://localhost:8001/data/', [
          {
            timestamp: this.timestamp,
            value: parseFloat(this.value), // Assurez-vous que la valeur est un nombre
            instrument_id: this.instrumentId
          }
        ])
        .then(() => {
          this.fetchData(); // Refresh data after collection
          this.timestamp = '';
          this.value = '';
          this.instrumentId = '';
        })
        .catch(error => {
          console.error('There was an error collecting the data!', error);
        });
      },
      fetchData() {
        axios.get('http://localhost:8001/data/')
        .then(response => {
          this.data = response.data;
        })
        .catch(error => {
          console.error('There was an error fetching the data!', error);
        });
      }
    },
    mounted() {
      this.fetchData(); // Fetch data when the component is mounted
    }
  };
  </script>
  
  <style scoped>
  /* Ajoutez vos styles ici */
  </style>
  