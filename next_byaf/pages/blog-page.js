import Layout from '../components/Layout'
import Link from 'next/link'
import { getAllPostsData } from '../lib/posts'
import Post from '../components/Post'

export default function BlogPage({ filteredPosts }) {
  return (
    <Layout title="Blog">
      <ul>
        {filteredPosts &&
          filteredPosts.map((post) => <Post key={post.id} post={post} />)}
      </ul>
      <Link href="/main-page">
        <div className="flex cursor-pointer mt-12">
          <p className="w-6 h-6 mr-3">おっぱい</p>
          <span>Back to main page</span>
        </div>
      </Link>
    </Layout>
  )
}

export async function getStaticProps() {
  const filteredPosts = await getAllPostsData()
  return {
    props: { filteredPosts },
    revalidate: 3,
  }
}
