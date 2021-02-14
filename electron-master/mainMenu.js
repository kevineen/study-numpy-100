module.exports = [
    {
        label: 'Electron',
        submenu: [
        {label: 'Item1'},
        {label: 'Item2',
        submenu: [{
        label: 'Sub Item 1'
        }]},
        {label: 'Item3'},
    ]
    },
    {
        label: 'Edit',
        submenu: [
            {
                label: 'undo',
                role: 'undo',
                accelerator: 'Control+Z'
            },
            {
                label: 'redo',
                role: 'redo',
                accelerator: 'Control+Shift+Z'
            },
            {
                label: 'copy',
                role: 'copy',
                accelerator: 'Control+C'
            },
            {
                label: 'paste',
                role: 'paste',
                accelerator: 'Control+V'
            },
        
        ]
    },
    {
        label: 'Actions',
        submenu: [
        {
            label: 'Action 1',
            role: 'toggleDevTools',
            accelerator: 'D'
        },
        {
            label: 'Action 2',
            submenu: [{
                label: 'Sub Item 1'
            }],
            enabled: false,
        },
        {
            label: 'Action 3',
            click: () => {
                console.log("clidk")
            },
            accelerator: 'G'
        },
        ]
    },
]