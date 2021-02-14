import React, {useState, useEffect} from 'react'
import axios from 'axios'

const TaskApiFetch = () => {

    const [tasks, setTask] = useState([])
    const [selectedTask, setSelectedTask] = useState([])
    const [id, setId] = useState(1)

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/tasks/'),{
            headers: {
                'Authorization': 'Token ca031d1641b68f11ccf36661af2b21685e1c4ded',
            }
        })

        .then(res => setTasks(res.data)})
    },[])

    return (
        <div>
            <ul>
                {
                    tasks.map(task => <li key={task.id} > {task.title}  {title.id}</li>)
                }

            </ul>

        </div>
    )
}

export default TaskApiFetch
