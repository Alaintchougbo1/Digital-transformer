<!-- <template>
       <PreAccueil />
</template>

<script setup>
import PreAccueil from './components/PreAccueil.vue';
// import Accueil from './components/Accueil.vue';
</script>

<style>

</style> -->

<!-- <template>
  <div class=" text-2xl bg-yellow-100 flex justify-center items-center min-h-screen">
        <PreAccueil v-if="showPreAccueil"/>
    <Profile v-else />
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import PreAccueil from './components/PreAccueil.vue';
import Accueil from './components/Accueil.vue';
import Decouvrir from "./components/Decouvrir.vue";
import Loader from "./components/Loader.vue";
import HomePage from "./components/HomePage.vue";
import Profile from "./components/Profile.vue";

const showPreAccueil = ref(true);

onMounted(() => {
  setTimeout(() => {
    showPreAccueil.value = false; // Passe à Accueil
  }, 3000);
});
</script>

<style>
/* Ajoutez vos styles ici si nécessaire */
</style> -->


<template>
  <div class="text-2xl bg-yellow-100 min-h-screen">
    <router-view />
    <!-- <RouterLink to="/decouvrir"></RouterLink> -->

  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
/* Ajoute des styles globaux si nécessaire */
</style>
