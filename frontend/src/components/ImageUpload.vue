<script setup lang="ts">
import { ref } from 'vue'
import axios from "axios"
import { Upload } from "@element-plus/icons-vue";

const loading = ref(false)
const result = ref<string>('')
const handleUpload = async (file: File) => {
    const formData = new FormData()
    formData.append('image', file)
    loading.value = true
    try {  
        const res = await axios.post('http://localhost:8002/predict', formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
        result.value = res.data.result
    } catch (error) {     
        console.error('API调用失败：', error)
    } finally {
        loading.value = false
    }
}
</script>

<template>
    <div class="upload-container">
        <el-upload action="#" :show-file-list="false" :before-upload="handleUpload">
            <el-button type="primary" :loading="loading">
                <el-icon><Upload/></el-icon>
                上传图片识别
            </el-button>

        </el-upload>
        <el-alert v-if="result" :title="`识别结果: ${result}`" type="success" />
    </div>
</template>