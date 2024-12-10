import { createRouter, createWebHistory } from 'vue-router';
import PreAccueil from '../components/PreAccueil.vue';
import Accueil from '../components/Accueil.vue';
import HomePage from '../components/HomePage.vue';
import Profile from '@/components/Profile.vue';
import Decouvrir from '@/components/Decouvrir.vue';

const routes = [
  { path: '/', name: 'PreAccueil', component: PreAccueil },
  { path: '/accueil', name: 'Accueil', component: Accueil },
  { path: '/home', name: 'Home', component: HomePage },
  { path: '/profile', name: 'Profile', component: Profile },
  { path: '/decouvrir', name: 'decouvrir',component: Decouvrir },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
