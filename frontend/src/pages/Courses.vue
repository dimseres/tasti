<template>
  <div class="courses content">
    <h1 class="courses__title">Ваши курсы</h1>
    <p>Each course contains video lectures, tasks, and text materials.
      All courses viewed by you are displayed in your personal account</p>
    <CourseList/>
  </div>
</template>

<script>
import CourseList from "../components/Course/CourseList";

export default {
  name: "Courses",
  components: {
    CourseList
  }
}
</script>

<style scoped lang="scss">
.courses {
  margin: auto;
}
.courses__title {
  font-size: 40px;
  color: $color_black;
}
</style>