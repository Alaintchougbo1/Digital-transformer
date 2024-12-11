import { createRouter, createWebHistory } from 'vue-router';
import PreAccueil from '../components/PreAccueil.vue';
import Accueil from '../components/Accueil.vue';
import HomePage from '../components/Decouvrir.vue';
import Profile from '@/components/Profile.vue';
import Decouvrir from '@/components/HomePage.vue';
// import { name } from '@vue/eslint-config-prettier/skip-formatting';
import AchatBillet from '@/components/AchatBillet.vue';
// import { name } from '@vue/eslint-config-prettier/skip-formatting';
import Evenement from '@/components/Evenement.vue';
import MesTickets from '@/components/MesTickets.vue';
// import { name } from '@vue/eslint-config-prettier/skip-formatting';
import FormOganizer from '@/components/FormOrganizer.vue';

const routes = [
  { path: '/', name: 'PreAccueil', component: PreAccueil },
  { path: '/accueil', name: 'Accueil', component: Accueil },
  { path: '/decouvrir', name: 'Home', component: HomePage },
  { path: '/profile', name: 'Profile', component: Profile },
  { path: '/home', name: 'Decouvrir', component: Decouvrir },
  { path: '/achat', name: 'Achat', component: AchatBillet },
  { path: '/eventfutu', name: 'Eventfutu', component: Evenement },
  { path: '/tickets', name: 'tickets', component: MesTickets },
  { path: '/formorganizer', name: 'Formorganizer', component: FormOganizer },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
