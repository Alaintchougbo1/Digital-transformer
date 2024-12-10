<template>
  <div class="bg-yellow-100 flex justify-center items-center min-h-screen">
  <div class="flex flex-col justify-center items-center">
    <!-- Welcome text -->
    <p class="text-lg text-gray-600 text-center">Bienvenue sur</p>

    <!-- Logo text with enhanced styles -->
    <span class="text-green-900 font-bold text-4xl tracking-wide drop-shadow-lg">
      Afro Steam
    </span>

    <!-- Description text -->
    <p class="mt-4 text-center text-gray-700 max-w-md">
      Les Événements qui Comptent, Toujours à Portée de Main
    </p>
  </div>
</div>

</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Accueil",
  mounted() {
    setTimeout(() => {
      this.$router.push('/home');
    }, 3000); // 3000 millisecondes = 3 secondes
  },
};
</script>

<style scoped></style>
