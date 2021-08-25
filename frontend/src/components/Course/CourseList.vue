<template>
  <div class="course__list">
      <CourseCard v-for="item in 3" :key="item" />
  </div>
</template>

<script>
import CourseCard from "./CourseCard";

export default {
  name: "CourseList",
  components: {
    CourseCard
  }
}
</script>

<style scoped lang="scss">
.course__list {
  margin: auto;
  display: flex;
}
</style>