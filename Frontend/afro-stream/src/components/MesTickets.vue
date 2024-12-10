<template>
  <div class="bg-amber-100 min-h-screen font-sans flex items-center justify-center">
    <div class="w-11/12 max-w-md bg-amber-100 rounded-2xl overflow-hidden">
      <!-- Barre de retour -->
      <header class="flex items-center p-4 bg-amber-100">
        <RouterLink to="/home">
        <button class="text-xl cursor-pointer text-gray-800 hover:underline">&larr; Retour</button>
      </RouterLink>
        <h1 class="flex-grow text-center text-xl font-bold">Mes Tickets</h1>
      </header>

      <!-- Liste des tickets -->
      <main class="p-4 flex flex-col space-y-4">
        <div class="flex items-center p-4 bg-white rounded-xl shadow-md">
          <img
            src="/eya.jpeg"
            alt="Afro music Festival"
            class="w-12 h-12 rounded-lg object-cover mr-4"
          />
          <div class="flex-grow">
            <h3 class="text-lg font-bold">Afro music Festival</h3>
            <p class="text-sm text-gray-600">10/12/2024<br>AFR Music Capital 2024</p>
          </div>
          <span class="text-xl text-gray-600">&rarr;</span>
        </div>

        <div class="flex items-center p-4 bg-white rounded-xl shadow-md">
          <img
            src="/eya.jpeg"
            alt="Live party"
            class="w-12 h-12 rounded-lg object-cover mr-4"
          />
          <div class="flex-grow">
            <h3 class="text-lg font-bold">Live party</h3>
            <p class="text-sm text-gray-600">11/12/2024<br>AFR Music Capital 2024</p>
          </div>
          <span class="text-xl text-gray-600">&rarr;</span>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
// import { RouterLink } from 'vue-router';

export default {
  name: 'MesTickets',
};
</script>

<style scoped>
/* La plupart des styles ont été remplacés par des classes Tailwind */
</style>
