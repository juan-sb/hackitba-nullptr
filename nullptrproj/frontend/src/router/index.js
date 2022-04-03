import { route } from 'quasar/wrappers'
import { createRouter, createMemoryHistory, createWebHistory, createWebHashHistory } from 'vue-router'
import routes from './routes'
import Proxy from '../Proxy'
/*
 * If not building with SSR mode, you can
 * directly export the Router instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Router instance.
 */


export default route(function (/* { store, ssrContext } */) {
  const createHistory = process.env.SERVER
    ? createMemoryHistory
    : (process.env.VUE_ROUTER_MODE === 'history' ? createWebHistory : createWebHashHistory)

  const Router = createRouter({
    scrollBehavior: () => ({ left: 0, top: 0 }),
    routes,

    // Leave this as is and make changes in quasar.conf.js instead!
    // quasar.conf.js -> build -> vueRouterMode
    // quasar.conf.js -> build -> publicPath
    history: createHistory(process.env.MODE === 'ssr' ? void 0 : process.env.VUE_ROUTER_BASE)
  })

  Router.beforeEach(async (to, from, next) => {
    const res = await Proxy.get("/api/dj-rest-auth/user/", {
      data: null,
      headers: { "Content-Type": "application/json" },
    }).catch(err => {
      if (to.name == "login") next();
      // Si no esta loggeado y se quiere loggear, siga
      else next({ name: "login" }); // SI no esta loggeado y no se quiere loggear, loggeese
    }).then(res => {
      //console.log(res)
      if (res && res.data && res.data.pk) {
        if (to.name == "login") next(false);
        // Esta loggeado y se quiere loggear, volvemos atras
        else next(); // Esta loggeado y no se quiere loggear, siga normal
      }
    })
  })

  return Router
})
