import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import firstPage from '../views/firstpage.vue'
import manRedirect from '../views/redirect.vue'
import Category_create from '@/views/category_create.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/firstpage',
    name: 'firstPagePathName',  
    component: firstPage
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/LoginView.vue')
  },
  {
    path: '/redirect/:name1',
    name: 'redirect',
    component: manRedirect
  },
  {
    path: '/category/create',
    name: 'category_create',
    component: Category_create
  },
  {
    path: '/category/update/:id',
    name: 'category_update',
    component: Category_create
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: () => import('@/views/dashboard.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
