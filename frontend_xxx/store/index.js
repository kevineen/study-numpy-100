import Vuex from 'vuex'

const createStore = () => {
  return new Vuex.Store({
    state() {
      return {
        message: 'This is ',
        counter: 0,
      }
    },
    mutations: {
      count(state, obj) {
        state.message = obj.message
        state.counter += obj.add
      },
      reset(state) {
        state.counter = 0
      },
    },
    actions: {
      doit(context) {
        const n = Math.floor(Math.random() * 10)
        context.commit('count', n)
        context.commit('say', 'add ' + n + '!')
      },
    },
  })
}

export default createStore
