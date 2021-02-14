<template>
  <div class="single-post-page">
    <section class="post">
      <h1 class="post-title">{{ loadedPost.title }}</h1>
      <div class="post-details">
        <div class="post-details">
          ldkfsajs{{ loadedPost.updatedDate | date }}
        </div>
        <div class="post-details">lfdkjasf;sdf{{ loadedPost.author }}</div>
      </div>
      <p class="post-content">>ldksaf;lds{{ loadedPost.content }}</p>
    </section>
    <section class="post-feedback">
      <p>send e-mail<a href="mailto:nabenabe16002@yahoo.co.jp">mail</a></p>
    </section>
  </div>
</template>

<script>
export default {
  asyncData(context) {
    return context.app.$axios
      .$get("/posts/" + context.params.id + ".json")
      .then((data) => {
        return {
          loadedPost: data,
        };
      })
      .catch((e) => context.error(e));
    // setTimeout(() => {
    //   callback(null, {
    //     loadedPosts: {
    //       id: "1",
    //       title: "First Post (ID: " + context.route.params.id + ")",
    //       previewText: "ldkfjadsaf",
    //       author: "kevin",
    //       updatedDate: new Date(),
    //       content: "contentt",
    //       thumbnail: "lkdfja;lfj",
    //     },
    //   });
    // }, 300);
  },
  head: {
    title: "Post",
  },
};
</script>


<style scoped>
.single-post-page {
  padding: 30px;
  text-align: center;
  box-sizing: border-box;
}

.post {
  width: 100%;
}

@media (min-width: 768px) {
  .post {
    width: 600px;
    margin: auto;
  }
}

.post-title {
  margin: 0;
}

.post-details {
  padding: 10px;
  box-sizing: border-box;
  border-bottom: 3px solid #ccc;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

@media (min-width: 768px) {
  .post-details {
    flex-direction: row;
  }
}
</style>