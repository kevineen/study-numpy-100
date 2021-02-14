module.exports = {
    root: true,
    env: {
        browser: true,
        node: true,
    },
    parserOptions: {
        parser: 'babel-eslint',
    },
    extends: [
        '@nuxtjs',
        'eslint:recommended',
        'prettier',
        'prettier/vue',
        'plugin:prettier/recommended',
        'plugin:nuxt/recommended',
    ],
    plugins: ['vue', 'prettier'],
    // add your custom rules here
    rules: {
        'semi': [2, "never"],
        'no-console': 'off',
        'vue/max-attributes-per-line': 'off',
        'prettier/prettier': ['error', {
            'semi': false
        }],
        'vue/no-unused-components': 'off',
        'no-unused-vars': 'off',
        'space-before-function-paren': 0,
    },
}