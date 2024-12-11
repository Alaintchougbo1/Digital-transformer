<template>
  <div class="bg-yellow-100 flex flex-col min-h-screen">
    <!-- Contenu principal -->
    <div class="flex-1 flex flex-col justify-center items-center">
      <div class="-mt-28">
        <img src="/log.png" height="50px" width="200px" alt="" />
      </div>
      <div class="w-80 p-4 -mt-14">
        <!-- Section de l'avatar et du nom -->
        <div class="flex items-center mb-6">
          <img
            class="w-20 h-20 rounded-full border-4 border-orange-500 object-cover"
            src="/profil.jpeg"
            alt="Avatar"
          />
          <div class="ml-4">
            <h2 class="text-lg font-bold text-gray-800">Max HGD</h2>
            <p class="text-sm text-gray-500">@maxfhgd2024</p>
          </div>
        </div>
        <div class="text-lg text-black-400 -mt-2 mb-2 px-2 py-4">
          @digitaltransformers@gmail.com
        </div>
        <!-- Boutons d'actions -->
        <div class="space-y-4">
          <button
            class="bg-orange-500 text-white py-2 px-6 rounded-lg w-full flex justify-center hover:bg-orange-400 text-lg"
          >
            Configurer le profil
          </button>
          <button
            class="bg-orange-500 text-white py-2 px-6 rounded-lg w-full flex justify-center hover:bg-orange-400 text-lg"
          >
            Changer le mot de passe
          </button>
          <button
            class="bg-orange-500 text-white py-2 px-6 rounded-lg w-full flex justify-center hover:bg-orange-400 text-lg"
          >
            Favoris
          </button>
          <button
            class="bg-orange-500 text-white py-2 px-6 rounded-lg w-full flex justify-center hover:bg-orange-400 text-lg"
          >
            Historique
          </button>
          <RouterLink to="/formorganizer">
            <button
              class="bg-orange-500 text-white py-2 px-6 rounded-lg w-full flex justify-center hover:bg-orange-400 text-lg mt-4"
            >
              Devenir organisateur
            </button>
          </RouterLink>
          <button
            class="bg-orange-500 text-white py-2 px-6 rounded-lg w-full flex justify-center hover:bg-orange-400 text-lg"
          >
            Se déconnecter
          </button>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <footer class="bg-[#0B8A58] flex justify-around items-center p-4 text-white text-xl">
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
  name: "ProfileComponent",
};
</script>

<style>
@import "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css";
</style>
