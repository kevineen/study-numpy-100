import Link from 'next/link'
import Cookie from 'universal-cookie'
import { useContext } from 'react'
import { StateContext } from '../context/StateContext'

const cookie = new Cookie()

export default function Task({ task, taskDeleted }) {
  const { setSelectedTask } = useContext(StateContext)
  const deleteTask = async () => {
    await fetch(`${process.env.NEXT_PUBLIC_RESTAPI_URL}api/tasks/${task.kd}`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `JWT ${cookie.get('access_token')}`,
      },
    }).then((res) => {
      if (res.status === 401) {
        alert('JWT Token not valied')
      }
    })
    taskDeleted()
  }

  return (
    <div>
      <span>{task.kd}</span>
      {' : '}
      <Link href={`/tasks/${task.kd}`}>
        <span className="cursor-pointer text-white border-b border-gray-500 hover:bg-gray-600">
          {task.title}
        </span>
      </Link>
      <div className="float-right ml-20">
        <p
          onClick={() => setSelectedTask(task)}
          className="w-6 h-6 float-left cursor-pointer"
        >
          編集
        </p>

        <p onClick={deleteTask} className="w-6 h-6 cursor-pointer">
          削除
        </p>
      </div>
    </div>
  )
}
