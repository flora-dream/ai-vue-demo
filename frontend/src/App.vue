<script setup lang="ts">
import ImageUpload from './components/ImageUpload.vue'
</script>

<template>
  <div class="container">
    <h1>AI图像识别演示（vue3）版</h1>
    <ImageUpload></ImageUpload>
  </div>
</template>

<style scoped>
.container {
  max-width: 600px;
  margin: 2rem auto;
  padding: 20px;
}
</style>
