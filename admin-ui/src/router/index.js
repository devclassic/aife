import { createRouter, createWebHashHistory } from 'vue-router'

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: '/login', component: () => import('../views/login/Login.vue') },
    { path: '/', component: () => import('../views/main/Main.vue') },
  ],
})

export default router
