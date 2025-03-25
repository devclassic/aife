<template>
  <div class="box">
    <div class="toolbar">
      <el-input v-model="data.input" placeholder="请输入问题" class="input" />
      <el-button type="info">开始收音</el-button>
      <el-button type="primary">提交</el-button>
      <el-button type="success">新的对话</el-button>
    </div>
    <div class="content">
      <div>
        <div class="question">你是谁？</div>
        <div class="answer">
          <div class="answer-loading">处理中...</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { reactive } from 'vue'

  const data = reactive({
    input: '',
  })
</script>

<style scoped>
  .box {
    width: 800px;
    margin: 0 auto;
  }

  .toolbar {
    margin-top: 10px;
    vertical-align: middle;
  }

  .input {
    width: 400px;
    margin-right: 12px;
  }

  .content {
    border: 1px solid #ccc;
    margin-top: 10px;
    padding: 10px;
    height: calc(100vh - 60px);
    overflow: auto;
  }

  .qa-box {
    margin-bottom: 20px;
  }

  .question {
    color: red;
  }

  .answer {
    color: blue;
  }

  .answer-loading {
    color: #ccc;
  }
</style>
