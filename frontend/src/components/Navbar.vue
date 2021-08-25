<template>
  <div class="navbar">
    <div class="navbar__container content">
      <h1 class="navbar__logo">
        <router-link :to="{name: 'Home'}" class="home__link">Edugree</router-link>
      </h1>
      <div class="navbar__menu">
        <div class="menu__list">
          <router-link :to="{name: 'Components'}" class="menu__item">Задания</router-link>
          <router-link :to="{name: 'Home'}" class="menu__item">Курсы</router-link>
        </div>
        <div class="menu__profile">
          <div class="profile__container">
            <span class="profile__name">Есин Дмитрий</span>
            <div class="profile__avatar"><img src="https://via.placeholder.com/1000x500" alt=""></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Navbar"
}
</script>

<style lang="scss" scoped>
.navbar {
  border-bottom: 1px solid $color_gray_light;

  &__container {
    margin: auto;
    display: flex;
    height: 76px;
    align-items: center;
    justify-content: space-between;
  }

  &__logo {
    color: $color_primary;
    font-family: 'Roboto';
    font-size: 24px;
    font-weight: 900;
  }

  &__menu {
    display: flex;
    align-items: center;
    height: 100%;
  }


}

.home__link {
  @extend .navbar__logo;
}

.menu {
  &__list {
    display: flex;
    height: 100%;
  }

  &__profile {
    margin-left: 50px;
  }

  &__item {
    display: flex;
    height: 100%;
    font-size: 16px;
    color: $color_gray;
    align-items: center;
    padding: 0px 15px;
    position: relative;

    &.router-link-exact-active {
      color: $color_black;
      &::after {
        position: absolute;
        bottom: 0;
        left: 0;
        content: '';
        width: 100%;
        height: 2px;
        background: $color_primary;
      }
      //border-bottom: 3px solid $color_primary;
    }
  }
}

.profile {
  &__container {
    display: flex;
    align-items: center;
  }

  &__name {
    color: $color_primary;
  }

  &__avatar {
    margin-left: 12px;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 44px;
    width: 44px;
    border-radius: 50%;

    img {
      height: 100%;
      width: 100%;
      object-fit: cover;
    }
  }
}

</style>