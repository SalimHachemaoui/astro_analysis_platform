<template>
  <div id="app">
    <header>
      <h1>Astro Analysis Platform</h1>
    </header>
    <main>
      <DataCollection />
      <DataAnalysis />
      <DataVisualization />
      <NotificationList />
    </main>
  </div>
</template>

<script>
import DataCollection from './components/DataCollection.vue';
import DataAnalysis from './components/DataAnalysis.vue';
import DataVisualization from './components/DataVisualization.vue';
import NotificationList from './components/NotificationList.vue';

export default {
  name: 'App',
  components: {
    DataCollection,
    DataAnalysis,
    DataVisualization,
    NotificationList,
  }
};
</script>

<style>
/* Ajoutez vos styles ici */
</style>
