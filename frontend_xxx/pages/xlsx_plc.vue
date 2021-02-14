<template>
  <v-row>
    <v-col class="text-center">
      <blockquote class="blockquote">
        <a hef="https://nmomos.com/tips/2019/12/01/vue-nuxt-ssr/"
          ><p>参考</p></a
        >
        PLC構成<br />
        <h1>{{ title }}</h1>
        <h3>{{ now }}</h3>

        <router-link to="/"><p>TOPページ</p></router-link><br />
        <h3>{{ $store.state.message }}</h3>
        <div
          class="link"
          @click.exact="
            $store.commit({ type: 'count', message: 'add 1', add: 1 })
          "
          @click.shift="
            $store.commit({ type: 'count', message: 'add 5', add: 5 })
          "
          @click.ctrl="
            $store.commit({ type: 'count', message: 'add 10', add: 10 })
          "
        >
          <a @click.stop="$store.commit('reset')">
            clicked: {{ $store.state.counter }}
          </a>
        </div>
        <div class="link" @click="$store.dipatch('doit')">あああああああ</div>
        <section>
          あああ
          <!--
          <input type="file" @change="onChange" />
          <xlsx-read :file="file">
            <xlsx-json :sheet="selectedSheet">
              <template #default="{ collection }">
                <div>
                  {{ collection }}
                  <div id="app"></div>
                </div>
              </template>
            </xlsx-json>
          </xlsx-read>
          -->
        </section>
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
      now: '',
    }
  },
  created() {
    // URLパラメータを取り出す
    // alert(this.$route.params.xyz)
    setInterval(() => {
      const d = new Date()
      this.now = d.getHours() + ':' + d.getMinutes() + ':' + d.getSeconds()
    }, 1000)
  },
  methods: {
    onChange(event) {
      this.file = event.target.files ? event.target.files[0] : null
    },
  },
}
</script>
