import React, {useContext} from 'react';
import AppContext from '../contexts/AppContext';

function CompC() {
    const { dispatchProvided } = useContext(AppContext)

    return (
        <div>
            <button onClick={()=> dispatchProvided('add_1')}>Add + 1</button>
            <button onClick={()=> dispatchProvided('multiple_3')}>* 3</button>
        </div>
    )
}

export default CompC
