<template>
  <div class="courses content">
    <div class="courses__header">
      <h1 class="courses__title">Ваши курсы</h1>
      <p class="courses__description">Each course contains video lectures, tasks, and text materials.
        All courses viewed by you are displayed in your personal account</p>
    </div>
    <div class="courses__search">
      <div class="search__container">
        <input type="text" class="search__input" placeholder="search">
      </div>
    </div>
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

  &__header {
    margin: 32px 0;
    width: 50%;
  }

  &__description {
    font-weight: 500;
  }

  &__title {
    margin: 0;
    font-weight: 900;
    font-size: 40px;
    color: $color_black;
  }

  &__search {
    width: 100%;
  }
}

.search {
  &__input {
    width: 100%;
    margin-bottom: 32px;
    box-shadow: 0px 4px 4px rgba(51, 51, 51, 0.04), 0px 4px 16px rgba(51, 51, 51, 0.08);
    padding: 16px 12px;
    outline: none;
    border: none;
    border-radius: 4px;
  }
}
</style>