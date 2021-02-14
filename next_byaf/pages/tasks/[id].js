import { useEffect } from "react"
import Link from 'next/link'
import Layout from '../../components/Layout'
import { useRouger } from 'next/router'
import { getAllTaskIds, getTaskData } from '../../lib/tasks'
import useSWR from "swr"

const fetcher = (url) => fetch(url).then((res) => res.json())

export default function Post({ staticTask, id }) {
  const router = useRouter()
  const { data: task, mutate } = useSWR(
      `${process.env.NEXT_PUBLIC_RESTAPI_URL}api/detail-task/${id}`,
      fetcher,
      {
          initialData: staticTask,
      }
    )
    useEffect(() => {
        mutate()
    }, [])

    if(router.isFallback || !task){
        return <div>Loading...</div>
    }
    return (
        <Layout title={task.title}>
            <span className="mb-4">
                {"ID: "}
                {task.id}
            </span>
            <p className="mb-4 text-xl font-bold">{task.title}</p>
            <p className="mb-12">{task.created_at}</p>
            <Link href="/task-page">
                <div className="flex cursor-pointer mt-8">
                    <p
                        className="w-6 h-6 mr-3">
                            戻る
                    </p>
                    <span>Back</span>
                </div>
            </Link>
        </Layout>
    )
}

export async function getStaticPaths() {
  const paths = await getAllTaskIds()

  return {
    paths,
    fallback: true,
  }
}

export async function getStaticProps({ params }) {
  const { task: staticTask } = await getTaskData(params.id)
  return {
    id: staticTask.id,
    staticTask,
  },
  revalidate: 3,
}
