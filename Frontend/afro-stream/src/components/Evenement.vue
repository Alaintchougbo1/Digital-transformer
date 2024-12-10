<template>
  <div class="bg-amber-100 min-h-screen font-sans">
    <!-- Header avec bouton de retour -->
    <header class="p-4">
      <button class="text-gray-800 text-lg cursor-pointer hover:underline">
        ← Retour
      </button>
    </header>

    <!-- Image de l'événement -->
    <main>
      <img
        src="/eya.jpeg"
        alt="Artiste sur scène"
        class="w-full h-auto block"
      />

      <!-- Informations de l'événement -->
      <section class="p-5">
        <div class="flex items-center mb-5">
          <img
            src="/eya_logo.png"
            alt="Logo événement"
            class="w-12 h-12 rounded-full mr-4"
          />
          <div>
            <h1 class="text-xl font-bold mb-1">We Love EYA - Festival Urbain</h1>
            <p class="text-gray-500 text-sm">0 vue . À venir</p>
          </div>
        </div>

        <!-- Description de l'événement -->
        <h2 class="text-lg font-semibold mb-2">Description</h2>
        <p class="text-base mb-5 leading-6">
          Les fans de musique Afrobeat et Urbaine du monde entier se donnent rendez-vous à Cotonou !
          Le festival <strong>#WeLoveEya 2024</strong> est l'événement incontournable de la fin d'année,
          avec plus de <strong>50 000 festivaliers</strong> attendus du 27 au 28 décembre 2024, à la PLACE DE L'AMAZONE à Cotonou !
          Venez vivre une expérience culturelle unique avec plus de <strong>30 artistes</strong> parmi les plus grands
          qui se produiront sur scène pour votre plus grand plaisir.
        </p>

        <!-- Bouton d'achat -->
        <button
          class="block w-full max-w-md mx-auto bg-green-600 hover:bg-green-700 text-white py-4 text-lg font-bold rounded-lg transition-colors">
          ACHETER
        </button>
      </section>
    </main>
  </div>
</template>

<script>
export default {
  name: 'EventDetail',
};
</script>

<style scoped>
/* Les styles Tailwind ont remplacé la plupart des styles CSS */
</style>
