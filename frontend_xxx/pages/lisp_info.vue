<template>
  <v-row>
    <v-col class="text-center">
      <blockquote class="blockquote">
        <p>LISP技</p>
        <div class="link" @click="$store.dipatch('doit')">あああああああ</div>
        <section>(vl-load-com)でVisualLISPを読み込む</section>
        <footer></footer>
      </blockquote>
    </v-col>
  </v-row>
</template>

<script>
import Xlsx from '~/components/Xlsx.vue'

const XlsxPopulate = require('xlsx-populate')
const axios = require('axios')

XlsxPopulate.fromBlankAsync().then((workbook) => {
  // Modify the workbook.
  workbook.sheet('Sheet1').cell('A1').value('This is neat!')

  // Write to file.
  return workbook.toFileAsync('./out.xlsx')
})

const input = {
  functional: true,
  props: {
    workbook: {
      type: Object,
      required: true,
    },
  },
  render(h, c) {
    return h('input', {
      domProps: {
        type: 'file',
      },
      on: {
        change(e) {
          const file = e.target.files[0]

          XlsxPopulate.fromDataAsync(file).then((workbook) => {
            workbook.sheets().forEach((sheet) => {
              console.log(sheet.usedRange().value())
            })
            c.parent.$emit('update:workbook', workbook)
          })
        },
      },
    })
  },
}

const wrapper = {
  mounted() {
    this.$on('update:workbook', (workbook) => {
      this.workbook = workbook
    })
  },
  data() {
    return {
      workbook: {},
    }
  },
}

export default {
  components: {},
  data() {
    return {
      file: null,
      title: 'he',
      now: '',
    }
  },
  created() {},
  methods: {},
}
</script>
