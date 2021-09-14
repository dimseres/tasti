<template>
  <div class="card__course">
    <div class="card__header">
      <div class="header__cover">
        <div class="header__progress">
          <div class="progress"><span class="progress__text">Progress 33%</span></div>
        </div>
        <div class="cover__container">
          <img src="https://via.placeholder.com/1000x500" alt="#">
        </div>
      </div>
      <div class="header__author">
        <div class="author__ava">
          <img class="ava" src="https://via.placeholder.com/1000x500" alt="#">
        </div>
        <div class="author__data"><span class="name">Попов Виктор Николаевич</span></div>
      </div>
    </div>
    <div class="card__content">
      <h3 class="header_title">{{ title }}</h3>
      <div class="card__info__container">
        <div class="card__info">
          <img class="info__icon" src="/icons/24px/student.svg" alt="">
          <span class="info__description">12 уроков</span>
        </div>
        <div class="card__info">
          <img class="info__icon" src="/icons/24px/pen.svg" alt="">
          <span class="info__description">12 заданий</span>
        </div>
        <div class="card__info">
          <img class="info__icon" src="/icons/24px/chemistry.svg" alt="">
          <span class="info__description">2 теста</span>
        </div>
      </div>
    </div>
    <div class="card__actions">
      <a href="#" class="card__button">продолжить</a>
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
  flex: 1;
  display: flex;
  flex-direction: column;
  margin: 0 15px;
  border-radius: 8px;
  overflow: hidden;
  //padding: 15px;
  //max-width: 400px;
  transition: .3s;

  &:hover {
    transform: translateY(-10px);
  }
}

.header__author {
  display: flex;
  position: absolute;
  bottom: 0;
  align-items: center;
  padding: 0 20px;
  transform: translateY(8px);
}

.author__data {
  .name {
    font-family: 'Roboto';
    color: $color_black;
    font-size: 16px;
  }
}

.author__ava {
  width: 56px;
  height: 56px;
  overflow: hidden;
  border-radius: 50%;
  margin-right: 12px;
  border: 2px solid #fff;

  .ava {
    height: 100%;
    width: 100%;
    object-fit: cover;
  }
}

.card__content {
  padding: 15px 20px;
}

.header_title {
  font-family: "Montserrat", sans-serif;
  font-weight: 700;
  font-size: 20px;
  color: $color_black;

}

.header__progress {
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 24px;

  .progress {
    width: 100%;
    display: flex;
    align-items: center;
    height: 100%;
    font-family: Roboto;
    color: #fff;
    padding: 0 20px;
    font-size: 13px;
    position: relative;

    &__text {
      color: #fff;
      z-index: 3;
    }

    &::after {
      position: absolute;
      left: 0;
      display: block;
      content: '';
      background: $color_green;
      height: 100%;
      width: 30%;
    }
  }
}

.card__info__container {
  display: flex;
  flex-wrap: wrap;
}

.card__info {
  display: flex;
  align-items: center;
  padding-right: 12px;
}

.header__cover {
  position: relative;
  //display: flex;
  //flex-direction: column;
  //overflow: hidden;
}

.card__header {
  flex: 1;
  position: relative;
}

.card__actions {
  padding: 15px 20px;
  display: flex;
}

.card__button {
  color: $color_primary;
  border: 1px solid $color_primary;
  border-radius: 4px;
  padding: 10px 20px;
  display: block;
}

.cover__container {
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 135px;

  img {
    height: 100%;
    width: 100%;
    object-fit: cover;
  }
}
</style>