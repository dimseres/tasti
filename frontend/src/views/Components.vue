<template>
  <div>
    <h1 class="title">Components Page</h1>
    <hr />
    <h2 class="title">Cards</h2>
    <CourseCard title="I'm Card"/>
  </div>
</template>

<script>
import CourseCard from "@/components/UI/Cards/CourseCard";

export default {
  name: "Components",
  components: {
    CourseCard
  }
}
</script>

<style scoped>
.title {
  font-family: "Montserrat", sans-serif;
  /*font-size: 22px;*/
  text-align: center;
  text-transform: uppercase;
}
</style>