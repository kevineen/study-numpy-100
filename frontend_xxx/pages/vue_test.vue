<template>
  <v-row>
    <v-col class="text-center">
      <blockquote class="blockquote">
        作成履歴<br />
        <div id="app1">
          <h1>{{ title }}</h1>
          <button @click="onChange">Change something in Vue 1</button>
        </div>

        <footer></footer>
      </blockquote>
    </v-col>
  </v-row>
</template>
<script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
<script>
// export default{
//   vm1 = new Vue({
//   el: '#app1',
//   data: {
//     title: 'The VueJS Instance',
//     showParagraph: false,
//   },
//   methods: {
//     show: function () {
//       this.showParagraph = true
//       this.updateTitle('The VueJS Updated')
//     },
//     updateTime: function (title) {
//       this.title = title
//     },
//   },
// })
// }
</script>
<style></style>
