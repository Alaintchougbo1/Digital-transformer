import { createRouter, createWebHistory } from 'vue-router';
import PreAccueil from '../components/PreAccueil.vue';
import Accueil from '../components/Accueil.vue';
import HomePage from '../components/Decouvrir.vue';
import Profile from '@/components/Profile.vue';
import Decouvrir from '@/components/HomePage.vue';

const routes = [
  { path: '/', name: 'PreAccueil', component: PreAccueil },
  { path: '/accueil', name: 'Accueil', component: Accueil },
  { path: '/decouvrir', name: 'Home', component: HomePage },
  { path: '/profile', name: 'Profile', component: Profile },
  { path: '/home', name: 'decouvrir',component: Decouvrir },
  {  path: }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
