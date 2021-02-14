import React, { useState } from 'react'

const Basic = (props) => {
    const clickHandler = () => {
        console.log('clicked')
    };

    const [product, setProducts] = useState({name: '', price: ''})
    // count, setCount 0

    return (
        <>
            <form>
                <input type='text' value={product.name}
                onChange={evt => setProducts({...product, name: evt.target.value})} />

                <input type='text' value={product.price}
                onChange={evt => setProducts({...product, price: evt.target.value})} />
            </form>
            {/*<button onClick={() => {setCount(prevCount=>prevCount+1); setCount(prevCount=>prevCount+1);} }>Count { count }</button>*/}
            <h3> ProductName { product.name }</h3>
            <h3> Price { product.price }</h3>
        </>
    )
}

export default Basic