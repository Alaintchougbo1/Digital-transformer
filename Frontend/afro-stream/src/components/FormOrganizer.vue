<template>
  <div class="flex flex-col min-h-screen bg-yellow-200">
    <!-- Contenu principal -->
    <div class="flex-1 flex justify-center items-center overflow-y-auto">
      <section class="w-full max-w-md p-4">
        <form
          class="bg-green-600 text-center p-6 rounded-2xl shadow-md"
          @submit.prevent="handleSubmit"
        >
          <h2 class="bg-white text-black inline-block py-2 px-6 rounded-full text-lg font-semibold mb-6">
            Formulaire
          </h2>

          <input
            type="text"
            v-model="form.nom"
            placeholder="Nom"
            class="w-full p-3 mb-4 rounded-lg border-none text-lg"
            required
          />
          <input
            type="text"
            v-model="form.prenom"
            placeholder="Prénom"
            class="w-full p-3 mb-4 rounded-lg border-none text-lg"
            required
          />
          <input
            type="tel"
            v-model="form.telephone"
            placeholder="Numéro de téléphone"
            class="w-full p-3 mb-4 rounded-lg border-none text-lg"
            required
          />
          <input
            type="text"
            v-model="form.entreprise"
            placeholder="Nom de l'entreprise"
            class="w-full p-3 mb-4 rounded-lg border-none text-lg"
            required
          />
          <input
            type="text"
            v-model="form.siteweb"
            placeholder="Site web / réseau social"
            class="w-full p-3 mb-4 rounded-lg border-none text-lg"
          />
          <input
            type="text"
            v-model="form.profession"
            placeholder="Profession"
            class="w-full p-3 mb-4 rounded-lg border-none text-lg"
            required
          />

          <select
            v-model="form.categorie"
            class="w-full p-3 mb-4 rounded-lg border-none text-lg"
            required
          >
            <option value="" disabled selected>Catégorie</option>
            <option value="cat1">Catégorie 1</option>
            <option value="cat2">Catégorie 2</option>
          </select>

          <input
            type="text"
            v-model="form.objectif"
            placeholder="Objectif"
            class="w-full p-3 mb-4 rounded-lg border-none text-lg"
            required
          />
          <textarea
            v-model="form.bio"
            rows="4"
            placeholder="Bio"
            class="w-full p-3 mb-4 rounded-lg border-none text-lg"
          ></textarea>

          <button
            type="submit"
            class="w-full bg-orange-500 text-white py-3 rounded-lg text-lg font-semibold hover:bg-orange-600"
          >
            Valider
          </button>
        </form>
      </section>
    </div>

    <!-- Footer Navigation -->
    <footer
      class="bg-[#0B8A58] fixed bottom-0 left-0 w-full flex justify-around items-center p-4 text-white text-xl z-50"
    >
      <RouterLink to="/home">
        <i class="fas fa-home"></i>
      </RouterLink>
      <RouterLink to="/decouvrir">
        <i class="fas fa-video"></i>
      </RouterLink>
      <i class="fas fa-ticket-alt"></i>
      <RouterLink to="/profile">
        <i class="fas fa-user"></i>
      </RouterLink>
    </footer>
  </div>
</template>

<script>
export default {
  name: "FormOrganizer",
  data() {
    return {
      form: {
        nom: "",
        prenom: "",
        telephone: "",
        entreprise: "",
        siteweb: "",
        profession: "",
        categorie: "",
        objectif: "",
        bio: "",
      },
    };
  },
  methods: {
    handleSubmit() {
      console.log("Données du formulaire :", this.form);
      alert("Formulaire soumis !");
    },
  },
};
</script>

<style scoped>
@import "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css";
</style>
