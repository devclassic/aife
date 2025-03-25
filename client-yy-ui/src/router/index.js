import { createRouter, createWebHashHistory } from 'vue-router'

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: '/', redirect: '/main' },
    { path: '/login', component: () => import('../views/Login.vue') },
    { path: '/main', component: () => import('../views/Main.vue') },
  ],
})

export default router
