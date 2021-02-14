import { useEffect } from 'react'
import Layout from '../components/Layout'
import Link from 'next/link'
import { getAllTasksData } from '../lib/tasks'
import Task from '../components/Task'
import useSWR from 'swr'
import StateContextProvider from '../context/StateContext'
import TaskForm from '../components/TaskForm'

const fetcher = (url) => fetch(url).then((res) => res.json())
const apiUrl = `${process.env.NEXT_PUBLIC_RESTAPI_URL}api/list-task/`

export default function TaskPage({ staticfileterdTasks }) {
  const { data: tasks, mutate } = useSWR(apiUr, fetcher, {
    initialData: staticfileterdTasks,
  })

  const filteredTasks = tasks?.sort(
    (a, b) => new Date(b.created_at) - new Date(a.created_at)
  )
  useEffect(() => {
    mutate()
  }, [])

  return (
    <StateContextProvider>
      <Layout title="Task">
        <TaskForm taskCreated={mutate} />
        <ul>
          {filteredTasks &&
            filteredTasks.map((task) => (
              <Task key={task.id} task={task} taskDeleted={mutate} />
            ))}
        </ul>
        <Link href="/main-page">
          <div className="flex cursor-pointer mt-12">
            <p className="w-6 h-6 mr-3">おっぱい</p>
            <span>Back to main page</span>
          </div>
        </Link>
      </Layout>
    </StateContextProvider>
  )
}

export async function getStaticProps() {
  const staticfileterdTasks = await getAllTasksData()

  return {
    props: { staticfileterdTasks },
    revalidate: 3,
  }
}
