<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="6">
      <div class="text-center">
        <img src="../static/beans_logo.png" />
      </div>
      <v-card>
        <v-card-title class="headline"> ビーンズユー株式会社 </v-card-title>
        <v-card-text>
          <p>仮 Beansyou AutoFormation System</p>
          <p>
            Vuetify, 公式ドキュメント
            <a
              href="https://vuetifyjs.com"
              target="_blank"
              rel="noopener noreferrer"
            >
              documentation
            </a>
          </p>

          <div class="text-xs-right">
            <em><small>&mdash; Kunihiro Watanabe</small></em>
          </div>
          <hr class="my-3" />
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn color="primary" nuxt to="/release_note">試す</v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  components: {},
}
</script>
