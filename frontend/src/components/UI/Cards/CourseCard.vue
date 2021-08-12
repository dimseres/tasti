<template>
  <div class="card__course">
    <div class="card__header">
      <h3 class="header_title">{{ title }}</h3>
    </div>
  </div>
</template>

<script>
export default {
  name: "CourseCard",
  props: {
    title: String,
  },
}
</script>

<style lang="scss" scoped>
.card__course {
  box-shadow: $shadow;
}
.header_title {
  font-family: "Montserrat", sans-serif;
  font-weight: 700;
  font-size: 20px;
  color: $color_gray;

}
</style>