<template>
  <div class="bg-yellow-50 min-h-screen">
    <header class="p-4">
      <button
        class="text-gray-700 text-lg font-semibold hover:text-gray-900"
        @click="goBack"
      >
        ← Retour
      </button>
    </header>
    <main class="flex flex-col items-center px-4">
      <section class="text-center bg-white rounded-lg shadow-md p-6 w-full max-w-md mb-6">
        <h1 class="text-2xl font-bold text-gray-800 mb-4">
          We Love EYA - Festival Urbain
        </h1>
        <p class="text-gray-600 mb-2">
          <strong>Date et heure</strong><br />
          28 au 29 Décembre<br />
          19h00
        </p>
        <p class="text-gray-600 mb-2">
          <strong>Lieu</strong><br />
          Palais des congrès
        </p>
        <p class="text-gray-600">
          <strong>Montant</strong><br />
          5000 Fcfa
        </p>
      </section>

      <form
        class="bg-white rounded-lg shadow-md p-6 w-full max-w-md"
        @submit.prevent="processPayment"
      >
        <label
          for="name"
          class="block text-sm font-semibold text-orange-600 mb-2"
        >
          Nom
        </label>
        <input
          type="text"
          id="name"
          v-model="formData.name"
          class="w-full border border-gray-300 rounded-lg p-2 mb-4 focus:outline-none focus:ring focus:ring-orange-400"
          placeholder="Nom"
          required
        />

        <label
          for="email"
          class="block text-sm font-semibold text-orange-600 mb-2"
        >
          Email
        </label>
        <input
          type="email"
          id="email"
          v-model="formData.email"
          class="w-full border border-gray-300 rounded-lg p-2 mb-4 focus:outline-none focus:ring focus:ring-orange-400"
          placeholder="Email"
          required
        />

        <label
          for="phone"
          class="block text-sm font-semibold text-orange-600 mb-2"
        >
          Téléphone
        </label>
        <input
          type="tel"
          id="phone"
          v-model="formData.phone"
          class="w-full border border-gray-300 rounded-lg p-2 mb-4 focus:outline-none focus:ring focus:ring-orange-400"
          placeholder="Téléphone"
          required
        />

        <button
          type="submit"
          class="w-full bg-green-600 text-white py-3 rounded-lg flex items-center justify-center hover:bg-green-700"
        >
          <img src="my-celtiis-logo.png" alt="My Celtiis" class="h-6 mr-2" />
          <span class="font-semibold">PAYER AVEC</span>
        </button>
      </form>
    </main>
  </div>
</template>

<script>
export default {
  name: "AchatBillet",
  data() {
    return {
      formData: {
        name: "",
        email: "",
        phone: "",
      },
    };
  },
  methods: {
    goBack() {
      this.$router.go(-1);
    },
    processPayment() {
      console.log("Données de paiement :", this.formData);
      alert("Paiement en cours...");
    },
  },
};
</script>

<style>
/* Aucun style supplémentaire requis puisque Tailwind CSS est utilisé */
</style>
