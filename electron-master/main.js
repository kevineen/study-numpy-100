// Modules
const electron = require('electron')
const {app, BrowserWindow, session, webContents,
      dialog, globalShortcut, Menu, MenuItem,
      Tray, ipcMain
    } = electron

const windowStateKeeper = require('electron-window-state')
// const { DownloadItem } = require('electron/main')

global['myglob'] = 'A var set in main.js'

// Keep a global reference of the window object, if you don't, the window will
// be closed automatically when the JavaScript object is garbage collected.
let mainWindow, secWindow, tray

let mainMenu = Menu.buildFromTemplate( require('./mainMenu'))

let contextMenu = Menu.buildFromTemplate([
  { label: 'Item1' },
  { role: 'editMenu' },
])

let trayMenu = Menu.buildFromTemplate([
  { label: 'Item1' },
  { role: 'quit' },
])

function createTray(){
  tray = new Tray('tray.png')
  tray.setToolTip('Tray details')

  tray.on('click', e => {
    if(e.shiftKey) {
      app.quit()
    } else {
    mainWindow.isVisible() ? mainWindow.hide() : mainWindow.show()
    }
  })

  tray.setContextMenu(trayMenu)
}

// Create a new BrowserWindow when `app` is ready
function createWindow () {

  createTray();

  let winState = windowStateKeeper({
    defaultWidth: 800, defaultHeight: 600
  })

  mainWindow = new BrowserWindow({
    width: winState.width, height: winState.height,
    x: winState.x, y: winState.y,
    minWidth: 400, minHeight: 600,
    maxWidth: 800, maxHeight: 800,
    // frame: false,
    titleBarStyle: 'hidden',
    webPreferences: { nodeIntegration: true },
    // backgroundColor: '#2c92f9'
  })

  // secWindow = new BrowserWindow({
  //   width: 300, height: 300,
  //   // x: 200, y: 200,
  //   webPreferences: {
  //     nodeIntegration: true,
  //     partition: 'persist:part1',
  //   },
  //   parent: mainWindow,
  //   // modal: true,
  //   // show: false,
  // })
  
  let ses = mainWindow.webContents.session
  // let ses2 = secWindow.webContents.session
  // let defaultSes = session.defaultSession

  ses.clearStorageData()

  // console.log(Object.is(ses, ses2))

  // mainWindow.webContents.on('will-download', (e, downloadItem, webContents) => {

  //   let fileName = downloadItem.getFileName()
  //   let fileSize = downloadItem.getTotalBytes()

  //   downloadItem.setSavePath(app.getPath('desktop') + `/${fileName}`)

  //   downloadItem.on('updated', (e, state) => {

  //     let received = downloadItem.getReceivedBytes()

  //     if(state === 'progressing' && received){
  //       let progress = Math.round((received/fileSize)*100)
  //       webContents.executeJavaScript(`window.progress.value = ${progress}`)
  //     }
  //   })
  // })

  // Load index.html into the new BrowserWindow
  mainWindow.loadFile('index.html')
  // secWindow.loadFile('index.html')

  // mainWindow.webContents.on('did-finish-load', () => {

    // dialog.showOpenDialog({
    //   buttonLabel: 'Select a data',
    //   defaultPath: app.getPath('desktop'),
    //   properties: ['multiSelections', 'createDirectory', 'openFile', 'openDirectory']
    // }, filepaths => {
    //   console.log(filepaths)
    // })

    // dialog.showSaveDialog({}, filename => {
    //   console.log(filename)
    // })

  //   const answers = ['Yes', 'No', 'Maybe']

  //   dialog.showMessageBox({
  //     title: "Message Box",
  //     message: "Please select an option",
  //     detail: "Message details",
  //     butotns: answers,
  //   }, response => {
  //     console.log(`User selected: ${answers[response]}`)
  //   })
  // })


  // console.log(BrowserWindow.getAllWindows())


  winState.manage(mainWindow)
  // winState.manage(secWindow)

  mainWindow.webContents.on('did-finish-load', e => {
    mainWindow.webContents.send('mailbox',{
      from: 'Ore',
      email: 'dlfkaj',
      priority: 1
    })
  })
  
  Menu.setApplicationMenu(mainMenu)

  mainWindow.webContents.on('context-menu', e => {
    contextMenu.popup(mainWindow)
  })


  // なぜかmodalおかしい
  // secWindow.loadFile('sec.html')

  // mainWindow.webContents.openDevTools();

  globalShortcut.register('CommandOrControl+G', () =>{
    console.log('G')
    globalShortcut.unregister('CommandOrControl+G')
  })

  mainWindow.on('closed',  () => {
    mainWindow = null
  })

  // secWindow.on('closed',  () => {
  //   secWindow = null
  // })

  // setTimeout( () => {
  //   secWindow.show()
  //   setTimeout( () => {
  //     secWindow.close()
  //     secWindow = null;
  //   }, 3000)
  // }, 2000)

  // electron.powerMonitor.on('resume', e => {
  //   if(!mainWindow) createWindow()
  // })

}

ipcMain.on('sync-message', (e, args) => {
  console.log(args)

  setTimeout( () =>{
    e.returnValue = 'A sync response from the main process'
  }, 4000)
  
})

ipcMain.on('channel1', (e, args) => {
  console.log(args)
  e.sender.send('channel1-response', 'Message received')
})

// Electron `app` is ready
app.on('ready', () => {
  console.log('App is ready')
  console.log(app.getPath('desktop'))

  createWindow()
})

// Quit when all windows are closed - (Not macOS - Darwin)
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit()
})

// When app icon is clicked and app is running, (macOS) recreate the BrowserWindow

// app.on('before-input-event', (e, input) => {
//   console.log(`${input.key} : ${input.type}`)
// })

app.on('activate', () => {
  if (mainWindow === null) createWindow()
})

app.on('before-quit', e =>{
  console.log('Preventing app from quitting')
  // e.preventDefault()
  // app.quit()
})

// app.on('browser-window-blur', e => {
//   console.log('App upfocused')
// })

// app.on('browser-window-focus', e => {
//   console.log('App focused')
// })

