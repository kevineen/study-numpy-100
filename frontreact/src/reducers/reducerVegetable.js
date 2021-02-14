import { SELL_VEGETABLE } from './actionTypes'

const reducerVegetable = (state=[], action) => {
    switch (action.type){
        case SELL_VEGETABLE: return {
            ...state,
            numOfVegetabel: state.numOfVegetabel - 1
        }
        default: return state
    }
}

export default reducerVegetable
