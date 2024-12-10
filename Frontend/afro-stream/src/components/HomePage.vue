<template>
    <div class="flex flex-col h-screen bg-yellow-50">
      <!-- Barre de recherche -->
      <div
        :class="{ hidden: hideHeader }"
        class="header h-40 w-60 ml-12 transition-all duration-500"
      >
        <img src="/log.png" height="50px" alt="" />
      </div>
  
      <div :class="{ hidden: hideHeader }" class="search-bar p-4 transition-all duration-500">
        <input
          type="text"
          placeholder="Rechercher sur Afro Stream"
          class="w-full p-2 rounded-md border border-gray-300 focus:outline-none focus:ring-2 focus:ring-yellow-500"
        />
      </div>
  
      <!-- Événements -->
      <main
        class="flex-1 overflow-y-auto space-y-4 px-4"
        @scroll="handleScroll"
        ref="scrollContainer"
      >
        <div
          v-for="event in events"
          :key="event.id"
          :style="{ backgroundImage: `url(${event.image})` }"
          class="relative bg-cover bg-center h-52 rounded-lg p-4 text-white flex flex-col justify-between"
        >
          <div>
            <h3 class="text-lg font-bold">{{ event.title }}</h3>
            <p class="text-sm">{{ event.views }} vues . {{ event.date }}</p>
          </div>
          <span
            :class="{
              'bg-red-600': event.status === 'Terminée',
              'bg-green-600': event.status === 'Bientôt'
            }"
            class="absolute top-4 right-4 px-2 py-1 text-xs rounded-md uppercase"
          >
            {{ event.status }}
          </span>
        </div>
      </main>
  
      <!-- Pied de page -->
      <footer class="bg-green-600 flex justify-around items-center p-4 text-white text-xl">
        <i class="fas fa-home"></i>
        <i class="fas fa-video"></i>
        <i class="fas fa-ticket-alt"></i>
        <i class="fas fa-user"></i>
      </footer>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        events: [
          {
            id: 1,
            title: "We Love EYA - Festival Urbain",
            views: 0,
            date: "A venir",
            status: "Bientôt",
            image: "/eya.jpeg",
          },
          {
            id: 2,
            title: "Vodun Days 10 Janvier",
            views: 500,
            date: "Il y a 11 mois",
            status: "Terminée",
            image: "vodun.jpg",
          },
          {
            id: 3,
            title: "HackerLab 2024 ASIN",
            views: 100,
            date: "Il y a 3 mois",
            status: "Terminée",
            image: "hackerlab.jpg",
          },
          {
            id: 4,
            title: "Celtiis Summer Show",
            views: 600,
            date: "Il y a 3 mois",
            status: "Terminée",
            image: "/Celtiis.jpeg",
          },
        ],
        hideHeader: false,
      };
    },
    methods: {
      handleScroll() {
        const container = this.$refs.scrollContainer;
        this.hideHeader = container.scrollTop > 5;
      },
    },
  };
  </script>
  
  <style>
  @import "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css";
  </style>
  