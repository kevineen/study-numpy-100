import React, {useState, useReducer, useCallback} from 'react'
import logo from './logo.svg';
import './App.css';
import Basic from './components/Basic'
import BasicLen from './components/BasicLen'
import BasicUseEffect from './components/BasicUseEffect'
import TimerContainer from './components/TimerContainer'
import ApiFetch from './components/ApiFetch';
import AppContext from './contexts/AppContext';
import B from './components/B';
import BasicReducer from './components/BasicReducer';
import CompB from './components/CompB';
import Memo from './components/Memo';
import CountDisplay from './components/CountDisplay';
import CountClick from './components/CountClick';

import rootReducer from './reducers/index';
import { SELL_MEAT, SELL_VEGETABLE } from './reducers/actionTypes';

const initialState = 0
const reducer = (currentState, action) => {
    switch(action){
        case 'add_1':
            return currentState + 1
        case 'multiple_3':
            return currentState * 3
        case 'reset':
            return initialState
        default:
            return currentState
    }
}

function App() {

    const initialState = {
        reducerMeat: {numOfMeat: 30},
        reducerVegetable: {numOfVegetabel:25},
    }
    const [state, dispatch] = useReducer(rootReducer, initialState)

    //const [count, dispatch] = useReducer(reducer, initialState)

    const [count1, setCount1] = useState(0)
    const [count2, setCount2] = useState(0)

    const AddCount1 = useCallback(() => {
        setCount1(prevCount1 => prevCount1 + 1)
    }, [count1])
    const AddCount2 = useCallback(() => {
        setCount2(prevCount2 => prevCount2 + 1)
    }, [count2])


    return (
        //<AppContext.Provider value={{countProvided: count, dispatchProvided: dispatch}}>
            <div className = "App" >
                <header className = "App-header" >
                <img src = { logo } className = "App-logo" alt = "logo" / >
                {/* <BasicLen name="Hooks"/> */}
                {/* <BasicUseEffect /> */}
                {/* <TimerContainer /> */}
                {/* <ApiFetch /> */}
                {/* <B /> */}
                {/* <BasicReducer /> */}
                {/* Count {count}
                <CompB/> */}
                {/* <Memo /> */}
                {/* <CountDisplay name="count1" count={ count1 }/>
                <CountClick handleClick={ AddCount1 }>Addcount1</CountClick>
                <CountDisplay name="count2" count={ count2 }/>
                <CountClick handleClick={ AddCount2 }>Addcount2</CountClick> */}

                <button onClick={()=>dispatch({type: SELL_MEAT})}>Sell Meat</button>
                Today's Meat: {state.reducerMeat.numOfMeat}
                <button onClick={()=>dispatch({type: SELL_VEGETABLE})}>Sell Vegetable</button>
                Today's Vegetable: {state.reducerVegetable.numOfVegetabel}

                </header>
            </div>
    );
}
        {/* //</AppContext.Provider> */}

export default App;