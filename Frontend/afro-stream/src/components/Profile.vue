<template>

    <div class="bg-yellow-100 flex justify-center items-center min-h-screen flex-col">
        <div
        class=" -mt-28"
      >
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
        <div class=" text-lg text-black-400 -mt-2 mb-2 px-2 py-4 ">
            @digitaltransformers@gmail.com
        </div>
        <!-- Boutons d'actions -->
        <div class="space-y-4">
          <button class="bg-orange-500 text-white py-2 px-6 rounded-lg w-full flex justify-center hover:bg-orange-400 text-lg">Configurer le profil</button>
          <button class="bg-orange-500 text-white py-2 px-6 rounded-lg w-full flex justify-center hover:bg-orange-400 text-lg">Changer le mot de passe</button>
          <button class="bg-orange-500 text-white py-2 px-6 rounded-lg w-full flex justify-center hover:bg-orange-400 text-lg">Favoris</button>
          <button class="bg-orange-500 text-white py-2 px-6 rounded-lg w-full flex justify-center hover:bg-orange-400 text-lg">Historique</button>
          <button class="bg-orange-500 text-white py-2 px-6 rounded-lg w-full flex justify-center hover:bg-orange-400 text-lg">Devenir oganisateur</button>
          <button class="bg-orange-500 text-white py-2 px-6 rounded-lg w-full flex justify-center hover:bg-orange-400 text-lg">Se déconnecter</button>
          <!-- <button class="bg-orange-500 text-white py-2 px-6 rounded-lg w-full flex justify-center hover:bg-orange-400 text-lg">Se déconnecter</button> -->
        </div>

        <!-- Liens en bas -->
        <!-- <div class="flex justify-between mt-6">
          <button class="bg-gray-200 text-gray-800 py-1 px-3 rounded-md hover:bg-gray-300">Paramètres</button>
          <button class="bg-gray-200 text-gray-800 py-1 px-3 rounded-md hover:bg-gray-300">Se déconnecter</button>
        </div> -->
      </div>
      <!-- <div class=" flex flex-col ">
        <span class=" bg-white rounded-full px-3 py-2 text-sm text-[#0B8A58]">
            Evenements / Tickets
        </span>
        <span class=" border border-b-4  -mt-4"></span>
    </div> -->
    </div>

  </template>

  <script>
  export default {
    name: "ProfileComponent",
  };
  </script>
