<template>
  <section class="post-list">
    <div class="posts-page">
      <section class="post-list">
        <!-- <h1>This is</h1> -->
        <PostPreview
          v-for="post in posts"
          :key="post.id"
          :id="post.id"
          :is-admin="isAdmin"
          :thumbnail="post.thumbnail"
          :title="post.title"
          :previewText="post.previewText"
        />
      </section>
    </div>
  </section>
</template>

<script>
import PostPreview from "@/components/Posts/PostPreview";

export default {
  components: {
    PostPreview,
  },
  props: {
    isAdmin: {
      type: Boolean,
      default: false,
    },
    posts: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style scoped>
.post-list {
  display: flex;
  padding: 20px;
  box-sizing: border-box;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
}
</style>