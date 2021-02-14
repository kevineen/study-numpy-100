import Cookie from "universal-cookie"
import { useRouter } from "next/router"
import Layout from "../components/Layout"
import Link from "next/link"

const cookie = new Cookie()

export default function MainPage(){
    const router = useRouter();
    const logout = () => {
        cookie.remove("access_token")
        router.push("/")
    }
    return (
        <Layout titlte="Main page">
            <div className="mb-10">
                <Link href="/blog-page">
                    <a className="gb-indigo-500 mr-8 hover:bg-indigo-600 text-white px-4 py-12 rounded">ブログ</a>
                </Link>
                <Link href="/task-page">
                    <a className="gb-gray-500 mr-8 hover:bg-indigo-600 text-white px-4 py-12 rounded">タスク</a>
                </Link>
            </div>

            <p className="mt-10 cursor-pointer w-6 h-6"
                onClick={logout}>
                ログアウト
            </p>
        </Layout>
    )
}