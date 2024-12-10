<template>
  <div class="bg-yellow-100 flex justify-center items-center min-h-screen">
    <div>
      <p class="text-lg text-gray-600 text-center">Bienvenue sur</p>
      <img
        src="/AfroStreamText1.png"
        alt="Logo AfroStream"
        class="w-48 mt-4"
      />
      <p class="mt-4 text-center">Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
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
