export default {
  mode: 'universal', // spa

  // Global page headers: https://go.nuxtjs.dev/config-head
  server: {
    host: '0.0.0.0' // default: localhost
  },
  head: {
    title: 'beasnyou Auto system',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      // { rel: 'stylesheet', href: "https://fonts.googleapis.com/css?family=M+PLUS+1p"}
    ]
  },

  // 上のローディングバーの色
  loading: {
    color: '#fa923f',
    height: '4px',
    duration: 5000
  },

  // spa シングルページの時に有効になる
  loadingIndicator: {
    name: 'circle',
    color: '#fa923f',
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    '~/assets/styles/main.css'
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    '~plugins/core-components.js',
    '~plugins/data-filter.js'
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  // components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
    // https://go.nuxtjs.dev/content
    '@nuxt/content',
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    baseURL: process.env.BASE_URL || 'https://vue-blog-b4395-default-rtdb.firebaseio.com/',
    credentials: false
  },

  // PWA module configuration: https://go.nuxtjs.dev/pwa
  pwa: {
    manifest: {
      lang: 'en'
    }
  },

  // Content module configuration: https://go.nuxtjs.dev/config-content
  content: {},

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    extend(config, ctx){

    }
  },

  generate: {
    fallback: true
  },

  env: {
    baseUrl: process.env.BASE_URL || 'https://vue-blog-b4395-default-rtdb.firebaseio.com/',
    fbAPIKey: 'AIzaSyDOvoOwbfsEDCK0qwhARzmz2JO7YYvmf6c',
  },
  
  // router: {
    // linkActiveClass: 'active',
    // middleware: 'log'
    // extendRoutes(routes, resolve){
    //   routes.push({
    //     path: '*',
    //     component: resolve(__dirname, 'pages/index.vue')
    //   })
    // }
  // },

  trainsition: {
    name: 'page',
    mode: 'out-in'
  },
}
