
const routes = [
  {
    path: '/',
    name: 'index',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/IndexPage.vue') },
      { path: '/chat', component: () => import('components/ChatPage.vue')},
      { path: '/pioneers', component: () => import('components/PioneerSearch')},
      { path: '/myprojects', component: () => import('components/PioneerProjects')},
    ]
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('components/LoginPage.vue')
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
