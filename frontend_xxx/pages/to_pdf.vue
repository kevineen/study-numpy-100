<template>
  <v-row>
    <v-col class="text-center">
      <blockquote class="blockquote">
        <h1></h1>
        <form class="simple-form">
          <h2>ファイルアップロード</h2>
          <label for="title">タイトル</label>
          <input type="text" name="title" />
          <drop></drop>
          <button>投稿する</button>
        </form>
        <footer></footer>
      </blockquote>
    </v-col>
  </v-row>
</template>

<script>
import Xlsx from '~/components/Xlsx.vue'

const fs = require('fs')

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

const download = {
  functional: true,
  render(h, c) {
    return h('button', {
      domProps: {
        type: 'button',
        innerHTML: 'Download',
      },
      on: {
        click() {
          c.parent.$emit('download:workbook')
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
    this.$on('download:workbook', async () => {
      const blob = await this.workbook.outputAsync()

      const url = window.URL.createObjectURL(blob)
      const a = document.createElement('a')

      document.body.appendChild(a)

      a.href = url
      a.download = 'out.xlsx'
      a.click()

      window.URL.revokeObjectURL(url)

      document.body.removeChild(a)
    })
  },
  data() {
    return {
      workbook: {},
    }
  },
  render(h) {
    return h('div', [
      h(input, {
        props: {
          workbook: this.workbook,
        },
      }),
      h(download),
    ])
  },
}

export default {
  components: {
    Xlsx,
  },
  data() {
    return {
      file: null,
      title: 'he',
      isDrag: null,
    }
  },
  created() {},
  methods: {
    onChange(event) {
      this.file = event.target.files ? event.target.files[0] : null
    },
  },
  checkDrag(event, key, status) {
    if (status && event.dataTransfer.types === 'text/plain') {
      // ファイルではなく、html要素をドラッグしてきた時は処理を中止
      return false
    }
    this.isDrag = status ? key : null
  },
}
</script>
