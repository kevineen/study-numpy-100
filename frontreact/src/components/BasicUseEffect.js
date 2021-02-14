import React, { useState, useEffect } from 'react'

export const BasicUseEffect = () => {

    const [count, setCount] = useState(0)
    const [item, setItem] = useState('')

    // 2引数で指定の時だけ実行するという形ができる
    // 空なら初回だけ
    useEffect(() => {
        console.log("use invoked")
    }, [count])


    return (
        <div>
            <button onClick={()=> setCount(prevCount=>prevCount+1)}> Click { count }</button>
            <input type='text' value={ item } onChange={ evt =>setItem(evt.target.value) } />
        </div>
    )
}

export default BasicUseEffect

