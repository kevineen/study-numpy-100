// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// All of the Node.js APIs are available in this process.
const remote = require('electron').remote
const { app, dialog, BrowserWindow } = remote
const { ipcRenderer } = require('electron')

const button = document.getElementById('test-button')
// console.log(remote)

// let i = 1
// setInterval( () => {
//     console.log(i)
//     i++
// }, 1000)

document.getElementById('talk').addEventListener('click', e => {

    // ipcRenderer.send('channel1', 'Hello from main window')

    let response = ipcRenderer.sendSync('sync-message', 'waiting for res')
    console.log(response)

})

ipcRenderer.on('channel1-response', (e, args) => {
    console.log(args)
})

ipcRenderer.on('mailbox', (e, args) => {
    console.log(args)
})

button.addEventListener('click', e => {
    // console.log('Testing')

    // dialog.showMessageBox({
    //     message: 'Dialog'
    // })

    let secWin = new BrowserWindow({
        with: 400, height: 350,
    })

    console.log( remote.getGlobal('myglob') )

    // app.quit()

    let win = remote.getCurrentWindow()
    win.maximize()
})