<template>
  <v-row>
    <v-col class="text-center">
      <blockquote class="blockquote">
        作成履歴<br />
        <small>
          <em>現状、PLC構成システムを構築中</em><br /><br />
          <h2>・To Doリスト</h2>
          <p></p>
          <h3>フロントエンド (画面表示される部分)</h3>
          <p>
            【NOWdoing】端子台配列とエクセルの連携<br />
            frontendでファイルを保存できるものを作成し、フォルダに保存<br />
            buttonを押したら裏でAutoLISPが動いて、処理を実行、<br />
            frontendにデータを返す<br />
            エクセルデータとdwgデータをアップロードしたものをまとめてPDF化<br />
            ・必要なPLC構成を入力して、IOリストのエクセルを出力し、
            ダウンロードを可能にする<br />
            ・入力したエクセルデータをアップロードして、自動構築されたCADデータを出力<br />
            ・まとめたPDFファイルの作成<br />
            ・記号紙データの作成<br />
            ・マークチューブデータの作成・線に適合するマークチューブサイズの記載（あとで）<br />
          </p>
          <h3>バックエンド（サーバー側部分）</h3>
          <p>
            ・ファイルサーバーとの連携<br />
            ・オーダーごとのフォルダ構成ZIPファイルの自動生成
          </p>
        </small>
        <footer></footer>
      </blockquote>
    </v-col>
  </v-row>
</template>
