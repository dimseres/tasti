<template>
  <div>
    <h1 class="title">Components Page</h1>
    <hr/>
    <h2 class="title">Cards</h2>
    <div class="course-card__wrapper">
<!--      <CourseCard v-for="x in 3" :key="x" title="I'm Card"/>-->
    </div>
  </div>
</template>

<script>
// import CourseCard from "@/components/UI/Cards/CourseCard";

export default {
  name: "Components",
  components: {}
}
</script>

<style scoped>
.title {
  font-family: "Montserrat", sans-serif;
  /*font-size: 22px;*/
  text-align: center;
  text-transform: uppercase;
}

.course-card__wrapper {
  display: flex;
  flex-wrap: wrap;
  width: 1150px;
  margin: auto;
}
</style>