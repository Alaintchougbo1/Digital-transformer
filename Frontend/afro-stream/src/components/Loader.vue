<template>
    <!-- <div class="flex items-center justify-center h-screen bg-gradient-to-r from-green-200 to-orange-200"> -->
      <div class="flex space-x-2">
        <div
          v-for="(dot, index) in dots"
          :key="index"
          :class="[
            'h-6 w-6 rounded-full transition-transform duration-300',
            dot.active ? 'scale-125 bg-orange-500' : 'bg-green-500',
          ]"
        ></div>
      </div>
    <!-- </div> -->
  </template>
  
  <script>
  export default {
    data() {
      return {
        dots: [
          { active: true },
          { active: false },
          { active: false },
        ],
        currentIndex: 0,
      };
    },
    mounted() {
      this.startAnimation();
    },
    methods: {
      startAnimation() {
        setInterval(() => {
          this.dots[this.currentIndex].active = false;
          this.currentIndex = (this.currentIndex + 1) % this.dots.length;
          this.dots[this.currentIndex].active = true;
        }, 500); // Change dot every 500ms
      },
    },
  };
  </script>
  
  <style scoped>
  /* Optionally, you can style more here if needed */
  </style>