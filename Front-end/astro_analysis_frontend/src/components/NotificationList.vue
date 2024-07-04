<template>
  <div>
    <h2>Notifications</h2>
    <ul>
      <li v-for="notification in notifications" :key="notification.timestamp">
        {{ notification.timestamp }} - {{ notification.message }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      notifications: [],
    };
  },
  created() {
    this.fetchNotifications();
    // Vérifiez régulièrement les notifications toutes les 10 secondes
    setInterval(this.fetchNotifications, 10000);
  },
  methods: {
    async fetchNotifications() {
      try {
        const response = await axios.get('http://localhost:8004/notifications/');
        this.notifications = response.data;
      } catch (error) {
        console.error('There was an error fetching notifications!', error);
      }
    },
  },
};
</script>
