<!-- <template>
    <div class="bg-yellow-100 flex justify-center items-center min-h-screen">
      <img
        src="/AfroStream.png"
        alt="AfroStream Logo"
        class=" w-full max-w-xs sm:max-w-sm md:max-w-md lg:max-w-lg"
      />
    </div>
  </template>

  <style scoped>
  </style>
   -->


   <template>
    <div class="bg-yellow-100 flex justify-center items-center min-h-screen">
      <img
        src="/AfroStream.png"
        alt="AfroStream Logo"
        class="w-48 max-w-xs"
      />
    </div>
  </template>

  <script>
  export default {
    name: 'PreAccueil',
    mounted() {
      setTimeout(() => {
        this.$router.push('/accueil');
      }, 3000);
    },
  };
  </script>

  <style scoped></style>

