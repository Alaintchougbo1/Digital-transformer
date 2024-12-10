<!-- <template>
       <PreAccueil />
</template>

<script setup>
import PreAccueil from './components/PreAccueil.vue';
// import Accueil from './components/Accueil.vue';
</script>

<style>

</style> -->

<template>
  <div class=" text-2xl bg-yellow-100 flex justify-center items-center min-h-screen">
        <PreAccueil v-if="showPreAccueil"/>
    <Accueil v-else />
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import PreAccueil from './components/PreAccueil.vue';
import Accueil from './components/Accueil.vue';

const showPreAccueil = ref(true);

onMounted(() => {
  setTimeout(() => {
    showPreAccueil.value = false; // Passe à Accueil
  }, 3000);
});
</script>

<style>
/* Ajoutez vos styles ici si nécessaire */
</style>

